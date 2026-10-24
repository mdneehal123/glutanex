const { clean } = require('./_shared');
const kv = require('./_kv');
const guard = require('./_guard');
const desk = require('./_orderdesk');
const coupons = require('./_coupons');

// Launch waitlist. POST {phone, name?, product, consent:true}. Only with consent: the number goes to the Order Desk customer list
// (Not bought yet), and the person gets a personal 10% launch code that works for 7 days from launch day (see WL in _coupons.js).
const NAMES = { all: 'all new products', gel: 'Aqua Fresh Shower Gel', wash: 'Gluta Boost Face Wash', duo: 'Glow Duo', washgel: 'Face Wash + Shower Gel combo',
  creamgel: 'Night Cream + Shower Gel combo', trio: 'Glow Trio' };
const TTL = 400 * 24 * 3600;

module.exports = async (req, res) => {
  res.setHeader('Cache-Control', 'no-store');
  if (req.method !== 'POST') return res.status(405).json({ ok: false });
  if (!kv.cfg()) return res.status(503).json({ ok: false, error: 'not_configured' });
  let b = req.body || {};
  if (typeof b === 'string') { try { b = JSON.parse(b); } catch (e) { b = {}; } }
  let phone = clean(b.phone, 20).replace(/\D/g, '');
  if (phone.length === 12 && phone.startsWith('91')) phone = phone.slice(2);
  if (!/^[6-9]\d{9}$/.test(phone)) return res.status(400).json({ ok: false, error: 'phone' });
  if (b.consent !== true) return res.status(400).json({ ok: false, error: 'consent' });
  const product = NAMES[b.product] ? String(b.product) : 'all';
  if (!(await guard.limit('wl:' + phone, 10, 3600)) || !(await guard.limit('wl', 3000, 86400))) return res.status(429).json({ ok: false, error: 'busy' });
  try {
    const key = 'wl:' + phone;
    let old = null;
    try { old = JSON.parse((await kv.cmd('GET', key)) || 'null'); } catch (e) { old = null; }
    const products = Array.from(new Set(((old && old.products) || []).concat(product)));
    const rec = { phone, name: clean(b.name, 80) || (old && old.name) || '', products, created: (old && old.created) || Date.now(), updated: Date.now() };
    await kv.cmd('SET', key, JSON.stringify(rec), 'EX', TTL);
    let code = '';
    try { code = (await coupons.issue({ pct: coupons.WL.pct, phone, kind: 'waitlist', days: 400, key: 'wl:' + phone, note: 'launch waitlist' })).code; } catch (e) { code = ''; }
    if (!old || !(old.products || []).includes(product)) { try { await desk.pushLead({ phone, name: rec.name, product: 'Launch waitlist: ' + NAMES[product] }); } catch (e) { /* never blocks */ } }
    return res.status(200).json({ ok: true, code, pct: coupons.WL.pct, days: coupons.WL.days });
  } catch (e) {
    return res.status(500).json({ ok: false });
  }
};
