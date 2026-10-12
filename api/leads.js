const kv = require('./_kv');
const guard = require('./_guard');

// Owner-only list of unfinished checkouts. Protected by the OWNER_CODE environment variable.
module.exports = async (req, res) => {
  res.setHeader('Cache-Control', 'no-store');
  if (!process.env.OWNER_CODE) return res.status(503).json({ ok: false, error: 'owner_code_missing' });
  if (!kv.cfg()) return res.status(503).json({ ok: false, error: 'database_missing' });
  const deny = await guard.owner(req);
  if (deny) return res.status(deny[0]).json(deny[1]);
  try {
    if (req.method === 'POST') {
      let b = req.body || {};
      if (typeof b === 'string') { try { b = JSON.parse(b); } catch (e) { b = {}; } }
      const phone = String(b.phone || '').replace(/\D/g, '').slice(-10);
      if (!/^[6-9]\d{9}$/.test(phone)) return res.status(400).json({ ok: false });
      const key = 'lead:' + phone;
      if (b.action === 'delete') {
        await kv.pipe([['DEL', key], ['ZREM', 'leads', phone]]);
      } else if (b.action === 'contacted') {
        const v = await kv.cmd('GET', key);
        if (v) { const l = JSON.parse(v); l.contacted = true; await kv.cmd('SET', key, JSON.stringify(l), 'KEEPTTL'); }
      }
      return res.status(200).json({ ok: true });
    }
    const phones = await kv.cmd('ZREVRANGE', 'leads', 0, 199);
    if (!phones || !phones.length) return res.status(200).json({ ok: true, leads: [] });
    const vals = await kv.pipe(phones.map((p) => ['GET', 'lead:' + p]));
    const leads = [], gone = [];
    vals.forEach((v, i) => { if (!v) { gone.push(phones[i]); return; } try { leads.push(JSON.parse(v)); } catch (e) { gone.push(phones[i]); } });
    if (gone.length) await kv.pipe([['ZREM', 'leads'].concat(gone)]);
    return res.status(200).json({ ok: true, leads });
  } catch (e) {
    return res.status(500).json({ ok: false });
  }
};
