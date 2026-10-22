# Google Web Stories (AMP story format). Read by build.py with exec(), after content.py.
# Stories can show in Google Discover and in a "Web Stories" row in search, which is big in India.
# Each story is short and honest, and its last page links to the full guide.
from PIL import Image as _Im, ImageDraw as _Dr, ImageFilter as _Fl
import math

STORY_HUES = [((255, 246, 236), (246, 214, 186)), ((255, 248, 240), (240, 222, 200)), ((253, 244, 238), (238, 206, 196)), ((250, 247, 240), (228, 216, 190)), ((255, 245, 232), (250, 205, 160))]


def _poster_plain(slug, hue):
    """640x853 portrait poster: soft gradient, the real jar photo cut-out and a floor shadow. No baked-in text."""
    W, H = 640, 853
    top, bot = hue
    bg = _Im.new('RGB', (W, H))
    d = _Dr.Draw(bg)
    for y in range(H):
        t = y / (H - 1)
        d.line([(0, y), (W, y)], fill=tuple(int(top[i] + (bot[i] - top[i]) * t) for i in range(3)))
    glow = _Im.new('L', (W, H), 0)
    _Dr.Draw(glow).ellipse([60, 170, 580, 690], fill=150)
    glow = glow.filter(_Fl.GaussianBlur(90))
    bg = _Im.composite(_Im.new('RGB', (W, H), (255, 255, 255)), bg, glow)
    sh = _Im.new('L', (W, H), 0)
    _Dr.Draw(sh).ellipse([150, 655, 490, 715], fill=120)
    sh = sh.filter(_Fl.GaussianBlur(18))
    bg = _Im.composite(_Im.new('RGB', (W, H), (150, 110, 80)), bg, sh)
    jar = _Im.open(os.path.join(ROOT, 'assets', 'img', 'jar-cut.png')).convert('RGBA')
    jw = 440
    jar = jar.resize((jw, int(jar.height * jw / jar.width)), _Im.LANCZOS)
    bg.paste(jar, ((W - jw) // 2, 690 - jar.height), jar)
    out = os.path.join(ROOT, 'assets', 'img', 'web-story-%s.jpg' % slug)
    bg.save(out, quality=84, optimize=True, progressive=True)
    return '/assets/img/web-story-%s.jpg' % slug


# Distinct cover per story (22 Oct 2026): each topic gets its own colour, its own real product photo in an arch frame
# and a simple topic icon, so the "Glutathione in one minute" row does not show six near-identical jars. No baked-in text.
_S = 2  # supersample factor


def _grad(W, H, top, bot):
    g = _Im.new('RGB', (1, H))
    for y in range(H):
        t = y / (H - 1)
        g.putpixel((0, y), tuple(int(top[i] + (bot[i] - top[i]) * t) for i in range(3)))
    return g.resize((W, H))


def _photo(name, w, h, focus=(0.5, 0.5), zoom=1.0):
    p = _Im.open(os.path.join(ROOT, 'assets', 'img', name)).convert('RGB')
    s = max(w / p.width, h / p.height)
    base = p.resize((int(p.width * s + 1), int(p.height * s + 1)), _Im.LANCZOS)
    if zoom < 1:
        # zoomed out: whole photo across the width, over a blurred, cover-cropped copy of itself
        x = (base.width - w) // 2; y = (base.height - h) // 2
        out = base.crop((x, y, x + w, y + h)).filter(_Fl.GaussianBlur(30))
        f = w / p.width * (1 / zoom if zoom > 0 else 1)
        f = min(f, h / p.height * 1.4)
        f = w / p.width if f * p.height > h else f
        q = p.resize((int(p.width * f), int(p.height * f)), _Im.LANCZOS)
        out.paste(q, ((w - q.width) // 2, int((h - q.height) * focus[1])))
        return out
    s *= zoom
    p = p.resize((int(p.width * s + 1), int(p.height * s + 1)), _Im.LANCZOS)
    x = int((p.width - w) * focus[0]); y = int((p.height - h) * focus[1])
    return p.crop((x, y, x + w, y + h))


def _arch(bg, photo, box, ring):
    x0, y0, x1, y1 = box
    w, h = x1 - x0, y1 - y0
    m = _Im.new('L', (w, h), 0)
    md = _Dr.Draw(m)
    md.ellipse([0, 0, w - 1, w - 1], fill=255)
    md.rectangle([0, w // 2, w - 1, h - 1], fill=255)
    sh = _Im.new('L', bg.size, 0)
    sh.paste(m, (x0 + 10 * _S, y0 + 18 * _S))
    sh = sh.filter(_Fl.GaussianBlur(22 * _S)).point(lambda v: v * 45 // 100)
    bg.paste(_Im.new('RGB', bg.size, (60, 40, 30)), (0, 0), sh)
    d = _Dr.Draw(bg)
    pad = 9 * _S
    d.ellipse([x0 - pad, y0 - pad, x1 + pad, y0 + w + pad], fill=ring)
    d.rectangle([x0 - pad, y0 + w // 2, x1 + pad, y1 + pad], fill=ring)
    bg.paste(photo, (x0, y0), m)


def _badge(d, cx, cy, r, fill, ring=(255, 255, 255)):
    d.ellipse([cx - r - 6 * _S, cy - r - 6 * _S, cx + r + 6 * _S, cy + r + 6 * _S], fill=ring)
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=fill)


def _star(d, cx, cy, r, fill):
    pts = []
    for k in range(8):
        a = math.pi / 4 * k - math.pi / 2
        rr = r if k % 2 == 0 else r * 0.28
        pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
    d.polygon(pts, fill=fill)


def _heart(d, cx, cy, s, fill):
    d.ellipse([cx - s, cy - s * 0.75, cx, cy + s * 0.25], fill=fill)
    d.ellipse([cx, cy - s * 0.75, cx + s, cy + s * 0.25], fill=fill)
    d.polygon([(cx - s * 0.97, cy - s * 0.12), (cx + s * 0.97, cy - s * 0.12), (cx, cy + s * 0.95)], fill=fill)


def _check_shield(d, cx, cy, s, fill, mark):
    d.polygon([(cx, cy - s), (cx + s * 0.85, cy - s * 0.62), (cx + s * 0.78, cy + s * 0.15), (cx, cy + s), (cx - s * 0.78, cy + s * 0.15), (cx - s * 0.85, cy - s * 0.62)], fill=fill)
    d.line([(cx - s * 0.38, cy), (cx - s * 0.08, cy + s * 0.32), (cx + s * 0.42, cy - s * 0.3)], fill=mark, width=int(s * 0.17), joint='curve')


def _drop(d, cx, cy, s, fill):
    d.ellipse([cx - s * 0.6, cy - s * 0.1, cx + s * 0.6, cy + s * 1.1], fill=fill)
    d.polygon([(cx, cy - s), (cx - s * 0.55, cy + s * 0.3), (cx + s * 0.55, cy + s * 0.3)], fill=fill)


def _capsule(d, cx, cy, s, c1, c2):
    w, h = s * 0.55, s * 1.5
    d.rounded_rectangle([cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2], radius=w / 2, fill=c1)
    d.rounded_rectangle([cx - w / 2, cy, cx + w / 2, cy + h / 2], radius=w / 2, fill=c2)
    d.rectangle([cx - w / 2, cy, cx + w / 2, cy + w / 2], fill=c2)


def _syringe(d, cx, cy, s, c):
    lw = int(s * 0.08)
    d.rounded_rectangle([cx - s * 0.2, cy - s * 0.6, cx + s * 0.2, cy + s * 0.45], radius=s * 0.06, outline=c, width=lw)
    d.line([(cx, cy + s * 0.45), (cx, cy + s * 0.9)], fill=c, width=int(lw * 0.7))
    d.line([(cx, cy - s * 0.6), (cx, cy - s * 0.85)], fill=c, width=lw)
    d.line([(cx - s * 0.25, cy - s * 0.88), (cx + s * 0.25, cy - s * 0.88)], fill=c, width=lw)
    for k in range(3):
        y = cy - s * 0.3 + k * s * 0.22
        d.line([(cx - s * 0.2, y), (cx, y)], fill=c, width=int(lw * 0.6))


POSTER_DESIGN = {
    'glutathione-benefits-for-skin': dict(bg=((255, 240, 226), (244, 196, 160)), ring=(255, 252, 247), photo='glutathione-night-cream-jar-glutanex.jpg', focus=(0.5, 0.62), zoom=0.5, icon='stars', accent=(232, 116, 42),
                                          alt='GlutaNex night cream jar on dark stone with gold sparkles'),
    'how-to-use-glutathione-cream': dict(bg=((236, 244, 234), (186, 210, 186)), ring=(250, 253, 248), photo='glutanex-glutathione-cream-in-hand.jpg', focus=(0.55, 0.5), icon='steps', accent=(74, 120, 86),
                                         alt='Hands holding a GlutaNex glutathione night cream jar'),
    'glutathione-side-effects': dict(bg=((236, 242, 248), (184, 202, 222)), ring=(250, 252, 255), photo='glutanex-glutathione-face-cream.jpg', focus=(0.5, 0.4), icon='shield', accent=(58, 96, 140),
                                     alt='GlutaNex night cream jar on marble with a safety shield icon'),
    'glutathione-cream-vs-tablets-vs-injections': dict(bg=((242, 236, 250), (200, 186, 228)), ring=(255, 255, 255), photo=None, icon='compare', accent=(96, 74, 150),
                                                       alt='Icons comparing a glutathione cream jar, a tablet and an injection'),
    'glutathione-before-wedding': dict(bg=((252, 232, 236), (206, 120, 140)), ring=(255, 246, 236), photo='glutanex-glutathione-night-cream-travel.jpg', focus=(0.4, 0.5), icon='heart', accent=(160, 40, 70),
                                       alt='GlutaNex night cream jar in a handbag with jewellery for wedding season'),
    'glutathione-cream-ke-fayde': dict(bg=((255, 244, 214), (246, 190, 92)), ring=(255, 251, 240), photo='glutanex-glow-duo-glutathione-cream-face-wash.jpg', focus=(0.5, 0.5), zoom=0.8, icon='drops', accent=(200, 110, 20),
                                       alt='GlutaNex glutathione night cream and face wash'),
}


def _poster(slug, hue):
    """640x853 portrait cover with its own colour, photo and icon per story. Important art stays in the top ~60%
    because the story cover fades the bottom into the title. Falls back to the old soft-gradient jar poster."""
    cfg = POSTER_DESIGN.get(slug)
    if not cfg:
        return _poster_plain(slug, hue)
    W, H = 640 * _S, 853 * _S
    bg = _grad(W, H, *cfg['bg'])
    glow = _Im.new('L', (W, H), 0)
    _Dr.Draw(glow).ellipse([W * 0.05, H * 0.02, W * 0.95, H * 0.62], fill=120)
    glow = glow.filter(_Fl.GaussianBlur(70 * _S))
    bg = _Im.composite(_Im.new('RGB', (W, H), (255, 255, 255)), bg, glow)
    d = _Dr.Draw(bg)
    acc, ring = cfg['accent'], cfg['ring']
    ax0, ay0, ax1, ay1 = 100 * _S, 64 * _S, 540 * _S, 590 * _S
    if cfg['photo']:
        _arch(bg, _photo(cfg['photo'], ax1 - ax0, ay1 - ay0, cfg.get('focus', (0.5, 0.5)), cfg.get('zoom', 1.0)), (ax0, ay0, ax1, ay1), ring)
        d = _Dr.Draw(bg)
    ic = cfg['icon']
    if ic == 'stars':
        for (x, y, r, c) in [(66, 150, 30, acc), (586, 100, 22, (214, 160, 60)), (560, 560, 44, acc), (70, 520, 20, (214, 160, 60)), (606, 300, 14, acc)]:
            _star(d, x * _S, y * _S, r * _S, c)
    elif ic == 'steps':
        for k, x in enumerate((210, 320, 430)):
            _badge(d, x * _S, 610 * _S, (26 + k * 6) * _S, acc, ring)
            d.ellipse([(x - 6 - k * 2) * _S, (604 - k * 2) * _S, (x + 6 + k * 2) * _S, (616 + k * 2) * _S], fill=ring)
        d.line([(244 * _S, 610 * _S), (282 * _S, 610 * _S)], fill=acc, width=5 * _S)
        d.line([(358 * _S, 610 * _S), (390 * _S, 610 * _S)], fill=acc, width=5 * _S)
    elif ic == 'shield':
        _badge(d, 520 * _S, 545 * _S, 70 * _S, acc, ring)
        _check_shield(d, 520 * _S, 545 * _S, 44 * _S, ring, acc)
    elif ic == 'heart':
        _badge(d, 520 * _S, 545 * _S, 68 * _S, acc, ring)
        _heart(d, 520 * _S, 541 * _S, 38 * _S, ring)
        for (x, y, s) in [(60, 140, 22), (64, 470, 14), (596, 110, 16)]:
            _heart(d, x * _S, y * _S, s * _S, acc)
    elif ic == 'drops':
        for (x, y, s) in [(60, 160, 30), (590, 110, 22), (566, 540, 38), (62, 500, 20)]:
            _drop(d, x * _S, y * _S, s * _S, acc)
            d.ellipse([(x - s * 0.25) * _S, (y + s * 0.35) * _S, (x - s * 0.02) * _S, (y + s * 0.6) * _S], fill=(255, 240, 210))
    elif ic == 'compare':
        jar = _Im.open(os.path.join(ROOT, 'assets', 'img', 'jar-cut.png')).convert('RGBA')
        cards = [(170, 250), (470, 250), (320, 500)]
        for (x, y) in cards:
            cx, cy = x * _S, y * _S
            sh = _Im.new('L', (W, H), 0)
            _Dr.Draw(sh).ellipse([cx - 118 * _S, cy - 106 * _S, cx + 122 * _S, cy + 130 * _S], fill=90)
            sh = sh.filter(_Fl.GaussianBlur(18 * _S))
            bg.paste(_Im.new('RGB', (W, H), (90, 70, 120)), (0, 0), sh)
            d = _Dr.Draw(bg)
            d.ellipse([cx - 112 * _S, cy - 112 * _S, cx + 112 * _S, cy + 112 * _S], fill=ring)
        jw = 170 * _S
        jr = jar.resize((jw, int(jar.height * jw / jar.width)), _Im.LANCZOS)
        bg.paste(jr, (cards[0][0] * _S - jw // 2, cards[0][1] * _S - jr.height // 2), jr)
        d = _Dr.Draw(bg)
        _capsule(d, cards[1][0] * _S, cards[1][1] * _S, 110 * _S, acc, (226, 214, 244))
        _syringe(d, cards[2][0] * _S, cards[2][1] * _S, 120 * _S, (150, 140, 160))
        d.line([(cards[2][0] - 70) * _S, (cards[2][1] + 70) * _S, (cards[2][0] + 70) * _S, (cards[2][1] - 70) * _S], fill=(196, 72, 72), width=9 * _S)
    out_im = bg.resize((640, 853), _Im.LANCZOS)
    out = os.path.join(ROOT, 'assets', 'img', 'web-story-%s.jpg' % slug)
    out_im.save(out, quality=86, optimize=True, progressive=True)
    return '/assets/img/web-story-%s.jpg' % slug


STORIES = [
    dict(slug='glutathione-benefits-for-skin', lang='en', guide='/glutathione-benefits-for-skin/',
         title='Glutathione for skin: 5 honest facts', kicker='Glutathione benefits',
         desc='What glutathione can and cannot do for your skin, in five quick slides.',
         pages=[('What it is', 'An antioxidant your body makes from three amino acids. It protects cells and recycles vitamins C and E.'),
                ('What it can do', 'Help tan and uneven tone look lighter and more even, gradually, over 8–12 weeks.'),
                ('What studies show', 'Small studies found modest, gradual drops in skin melanin over 4–12 weeks.'),
                ('What it can\'t do', 'It does not change your natural skin colour. "Permanent whitening" claims are hype.'),
                ('The step that matters most', 'SPF 30+ sunscreen every morning. Without it, results fade.')],
         end='Read the full guide'),
    dict(slug='how-to-use-glutathione-cream', lang='en', guide='/how-to-use-glutathione-cream/',
         title='How to use glutathione cream: a simple night routine', kicker='Glutathione cream',
         desc='A five-step night and morning routine for glutathione cream.',
         pages=[('1 · Cleanse', 'Wash with a gentle face wash and pat your skin dry.'),
                ('2 · A pea-sized amount', 'Dot it on forehead, cheeks, chin and neck, then spread in thin upward strokes.'),
                ('3 · Start slowly', 'Creams with retinol: 2–3 nights a week for the first two weeks, then more often.'),
                ('4 · Morning sunscreen', 'Cleanse, then SPF 30 or higher. Reapply if you are out in the sun.'),
                ('5 · Give it time', 'A brighter look in 4–8 weeks; lighter tan in 8–12 weeks.')],
         end='See the full routine'),
    dict(slug='glutathione-side-effects', lang='en', guide='/glutathione-side-effects/',
         title='Glutathione side effects: what\'s normal and what\'s not', kicker='Glutathione safety',
         desc='Which glutathione side effects are common, which need a doctor, and why injections are different.',
         pages=[('Usually fine', 'Glutathione creams are generally well tolerated by most adults.'),
                ('Can happen at first', 'Mild tingling, redness or dryness. Use it less often and moisturise.'),
                ('Patch test first', 'Try a little behind the ear or on the inner arm for 24 hours.'),
                ('Stop and get help', 'Swelling, a spreading rash or breathing trouble need urgent medical care.'),
                ('Avoid injections', 'Skin-lightening injections lack proper trials and carry regulator warnings.')],
         end='Read the full guide'),
    dict(slug='glutathione-cream-vs-tablets-vs-injections', lang='en', guide='/glutathione-cream-vs-tablets-vs-injections/',
         title='Glutathione cream vs tablets vs injections', kicker='Compare',
         desc='The three ways people use glutathione, compared on evidence and risk.',
         pages=[('Cream', 'Applied to skin. Low risk. Modest, gradual results with daily sunscreen.'),
                ('Tablets', 'Studies used 250–500 mg a day and found modest changes. Take only with a doctor\'s advice.'),
                ('Injections', 'No clinical trial supports them for skin lightening, and regulators have issued warnings.'),
                ('Give it time', 'Whatever you choose, expect gradual change over 8–12 weeks, not days.'),
                ('The low-risk choice', 'A leave-on cream at night, plus sunscreen every morning.')],
         end='Read the full comparison'),
    dict(slug='glutathione-before-wedding', lang='en', guide='/glutathione-before-wedding/',
         title='Glutathione before your wedding: a 12-week plan', kicker='Wedding season',
         desc='When to start a glutathione cream before your wedding, and what to skip.',
         pages=[('12 weeks before', 'Patch test, then use the night cream 2–3 nights a week. Sunscreen every morning.'),
                ('10 weeks before', 'Skin comfortable? Move to every other night.'),
                ('8 to 3 weeks', 'Every night if your skin is happy. No new products.'),
                ('Final 2 weeks', 'Same routine. No new creams, peels or bleach. Last facial a week before.'),
                ('Skip the drips', 'Glutathione injections and IV glow drips lack trials and carry warnings.')],
         end='See the full plan'),
    dict(slug='glutathione-cream-ke-fayde', lang='hi', guide='/hi/glutathione-cream-ke-fayde/',
         title='ग्लूटाथियोन क्रीम के फायदे: 5 सच्ची बातें', kicker='ग्लूटाथियोन',
         desc='ग्लूटाथियोन क्रीम क्या कर सकती है और क्या नहीं, पांच छोटी स्लाइड में।',
         pages=[('ग्लूटाथियोन क्या है?', 'एक एंटीऑक्सीडेंट जो शरीर खुद बनाता है। यह कोशिकाओं को नुकसान से बचाता है।'),
                ('क्या फायदा हो सकता है?', 'टैनिंग और असमान रंगत 8–12 हफ्तों में धीरे-धीरे हल्की और एक-सी दिख सकती है।'),
                ('क्या नहीं होता?', 'यह आपकी प्राकृतिक त्वचा का रंग नहीं बदलती। "हमेशा के लिए गोरा" जैसे दावे सच नहीं हैं।'),
                ('कैसे लगाएं?', 'रात को चेहरा धोकर मटर के दाने जितनी क्रीम। सुबह SPF 30+ सनस्क्रीन ज़रूर।'),
                ('सावधानी', 'पहले पैच टेस्ट करें। जलन, सूजन या रैश हो तो इस्तेमाल बंद करें।')],
         end='पूरा लेख पढ़ें'),
]

_AMP_BOILER = ('<style amp-boilerplate>body{-webkit-animation:-amp-start 8s steps(1,end) 0s 1 normal both;-moz-animation:-amp-start 8s steps(1,end) 0s 1 normal both;-ms-animation:-amp-start 8s steps(1,end) 0s 1 normal both;animation:-amp-start 8s steps(1,end) 0s 1 normal both}@-webkit-keyframes -amp-start{from{visibility:hidden}to{visibility:visible}}@-moz-keyframes -amp-start{from{visibility:hidden}to{visibility:visible}}@-ms-keyframes -amp-start{from{visibility:hidden}to{visibility:visible}}@-o-keyframes -amp-start{from{visibility:hidden}to{visibility:visible}}@keyframes -amp-start{from{visibility:hidden}to{visibility:visible}}</style>'
               '<noscript><style amp-boilerplate>body{-webkit-animation:none;-moz-animation:none;-ms-animation:none;animation:none}</style></noscript>')

_STORY_CSS = '''@font-face{font-family:Manrope;src:url(/assets/fonts/manrope.woff) format("woff");font-weight:400 800;font-display:swap}
@font-face{font-family:Cormorant;src:url(/assets/fonts/cormorant.woff) format("woff");font-weight:500 700;font-display:swap}
amp-story{font-family:Manrope,system-ui,"Noto Sans Devanagari",sans-serif;color:#1B1713}
amp-story-page{background:linear-gradient(170deg,#FFF8F0 0%%,#F6E3CF 100%%)}
.alt{background:linear-gradient(170deg,#FFFDF9 0%%,#F3E7D6 100%%)}
.shade{background:linear-gradient(180deg,rgba(255,250,244,0) 45%%,rgba(255,248,240,.96) 78%%)}
.k{font-size:13px;font-weight:800;letter-spacing:.14em;text-transform:uppercase;color:#B4561B;margin:0 0 10px}
:lang(hi) .k{letter-spacing:0}
h1{font-family:Cormorant,Georgia,serif;font-size:40px;line-height:1.08;font-weight:700;margin:0}
:lang(hi) h1{font-family:Manrope,"Noto Sans Devanagari",sans-serif;font-size:32px;line-height:1.3}
h2{font-family:Cormorant,Georgia,serif;font-size:38px;line-height:1.1;font-weight:700;margin:0 0 16px;color:#1B1713}
:lang(hi) h2{font-family:Manrope,"Noto Sans Devanagari",sans-serif;font-size:30px;line-height:1.35}
p{font-size:21px;line-height:1.5;margin:0;color:#3B342D}
.num{font-size:64px;font-family:Cormorant,Georgia,serif;font-weight:700;color:#E8742A;line-height:1;margin:0 0 6px}
.pad{padding:56px 28px 40px;align-content:end}
.mid{padding:72px 28px;align-content:center}
.brand{font-size:14px;font-weight:800;color:#665D53;margin:18px 0 0}
.card{background:rgba(255,255,255,.88);border:1px solid #E7DDCF;border-radius:20px;padding:20px 18px;margin-top:22px}
.card b{display:block;font-size:18px}.card span{font-size:16px;color:#665D53}
.jar{width:62%%;margin:0 auto 10px}
'''


def _story_html(s, poster):
    path = ('/hi' if s['lang'] == 'hi' else '') + '/web-stories/%s/' % s['slug']
    logo = SITE + '/icon-192.png'
    hl = 'hi-IN' if s['lang'] == 'hi' else 'en-IN'
    ld = json.dumps({'@context': 'https://schema.org', '@type': 'Article', 'headline': s['title'], 'description': s['desc'], 'inLanguage': hl,
                     'image': [SITE + poster], 'datePublished': TODAY, 'dateModified': TODAY, 'mainEntityOfPage': SITE + path,
                     'author': {'@type': 'Organization', 'name': 'GlutaNex', 'url': SITE + '/'},
                     'publisher': {'@type': 'Organization', 'name': 'GlutaNex', 'logo': {'@type': 'ImageObject', 'url': logo, 'width': 192, 'height': 192}}}, ensure_ascii=False)
    e = html.escape
    pg = ['''<amp-story-page id="cover" auto-advance-after="7s">
<amp-story-grid-layer template="fill"><amp-img src="%s" layout="fill" object-fit="cover" alt="%s"></amp-img></amp-story-grid-layer>
<amp-story-grid-layer template="fill" class="shade"></amp-story-grid-layer>
<amp-story-grid-layer template="vertical" class="pad"><p class="k" animate-in="fade-in">%s</p><h1 animate-in="fly-in-bottom" animate-in-delay=".2s">%s</h1><p class="brand">GlutaNex</p></amp-story-grid-layer>
</amp-story-page>''' % (poster, e(POSTER_DESIGN.get(s['slug'], {}).get('alt', 'GlutaNex Glutathione Night Cream jar')), e(s['kicker']), e(s['title']))]
    for i, (h, t) in enumerate(s['pages']):
        pg.append('''<amp-story-page id="p%d"%s auto-advance-after="8s">
<amp-story-grid-layer template="vertical" class="mid"><p class="num" animate-in="fade-in">%02d</p><h2 animate-in="fly-in-left" animate-in-delay=".15s">%s</h2><p animate-in="fade-in" animate-in-delay=".45s">%s</p></amp-story-grid-layer>
</amp-story-page>''' % (i + 1, ' class="alt"' if i % 2 else '', i + 1, e(h), e(t)))
    c = PRODUCTS[0]
    pg.append('''<amp-story-page id="end">
<amp-story-grid-layer template="vertical" class="mid"><amp-img class="jar" src="%s" width="650" height="614" layout="responsive" alt="%s"></amp-img>
<div class="card"><b>%s</b><span>%s · %s · free shipping · COD</span></div></amp-story-grid-layer>
<amp-story-page-outlink layout="nodisplay" theme="custom" cta-accent-color="#E8742A" cta-accent-element="background"><a href="%s">%s</a></amp-story-page-outlink>
</amp-story-page>''' % (im('jar-cut', 'png'), e(c['name']), e(c['name']), e(c['size']), rs(c['price']), SITE + s['guide'], e(s['end'])))
    doc = '''<!doctype html>
<html amp lang="%s">
<head>
<meta charset="utf-8">
<title>%s | GlutaNex</title>
<link rel="canonical" href="%s">
<meta name="viewport" content="width=device-width">
<meta name="description" content="%s">
<meta name="robots" content="%s">
<meta property="og:title" content="%s"><meta property="og:image" content="%s"><meta property="og:type" content="article">
<link rel="icon" href="/favicon.ico">
<script async src="https://cdn.ampproject.org/v0.js"></script>
<script async custom-element="amp-story" src="https://cdn.ampproject.org/v0/amp-story-1.0.js"></script>
%s
<style amp-custom>%s</style>
<script type="application/ld+json">%s</script>
</head>
<body>
<amp-story standalone title="%s" publisher="GlutaNex" publisher-logo-src="%s" poster-portrait-src="%s">
%s
</amp-story>
</body>
</html>
''' % (hl, e(s['title']), SITE + path, e(s['desc']), 'noindex, nofollow' if PREVIEW else 'index, follow, max-image-preview:large',
       e(s['title']), SITE + poster, _AMP_BOILER, _STORY_CSS % (), ld, e(s['title']), logo, SITE + poster, '\n'.join(pg))
    d = os.path.join(ROOT, path.strip('/'))
    os.makedirs(d, exist_ok=True)
    open(os.path.join(d, 'index.html'), 'w', encoding='utf-8').write(doc)
    pages.append(path)
    return path


_story_cards = []
for _i, _s in enumerate(STORIES):
    _po = _poster(_s['slug'], STORY_HUES[_i % len(STORY_HUES)])
    _pth = _story_html(_s, _po)
    _story_cards.append('<a class="story-card" href="%s"%s><img src="%s" width="640" height="853" alt="" loading="lazy" decoding="async"><span>%s</span></a>' % (
        _pth, ' lang="hi"' if _s['lang'] == 'hi' else '', _po, html.escape(_s['title'])))

STORIES_HUB = ('<section class="section"><div class="wrap"><p class="eyebrow">Tap through</p><h1>Glutathione Web Stories</h1>'
               '<p class="story-intro">Quick, honest slides on glutathione for skin. Each one takes under a minute and links to the full guide.</p>'
               '<div class="story-grid">%s</div></div></section>' % ''.join(_story_cards))
page('/web-stories/', 'Glutathione Web Stories: quick visual guides | GlutaNex', 'Short tap-through stories on glutathione benefits, side effects, how to use glutathione cream, and cream vs tablets vs injections.',
     STORIES_HUB, crumbs=[('Web Stories', '/web-stories/')],
     schema=[{'@type': 'ItemList', 'itemListElement': [{'@type': 'ListItem', 'position': i + 1, 'url': SITE + ('/hi' if s['lang'] == 'hi' else '') + '/web-stories/%s/' % s['slug'], 'name': s['title']} for i, s in enumerate(STORIES)]}])
