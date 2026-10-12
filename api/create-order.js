const { BRAND, ADVANCE, keys, clean, cartFrom } = require('./_shared');
const coupons = require('./_coupons');
const guard = require('./_guard');

// Creates a Razorpay order for the cart. The amount is worked out here from the fixed price table.
module.exports = async (req, res) => {
  res.setHeader('Cache-Control', 'no-store');
  if (req.method !== 'POST') return res.status(405).json({ error: 'method_not_allowed' });
  const k = keys();
  if (!k) return res.status(503).json({ error: 'not_configured' });
  let body = req.body || {};
  if (typeof body === 'string') { try { body = JSON.parse(body); } catch (e) { body = {}; } }
  const cart = cartFrom(body.items);
  const name = clean(body.name, 80);
  const phone = clean(body.phone, 20).replace(/\D/g, '').slice(-10);
  const address = clean(body.address, 250);
  const city = clean(body.city, 60);
  const pincode = clean(body.pincode, 6);
  if (!cart || name.length < 2 || !/^[6-9]\d{9}$/.test(phone) || address.length < 8 || city.length < 2 || !/^[1-9]\d{5}$/.test(pincode)) {
    return res.status(400).json({ error: 'invalid_details' });
  }
  if (!(await guard.limit('order:' + phone, 15, 3600)) || !(await guard.limit('order', 1000, 3600))) return res.status(429).json({ error: 'busy' });
  const advance = body.mode === 'advance';
  // reward code: checked here on the server; it is only marked as used once the payment succeeds (api/verify.js)
  let off = 0, code = '';
  if (body.coupon) {
    const v = await coupons.check(body.coupon, phone, cart.total).catch(() => ({ ok: false, reason: 'off' }));
    if (!v.ok) return res.status(400).json({ error: 'coupon', reason: v.reason, message: coupons.REASONS[v.reason] || 'This code cannot be used.' });
    off = v.off; code = v.code;
  }
  const payable = cart.total - off;
  const amount = (advance ? ADVANCE : payable) * 100;
  const balance = advance ? payable - ADVANCE : 0;
  try {
    const r = await fetch('https://api.razorpay.com/v1/orders', {
      method: 'POST',
      headers: { Authorization: 'Basic ' + Buffer.from(k.id + ':' + k.secret).toString('base64'), 'Content-Type': 'application/json' },
      body: JSON.stringify({
        amount, currency: 'INR', receipt: 'gn_' + Date.now(),
        notes: {
          brand: BRAND, product: BRAND + ': ' + cart.label.slice(0, 200), items: cart.code, total: String(cart.total),
          name, phone, address, city, pincode, mode: advance ? 'advance' : 'full',
          payment: (advance ? 'Advance Rs ' + ADVANCE + ' paid, Rs ' + balance + ' cash on delivery' : 'Paid in full online') + (off ? ' (code ' + code + ' -Rs ' + off + ')' : ''),
          coupon: code, coupon_off: String(off)
        }
      })
    });
    const data = await r.json();
    if (!r.ok || !data.id) return res.status(502).json({ error: 'gateway_error' });
    return res.status(200).json({ order_id: data.id, amount: data.amount, currency: data.currency, key_id: k.id, total: payable, off, balance });
  } catch (e) {
    return res.status(502).json({ error: 'gateway_unreachable' });
  }
};
