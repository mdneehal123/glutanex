const crypto = require('crypto');
const { keys, shipArgs, customer } = require('./_shared');
const coupons = require('./_coupons');
const { pushToDesk } = require('./_orderdesk');

// Paid online orders: checks the Razorpay signature, confirms with Razorpay that the payment is really captured
// for this order and for the server price, marks the reward code as used, then puts the order into the
// Order Desk as PAID. Paid orders are NOT booked with Delhivery here (the Order Desk handles them).
function auth(k) { return { Authorization: 'Basic ' + Buffer.from(k.id + ':' + k.secret).toString('base64') }; }
async function rpGet(k, path) {
  try { const r = await fetch('https://api.razorpay.com/v1' + path, { headers: auth(k) }); return r.ok ? await r.json() : null; } catch (e) { return null; }
}

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

  const [p, o] = await Promise.all([rpGet(k, '/payments/' + encodeURIComponent(paymentId)), rpGet(k, '/orders/' + encodeURIComponent(orderId))]);
  if (p && (p.order_id !== orderId || !(p.status === 'captured' || p.status === 'authorized'))) {
    return res.status(400).json({ ok: false, error: 'not_paid', status: p.status });
  }
  const args = o ? shipArgs(o) : null;
  if (!args) {
    // Signed by Razorpay, but the order details could not be read: the customer has paid, so never show an error.
    console.error('paid order lookup failed', orderId, paymentId);
    return res.status(200).json({ ok: true, savedToDesk: false });
  }
  const confirmed = !!p;
  const charged = confirmed ? p.amount / 100 : args.cart.total - args.off;
  const priced = args.cart.total - args.off; // server price (cart from the fixed price table, minus the reward code)
  const warn = [];
  if (!confirmed) warn.push('⚠ could not confirm the payment with Razorpay: check the dashboard before shipping');
  if (confirmed && p.amount !== priced * 100) warn.push('⚠ amount ₹' + charged + ' differs from the price ₹' + priced);

  if (args.coupon && confirmed) {
    try { if (!(await coupons.redeem(args.coupon, orderId))) console.error('reward code reused', args.coupon, orderId); } catch (e) { console.error('redeem failed', e && e.message); }
  }

  const c = customer({ name: args.name, phone: args.phone, address: args.address, city: args.city, pincode: args.pincode }) ||
    { name: String(args.name || ''), phone: String(args.phone || ''), address: String(args.address || ''), city: String(args.city || ''), pin: String(args.pincode || ''), state: '' };
  const ref = args.ref || ('GX' + orderId.replace(/^order_/, '').toUpperCase()).slice(0, 20);
  const desk = await pushToDesk({
    ref, c, lines: args.cart.lines, sub: args.cart.total, disc: args.off, coupon: args.coupon, total: charged,
    pay: 'upi', paid: confirmed, payId: paymentId,
    note: ['Paid online via Razorpay' + (confirmed && p.method ? ' (' + p.method + ')' : '') + ' ' + paymentId + ' · ' + orderId].concat(args.coupon ? ['reward code ' + args.coupon + ' −₹' + args.off] : [], warn).join(' · ')
  });
  if (!desk.ok) console.error('order desk push failed', ref, orderId, desk.error);
  return res.status(200).json({ ok: true, ref, savedToDesk: desk.ok });
};
