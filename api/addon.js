const crypto = require('crypto');
const { PRODUCTS, BRAND, ADVANCE, keys, cartFrom, shipArgs } = require('./_shared');
const shiprocket = require('./_shiprocket');

// After-payment add-on: for 15 minutes after paying, the customer can add the missing half of the Glow Duo
// to the same parcel at the Duo price difference (Face Wash +₹200 to a Night Cream order, Night Cream +₹2,300
// to a Face Wash order). Cash on Delivery orders can add it to the amount paid at the door; others pay online.
// Nothing is stored here: the add-on is recorded on the original Razorpay order (notes), which also makes it
// impossible to add twice.
//   POST {action:'offer', order_id, payment_id}            -> what can be added, price and deadline
//   POST {action:'cod', order_id, payment_id}              -> add to Cash on Delivery
//   POST {action:'create', order_id, payment_id}           -> Razorpay order for paying the add-on online
//   POST {action:'confirm', razorpay_order_id, razorpay_payment_id, razorpay_signature} -> record a paid add-on
const WINDOW = 15 * 60e3;      // shown to the customer
const GRACE = 3 * 60e3;        // small allowance for slow phones

function rp(k) { return { Authorization: 'Basic ' + Buffer.from(k.id + ':' + k.secret).toString('base64'), 'Content-Type': 'application/json' }; }
async function rpGet(k, path) { const r = await fetch('https://api.razorpay.com/v1' + path, { headers: rp(k) }); return r.ok ? r.json() : null; }

function offerFor(n) {
  if (n.kind === 'addon' || n.addon) return null;
  const cart = cartFrom(String(n.items || ''));
  if (!cart) return null;
  const has = (id) => cart.lines.some((l) => l.id === id);
  const item = has('cream') && !has('wash') ? 'wash' : has('wash') && !has('cream') ? 'cream' : null;
  if (!item) return null;
  const after = cartFrom(cart.code + ',' + item + ':1');
  const price = after.total - cart.total;
  if (!(price > 0 && price < PRODUCTS[item].price)) return null;
  return { item, name: PRODUCTS[item].name, price, regular: PRODUCTS[item].price, before: cart, after };
}

// The parent order must belong to this shop, be paid, and the caller must know its payment id (proof of purchase).
async function parent(k, orderId, paymentId, grace) {
  if (!/^order_\w{6,40}$/.test(String(orderId)) || !/^pay_\w{6,40}$/.test(String(paymentId))) return { err: 'bad_request' };
  const o = await rpGet(k, '/orders/' + orderId);
  if (!o || (o.notes || {}).brand !== BRAND) return { err: 'not_found' };
  const pays = await rpGet(k, '/orders/' + orderId + '/payments');
  const p = pays && Array.isArray(pays.items) ? pays.items.find((x) => x.id === paymentId && (x.status === 'captured' || x.status === 'authorized')) : null;
  if (!p) return { err: 'not_found' };
  const until = p.created_at * 1000 + WINDOW;
  return { o, until, open: Date.now() <= until + (grace || GRACE) };
}

function paymentText(n, total, extra) {
  if (n.mode === 'advance') return 'Advance Rs ' + ADVANCE + (extra ? ' + Rs ' + extra + ' add-on' : '') + ' paid online, Rs ' + (total - ADVANCE - extra) + ' cash on delivery';
  return 'Paid in full online' + (extra ? ' (incl. Rs ' + extra + ' add-on)' : '');
}

// Records the add-on on the original order, then updates the Shiprocket order (or ships it separately if that fails).
async function apply(k, o, off, how, addonOrderId) {
  const n = Object.assign({}, o.notes);
  const extra = how === 'online' ? off.price : 0;
  const prevExtra = Math.floor(Number(n.extra_paid || 0));
  n.items = off.after.code;
  n.total = String(off.after.total);
  n.product = (BRAND + ': ' + off.after.label).slice(0, 250);
  n.addon = (off.item + ':1:' + how + ':' + (addonOrderId || 'cod')).slice(0, 250);
  n.extra_paid = String(prevExtra + extra);
  n.payment = paymentText(n, off.after.total, prevExtra + extra).slice(0, 250);
  const r = await fetch('https://api.razorpay.com/v1/orders/' + o.id, { method: 'PATCH', headers: rp(k), body: JSON.stringify({ notes: n }) });
  if (!r.ok) return { ok: false, error: 'record_failed' };
  const updated = Object.assign({}, o, { notes: n });
  let shipping = 'off';
  if (shiprocket.settings()) {
    try {
      shipping = (await shiprocket.updateOrder(shipArgs(updated))).status;
      if (shipping !== 'updated') {
        // already with a courier: send the add-on as its own small parcel instead
        const line = Object.assign({ id: off.item, qty: 1 }, PRODUCTS[off.item], { price: off.price });
        const cart = { lines: [line], total: off.price, kg: PRODUCTS[off.item].kg };
        const a = shipArgs(updated);
        shipping = (await shiprocket.createOrder(Object.assign({}, a, { id: o.id + '-A', cart, cod: how === 'cod', discount: 0, collect: how === 'cod' ? off.price : 0, paid: how === 'cod' ? null : off.price,
          comment: 'Add-on to website order ' + o.id }))).status === 'created' ? 'separate' : 'failed';
      }
    } catch (e) {
      console.error('addon shipping failed', e && e.message);
      shipping = 'failed';
    }
  }
  const args = shipArgs(updated);
  return { ok: true, item: off.item, name: off.name, total: off.after.total - Math.floor(Number(n.coupon_off || 0)), collect: args ? args.collect : 0, shipping };
}

module.exports = async (req, res) => {
  res.setHeader('Cache-Control', 'no-store');
  if (req.method !== 'POST') return res.status(405).json({ ok: false });
  const k = keys();
  if (!k) return res.status(503).json({ ok: false, error: 'not_configured' });
  let b = req.body || {};
  if (typeof b === 'string') { try { b = JSON.parse(b); } catch (e) { b = {}; } }
  try {
    if (b.action === 'confirm') {
      const oid = String(b.razorpay_order_id || ''), pid = String(b.razorpay_payment_id || ''), sig = String(b.razorpay_signature || '');
      const want = crypto.createHmac('sha256', k.secret).update(oid + '|' + pid).digest('hex');
      if (!sig || want.length !== sig.length || !crypto.timingSafeEqual(Buffer.from(want), Buffer.from(sig))) return res.status(400).json({ ok: false });
      const ao = await rpGet(k, '/orders/' + oid);
      const an = (ao && ao.notes) || {};
      if (an.brand !== BRAND || an.kind !== 'addon') return res.status(400).json({ ok: false });
      const o = await rpGet(k, '/orders/' + an.parent);
      if (!o) return res.status(404).json({ ok: false });
      if (String((o.notes || {}).addon || '').indexOf(oid) >= 0) return res.status(200).json({ ok: true, already: true });
      const off = offerFor(o.notes || {});
      if (!off || off.item !== an.item || off.price * 100 !== ao.amount) return res.status(409).json({ ok: false, error: 'changed' });
      return res.status(200).json(await apply(k, o, off, 'online', oid));
    }
    const isCreate = b.action === 'create';
    const pr = await parent(k, b.order_id, b.payment_id);
    if (pr.err) return res.status(404).json({ ok: false, error: pr.err });
    const off = offerFor(pr.o.notes || {});
    if (!off || !pr.open) return res.status(200).json({ ok: false, error: off ? 'expired' : 'none' });
    const cod = (pr.o.notes || {}).mode === 'advance';
    if (b.action === 'offer') return res.status(200).json({ ok: true, item: off.item, name: off.name, price: off.price, regular: off.regular, until: pr.until, cod });
    if (b.action === 'cod') {
      if (!cod) return res.status(400).json({ ok: false, error: 'not_cod' });
      return res.status(200).json(await apply(k, pr.o, off, 'cod'));
    }
    if (isCreate) {
      const n = pr.o.notes || {};
      const r = await fetch('https://api.razorpay.com/v1/orders', { method: 'POST', headers: rp(k), body: JSON.stringify({
        amount: off.price * 100, currency: 'INR', receipt: 'gn_addon_' + Date.now(),
        notes: { brand: BRAND, kind: 'addon', parent: pr.o.id, item: off.item, product: BRAND + ' add-on: ' + off.name, name: n.name, phone: n.phone }
      }) });
      const d = await r.json();
      if (!r.ok || !d.id) return res.status(502).json({ ok: false, error: 'gateway_error' });
      return res.status(200).json({ ok: true, order_id: d.id, amount: d.amount, currency: d.currency, key_id: k.id });
    }
    return res.status(400).json({ ok: false });
  } catch (e) {
    return res.status(500).json({ ok: false });
  }
};
