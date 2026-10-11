const kv = require('./_kv');
const KB = require('./_kb.json');

// GlutaNex question assistant. It answers only from the site's own guides and product facts (api/_kb.json,
// written by _build/build.py), using Claude through the Anthropic API. Needs ANTHROPIC_API_KEY in Vercel.
// Optional: ASK_DAILY_LIMIT (default 300 questions a day, counted only when the Redis database is connected), ASK_MODEL.

const STOP = new Set('a an the is are was were be to of and or in on for with what how why when which who does do can i my me you your it its this that use using about from glutathione glutanex'.split(' '));
const HI = { 'फायदे': 'benefits', 'फायदा': 'benefits', 'नुकसान': 'side effects safe', 'साइड': 'side effects', 'कैसे': 'how use', 'लगाएं': 'apply use', 'लगाये': 'apply use',
  'कीमत': 'price', 'दाम': 'price', 'गोरा': 'whitening skin colour', 'गोरी': 'whitening skin colour', 'दाग': 'dark spots', 'टैन': 'tan', 'गर्भावस्था': 'pregnancy', 'सुरक्षित': 'safe',
  'इंजेक्शन': 'injections', 'गोली': 'tablets', 'डिलीवरी': 'delivery shipping', 'रिटर्न': 'returns refund' };

function words(s) {
  let t = String(s || '').toLowerCase();
  Object.keys(HI).forEach((k) => { if (t.includes(k)) t += ' ' + HI[k]; });
  return t.replace(/[^a-z0-9ऀ-ॿ\s]/g, ' ').split(/\s+/).filter((w) => w.length > 2 && !STOP.has(w));
}

// document frequency for a light idf weighting
const DF = {};
KB.forEach((c) => { new Set(words(c.t + ' ' + c.s + ' ' + c.x)).forEach((w) => { DF[w] = (DF[w] || 0) + 1; }); });

function pick(q) {
  const qs = words(q);
  const scored = KB.map((c, i) => {
    const hay = (c.t + ' ' + c.s + ' ' + c.s + ' ' + c.x).toLowerCase();
    let sc = c.always ? 0.5 : 0;
    qs.forEach((w) => { if (hay.includes(w)) sc += Math.log(1 + KB.length / (DF[w] || 1)); });
    return { i, sc };
  }).sort((a, b) => b.sc - a.sc);
  const out = [];
  let len = 0;
  KB.forEach((c, i) => { if (c.always) { out.push(i); len += c.x.length; } });
  for (const s of scored) {
    if (out.length >= 8 || len > 9000) break;
    if (out.includes(s.i) || s.sc <= 0) continue;
    out.push(s.i); len += KB[s.i].x.length;
  }
  return out.map((i) => KB[i]);
}

const SYSTEM = `You are the GlutaNex assistant on glutanex.co.in, a shop selling GlutaNex glutathione skincare (Night Cream 30 g, Gluta Boost Face Wash 100 ml, Glow Duo) in India.

Rules:
- Answer ONLY using the reference notes below. If the notes do not cover the question, say you are not sure and suggest messaging the team on WhatsApp (+91 99808 81230). Never invent facts, prices, studies or ingredients.
- Be honest and careful: glutathione may help skin look brighter and more even over weeks with daily sunscreen; it does NOT change natural skin colour. Never promise whitening, fairness, cures or guaranteed results.
- This is cosmetic information, not medical advice. For pregnancy, breastfeeding, skin conditions, melasma or reactions, advise seeing a doctor or dermatologist. The Night Cream contains retinol and salicylic acid.
- Discourage glutathione injections for skin lightening, as the notes explain.
- Reply in the customer's language (English, Hindi or Hinglish). Keep answers short: 2 to 5 sentences or a few bullet points.
- When useful, link one or two relevant pages from the notes in the form [page title](/path/). Use only paths that appear in the notes.
- You can mention the products and prices from the notes when relevant, without being pushy.`;

module.exports = async (req, res) => {
  res.setHeader('Cache-Control', 'no-store');
  if (req.method !== 'POST') return res.status(405).json({ error: 'method_not_allowed' });
  const key = process.env.ANTHROPIC_API_KEY;
  if (!key) return res.status(503).json({ error: 'not_configured' });
  let b = req.body || {};
  if (typeof b === 'string') { try { b = JSON.parse(b); } catch (e) { b = {}; } }
  const q = String(b.q || '').trim().slice(0, 500);
  if (q.length < 2) return res.status(400).json({ error: 'empty' });

  // daily cap, so a flood of questions cannot run up the API bill
  if (kv.cfg()) {
    try {
      const day = 'ask:' + new Date().toISOString().slice(0, 10);
      const [n] = await kv.pipe([['INCR', day], ['EXPIRE', day, 172800]]);
      if (n > (Number(process.env.ASK_DAILY_LIMIT) || 300)) return res.status(429).json({ error: 'busy' });
    } catch (e) { /* database hiccup: still answer */ }
  }

  // last few turns of the conversation, cleaned and alternating
  const hist = Array.isArray(b.history) ? b.history.slice(-6) : [];
  const msgs = [];
  hist.forEach((m) => {
    const role = m && m.role === 'assistant' ? 'assistant' : 'user';
    const content = String((m && m.content) || '').slice(0, 1200);
    if (!content) return;
    if (!msgs.length && role !== 'user') return;
    if (msgs.length && msgs[msgs.length - 1].role === role) msgs[msgs.length - 1].content += '\n' + content;
    else msgs.push({ role, content });
  });
  if (msgs.length && msgs[msgs.length - 1].role === 'user') msgs.pop();
  msgs.push({ role: 'user', content: q });

  const notes = pick(q + ' ' + hist.filter((m) => m && m.role !== 'assistant').map((m) => m.content).slice(-2).join(' '))
    .map((c) => '### ' + c.t + (c.s ? ' — ' + c.s : '') + ' (' + c.u + ')\n' + c.x).join('\n\n');

  const ctl = new AbortController();
  const timer = setTimeout(() => ctl.abort(), 9000);
  try {
    const r = await fetch('https://api.anthropic.com/v1/messages', {
      method: 'POST',
      signal: ctl.signal,
      headers: { 'x-api-key': key, 'anthropic-version': '2023-06-01', 'content-type': 'application/json' },
      body: JSON.stringify({ model: process.env.ASK_MODEL || 'claude-haiku-4-5-20251001', max_tokens: 450, system: SYSTEM + '\n\nReference notes:\n\n' + notes, messages: msgs })
    });
    const j = await r.json();
    if (!r.ok) return res.status(502).json({ error: 'upstream' });
    const answer = (j.content || []).filter((x) => x.type === 'text').map((x) => x.text).join('').trim();
    return res.status(200).json({ answer: answer || null });
  } catch (e) {
    return res.status(504).json({ error: 'timeout' });
  } finally {
    clearTimeout(timer);
  }
};
