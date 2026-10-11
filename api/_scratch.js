const coupons = require('./_coupons');
const { paidOrder } = require('./_proof');

// Scratch card on the thank-you page: one reward code per paid order, for the NEXT order.
// ₹50 to ₹150 (most cards ₹50–100), valid 60 days, linked to the buyer's mobile number. Asking again returns the same card.
const PRIZES = [[50, 40], [75, 25], [100, 25], [150, 10]];
function pick() { let r = Math.random() * 100; for (const [v, w] of PRIZES) { if ((r -= w) < 0) return v; } return 50; }

module.exports = async (req, res) => {
  res.setHeader('Cache-Control', 'no-store');
  if (req.method !== 'POST') return res.status(405).json({ ok: false });
  let b = req.body || {};
  if (typeof b === 'string') { try { b = JSON.parse(b); } catch (e) { b = {}; } }
  try {
    const pr = await paidOrder(b.order_id, b.payment_id);
    if (pr.err) return res.status(pr.err === 'not_configured' ? 503 : 404).json({ ok: false });
    const n = pr.o.notes || {};
    if (n.kind === 'addon') return res.status(200).json({ ok: false });
    const c = await coupons.issue({ off: pick(), phone: n.phone, days: 60, kind: 'scratch', order: pr.o.id, key: 'scratch:' + pr.o.id });
    return res.status(200).json({ ok: true, code: c.code, off: c.off, exp: c.exp, phone: String(c.phone).slice(-4) });
  } catch (e) {
    return res.status(String(e && e.message) === 'kv_off' ? 503 : 500).json({ ok: false });
  }
};
