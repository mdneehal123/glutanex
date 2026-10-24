// POST /api/cod-order — Cash on Delivery with nothing paid upfront.
// The price (and any reward code) is worked out here on the server, Delhivery is checked for the pincode,
// the shipment is booked with Delhivery, and the order is ALWAYS saved in the Order Desk
// (with the Delhivery tracking number when booked, or flagged for manual booking when not).
// Served through api/hub.js (vercel.json rewrites /api/cod-order) to stay inside the Vercel Hobby function limit.
const { cartFrom, customer, orderRef } = require('./_shared');
const coupons = require('./_coupons');
const guard = require('./_guard');
const kv = require('./_kv');
const { delhiveryOn, serviceable, createShipment } = require('./_delhivery');
const { pushToDesk, deskOn } = require('./_orderdesk');

const KEEP = 120 * 86400; // how long the order record is kept for tracking (seconds)

async function kvGet(key) { if (!kv.cfg()) return null; try { return JSON.parse((await kv.cmd('GET', key)) || 'null'); } catch (e) { return null; } }

module.exports = async (req, res) => {
  res.setHeader('Cache-Control', 'no-store');
  if (req.method !== 'POST') return res.status(405).json({ error: 'method_not_allowed' });
  let body = req.body || {};
  if (typeof body === 'string') { try { body = JSON.parse(body); } catch (e) { body = {}; } }
  if (body.website) return res.status(200).json({ ok: true }); // form trap for bots
  const cart = cartFrom(body.items, true);
  const c = customer(body);
  if (!cart || !c) return res.status(400).json({ error: 'invalid_details' });
  // Without Delhivery and without the Order Desk the order could not be saved anywhere: the page offers WhatsApp instead.
  if (!delhiveryOn() && !deskOn()) return res.status(503).json({ error: 'not_configured' });
  // Public endpoint that books real shipments: limited per mobile number and for the whole shop.
  if (!(await guard.limit('cod:' + c.phone, 6, 3600)) || !(await guard.limit('cod', 300, 3600))) return res.status(429).json({ error: 'busy' });

  const ref = orderRef(body.ref);
  // The same checkout sent twice (double tap, slow network) gets the first answer back instead of a second parcel.
  if (kv.cfg()) {
    try {
      const fresh = await kv.cmd('SET', 'codord:' + ref, JSON.stringify({ pending: true, phone: c.phone }), 'NX', 'EX', KEEP);
      if (!fresh) {
        const prev = await kvGet('codord:' + ref);
        if (prev && prev.result && prev.phone === c.phone) return res.status(200).json(prev.result);
        return res.status(409).json({ error: 'in_progress' });
      }
    } catch (e) { /* database hiccup: carry on, Order Desk still de-duplicates by order number */ }
  }
  const release = async () => { if (kv.cfg()) { try { await kv.cmd('DEL', 'codord:' + ref); } catch (e) { /* ignore */ } } };

  // Reward code: checked here; marked as used only once the order is placed (below).
  let off = 0, code = '';
  if (body.coupon) {
    const v = await coupons.check(body.coupon, c.phone, cart.total, cart.lines).catch(() => ({ ok: false, reason: 'off' }));
    if (!v.ok) { await release(); return res.status(400).json({ error: 'coupon', reason: v.reason, message: coupons.REASONS[v.reason] || 'This code cannot be used.' }); }
    off = v.off; code = v.code;
  }
  const total = cart.total - off;

  let d = { ok: false, error: 'Delhivery is not set up on the website (DELHIVERY_TOKEN / DELHIVERY_PICKUP missing)' };
  if (delhiveryOn()) {
    try {
      const s = await serviceable(c.pin);
      if (!s.cod) {
        await release();
        return res.status(409).json({ error: 'cod_unavailable', codUnavailable: true, message: 'Cash on Delivery is not available for pincode ' + c.pin + '. Please pay online instead.' });
      }
    } catch (e) { /* if the check itself fails, still try to book */ }
    try { d = await createShipment({ ref, c, cart, total, pay: 'cod' }); } catch (e) { d = { ok: false, error: String((e && e.message) || e) }; }
  }

  const lines = cart.lines;
  const order = { ref, c, lines, sub: cart.total, disc: off, coupon: code, total, pay: 'cod', paid: false };
  const codeNote = code ? ' · reward code ' + code + ' −₹' + off : '';
  const desk = await pushToDesk(d.ok
    ? Object.assign(order, { courier: 'Delhivery', awb: d.awb, note: 'COD booked with Delhivery · AWB ' + d.awb + ' · print the label from the Delhivery panel' + codeNote })
    : Object.assign(order, { note: '⚠ COD website order — Delhivery booking failed: ' + d.error + '. Please book it in Delhivery.' + codeNote }));
  if (!desk.ok) console.error('order desk push failed', ref, desk.error);

  if (!d.ok && !desk.ok) {
    // Not booked and not saved: never tell the customer it worked. Log it so it can be recovered, and let the page offer WhatsApp.
    console.error('COD order NOT saved', JSON.stringify({ ref, name: c.name, phone: c.phone, pin: c.pin, items: cart.code, total, coupon: code, delhivery: d.error, desk: desk.error }));
    await release();
    return res.status(502).json({ error: 'not_saved' });
  }

  // The order is placed: now the reward code counts as used.
  if (code) {
    try { if (!(await coupons.redeem(code, ref))) console.error('reward code reused', code, ref); } catch (e) { console.error('redeem failed', e && e.message); }
  }

  const result = { ok: true, ref, total, off, awb: d.ok ? d.awb : '', courier: d.ok ? 'Delhivery' : '', pending: !d.ok, savedToDesk: desk.ok,
    trackUrl: d.ok ? 'https://www.delhivery.com/track/package/' + d.awb : '' };
  if (kv.cfg()) {
    // Kept for the tracking page (order number, or mobile number + pincode) and for retries of the same checkout.
    const rec = { result, phone: c.phone, pin: c.pin, awb: result.awb, items: cart.code, total, at: Date.now() };
    try { await kv.pipe([['SET', 'codord:' + ref, JSON.stringify(rec), 'EX', KEEP], ['SET', 'codp:' + c.phone + ':' + c.pin, JSON.stringify({ ref, at: rec.at }), 'EX', KEEP]]); } catch (e) { /* tracking falls back to the AWB */ }
  }
  return res.status(200).json(result);
};
