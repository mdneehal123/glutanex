// Reward codes (scratch card, routine streak, unboxing reel, owner-issued). Stored in the Redis database.
// A code is single-use, has an expiry date and is linked to one mobile number, so it cannot be passed around.
//   cpn:<CODE>       -> {off, kind, phone, exp, note, order, created}
//   cpn-used:<CODE>  -> the order id that used it (written only after a successful payment)
const crypto = require('crypto');
const kv = require('./_kv');

const ALPHA = 'ABCDEFGHJKMNPQRSTUVWXYZ23456789'; // no 0/O, 1/I/L
const MIN_ORDER = 399;
const MAX_OFF = 500;
// Launch waitlist: 10% off for 7 days from launch day. The code is issued when someone joins, but only works from launchAt.
// TO LAUNCH: set launchAt to the launch moment, e.g. '2026-11-01T00:00:00+05:30', in the same change that makes the new products orderable.
const WL = { pct: 10, days: 7, launchAt: null, maxOff: 1000 };

function norm(code) { return String(code || '').toUpperCase().replace(/[^A-Z0-9]/g, '').replace(/^GNX/, ''); }
function fmt(raw) { return 'GNX-' + raw; }
function phone10(p) { return String(p || '').replace(/\D/g, '').slice(-10); }

function makeRaw() {
  const b = crypto.randomBytes(6);
  let s = '';
  for (let i = 0; i < 6; i++) s += ALPHA[b[i] % ALPHA.length];
  return s;
}

// Creates a code. rec: {off, kind, phone, days, note, order, key}. With 'key', the same key always returns the same code.
async function issue(rec) {
  if (!kv.cfg()) throw new Error('kv_off');
  const pct = Math.floor(Number(rec.pct) || 0);
  const off = pct ? 0 : Math.floor(Number(rec.off));
  if (pct ? !(pct >= 1 && pct <= 30) : !(off >= 10 && off <= MAX_OFF)) throw new Error('bad_amount');
  const ph = phone10(rec.phone);
  if (!/^[6-9]\d{9}$/.test(ph)) throw new Error('bad_phone');
  const days = Math.min(365, Math.max(1, Math.floor(Number(rec.days) || 60)));
  if (rec.key) {
    const prev = await kv.cmd('GET', 'cpn-key:' + rec.key);
    if (prev) { const p = JSON.parse(await kv.cmd('GET', 'cpn:' + prev) || 'null'); if (p) return Object.assign({ code: fmt(prev) }, p); }
  }
  for (let tries = 0; tries < 5; tries++) {
    const raw = makeRaw();
    const data = { off, pct, kind: String(rec.kind || 'manual').slice(0, 20), phone: ph, exp: Date.now() + days * 864e5, note: String(rec.note || '').slice(0, 120), order: String(rec.order || '').slice(0, 60), created: Date.now() };
    const ok = await kv.cmd('SET', 'cpn:' + raw, JSON.stringify(data), 'NX', 'EX', days * 86400 + 86400);
    if (ok) {
      if (rec.key) await kv.cmd('SET', 'cpn-key:' + rec.key, raw, 'EX', days * 86400 + 86400);
      return Object.assign({ code: fmt(raw) }, data);
    }
  }
  throw new Error('issue_failed');
}

// Checks a code for this mobile number and cart total. Returns {ok, code, off} or {ok:false, reason}.
async function check(code, phone, total, lines) {
  const raw = norm(code);
  if (!/^[A-Z0-9]{6}$/.test(raw)) return { ok: false, reason: 'unknown' };
  if (!kv.cfg()) return { ok: false, reason: 'off' };
  const [rec, used] = await kv.pipe([['GET', 'cpn:' + raw], ['GET', 'cpn-used:' + raw]]);
  if (!rec) return { ok: false, reason: 'unknown' };
  const d = JSON.parse(rec);
  if (used) return { ok: false, reason: 'used' };
  if (Date.now() > d.exp) return { ok: false, reason: 'expired' };
  if (d.phone && phone10(phone) !== d.phone) return { ok: false, reason: 'phone' };
  if (Number(total) < MIN_ORDER) return { ok: false, reason: 'min', min: MIN_ORDER };
  if (d.kind === 'waitlist') {
    const L = WL.launchAt ? Date.parse(WL.launchAt) : 0;
    if (!L || Date.now() < L) return { ok: false, reason: 'notyet' };
    if (Date.now() > L + WL.days * 864e5) return { ok: false, reason: 'expired' };
    if (!Array.isArray(lines) || !lines.some((l) => l.id !== 'cream')) return { ok: false, reason: 'product' };
    return { ok: true, code: fmt(raw), off: Math.max(0, Math.min(Math.floor(Number(total) * (d.pct || WL.pct) / 100), WL.maxOff, Number(total) - 199)), pct: d.pct || WL.pct, kind: d.kind, exp: L + WL.days * 864e5 };
  }
  return { ok: true, code: fmt(raw), off: Math.min(d.off, Number(total) - 199), kind: d.kind, exp: d.exp };
}

// Marks a code as used by a paid order. Returns false if another paid order already used it.
async function redeem(code, orderId) {
  const raw = norm(code);
  if (!raw || !kv.cfg()) return false;
  return !!(await kv.cmd('SET', 'cpn-used:' + raw, String(orderId), 'NX', 'EX', 400 * 86400));
}

const REASONS = { unknown: 'This code was not found. Please check it and try again.', used: 'This code has already been used.', notyet: 'This waitlist code works from launch day. We will message you when it opens.', product: 'This waitlist code works on the new launch products.', expired: 'This code has expired.',
  phone: 'This code is linked to a different mobile number. Use the number it was issued to.', min: 'Codes work on orders of ₹' + MIN_ORDER + ' or more.', off: 'Codes are not available right now.' };

module.exports = { issue, check, redeem, norm, fmt, REASONS, MIN_ORDER, WL };
