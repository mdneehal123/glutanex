const coupons = require('./_coupons');
const { cartFrom } = require('./_shared');
const guard = require('./_guard');

// GET  /api/coupon?code=GNX-XXXXXX&phone=98xxxxxxxx&total=2499  -> preview a reward code at checkout
// POST /api/coupon  (header x-owner-code)  {phone, off, days, note}  -> owner creates a code (e.g. unboxing reel reward)
module.exports = async (req, res) => {
  res.setHeader('Cache-Control', 'no-store');
  try {
    if (req.method === 'GET') {
      const q = req.query || {};
      const ph = String(q.phone || '').replace(/\D/g, '').slice(-10);
      if (!(await guard.limit('cpn:' + ph, 20, 3600)) || !(await guard.limit('cpn', 3000, 3600))) return res.status(429).json({ ok: false, reason: 'busy', message: 'Too many tries. Please wait a while and try again.' });
      const cart = q.items ? cartFrom(String(q.items), true) : null;
      const v = await coupons.check(q.code, q.phone, Number(q.total) || 0, cart ? cart.lines : []);
      return res.status(200).json(v.ok ? { ok: true, code: v.code, off: v.off, pct: v.pct || 0, exp: v.exp } : { ok: false, reason: v.reason, message: coupons.REASONS[v.reason] });
    }
    if (req.method === 'POST') {
      const deny = await guard.owner(req);
      if (deny) return res.status(deny[0]).json(deny[1]);
      let b = req.body || {};
      if (typeof b === 'string') { try { b = JSON.parse(b); } catch (e) { b = {}; } }
      const c = await coupons.issue({ off: b.off, phone: b.phone, days: b.days || 60, kind: b.kind || 'manual', note: b.note });
      return res.status(200).json({ ok: true, code: c.code, off: c.off, exp: c.exp, phone: c.phone });
    }
    return res.status(405).json({ ok: false });
  } catch (e) {
    const m = String(e && e.message);
    return res.status(m === 'kv_off' ? 503 : 400).json({ ok: false, error: m });
  }
};
