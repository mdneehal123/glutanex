// GlutaNex store: prices are fixed here, on the server, so the amount charged cannot be changed from the browser.
// Prices confirmed 11 Oct 2026. They must match _build/build.py.
const PRODUCTS = {
  cream: { name: 'GlutaNex Glutathione Night Cream 30g', sku: 'GNX-CREAM', price: 2499, mrp: 3000, kg: 0.12 },
  wash: { name: 'GlutaNex Gluta Boost Face Wash 100ml', sku: 'GNX-WASH-100', price: 399, mrp: 599, kg: 0.14 },
  duo: { name: 'GlutaNex Glow Duo: Night Cream + Face Wash', sku: 'GNX-DUOx2', price: 2699, mrp: 3599, kg: 0.26 }
};
const BRAND = 'GlutaNex';
// Cash on Delivery needs this much paid online in advance (refunded if cancelled, refused or undeliverable).
const ADVANCE = 99;
const MAX_QTY = 10;

function keys() {
  const id = process.env.RAZORPAY_KEY_ID;
  const secret = process.env.RAZORPAY_KEY_SECRET;
  return id && secret ? { id, secret } : null;
}

function clean(value, max) {
  return String(value == null ? '' : value).replace(/\s+/g, ' ').trim().slice(0, max);
}

// Accepts [{id, qty}] or the compact "cream:2,wash:1" form stored on the order. Unknown items are dropped.
function cartFrom(input) {
  let list = input;
  if (typeof input === 'string') list = input.split(',').map((s) => { const [id, q] = s.split(':'); return { id, qty: q }; });
  if (!Array.isArray(list)) return null;
  const merged = {};
  list.forEach((it) => {
    const id = String((it && it.id) || '');
    const qty = Math.floor(Number(it && it.qty));
    if (!PRODUCTS[id] || !(qty >= 1)) return;
    merged[id] = Math.min(MAX_QTY, (merged[id] || 0) + qty);
  });
  // A Night Cream plus a Face Wash is always charged as the cheaper Glow Duo (same as the cart on the site).
  const pairs = Math.min(merged.cream || 0, merged.wash || 0);
  if (pairs > 0) {
    merged.cream -= pairs; merged.wash -= pairs; merged.duo = Math.min(MAX_QTY, (merged.duo || 0) + pairs);
    if (!merged.cream) delete merged.cream;
    if (!merged.wash) delete merged.wash;
  }
  const lines = Object.keys(merged).map((id) => Object.assign({ id, qty: merged[id] }, PRODUCTS[id]));
  if (!lines.length) return null;
  const total = lines.reduce((a, l) => a + l.price * l.qty, 0);
  const mrp = lines.reduce((a, l) => a + l.mrp * l.qty, 0);
  const kg = lines.reduce((a, l) => a + l.kg * l.qty, 0);
  const code = lines.map((l) => l.id + ':' + l.qty).join(',');
  const label = lines.map((l) => l.name + (l.qty > 1 ? ' x' + l.qty : '')).join('; ');
  return { lines, total, mrp, kg, code, label };
}

function shipArgs(o) {
  const n = (o && o.notes) || {};
  if (n.brand !== BRAND) return null;
  const cart = cartFrom(String(n.items || ''));
  if (!cart || !n.name) return null;
  const advance = n.mode === 'advance';
  // extra_paid: money paid online after the order (the after-payment add-on), so the courier collects less
  const extra = Math.max(0, Math.floor(Number(n.extra_paid || 0)));
  const off = Math.max(0, Math.floor(Number(n.coupon_off || 0))); // reward code discount
  return { id: o.id, cart, name: n.name, phone: n.phone, address: n.address, city: n.city, pincode: n.pincode,
    cod: advance, discount: (advance ? ADVANCE + extra : 0) + off, collect: advance ? cart.total - ADVANCE - extra - off : 0,
    paid: advance ? null : cart.total - off };
}

module.exports = { PRODUCTS, BRAND, ADVANCE, keys, clean, cartFrom, shipArgs };
