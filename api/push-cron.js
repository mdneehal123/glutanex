const kv = require('./_kv');
const push = require('./_push');

// Runs once a day at 9:30 pm IST (Vercel Cron, see vercel.json) and sends the reminders that are due.
// Night Cream routine: start slowly (nights 1, 4, 7, 10, 13 of the first two weeks), then every night until week 8.
// Refill: once, on the saved refill date.
// If CRON_SECRET is set in Vercel, the request must carry it (Vercel Cron sends it automatically).
const DAY = 864e5;

function routineMsg(day) {
  if (day < 14) {
    if (day % 3 !== 0) return null; // rest night in the first two weeks
    return { title: 'Night Cream tonight 🌙', body: 'Cleanse, pat dry, then a pea-sized amount on face and neck. Weeks 1–2: just 2–3 nights a week.', url: '/how-to-use-glutathione-cream/' };
  }
  if (day === 14) return { title: 'Week 3: every other night', body: 'Skin comfortable? Use the Night Cream every other night now. Sunscreen every morning.', url: '/how-to-use-glutathione-cream/' };
  if (day < 28) return day % 2 === 0 ? { title: 'Night Cream tonight 🌙', body: 'Cleanse, apply, rest. Sunscreen tomorrow morning.', url: '/how-to-use-glutathione-cream/' } : null;
  if (day === 28) return { title: 'Week 5: every night', body: 'If your skin is happy, use the Night Cream every night. Keep up the morning sunscreen.', url: '/how-to-use-glutathione-cream/' };
  if (day < 56) return { title: 'Night Cream time 🌙', body: 'Cleanse, pat dry, apply. Consistency is what shows results.', url: '/glutathione-benefits-for-skin/' };
  if (day === 56) return { title: '8 weeks done ✨', body: 'Compare your skin with week 1. Keep going with the Night Cream and daily sunscreen.', url: '/shop/' };
  return null;
}

module.exports = async (req, res) => {
  res.setHeader('Cache-Control', 'no-store');
  const secret = process.env.CRON_SECRET;
  if (secret && req.headers.authorization !== 'Bearer ' + secret) return res.status(401).json({ ok: false });
  if (!kv.cfg()) return res.status(503).json({ ok: false, error: 'not_configured' });
  const today = new Date(Date.now() + 5.5 * 3600e3).toISOString().slice(0, 10); // date in India
  const first = await kv.cmd('SET', 'push:ran:' + today, '1', 'NX', 'EX', 2 * 24 * 3600);
  if (!first && req.query && req.query.force !== '1') return res.status(200).json({ ok: true, skipped: 'already ran today' });
  const ids = (await kv.cmd('SMEMBERS', 'push:subs')) || [];
  const stats = { checked: ids.length, sent: 0, removed: 0 };
  for (let i = 0; i < ids.length; i += 50) {
    const chunk = ids.slice(i, i + 50);
    const vals = await kv.pipe(chunk.map((id) => ['GET', 'push:' + id]));
    for (let j = 0; j < chunk.length; j++) {
      const id = chunk[j];
      if (!vals[j]) { await kv.cmd('SREM', 'push:subs', id); stats.removed++; continue; }
      let rec; try { rec = JSON.parse(vals[j]); } catch (e) { continue; }
      const msgs = [];
      if (rec.routine && rec.routineStart) {
        const m = routineMsg(Math.floor((Date.now() - rec.routineStart) / DAY));
        if (m) msgs.push(m);
      }
      let changed = false;
      if (rec.refill && rec.refillAt && !rec.refillSent && Date.now() >= rec.refillAt - 12 * 3600e3) {
        msgs.push({ title: 'Running low on Night Cream?', body: 'A 30 g jar lasts about 6–8 weeks. Reorder now to keep your routine going. Free shipping, COD available.', url: '/product/glutanex-glutathione-night-cream/' });
        rec.refillSent = true; changed = true;
      }
      for (const m of msgs) {
        const r = await push.send(rec.sub, m);
        if (r === 'gone') { await kv.pipe([['DEL', 'push:' + id], ['SREM', 'push:subs', id]]); stats.removed++; changed = false; break; }
        if (r === 'ok') stats.sent++;
      }
      if (changed) await kv.cmd('SET', 'push:' + id, JSON.stringify(rec), 'KEEPTTL');
    }
  }
  return res.status(200).json(Object.assign({ ok: true }, stats));
};
