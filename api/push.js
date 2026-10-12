const crypto = require('crypto');
const kv = require('./_kv');
const push = require('./_push');
const guard = require('./_guard');

// App reminders: GET returns the public key; POST subscribes, updates or unsubscribes a phone.
// Stored per subscription (30-day rolling expiry refreshed by the daily job): which reminders are on and the dates they start.
const DAY = 864e5;

function idOf(endpoint) { return crypto.createHash('sha256').update(String(endpoint)).digest('hex').slice(0, 32); }

module.exports = async (req, res) => {
  res.setHeader('Cache-Control', 'no-store');
  if (!kv.cfg()) return res.status(503).json({ ok: false, error: 'not_configured' });
  try {
    if (req.method === 'GET') return res.status(200).json({ ok: true, key: (await push.vapid()).pub });
    if (req.method !== 'POST') return res.status(405).json({ ok: false });
    if (!(await guard.limit('push', 1000, 3600))) return res.status(429).json({ ok: false, error: 'busy' });
    let b = req.body || {};
    if (typeof b === 'string') { try { b = JSON.parse(b); } catch (e) { b = {}; } }
    const sub = b.sub || {};
    if (!/^https:\/\//.test(String(sub.endpoint || '')) || !sub.keys || !sub.keys.p256dh || !sub.keys.auth || String(sub.endpoint).length > 800) {
      return res.status(400).json({ ok: false, error: 'subscription' });
    }
    const id = idOf(sub.endpoint), key = 'push:' + id;
    if (b.action === 'unsubscribe') {
      await kv.pipe([['DEL', key], ['SREM', 'push:subs', id]]);
      return res.status(200).json({ ok: true });
    }
    const prev = await kv.cmd('GET', key);
    let old = {};
    try { old = prev ? JSON.parse(prev) : {}; } catch (e) { old = {}; }
    const now = Date.now();
    const refillAt = Number(b.refillAt) > now && Number(b.refillAt) < now + 120 * DAY ? Number(b.refillAt) : (old.refillAt || now + 40 * DAY);
    const rec = {
      sub: { endpoint: sub.endpoint, keys: { p256dh: String(sub.keys.p256dh).slice(0, 200), auth: String(sub.keys.auth).slice(0, 60) } },
      routine: !!b.routine,
      routineStart: b.routine ? (old.routine && old.routineStart ? old.routineStart : now) : null,
      refill: !!b.refill,
      refillAt: b.refill ? refillAt : null,
      refillSent: old.refillAt === refillAt ? !!old.refillSent : false,
      created: old.created || now
    };
    if (!rec.routine && !rec.refill) {
      await kv.pipe([['DEL', key], ['SREM', 'push:subs', id]]);
      return res.status(200).json({ ok: true, off: true });
    }
    await kv.pipe([['SET', key, JSON.stringify(rec), 'EX', 150 * 24 * 3600], ['SADD', 'push:subs', id]]);
    if (!prev) {
      const r = await push.send(rec.sub, { title: 'Reminders are on ✓', body: rec.routine ? 'We will remind you at 9:30 pm on your Night Cream nights.' : 'We will remind you when it is time to reorder.', url: '/reminders/' });
      if (r === 'gone') { await kv.pipe([['DEL', key], ['SREM', 'push:subs', id]]); return res.status(410).json({ ok: false, error: 'gone' }); }
    }
    return res.status(200).json({ ok: true, routine: rec.routine, refill: rec.refill, refillAt: rec.refillAt });
  } catch (e) {
    return res.status(500).json({ ok: false });
  }
};
