const { BRAND, keys, cartFrom, customer, orderRef } = require('./_shared');
const coupons = require('./_coupons');
const guard = require('./_guard');

// Creates a Razorpay order for the full amount of the cart. The amount is worked out here from the fixed price table.
// (Cash on Delivery has nothing to pay online: it goes to api/cod-order instead.)
module.exports = async (req, res) => {
  res.setHeader('Cache-Control', 'no-store');
  if (req.method !== 'POST') return res.status(405).json({ error: 'method_not_allowed' });
  const k = keys();
  if (!k) return res.status(503).json({ error: 'not_configured' });
  let body = req.body || {};
  if (typeof body === 'string') { try { body = JSON.parse(body); } catch (e) { body = {}; } }
  const cart = cartFrom(body.items);
  const c = customer(body);
  if (!cart || !c) return res.status(400).json({ error: 'invalid_details' });
  if (!(await guard.limit('order:' + c.phone, 15, 3600)) || !(await guard.limit('order', 1000, 3600))) return res.status(429).json({ error: 'busy' });
  // reward code: checked here on the server; it is only marked as used once the payment succeeds (api/verify.js)
  let off = 0, code = '';
  if (body.coupon) {
    const v = await coupons.check(body.coupon, c.phone, cart.total).catch(() => ({ ok: false, reason: 'off' }));
    if (!v.ok) return res.status(400).json({ error: 'coupon', reason: v.reason, message: coupons.REASONS[v.reason] || 'This code cannot be used.' });
    off = v.off; code = v.code;
  }
  let payable = cart.total - off;
  // Owner test: when TEST_ONE_RUPEE_PHONE (Vercel setting) matches this mobile number, the online payment is ₹1.
  // The Order Desk entry then shows a warning that ₹1 differs from the price. Delete the setting after testing.
  const testPhone = String(process.env.TEST_ONE_RUPEE_PHONE || '').replace(/\D/g, '').slice(-10);
  const isTest = /^[6-9]\d{9}$/.test(testPhone) && testPhone === c.phone;
  if (isTest) payable = 1;
  const ref = orderRef(body.ref);
  try {
    const r = await fetch('https://api.razorpay.com/v1/orders', {
      method: 'POST',
      headers: { Authorization: 'Basic ' + Buffer.from(k.id + ':' + k.secret).toString('base64'), 'Content-Type': 'application/json' },
      body: JSON.stringify({
        amount: payable * 100, currency: 'INR', receipt: ref,
        notes: {
          brand: BRAND, ref, product: BRAND + ': ' + cart.label.slice(0, 200), items: cart.code, total: String(cart.total),
          name: c.name, phone: c.phone, address: c.address, city: c.city, pincode: c.pin,
          payment: (isTest ? 'OWNER TEST Rs 1 · ' : '') + 'Paid in full online' + (off ? ' (code ' + code + ' -Rs ' + off + ')' : ''),
          coupon: code, coupon_off: String(off)
        }
      })
    });
    const data = await r.json();
    if (!r.ok || !data.id) return res.status(502).json({ error: 'gateway_error' });
    return res.status(200).json({ order_id: data.id, amount: data.amount, currency: data.currency, key_id: k.id, total: payable, off, ref });
  } catch (e) {
    return res.status(502).json({ error: 'gateway_unreachable' });
  }
};
