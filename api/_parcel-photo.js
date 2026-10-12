const kv = require('./_kv');
const guard = require('./_guard');
const { BRAND, keys } = require('./_shared');

// Owner uploads one photo of the sealed parcel; the buyer sees it on the tracking page ("Packed today in Bhatkal").
// POST (header x-owner-code) {order: 'pay_...' or 'order_...', image: 'data:image/jpeg;base64,...'}
// Photos are kept for 90 days. The tracking API (api/track.js) adds the photo to its answer.
module.exports = async (req, res) => {
  res.setHeader('Cache-Control', 'no-store');
  if (req.method !== 'POST') return res.status(405).json({ ok: false });
  const deny = await guard.owner(req);
  if (deny) return res.status(deny[0]).json(deny[1]);
  if (!kv.cfg()) return res.status(503).json({ ok: false, error: 'database_missing' });
  const k = keys();
  if (!k) return res.status(503).json({ ok: false, error: 'not_configured' });
  let b = req.body || {};
  if (typeof b === 'string') { try { b = JSON.parse(b); } catch (e) { b = {}; } }
  const img = String(b.image || '');
  if (!/^data:image\/(jpeg|webp);base64,[A-Za-z0-9+/=]+$/.test(img) || img.length > 400000) return res.status(400).json({ ok: false, error: 'image' });
  const auth = { Authorization: 'Basic ' + Buffer.from(k.id + ':' + k.secret).toString('base64') };
  try {
    let id = String(b.order || '').trim();
    if (/^pay_\w{6,40}$/.test(id)) {
      const r = await fetch('https://api.razorpay.com/v1/payments/' + id, { headers: auth });
      const p = r.ok ? await r.json() : null;
      id = p && p.order_id ? p.order_id : '';
    }
    if (!/^order_\w{6,40}$/.test(id)) return res.status(404).json({ ok: false, error: 'order_not_found' });
    const r2 = await fetch('https://api.razorpay.com/v1/orders/' + id, { headers: auth });
    const o = r2.ok ? await r2.json() : null;
    if (!o || (o.notes || {}).brand !== BRAND) return res.status(404).json({ ok: false, error: 'order_not_found' });
    await kv.pipe([['SET', 'photo:' + id, img, 'EX', 90 * 86400], ['SET', 'photo-at:' + id, String(Date.now()), 'EX', 90 * 86400]]);
    return res.status(200).json({ ok: true, order: id, name: String((o.notes || {}).name || '').split(' ')[0] });
  } catch (e) {
    return res.status(500).json({ ok: false });
  }
};
