# Writes photo credit and licence data (IPTC fields as XMP) into the site's images, without re-compressing them.
# Google Images reads these fields (Creator, Credit Line, Copyright Notice, Web Statement of Rights, Licensor URL)
# and shows the credit and licence details next to the image. Safe to run on every build: images that already
# carry XMP are left alone. Handles JPEG, PNG and WebP.
import os
import struct
import zlib

MARK = b'GlutaNex-credit-v1'


def xmp_packet(site, owner, year):
    lic = site + '/image-licence/'
    x = '''<?xpacket begin="﻿" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="%s">
<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
<rdf:Description rdf:about=""
 xmlns:dc="http://purl.org/dc/elements/1.1/"
 xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/"
 xmlns:xmpRights="http://ns.adobe.com/xap/1.0/rights/"
 xmlns:plus="http://ns.useplus.org/ldf/xmp/1.0/"
 photoshop:Credit="GlutaNex"
 xmpRights:Marked="True"
 xmpRights:WebStatement="%s">
<dc:creator><rdf:Seq><rdf:li>GlutaNex</rdf:li></rdf:Seq></dc:creator>
<dc:rights><rdf:Alt><rdf:li xml:lang="x-default">© %s GlutaNex (%s). Use rules: %s</rdf:li></rdf:Alt></dc:rights>
<plus:Licensor><rdf:Seq><rdf:li rdf:parseType="Resource"><plus:LicensorName>GlutaNex</plus:LicensorName><plus:LicensorURL>%s</plus:LicensorURL></rdf:li></rdf:Seq></plus:Licensor>
</rdf:Description>
</rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>''' % (MARK.decode(), lic, year, owner, lic, lic)
    return x.encode('utf-8')


def _jpeg(data, xmp):
    if b'http://ns.adobe.com/xap/1.0/\x00' in data[:65536]:
        return None
    seg = b'http://ns.adobe.com/xap/1.0/\x00' + xmp
    app1 = b'\xff\xe1' + struct.pack('>H', len(seg) + 2) + seg
    pos = 2
    if data[2:4] == b'\xff\xe0':  # keep the JFIF header first
        pos = 4 + struct.unpack('>H', data[4:6])[0]
    return data[:pos] + app1 + data[pos:]


def _png(data, xmp):
    if b'XML:com.adobe.xmp' in data:
        return None
    body = b'XML:com.adobe.xmp\x00\x00\x00\x00\x00' + xmp
    chunk = struct.pack('>I', len(body)) + b'iTXt' + body + struct.pack('>I', zlib.crc32(b'iTXt' + body) & 0xffffffff)
    i = data.index(b'IDAT') - 4
    return data[:i] + chunk + data[i:]


def _webp(data, xmp, size, alpha):
    chunks, p = [], 12
    while p + 8 <= len(data):
        cid, ln = data[p:p + 4], struct.unpack('<I', data[p + 4:p + 8])[0]
        chunks.append([cid, data[p + 8:p + 8 + ln]])
        p += 8 + ln + (ln & 1)
    if any(c[0] == b'XMP ' for c in chunks):
        return None
    if chunks[0][0] == b'VP8X':
        fl = bytearray(chunks[0][1]); fl[0] |= 0x04; chunks[0][1] = bytes(fl)
    else:
        w, h = size
        flags = 0x04 | (0x10 if alpha else 0)
        vp8x = bytes([flags, 0, 0, 0]) + (w - 1).to_bytes(3, 'little') + (h - 1).to_bytes(3, 'little')
        chunks.insert(0, [b'VP8X', vp8x])
    chunks.append([b'XMP ', xmp])
    out = b''.join(c + struct.pack('<I', len(d)) + d + (b'\x00' if len(d) & 1 else b'') for c, d in chunks)
    return b'RIFF' + struct.pack('<I', len(out) + 4) + b'WEBP' + out


def stamp_dir(folder, site, owner, year='2026'):
    from PIL import Image
    xmp = xmp_packet(site, owner, year)
    done = 0
    for f in sorted(os.listdir(folder)):
        path = os.path.join(folder, f)
        ext = f.rsplit('.', 1)[-1].lower()
        if ext not in ('jpg', 'jpeg', 'png', 'webp'):
            continue
        data = open(path, 'rb').read()
        if MARK in data:
            continue
        if ext in ('jpg', 'jpeg'):
            new = _jpeg(data, xmp)
        elif ext == 'png':
            new = _png(data, xmp)
        else:
            im = Image.open(path)
            new = _webp(data, xmp, im.size, 'A' in im.getbands())
        if new:
            open(path, 'wb').write(new)
            Image.open(path).load()  # the edited file must still decode
            done += 1
    return done
