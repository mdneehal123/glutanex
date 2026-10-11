// Proof of purchase: the order must belong to this shop and be paid, and the caller must know its payment id
// (which only the buyer sees). Used by the add-on, scratch card and routine streak.
const { BRAND, keys } = require('./_shared');

function auth(k) { return { Authorization: 'Basic ' + Buffer.from(k.id + ':' + k.secret).toString('base64') }; }

async function paidOrder(orderId, paymentId) {
  const k = keys();
  if (!k) return { err: 'not_configured' };
  if (!/^order_\w{6,40}$/.test(String(orderId)) || !/^pay_\w{6,40}$/.test(String(paymentId))) return { err: 'bad_request' };
  const r = await fetch('https://api.razorpay.com/v1/orders/' + orderId, { headers: auth(k) });
  const o = r.ok ? await r.json() : null;
  if (!o || (o.notes || {}).brand !== BRAND) return { err: 'not_found' };
  const pr = await fetch('https://api.razorpay.com/v1/orders/' + orderId + '/payments', { headers: auth(k) });
  const pays = pr.ok ? await pr.json() : null;
  const p = pays && Array.isArray(pays.items) ? pays.items.find((x) => x.id === paymentId && (x.status === 'captured' || x.status === 'authorized')) : null;
  if (!p) return { err: 'not_found' };
  return { o, p };
}

// Looks up an order from a payment id alone (the order number customers see). Returns the same shape.
async function fromPayment(paymentId) {
  const k = keys();
  if (!k || !/^pay_\w{6,40}$/.test(String(paymentId))) return { err: 'bad_request' };
  const r = await fetch('https://api.razorpay.com/v1/payments/' + paymentId, { headers: auth(k) });
  const p = r.ok ? await r.json() : null;
  if (!p || !p.order_id) return { err: 'not_found' };
  return paidOrder(p.order_id, paymentId);
}

module.exports = { paidOrder, fromPayment };
