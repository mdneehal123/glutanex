const { clean, cartFrom } = require('./_shared');
const kv = require('./_kv');

// Saves an unfinished checkout so the shop can help on WhatsApp, only when the customer ticked the consent box.
// status "done" removes it (order placed). Entries expire by themselves after 30 days.
const TTL = 30 * 24 * 3600;

module.exports = async (req, res) => {
  res.setHeader('Cache-Control', 'no-store');
  if (req.method !== 'POST') return res.status(405).json({ ok: false });
  if (!kv.cfg()) return res.status(503).json({ ok: false, error: 'not_configured' });
  let b = req.body || {};
  if (typeof b === 'string') { try { b = JSON.parse(b); } catch (e) { b = {}; } }
  let phone = clean(b.phone, 20).replace(/\D/g, '');
  if (phone.length === 12 && phone.startsWith('91')) phone = phone.slice(2);
  if (!/^[6-9]\d{9}$/.test(phone)) return res.status(400).json({ ok: false, error: 'phone' });
  const key = 'lead:' + phone;
  try {
    if (b.status === 'done' || b.consent === false) {
      await kv.pipe([['DEL', key], ['ZREM', 'leads', phone]]);
      return res.status(200).json({ ok: true });
    }
    if (b.consent !== true) return res.status(400).json({ ok: false, error: 'consent' });
    const cart = cartFrom(b.items);
    const prev = await kv.cmd('GET', key);
    let old = {};
    try { old = prev ? JSON.parse(prev) : {}; } catch (e) { old = {}; }
    const pin = clean(b.pin, 6);
    const lead = {
      phone,
      name: clean(b.name, 80) || old.name || '',
      address: clean(b.address, 250) || old.address || '',
      city: clean(b.city, 60) || old.city || '',
      pin: /^[1-9]\d{5}$/.test(pin) ? pin : (old.pin || ''),
      items: cart ? cart.label : (old.items || ''),
      code: cart ? cart.code : (old.code || ''),
      total: cart ? cart.total : (old.total || 0),
      step: Math.max(1, Math.min(3, Number(b.step) || 1)),
      created: old.created || Date.now(),
      updated: Date.now(),
      contacted: !!old.contacted
    };
    await kv.pipe([['SET', key, JSON.stringify(lead), 'EX', TTL], ['ZADD', 'leads', Date.now(), phone], ['ZREMRANGEBYRANK', 'leads', 0, -501]]);
    return res.status(200).json({ ok: true });
  } catch (e) {
    return res.status(500).json({ ok: false });
  }
};
