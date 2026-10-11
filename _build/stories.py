# Google Web Stories (AMP story format). Read by build.py with exec(), after content.py.
# Stories can show in Google Discover and in a "Web Stories" row in search, which is big in India.
# Each story is short and honest, and its last page links to the full guide.
from PIL import Image as _Im, ImageDraw as _Dr, ImageFilter as _Fl

STORY_HUES = [((255, 246, 236), (246, 214, 186)), ((255, 248, 240), (240, 222, 200)), ((253, 244, 238), (238, 206, 196)), ((250, 247, 240), (228, 216, 190)), ((255, 245, 232), (250, 205, 160))]


def _poster(slug, hue):
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
</amp-story-page>''' % (poster, e('GlutaNex Glutathione Night Cream jar'), e(s['kicker']), e(s['title']))]
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
