const { keys } = require('./_shared');
const { delhiveryOn } = require('./_delhivery');
const { deskOn } = require('./_orderdesk');
const shiprocket = require('./_shiprocket');
const kv = require('./_kv');

// Tells the store page which services are switched on. Never returns any secret.
// cod: Cash on Delivery can be placed on the site (booked with Delhivery, or saved in the Order Desk to book by hand).
// pincode: the pincode check can answer (Delhivery, or the old Shiprocket lookup while it is still connected).
module.exports = (req, res) => {
  res.setHeader('Cache-Control', 'no-store');
  const cod = delhiveryOn() || deskOn();
  res.status(200).json({ razorpay: !!keys(), cod, delhivery: delhiveryOn(), orderdesk: deskOn(), pincode: delhiveryOn() || !!shiprocket.settings(),
    leads: !!kv.cfg() || deskOn(), push: !!kv.cfg(), ask: !!process.env.ANTHROPIC_API_KEY, rewards: !!kv.cfg() });
};
