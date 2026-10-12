const kv = require('./_kv');
const guard = require('./_guard');
const PAGES = require('./_pages.json');

// IndexNow: tells Bing (which also feeds ChatGPT search and Copilot), Yandex, Seznam and Naver
// which pages are new or changed, so they are crawled within hours instead of weeks.
// Runs daily (Vercel Cron). Each page carries a content fingerprint from the build; only pages whose
// fingerprint differs from the last successful submission are sent. The first run sends every page.
const KEY = 'a7f3c9e15b2d4086b1e8d3f0c62a97e4';
const HOST = 'glutanex.co.in';

module.exports = async (req, res) => {
  res.setHeader('Cache-Control', 'no-store');
  const secret = process.env.CRON_SECRET;
  const owner = guard.sameCode(req.headers['x-owner-code'], process.env.OWNER_CODE);
  if (secret && !owner && req.headers.authorization !== 'Bearer ' + secret) return res.status(401).json({ ok: false });
  if (!kv.cfg()) return res.status(503).json({ ok: false, error: 'not_configured' });
  try {
    const urls = Object.keys(PAGES);
    const sent = owner && req.query && req.query.all === '1' ? {} : ((await kv.cmd('GET', 'indexnow:sent')) ? JSON.parse(await kv.cmd('GET', 'indexnow:sent')) : {});
    const changed = urls.filter((u) => sent[u] !== PAGES[u]);
    if (!changed.length) return res.status(200).json({ ok: true, changed: 0 });
    const r = await fetch('https://api.indexnow.org/indexnow', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json; charset=utf-8' },
      body: JSON.stringify({ host: HOST, key: KEY, keyLocation: 'https://' + HOST + '/' + KEY + '.txt', urlList: changed.slice(0, 10000) })
    });
    if (r.status !== 200 && r.status !== 202) return res.status(502).json({ ok: false, status: r.status });
    const next = {};
    urls.forEach((u) => { next[u] = changed.includes(u) ? PAGES[u] : sent[u]; });
    await kv.cmd('SET', 'indexnow:sent', JSON.stringify(next));
    return res.status(200).json({ ok: true, changed: changed.length, status: r.status });
  } catch (e) {
    return res.status(500).json({ ok: false });
  }
};
