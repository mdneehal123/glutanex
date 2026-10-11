const coupons = require('./_coupons');

// GET  /api/coupon?code=GNX-XXXXXX&phone=98xxxxxxxx&total=2499  -> preview a reward code at checkout
// POST /api/coupon  (header x-owner-code)  {phone, off, days, note}  -> owner creates a code (e.g. unboxing reel reward)
module.exports = async (req, res) => {
  res.setHeader('Cache-Control', 'no-store');
  try {
    if (req.method === 'GET') {
      const q = req.query || {};
      const v = await coupons.check(q.code, q.phone, Number(q.total) || 0);
      return res.status(200).json(v.ok ? { ok: true, code: v.code, off: v.off, exp: v.exp } : { ok: false, reason: v.reason, message: coupons.REASONS[v.reason] });
    }
    if (req.method === 'POST') {
      const want = process.env.OWNER_CODE || '';
      if (!want) return res.status(503).json({ ok: false, error: 'owner_code_missing' });
      if (String(req.headers['x-owner-code'] || '') !== want) return res.status(401).json({ ok: false });
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
