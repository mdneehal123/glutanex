const { keys } = require('./_shared');
const shiprocket = require('./_shiprocket');
const kv = require('./_kv');

// Tells the store page which services are switched on. Never returns any secret.
module.exports = (req, res) => {
  res.setHeader('Cache-Control', 'no-store');
  res.status(200).json({ razorpay: !!keys(), shiprocket: !!shiprocket.settings(), leads: !!kv.cfg(), push: !!kv.cfg(), ask: !!process.env.ANTHROPIC_API_KEY, rewards: !!kv.cfg() });
};
