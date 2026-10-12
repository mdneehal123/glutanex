// Abuse protection without tracking people: limits are counted per mobile number, per order, or for the
// whole shop, never per IP address. Everything is skipped when the Redis database is not connected.
const crypto = require('crypto');
const kv = require('./_kv');

// true while under the limit (max hits per window seconds); fails open if the database has a hiccup
async function limit(key, max, sec) {
  if (!kv.cfg()) return true;
  try {
    const [n] = await kv.pipe([['INCR', 'rl:' + key], ['EXPIRE', 'rl:' + key, sec, 'NX']]);
    return n <= max;
  } catch (e) { return true; }
}

function sameCode(got, want) {
  got = String(got || ''); want = String(want || '');
  if (want.length < 6 || got.length !== want.length) return false;
  return crypto.timingSafeEqual(Buffer.from(got), Buffer.from(want));
}

// Owner code check with a lockout: 10 wrong codes in 15 minutes locks owner actions for 15 minutes.
// Returns null when allowed, otherwise [status, body] to send back.
async function owner(req) {
  const want = process.env.OWNER_CODE || '';
  if (!want) return [503, { ok: false, error: 'owner_code_missing' }];
  let fails = 0;
  if (kv.cfg()) { try { fails = Number(await kv.cmd('GET', 'rl:owner-fail')) || 0; } catch (e) { fails = 0; } }
  if (fails >= 10) return [429, { ok: false, error: 'locked' }];
  if (sameCode(req.headers['x-owner-code'], want)) return null;
  if (kv.cfg()) { try { await kv.pipe([['INCR', 'rl:owner-fail'], ['EXPIRE', 'rl:owner-fail', 900, 'NX']]); } catch (e) { /* ignore */ } }
  await new Promise((r) => setTimeout(r, 600));
  return [401, { ok: false, error: 'wrong_code' }];
}

module.exports = { limit, owner, sameCode };
