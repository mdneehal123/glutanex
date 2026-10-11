const crypto = require('crypto');
const { keys, shipArgs } = require('./_shared');
const shiprocket = require('./_shiprocket');
const coupons = require('./_coupons');
const kv = require('./_kv');

// Confirms that a payment reported by the browser was really signed by Razorpay, then hands it to Shiprocket.
module.exports = async (req, res) => {
  res.setHeader('Cache-Control', 'no-store');
  if (req.method !== 'POST') return res.status(405).json({ error: 'method_not_allowed' });
  const k = keys();
  if (!k) return res.status(503).json({ error: 'not_configured' });
  let body = req.body || {};
  if (typeof body === 'string') { try { body = JSON.parse(body); } catch (e) { body = {}; } }
  const orderId = String(body.razorpay_order_id || '');
  const paymentId = String(body.razorpay_payment_id || '');
  const signature = String(body.razorpay_signature || '');
  if (!orderId || !paymentId || !signature) return res.status(400).json({ ok: false });
  const expected = crypto.createHmac('sha256', k.secret).update(orderId + '|' + paymentId).digest('hex');
  const a = Buffer.from(expected), b = Buffer.from(signature);
  if (!(a.length === b.length && crypto.timingSafeEqual(a, b))) return res.status(400).json({ ok: false });
  // A shipping problem must never turn a successful payment into an error for the customer.
  let shipping = 'off', o = null;
  if (shiprocket.settings() || kv.cfg()) {
    try {
      const r = await fetch('https://api.razorpay.com/v1/orders/' + encodeURIComponent(orderId), {
        headers: { Authorization: 'Basic ' + Buffer.from(k.id + ':' + k.secret).toString('base64') }
      });
      o = r.ok ? await r.json() : null;
    } catch (e) { o = null; }
  }
  if (o && (o.notes || {}).coupon) {
    try { if (!(await coupons.redeem(o.notes.coupon, orderId))) console.error('reward code reused', o.notes.coupon, orderId); } catch (e) { console.error('redeem failed', e && e.message); }
  }
  if (shiprocket.settings()) {
    try {
      const args = o ? shipArgs(o) : null;
      if (!args) throw new Error('order_lookup_failed');
      shipping = (await shiprocket.createOrder(args)).status;
    } catch (e) {
      console.error('shipping hand-off failed', e && e.message, JSON.stringify((e && e.detail) || {}));
      shipping = 'failed';
    }
  }
  return res.status(200).json({ ok: true, shipping });
};
