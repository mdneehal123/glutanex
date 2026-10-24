// One serverless function for several small endpoints (the Vercel Hobby plan allows 12 functions).
// vercel.json rewrites /api/<name> to /api/hub?fn=<name>, so the public addresses stay the same.
const ROUTES = {
  addon: () => require('./_addon'), indexnow: () => require('./_indexnow'), coupon: () => require('./_coupon'),
  scratch: () => require('./_scratch'), routine: () => require('./_routine'), 'parcel-photo': () => require('./_parcel-photo'),
  'cod-order': () => require('./_cod-order'), waitlist: () => require('./_waitlist'), 'delhivery-check': () => require('./_delhivery-check')
};
module.exports = (req, res) => {
  const fn = String(([].concat((req.query || {}).fn))[0] || '');
  if (!ROUTES[fn]) { res.setHeader('Cache-Control', 'no-store'); return res.status(404).json({ ok: false }); }
  return ROUTES[fn]()(req, res);
};
