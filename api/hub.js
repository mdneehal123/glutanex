// One serverless function for several small endpoints (the Vercel Hobby plan allows 12 functions).
// vercel.json rewrites /api/<name> to /api/hub?fn=<name>, so the public addresses stay the same.
const ROUTES = {
  addon: './_addon', indexnow: './_indexnow', coupon: './_coupon',
  scratch: './_scratch', routine: './_routine', 'parcel-photo': './_parcel-photo',
  'cod-order': './_cod-order', 'delhivery-check': './_delhivery-check'
};
module.exports = (req, res) => {
  const fn = String(([].concat((req.query || {}).fn))[0] || '');
  if (!ROUTES[fn]) { res.setHeader('Cache-Control', 'no-store'); return res.status(404).json({ ok: false }); }
  return require(ROUTES[fn])(req, res);
};
