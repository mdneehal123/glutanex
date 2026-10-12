const crypto = require('crypto');
const kv = require('./_kv');
const coupons = require('./_coupons');
const { fromPayment } = require('./_proof');
const guard = require('./_guard');

// Routine streak: buyers tap "Done tonight" after applying the Night Cream. One tap counts per day (India time,
// decided here on the server, so dates cannot be faked). 56 nights unlock a ₹200 code for the next order.
// Tied to a real paid order: joining needs the order number (payment id) and the mobile number on that order.
//   streak:<orderId>   -> {phone, start, dates:[YYYY-MM-DD...], token, claimed}
//   streak-tok:<token> -> orderId
const GOAL = 56, REWARD = 200, TTL = 200 * 86400;
const today = () => new Date(Date.now() + 5.5 * 3600e3).toISOString().slice(0, 10);

function view(s) {
  const d = s.dates || [];
  let streak = 0;
  const day = (x) => Math.round(Date.parse(x + 'T00:00:00Z') / 864e5);
  const t = day(today());
  if (d.length && t - day(d[d.length - 1]) <= 1) {
    streak = 1;
    for (let i = d.length - 1; i > 0; i--) { if (day(d[i]) - day(d[i - 1]) === 1) streak++; else break; }
  }
  return { ok: true, nights: d.length, goal: GOAL, reward: REWARD, streak, doneToday: d[d.length - 1] === today(), recent: d.slice(-GOAL), start: s.start, claimed: s.claimed || null };
}

async function load(token) {
  if (!/^[a-f0-9]{32}$/.test(String(token))) return null;
  const id = await kv.cmd('GET', 'streak-tok:' + token);
  if (!id) return null;
  const raw = await kv.cmd('GET', 'streak:' + id);
  return raw ? { id, s: JSON.parse(raw) } : null;
}

module.exports = async (req, res) => {
  res.setHeader('Cache-Control', 'no-store');
  if (!kv.cfg()) return res.status(503).json({ ok: false, error: 'not_configured' });
  let b = req.method === 'GET' ? (req.query || {}) : (req.body || {});
  if (typeof b === 'string') { try { b = JSON.parse(b); } catch (e) { b = {}; } }
  try {
    if (b.action === 'join') {
      if (!(await guard.limit('rt:' + String(b.order || '').slice(0, 40), 10, 3600)) || !(await guard.limit('rt', 2000, 3600))) return res.status(429).json({ ok: false, error: 'busy' });
      const pr = await fromPayment(String(b.order || '').trim());
      if (pr.err) return res.status(404).json({ ok: false, error: 'order_not_found' });
      const n = pr.o.notes || {};
      const phone = String(b.phone || '').replace(/\D/g, '').slice(-10);
      if (!n.phone || phone !== String(n.phone).replace(/\D/g, '').slice(-10)) return res.status(403).json({ ok: false, error: 'phone_mismatch' });
      if (!/(^|,)(cream|duo):/.test(String(n.items || ''))) return res.status(400).json({ ok: false, error: 'no_cream' });
      const key = 'streak:' + pr.o.id;
      let s = JSON.parse((await kv.cmd('GET', key)) || 'null');
      if (!s) {
        s = { phone, start: today(), dates: [], token: crypto.randomBytes(16).toString('hex'), claimed: null };
        await kv.pipe([['SET', key, JSON.stringify(s), 'EX', TTL], ['SET', 'streak-tok:' + s.token, pr.o.id, 'EX', TTL]]);
      }
      return res.status(200).json(Object.assign(view(s), { token: s.token }));
    }
    const got = await load(b.token);
    if (!got) return res.status(404).json({ ok: false, error: 'unknown' });
    const { id, s } = got;
    if (b.action === 'checkin') {
      const d = today();
      if (s.dates[s.dates.length - 1] !== d) {
        s.dates.push(d);
        if (s.dates.length > 120) s.dates = s.dates.slice(-120);
        await kv.cmd('SET', 'streak:' + id, JSON.stringify(s), 'KEEPTTL');
      }
      return res.status(200).json(view(s));
    }
    if (b.action === 'claim') {
      if (s.dates.length < GOAL) return res.status(400).json(Object.assign(view(s), { ok: false, error: 'not_yet' }));
      const c = await coupons.issue({ off: REWARD, phone: s.phone, days: 60, kind: 'streak', order: id, key: 'streak:' + id });
      if (!s.claimed) { s.claimed = { code: c.code, exp: c.exp }; await kv.cmd('SET', 'streak:' + id, JSON.stringify(s), 'KEEPTTL'); }
      return res.status(200).json(Object.assign(view(s), { code: c.code, off: c.off, exp: c.exp }));
    }
    return res.status(200).json(view(s));
  } catch (e) {
    return res.status(500).json({ ok: false });
  }
};
