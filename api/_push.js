// Web Push for GlutaNex app reminders, built on Node's crypto (no extra packages).
// Payload encryption follows RFC 8291 (aes128gcm) and sender identification follows RFC 8292 (VAPID).
// The VAPID key pair is created once and kept in the Redis database, so there is nothing to configure by hand.
const crypto = require('crypto');
const kv = require('./_kv');

const b64u = (buf) => Buffer.from(buf).toString('base64').replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '');
const unb64u = (s) => Buffer.from(String(s).replace(/-/g, '+').replace(/_/g, '/'), 'base64');
const hmac = (key, data) => crypto.createHmac('sha256', key).update(data).digest();

async function vapid() {
  const saved = await kv.cmd('GET', 'push:vapid');
  if (saved) return JSON.parse(saved);
  const { privateKey } = crypto.generateKeyPairSync('ec', { namedCurve: 'prime256v1' });
  const jwk = privateKey.export({ format: 'jwk' });
  const pub = b64u(Buffer.concat([Buffer.from([4]), unb64u(jwk.x), unb64u(jwk.y)]));
  const v = { jwk, pub };
  // NX: if two requests race, keep the first key pair
  await kv.cmd('SET', 'push:vapid', JSON.stringify(v), 'NX');
  return JSON.parse(await kv.cmd('GET', 'push:vapid'));
}

function jwt(aud, v, subject) {
  const head = b64u(JSON.stringify({ typ: 'JWT', alg: 'ES256' }));
  const body = b64u(JSON.stringify({ aud, exp: Math.floor(Date.now() / 1000) + 12 * 3600, sub: subject }));
  const key = crypto.createPrivateKey({ key: v.jwk, format: 'jwk' });
  const sig = crypto.sign('sha256', Buffer.from(head + '.' + body), { key, dsaEncoding: 'ieee-p1363' });
  return head + '.' + body + '.' + b64u(sig);
}

function encrypt(sub, payload) {
  const uaPub = unb64u(sub.keys.p256dh);
  const auth = unb64u(sub.keys.auth);
  const ecdh = crypto.createECDH('prime256v1');
  const asPub = ecdh.generateKeys();
  const shared = ecdh.computeSecret(uaPub);
  const ikm = hmac(hmac(auth, shared), Buffer.concat([Buffer.from('WebPush: info\0'), uaPub, asPub, Buffer.from([1])]));
  const salt = crypto.randomBytes(16);
  const prk = hmac(salt, ikm);
  const cek = hmac(prk, Buffer.concat([Buffer.from('Content-Encoding: aes128gcm\0'), Buffer.from([1])])).subarray(0, 16);
  const nonce = hmac(prk, Buffer.concat([Buffer.from('Content-Encoding: nonce\0'), Buffer.from([1])])).subarray(0, 12);
  const cipher = crypto.createCipheriv('aes-128-gcm', cek, nonce);
  const ct = Buffer.concat([cipher.update(Buffer.concat([Buffer.from(payload), Buffer.from([2])])), cipher.final(), cipher.getAuthTag()]);
  const rs = Buffer.alloc(4); rs.writeUInt32BE(4096);
  return Buffer.concat([salt, rs, Buffer.from([asPub.length]), asPub, ct]);
}

// Sends one notification. Returns 'ok', 'gone' (subscription expired: delete it) or 'error'.
async function send(sub, msg, subject) {
  try {
    const v = await vapid();
    const url = new URL(sub.endpoint);
    const r = await fetch(sub.endpoint, {
      method: 'POST',
      headers: { 'Content-Encoding': 'aes128gcm', 'Content-Type': 'application/octet-stream', TTL: '43200', Urgency: 'normal',
        Authorization: 'vapid t=' + jwt(url.origin, v, subject || 'https://glutanex.co.in') + ', k=' + v.pub },
      body: encrypt(sub, JSON.stringify(msg))
    });
    if (r.status === 404 || r.status === 410) return 'gone';
    return r.ok ? 'ok' : 'error';
  } catch (e) {
    return 'error';
  }
}

module.exports = { vapid, send, encrypt, jwt, b64u, unb64u };
