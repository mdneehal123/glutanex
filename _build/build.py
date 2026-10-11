#!/usr/bin/env python3
"""Builds the GlutaNex static store into the repository root.
Run: python3 _build/build.py
Everything marked CONFIRM must be checked with the owner before the site goes live (PREVIEW = False)."""
import json, os, re, html, shutil, urllib.parse

B = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(B)

# ---------------- Settings (CONFIRM before launch) ----------------
PREVIEW = False                         # True: shows a "preview" ribbon and asks search engines not to index anything
SITE = 'https://glutanex.co.in'
WA = '919980881230'                    # same number as Youth Face and Fair N Pink
WA_SHOW = '+91 99808 81230'
OWNER = 'Beauty Mart Pvt Ltd'          # same seller as Fair N Pink
ADDR = 'Azad Nagar 4th Cross, near Anfa Park, Bhatkal, Uttara Kannada, Karnataka 581320, India'
ADVANCE = 99                           # Cash on Delivery advance, refunded if the order is cancelled, refused or undeliverable
TODAY = '2026-10-11'

PRODUCTS = [
    dict(id='cream', slug='glutanex-glutathione-night-cream', short='Night Cream', sku='GNX-CREAM',
         name='GlutaNex Glutathione Night Cream', size='30 g jar', price=2499, mrp=3000,  # confirmed 11 Oct 2026
         tag='Bestseller',
         imgs=['cream-square', 'jar-night', 'jar-hand', 'jar-bag'], og='cream-square',
         summary='A rich night cream that pairs glutathione with niacinamide, vitamin C, retinol, hyaluronic acid, ceramides and peptides, plus aloe, turmeric and neem. Made for skin that looks brighter, smoother and more even by morning.',
         title='GlutaNex Glutathione Night Cream 30g | Glutathione Cream for Face',
         desc='GlutaNex Glutathione Night Cream with niacinamide, vitamin C, retinol and hyaluronic acid for a brighter-looking, more even complexion. Cash on Delivery across India.'),
    dict(id='wash', slug='glutanex-gluta-boost-face-wash', short='Face Wash', sku='GNX-WASH-100',
         name='GlutaNex Gluta Boost Face Wash', size='100 ml pump bottle', price=399, mrp=599,  # confirmed 11 Oct 2026
         tag='New',
         imgs=['facewash-square', 'facewash'], og='facewash-square',
         summary='A gentle daily face wash from GlutaNex that cleans without stripping, the first step before your glutathione night cream.',
         title='GlutaNex Gluta Boost Face Wash 100 ml | Glutathione Face Wash',
         desc='GlutaNex Gluta Boost Face Wash, 100 ml: a gentle glutathione face wash for daily cleansing. Cash on Delivery across India.'),
    dict(id='duo', slug='glutanex-glow-duo-night-cream-face-wash', short='Glow Duo', sku='GNX-DUO',
         name='GlutaNex Glow Duo: Night Cream + Face Wash', size='Night Cream 30 g + Face Wash 100 ml', price=2699, mrp=3599,  # duo: MRP = 3000 + 599; saves 199 vs buying both separately (2898)
         tag='Save more',
         imgs=['duo-square', 'cream-square', 'facewash-square'], og='duo-square',
         summary='The full GlutaNex ritual: cleanse with Gluta Boost Face Wash, then finish with the Glutathione Night Cream. Together for ₹2,699, ₹199 less than buying both separately.',
         title='GlutaNex Glow Duo: Glutathione Night Cream + Face Wash',
         desc='GlutaNex Glow Duo: Glutathione Night Cream with Gluta Boost Face Wash at one price. A complete glutathione night routine. Cash on Delivery.'),
]
BYID = {p['id']: p for p in PRODUCTS}


def url(p):
    return '/product/%s/' % p['slug']


def rs(n):
    return '₹{:,}'.format(n)


def pct(p):
    return round((p['mrp'] - p['price']) * 100 / p['mrp']) if p['mrp'] > p['price'] else 0


def im(name, ext='webp'):
    return '/assets/img/%s.%s' % (name, ext)


NAV = [('/', 'Home'), ('/shop/', 'Shop'), ('/glutathione/', 'Glutathione'), ('/glutathione-cream/', 'Glutathione Cream'), ('/glutathione-guides/', 'Guides'),
       ('/about/', 'About'), ('/faq/', 'FAQ'), ('/track-order/', 'Track Order')]
POLICIES = [('/privacy-policy/', 'Privacy Policy'), ('/terms/', 'Terms'), ('/refund-policy/', 'Returns & Refunds'), ('/shipping-policy/', 'Shipping')]
SVG_BAG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 7h14l-1.2 11.2a2 2 0 0 1-2 1.8H8.2a2 2 0 0 1-2-1.8L5 7Z"/><path d="M9 7V6a3 3 0 0 1 6 0v1"/></svg>'
SVG_MENU = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg>'
SVG_X = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6 6 18"/></svg>'
WA_IMG = '<img src="/assets/whatsapp-glyph-green.svg" alt="" width="20" height="20">'

pages = []


def graph_base():
    return [{'@type': 'Organization', '@id': SITE + '/#org', 'name': 'GlutaNex', 'url': SITE + '/', 'logo': SITE + '/assets/img/glutanex-logo-dark.png',
             'contactPoint': {'@type': 'ContactPoint', 'telephone': '+' + WA, 'contactType': 'customer service', 'areaServed': 'IN'}},
            {'@type': 'WebSite', '@id': SITE + '/#site', 'url': SITE + '/', 'name': 'GlutaNex', 'publisher': {'@id': SITE + '/#org'}}]


def product_ld(p):
    return {'@type': 'Product', '@id': SITE + url(p) + '#product', 'name': p['name'], 'sku': p['sku'], 'brand': {'@type': 'Brand', 'name': 'GlutaNex'},
            'image': [SITE + im(i, 'jpg') for i in p['imgs']], 'description': p['desc'],
            'offers': {'@type': 'Offer', 'url': SITE + url(p), 'price': str(p['price']), 'priceCurrency': 'INR', 'availability': 'https://schema.org/InStock',
                       'itemCondition': 'https://schema.org/NewCondition', 'seller': {'@id': SITE + '/#org'},
                       'shippingDetails': {'@type': 'OfferShippingDetails', 'shippingRate': {'@type': 'MonetaryAmount', 'value': '0', 'currency': 'INR'},
                                           'shippingDestination': {'@type': 'DefinedRegion', 'addressCountry': 'IN'},
                                           'deliveryTime': {'@type': 'ShippingDeliveryTime', 'handlingTime': {'@type': 'QuantitativeValue', 'minValue': 1, 'maxValue': 2, 'unitCode': 'DAY'},
                                                            'transitTime': {'@type': 'QuantitativeValue', 'minValue': 3, 'maxValue': 7, 'unitCode': 'DAY'}}},
                       'hasMerchantReturnPolicy': {'@type': 'MerchantReturnPolicy', 'applicableCountry': 'IN', 'returnPolicyCategory': 'https://schema.org/MerchantReturnFiniteReturnWindow',
                                                   'merchantReturnDays': 7, 'returnMethod': 'https://schema.org/ReturnByMail', 'returnFees': 'https://schema.org/ReturnFeesCustomerResolution'}}}


def faq_ld(items):
    return {'@type': 'FAQPage', 'mainEntity': [{'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in items]}


def faq_html(items):
    return '<div class="faq">' + ''.join('<details><summary>%s</summary><p>%s</p></details>' % qa for qa in items) + '</div>'


def page(path, title, desc, body, schema=None, crumbs=None, index=True, og='website', ogimg='night-shift-banner', extra='', js='store.js', jar=False, lang='en-IN'):
    full = SITE + path
    nav = ''.join('<a href="%s"%s>%s</a>' % (h, ' aria-current="page"' if h == path else '', t) for h, t in NAV)
    graph = graph_base()
    if crumbs:
        graph.append({'@type': 'BreadcrumbList', 'itemListElement': [{'@type': 'ListItem', 'position': 1, 'name': 'Home', 'item': SITE + '/'}] +
                      [{'@type': 'ListItem', 'position': i + 2, 'name': n, 'item': SITE + u} for i, (n, u) in enumerate(crumbs)]})
        body = '<div class="wrap"><nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a> / ' + ' / '.join(
            ('<a href="%s">%s</a>' % (u, html.escape(n)) if i < len(crumbs) - 1 else html.escape(n)) for i, (n, u) in enumerate(crumbs)) + '</nav></div>' + body
    if schema:
        graph += schema
    robots = 'noindex, nofollow' if (PREVIEW or not index) else 'index, follow, max-image-preview:large'
    scripts = ''.join('<script src="/assets/%s" defer></script>' % j for j in (['jar3d.js'] if jar else []) + js.split(','))
    doc = '''<!doctype html>
<html lang="%(lang)s">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(title)s</title>
<meta name="description" content="%(desc)s">
<meta name="robots" content="%(robots)s">
<link rel="canonical" href="%(url)s">
<meta name="theme-color" content="#FBF7F1">
<meta property="og:type" content="%(og)s"><meta property="og:site_name" content="GlutaNex"><meta property="og:title" content="%(title)s">
<meta property="og:description" content="%(desc)s"><meta property="og:url" content="%(url)s"><meta property="og:image" content="%(site)s/assets/img/%(ogimg)s.jpg">
<meta name="twitter:card" content="summary_large_image">
%(extra)s<link rel="manifest" href="/site.webmanifest"><link rel="icon" href="/favicon.ico" sizes="48x48"><link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=Manrope:wght@400;500;600;700;800&display=swap">
<link rel="stylesheet" href="/assets/site.css">
<script type="application/ld+json">%(ld)s</script>
</head>
<body><div class="progress" aria-hidden="true"></div>
<a class="skip" href="#main">Skip to content</a>
%(ribbon)s<div class="strip">Free shipping across India<span> · </span><b>Cash on Delivery</b><span> · </span>WhatsApp support</div>
<header class="head"><div class="wrap head-in">
  <a class="brand" href="/" aria-label="GlutaNex home"><img src="/assets/img/glutanex-logo-dark.png" alt="GlutaNex – Restore your youthness" width="515" height="150"></a>
  <nav class="nav" id="nav" aria-label="Main">%(nav)s</nav>
  <button class="icon-btn menu-btn" type="button" aria-controls="nav" aria-expanded="false" aria-label="Menu">%(menu)s</button>
  <button class="icon-btn cart-btn" type="button" aria-label="Open cart" data-open-cart>%(bag)s<span class="cart-count" hidden>0</span></button>
</div></header>
<main id="main">
%(body)s
</main>
<footer><div class="wrap">
  <div class="fgrid">
    <div><a class="brand" href="/"><img src="/assets/img/glutanex-logo-light.png" alt="GlutaNex" width="515" height="150" style="height:36px;width:auto"></a>
      <p class="about">Glutathione skincare for your night ritual. Sold and shipped by %(owner)s, %(addr)s.</p></div>
    <div><h4>Shop</h4>%(shop)s</div>
    <div><h4>Glutathione guides</h4><a href="/glutathione/">What is glutathione?</a><a href="/glutathione-cream/">Glutathione cream</a><a href="/glutathione-benefits-for-skin/">Benefits for skin</a><a href="/glutathione-side-effects/">Side effects</a><a href="/how-to-use-glutathione-cream/">How to use</a><a href="/hi/">हिंदी गाइड</a><a href="/glutathione-guides/">All guides</a></div>
    <div><h4>Help</h4><a href="/contact/">Contact</a><a href="/track-order/">Track order</a>%(pol)s</div>
  </div>
  <div class="install" id="install-app" hidden><img src="/icon-192.png" alt="" width="40" height="40"><div><b>Get the GlutaNex app</b><span id="install-hint">Add GlutaNex to your home screen for quick access.</span></div><button class="btn sm" type="button" id="install-btn">Install</button></div>
  <div class="legal"><span>© 2026 GlutaNex · %(owner)s · %(addr)s</span><span>Cosmetic products. Results vary from person to person. Payments secured by Razorpay.</span></div>
</div></footer>
<div class="drawer-bg" data-close-cart></div>
<div class="drawer-wrap" aria-hidden="true"><aside class="drawer" role="dialog" aria-label="Your cart">
  <div class="drawer-h"><h2>Your cart</h2><button class="icon-btn" type="button" data-close-cart aria-label="Close cart">%(x)s</button></div>
  <div class="drawer-body" id="drawer-lines"></div>
  <div class="drawer-foot"><div class="sum" id="drawer-sum"></div><a class="btn block" href="/checkout/" id="drawer-go">Checkout</a><a class="btn wa block" id="drawer-wa" href="https://wa.me/%(wa)s" target="_blank" rel="noopener">%(waimg)s Order on WhatsApp</a></div>
</aside></div>
<a class="wa-float" href="https://wa.me/%(wa)s?text=%(watext)s" target="_blank" rel="noopener" aria-label="Chat with GlutaNex on WhatsApp"><img src="/assets/whatsapp-glyph-green.svg" alt="" width="58" height="58"></a>
%(scripts)s
</body>
</html>
''' % dict(lang=lang, title=html.escape(title), desc=html.escape(desc), robots=robots, url=full, og=og, site=SITE, ogimg=ogimg, extra=extra,
           ld=json.dumps({'@context': 'https://schema.org', '@graph': graph}, ensure_ascii=False),
           ribbon='<div class="preview-ribbon">PREVIEW · prices, business details and product facts are samples until confirmed</div>' if PREVIEW else '',
           nav=nav, menu=SVG_MENU, bag=SVG_BAG, x=SVG_X, body=body, owner=OWNER, addr=ADDR, wa=WA, waimg=WA_IMG,
           watext=urllib.parse.quote('Hi GlutaNex, I have a question.'),
           shop=''.join('<a href="%s">%s</a>' % (url(p), p['short']) for p in PRODUCTS),
           pol=''.join('<a href="%s">%s</a>' % x for x in POLICIES), scripts=scripts)
    out = os.path.join(ROOT, '404.html') if path == '/404' else os.path.join(ROOT, path.strip('/'), 'index.html')
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, 'w').write(doc)
    if index:
        pages.append(path)


def top(eyebrow, h1, lead=''):
    return '<div class="wrap page-top"><span class="eyebrow">%s</span><h1>%s</h1>%s</div>' % (eyebrow, h1, '<p>%s</p>' % lead if lead else '')


def card(p, h='h3'):
    off = pct(p)
    return '''<article class="card tilt reveal"><span class="tag">%s</span><a class="ph" href="%s"><img src="%s" alt="%s" width="800" height="800" loading="lazy"></a>
  <div class="bd"><%s><a href="%s">%s</a></%s><span class="size">%s</span>
  <div class="price"><b>%s</b>%s%s</div>
  <div class="acts"><button class="btn ghost" type="button" data-add="%s">Add to cart</button><button class="btn" type="button" data-buy="%s">Buy now</button></div></div></article>''' % (
        p['tag'], url(p), im(p['imgs'][0]), html.escape(p['name']), h, url(p), p['name'], h, p['size'], rs(p['price']),
        '<s>MRP %s</s>' % rs(p['mrp']) if off else '', '<span class="off">%d%% off</span>' % off if off else '', p['id'], p['id'])


# ---------------- Home ----------------
HOME_FAQ = [
    ('What is glutathione?', 'Glutathione is an antioxidant made of three amino acids, found naturally in the body. In skincare it is used in creams and face washes made for brighter-looking, more even skin.'),
    ('How do I use the GlutaNex Night Cream?', 'At night, wash your face with a gentle cleanser such as Gluta Boost Face Wash, pat dry and apply a small amount of the cream to the face and neck. Use sunscreen every morning.'),
    ('When will I see a difference?', 'Skin changes slowly. Use your routine every night for at least 6 to 8 weeks, with daily sunscreen, before judging. Results vary from person to person.'),
    ('Is Cash on Delivery available?', 'Yes. Pay %s online to confirm the order and the rest in cash at delivery. The advance is refunded if the order is cancelled, refused or cannot be delivered. You can also pay in full online or order on WhatsApp.' % rs(ADVANCE)),
    ('Are glutathione creams the same as glutathione injections?', 'No. Creams and face washes are cosmetics applied to the skin. Injections are a medical procedure; regulators have warned that skin-lightening injections can be unsafe. Read our guide on <a href="/glutathione-cream-vs-tablets-vs-injections/">cream vs tablets vs injections</a>.'),
]
INGREDIENTS = [
    ('Glutathione', 'Antioxidant at the heart of the formula, for a brighter-looking, more even tone.'),
    ('Niacinamide (Vitamin B3)', 'Helps with the look of dullness and uneven tone, and supports the skin barrier.'),
    ('Hyaluronic Acid', 'Draws water into the skin so it feels hydrated and looks plumper.'),
    ('Vitamin C (Ascorbic Acid)', 'Antioxidant that helps skin look fresher and more radiant.'),
    ('Retinol (Vitamin A)', 'Night-time ingredient that helps skin look smoother and more refined.'),
    ('Ceramides', 'Support the skin barrier and help lock in moisture overnight.'),
    ('Salicylic Acid (BHA)', 'Gently exfoliates inside pores so skin feels smoother and clearer.'),
    ('Peptides', 'Help skin look firmer, softer and smoother.'),
    ('Aloe Vera Extract', 'Soothes and hydrates, keeping the formula comfortable.'),
    ('Turmeric (Haldi) Extract', 'A traditional Indian ingredient loved for a radiant-looking glow.'),
    ('Neem Extract', 'A traditional Indian botanical used for clean, calm-feeling skin.'),
]
def ing_html(cls='ing'):
    return '<ul class="%s">' % cls + ''.join('<li><b>%s</b><span>%s</span></li>' % (html.escape(n), html.escape(d)) for n, d in INGREDIENTS) + '</ul>'
CREAM_USE = ('<p>Use at night only. Cleanse and pat your face dry, then smooth a pea-sized amount over the face and neck, avoiding the eyes and lips.</p>'
             '<p><b>Start slowly:</b> this cream contains retinol and salicylic acid, so use it 2 to 3 nights a week for the first two weeks, then every night if your skin is comfortable. Mild tingling or dryness at the start is common; stop if redness or burning continues.</p>'
             '<p><b>Every morning, use a broad-spectrum sunscreen</b>, because retinol and acids make skin more sensitive to the sun.</p>'
             '<p>Do not use it on the same night as other retinol, AHA/BHA or peel products. Patch test on a small area for 24 hours before first use. Not for use during pregnancy or breastfeeding unless your doctor says it is fine.</p>')
c, w, d = BYID['cream'], BYID['wash'], BYID['duo']
home = '''<section class="hero" style="padding:0"><div class="aurora" aria-hidden="true"><i></i><i></i><i></i></div><div class="spot" aria-hidden="true"></div><div class="hero-word" aria-hidden="true">Glutathione</div><div class="wrap hero-in">
  <div class="reveal">
    <h1><span class="h1-brand">GlutaNex Glutathione Night Cream</span>Your skin's <span class="gold">night shift</span> starts here.</h1>
    <p class="lead">Glutathione night care that works while you sleep: cleanse with Gluta Boost, finish with the Night Cream, wake up to skin that looks brighter and more even.</p>
    <div class="price-line"><b>%(cprice)s</b><span>Glutathione Night Cream · free shipping · Cash on Delivery</span></div>
    <div class="cta"><button class="btn" type="button" data-buy="cream">Buy the Night Cream</button><a class="btn ghost" href="/glutathione-cream/">What is glutathione cream?</a></div>
    <div class="badges"><span>Glutathione care</span><span>Night routine</span><span>Ships across India</span><span>7-day returns on sealed packs</span></div>
  </div>
  <div class="hero-stage">
    <div class="jar3d" data-jar3d data-src="/assets/img/jar-cut.webp" data-alt="GlutaNex Glutathione Night Cream jar"><img class="j3-img j3-seed" src="/assets/img/jar-cut.webp" alt="GlutaNex Glutathione Night Cream jar" width="650" height="614" fetchpriority="high" decoding="async"></div>
    <div class="orbit" aria-hidden="true"><span class="o1"><b>✦</b> Glutathione</span><span class="o2">Night ritual <b>✦</b></span><span class="o3"><b>%(cprice)s</b> · COD</span></div>
    <div class="jar-hint">Move or drag to tilt</div>
  </div>
</div></section>
<div class="marquee" aria-hidden="true"><div>%(mq)s%(mq)s</div></div>
<section id="shop"><div class="wrap">
  <div class="sec-h reveal"><span class="eyebrow">The collection</span><h2>Glutathione care, <span class="gold">made simple</span></h2><p>Two products, one ritual. Start with the Night Cream, add the Face Wash, or take the Glow Duo for the full routine.</p></div>
  <div class="grid">%(cards)s</div>
</div></section>
<section style="padding-top:0"><div class="wrap split">
  <div class="reveal"><img src="%(img_marble)s" alt="GlutaNex glutathione cream jar on a marble stand" width="586" height="645" loading="lazy"></div>
  <div class="prose reveal"><span class="eyebrow">The ingredient</span><h2 style="font-size:clamp(2.2rem,4.4vw,3.2rem);margin-top:12px">What is a glutathione cream?</h2>
    <p>Glutathione is an antioxidant made of three amino acids that the body produces naturally. In skincare, it is added to creams and face washes made for <b>brighter-looking, more even skin</b>, often alongside ingredients like niacinamide.</p>
    <p>Research on glutathione applied to the skin is still limited but encouraging: a small 2014 placebo-controlled study of a 2%% glutathione lotion found a modest, gradual improvement in skin tone over 10 weeks. Consistent use and daily sunscreen matter more than any single product.</p>
    <p><a href="/glutathione/">What is glutathione? The complete guide</a> · <a href="/glutathione-cream/">Glutathione cream guide</a> · <a href="/glutathione-side-effects/">Side effects and safe use</a></p></div>
</div></section>
<section style="padding-top:0"><div class="wrap">
  <div class="sec-h reveal"><span class="eyebrow">Inside the jar</span><h2>Glutathione, <span class="gold">plus ten skin heroes</span></h2><p>The GlutaNex Night Cream blends glutathione with well-known skincare actives and traditional Indian botanicals.</p></div>
  <div class="reveal">%(ing)s</div>
  <p class="muted reveal" style="margin-top:18px;font-size:.9rem">Contains retinol and salicylic acid: start 2 to 3 nights a week, use sunscreen every morning, and avoid during pregnancy or breastfeeding unless your doctor says it is fine.</p>
</div></section>
<section style="padding-top:0"><div class="wrap">
  <div class="sec-h reveal"><span class="eyebrow">The ritual</span><h2>Three steps, every night</h2></div>
  <ol class="ritual"><li class="reveal"><h3>Cleanse</h3><p>Massage Gluta Boost Face Wash onto damp skin and rinse. Pat dry.</p></li><li class="reveal"><h3>Apply</h3><p>Smooth a small amount of Glutathione Night Cream over face and neck.</p></li><li class="reveal"><h3>Protect</h3><p>Every morning, finish with a broad-spectrum sunscreen. It protects the work of the night.</p></li></ol>
</div></section>
<section style="padding-top:0"><div class="wrap"><div class="gallery">
  <figure class="tilt reveal"><img src="%(img_night)s" alt="GlutaNex Night Cream on a black stone with a swatch of cream" width="1134" height="680" loading="lazy"></figure>
  <figure class="tilt reveal"><img src="%(img_hand)s" alt="Hand holding the GlutaNex jar" width="1024" height="682" loading="lazy"></figure>
  <figure class="tilt reveal"><img src="%(img_bag)s" alt="GlutaNex jar in a handbag with pearls" width="1024" height="684" loading="lazy"></figure>
</div></div></section>
<section style="padding-top:0"><div class="wrap">
  <div class="sec-h reveal"><span class="eyebrow">Glutathione guides</span><h2>Know before you buy</h2></div>
  <div class="guides">
    <a class="reveal" href="/glutathione-benefits-for-skin/"><span class="eyebrow">Guide</span><h3>Glutathione benefits for skin</h3><p>What it can and cannot do, and what the research says.</p></a>
    <a class="reveal" href="/glutathione-side-effects/"><span class="eyebrow">Guide</span><h3>Glutathione side effects</h3><p>Who should be careful, and how to use creams safely.</p></a>
    <a class="reveal" href="/glutathione-cream-vs-tablets-vs-injections/"><span class="eyebrow">Guide</span><h3>Cream vs tablets vs injections</h3><p>The honest differences, including the safety warnings.</p></a>
  </div>
</div></section>
<section style="padding-top:0"><div class="wrap">
  <div class="sec-h reveal"><span class="eyebrow">Questions</span><h2>Before you order</h2></div>%(faq)s
</div></section>
<section style="padding-top:0"><div class="wrap"><div class="band2 reveal">
  <div class="b2-copy">
    <span class="eyebrow">Order your way</span>
    <h2>Pay online, on delivery, <span class="gold">or on WhatsApp</span></h2>
    <p>Choose whatever feels easiest. Every order ships free across India.</p>
    <ul class="ways">
      <li><i aria-hidden="true">₹</i><div><b>Pay online</b><span class="l">UPI, cards or net banking</span><span class="s">UPI · cards</span></div></li>
      <li><i aria-hidden="true">⌂</i><div><b>Cash on Delivery</b><span class="l">%(adv)s refundable advance, rest at your door</span><span class="s">%(adv)s advance</span></div></li>
      <li><i aria-hidden="true">✆</i><div><b>WhatsApp order</b><span class="l">Message us and we will confirm it for you</span><span class="s">We confirm it</span></div></li>
    </ul>
    <div class="b2-cta"><button class="btn" type="button" data-buy="duo"><span class="l">Get the Glow Duo · </span><span class="s">Glow Duo · </span>%(dprice)s</button><a class="btn wa" href="https://wa.me/%(wa)s?text=%(watext)s" target="_blank" rel="noopener">%(waimg)s WhatsApp<span class="l">&nbsp;us</span></a></div>
  </div>
  <figure class="b2-media"><img src="%(img_night)s" alt="GlutaNex Glutathione Night Cream jar beside a swirl of cream" loading="lazy" width="1134" height="680"></figure>
</div></div></section>''' % dict(cprice=rs(c['price']), dprice=rs(d['price']), cards=''.join(card(p) for p in PRODUCTS), faq=faq_html(HOME_FAQ), ing=ing_html(), adv=rs(ADVANCE),
                                      mq=''.join('<span>%s</span><i>✦</i>' % t for t in ['Glutathione night cream', 'Gluta Boost face wash', 'Free shipping', 'Cash on Delivery', 'Restore your youthness']),
                                      img_marble=im('jar-marble'), img_night=im('jar-night'), img_hand=im('jar-hand'), img_bag=im('jar-bag'), img_banner=im('night-shift-banner'),
                                      wa=WA, watext=urllib.parse.quote('Hi GlutaNex, I want to order.'), waimg=WA_IMG)
page('/', 'Glutathione Cream for Face | GlutaNex Night Cream & Face Wash', 'GlutaNex glutathione cream and face wash for a brighter-looking, more even complexion. Glutathione night cream from %s, free shipping, Cash on Delivery.' % rs(c['price']),
     home, jar=True, extra='<link rel="preload" as="image" href="/assets/img/jar-cut.webp" type="image/webp" fetchpriority="high">\n', schema=[{'@type': 'ItemList', 'itemListElement': [{'@type': 'ListItem', 'position': i + 1, 'url': SITE + url(p)} for i, p in enumerate(PRODUCTS)]}, faq_ld(HOME_FAQ)])

# ---------------- Shop ----------------
page('/shop/', 'Shop GlutaNex | Glutathione Night Cream, Face Wash & Duo', 'Shop GlutaNex glutathione skincare: Glutathione Night Cream, Gluta Boost Face Wash and the Glow Duo. Free shipping and Cash on Delivery across India.',
     top('Shop', 'Shop <span class="gold">GlutaNex</span>', 'Glutathione skincare for your night routine. Free shipping and Cash on Delivery on every order.') +
     '<section style="padding-top:30px"><div class="wrap"><div class="grid">%s</div></div></section>' % ''.join(card(p, 'h2') for p in PRODUCTS), crumbs=[('Shop', '/shop/')])

# ---------------- Product pages ----------------
TABS = {
    'cream': [('Key ingredients', ing_html('ing ing-sm') + '<p class="muted" style="margin-top:12px;font-size:.88rem">The complete ingredient list is printed on the pack.</p>'),
              ('How to use', CREAM_USE)],
    'wash': [('How to use', '<p>Wet your face, work a small amount into a lather and massage gently in circles. Rinse well. Use morning and night.</p>'),
             ('Ingredients', '<p class="todo">The full ingredient list will appear here exactly as printed on the pack. (CONFIRM from the final label.)</p>')],
    'duo': [('What you get', '<p>1 × GlutaNex Glutathione Night Cream 30 g and 1 × GlutaNex Gluta Boost Face Wash 100 ml.</p>'),
            ('How to use', '<p>Night: cleanse with Gluta Boost Face Wash, pat dry, then apply the Night Cream (start with 2 to 3 nights a week, as it contains retinol and salicylic acid). Morning: cleanse and finish with sunscreen.</p>'),
            ('Night Cream key ingredients', ing_html('ing ing-sm'))],
}
SHIP_TAB = ('Shipping & returns', '<p>Free shipping across India. Pay online, or choose Cash on Delivery with a %s advance (refunded if the order is cancelled, refused or cannot be delivered). Orders are packed in 1 to 2 business days and delivered in 3 to 7 business days. Sealed packs can be returned within 7 days of delivery.</p>' % rs(ADVANCE))
CREAM_FAQ = [('Can I use it during pregnancy?', 'The Night Cream contains retinol (vitamin A) and salicylic acid. Do not use it during pregnancy or breastfeeding unless your doctor says it is fine.'),
             ('Why start 2 to 3 nights a week?', 'Retinol and salicylic acid can cause mild dryness or tingling while skin gets used to them. Starting slowly and using sunscreen every morning keeps it comfortable.')]
PDP_FAQ = [('Can I pay Cash on Delivery?', 'Yes. Pay %s online to confirm and the rest at delivery. The advance is refunded if the order is cancelled, refused or cannot be delivered.' % rs(ADVANCE)),
           ('When will I see results?', 'Use it every night with daily sunscreen for at least 6 to 8 weeks before judging. Results vary from person to person.'),
           ('Is it safe for sensitive skin?', 'Patch test first on a small area for 24 hours. If redness, itching or burning continues, stop and speak to a dermatologist.')]
for p in PRODUCTS:
    off = pct(p)
    thumbs = ''.join('<button type="button" data-src="%s"%s aria-label="Picture %d"><img src="%s" alt="" width="78" height="78" loading="lazy"></button>' % (
        im(i), ' class="on"' if n == 0 else '', n + 1, im(i)) for n, i in enumerate(p['imgs']))
    tabs = TABS[p['id']] + [SHIP_TAB]
    faq_items = PDP_FAQ + (CREAM_FAQ if p['id'] in ('cream', 'duo') else [])
    others = [q for q in PRODUCTS if q['id'] != p['id']]
    body = '''<div class="wrap pdp">
  <div class="pdp-media"><div class="pdp-main tilt"><img id="pdp-img" src="%(main)s" alt="%(alt)s" width="800" height="800" fetchpriority="high"></div><div class="thumbs">%(thumbs)s</div></div>
  <div>
    <span class="eyebrow">GlutaNex · %(tag)s</span>
    <h1>%(name)s</h1>
    <div class="price"><b>%(price)s</b>%(mrp)s%(off)s</div>
    <p class="tax">Inclusive of all taxes · Free shipping · %(size)s</p>
    <p class="summary">%(summary)s</p>
    <div class="qty-row"><div class="qty" data-qty><button type="button" data-dec aria-label="Less">−</button><output>1</output><button type="button" data-inc aria-label="More">+</button></div><span class="muted" style="font-size:.88rem">In stock</span></div>
    <div class="acts"><button class="btn ghost" type="button" data-add="%(id)s" data-useqty>Add to cart</button><button class="btn" type="button" data-buy="%(id)s" data-useqty>Buy now</button><a class="btn wa" href="https://wa.me/%(wa)s?text=%(watext)s" target="_blank" rel="noopener">%(waimg)s Order on WhatsApp</a></div>
    <ul class="perks"><li>Cash on Delivery with a refundable %(adv)s advance</li><li>Free shipping across India</li><li>Sealed packs: 7-day returns</li></ul>
    <div class="tabs">%(tabs)s</div>
  </div>
</div>
<section style="padding-top:10px"><div class="wrap"><div class="sec-h"><h2>Questions</h2></div>%(faq)s
<p style="margin-top:22px" class="muted">Learn more: <a href="/glutathione-cream/">Glutathione cream guide</a> · <a href="/glutathione-side-effects/">Side effects</a> · <a href="/how-to-use-glutathione-cream/">How to use</a></p></div></section>
<section style="padding-top:10px"><div class="wrap"><div class="sec-h"><span class="eyebrow">Complete the ritual</span><h2>You may also like</h2></div><div class="grid">%(rel)s</div></div></section>
<div class="buybar" id="buybar" aria-hidden="true"><img src="%(main)s" alt="" width="44" height="44"><div class="bb-t"><b>%(short)s</b><span>%(price)s · Free shipping · COD</span></div><button class="icon-btn bb-add" type="button" data-add="%(id)s" aria-label="Add to cart">%(bag)s</button><button class="btn" type="button" data-buy="%(id)s">Buy now</button></div>''' % dict(
        main=im(p['imgs'][0]), short=html.escape(p['short']), bag=SVG_BAG, alt=html.escape(p['name']), thumbs=thumbs, tag=p['tag'], name=html.escape(p['name']), price=rs(p['price']),
        mrp='<s>MRP %s</s>' % rs(p['mrp']) if off else '', off='<span class="off">%d%% off</span>' % off if off else '', size=p['size'], summary=p['summary'], id=p['id'],
        wa=WA, watext=urllib.parse.quote('Hi GlutaNex, I want to order: %s' % p['name']), waimg=WA_IMG, adv=rs(ADVANCE),
        tabs=''.join('<details%s><summary>%s</summary><div class="in">%s</div></details>' % (' open' if n == 0 else '', t, x) for n, (t, x) in enumerate(tabs)),
        faq=faq_html(faq_items), rel=''.join(card(q) for q in others))
    page(url(p), p['title'], p['desc'], body, og='product', ogimg=p['og'], crumbs=[('Shop', '/shop/'), (p['short'], url(p))], schema=[product_ld(p), faq_ld(faq_items)],
         extra='<meta property="product:price:amount" content="%d"><meta property="product:price:currency" content="INR">\n' % p['price'])

# ---------------- Cart & checkout ----------------
page('/cart/', 'Cart | GlutaNex', 'Your GlutaNex cart.', top('Your cart', 'Cart') + '''<div class="wrap co"><div class="panel" id="cart-lines"><div class="empty">Loading your cart…</div></div>
<aside class="panel"><h2 style="font-size:1.6rem;margin-bottom:14px">Summary</h2><div class="sum" id="cart-sum"></div><a class="btn block" href="/checkout/" id="to-checkout" style="margin-top:16px">Checkout</a></aside></div>''', index=False)

checkout = top('Secure checkout', 'Checkout') + '''<div class="wrap co" id="checkout">
<div class="panel">
  <div class="steps-nav" id="steps-nav"><span class="on">1 · Contact</span><span>2 · Address</span><span>3 · Payment</span></div>
  <form class="form" id="co-form" novalidate>
  <div class="stage3d" id="stage3d">
    <div class="step on" data-step="1"><h2>Who is it for?</h2>
      <div class="f"><label for="co-name">Full name</label><input id="co-name" autocomplete="name"></div>
      <div class="f"><label for="co-phone">Mobile number</label><input id="co-phone" type="tel" inputmode="numeric" maxlength="16" autocomplete="tel"></div>
      <label class="consent" id="consent-row" hidden><input type="checkbox" id="co-consent"><span>If I don't finish my order, GlutaNex may message me on WhatsApp to help.</span></label>
      <div class="step-acts"><button class="btn" type="button" data-next>Continue to address</button></div></div>
    <div class="step" data-step="2"><h2>Where should we deliver?</h2>
      <div class="f"><label for="co-address">Full address (house no., street, area)</label><textarea id="co-address" rows="2" autocomplete="street-address"></textarea></div>
      <div class="two"><div class="f"><label for="co-pin">Pincode</label><input id="co-pin" inputmode="numeric" maxlength="6" autocomplete="postal-code"></div><div class="f"><label for="co-city">City</label><input id="co-city" autocomplete="address-level2"></div></div>
      <p class="pinnote" id="pin-note" hidden></p>
      <div class="step-acts"><button class="btn ghost" type="button" data-back>Back</button><button class="btn" type="button" data-next>Continue to payment</button></div></div>
    <div class="step" data-step="3"><h2>How would you like to pay?</h2>
      <div class="review" id="co-review"></div>
      <fieldset class="pay"><legend class="muted" style="font-size:.82rem;margin-bottom:6px">Choose one</legend>
        <label><em class="rec">Recommended</em><input type="radio" name="pay" value="online" checked><span>Pay online<small>UPI, cards, netbanking · nothing to pay at the door</small></span><b id="amt-online"></b></label>
        <label><input type="radio" name="pay" value="cod"><span>Cash on Delivery<small id="cod-note">Pay a small refundable advance now, the rest at delivery</small></span><b id="amt-cod"></b></label>
        <label><input type="radio" name="pay" value="wa"><span>Order on WhatsApp<small>Send your order, we confirm on chat</small></span><b id="amt-wa"></b></label>
      </fieldset>
      <p class="muted" id="cod-terms" style="font-size:.82rem" hidden>The advance is part of the price, not an extra charge. It is refunded in full if the order is cancelled, refused at delivery or cannot be delivered.</p>
      <div class="notyet" id="not-yet" hidden><p><b>Your order isn't placed yet.</b> The payment window closed before it finished. Your details are saved.</p><button type="button" class="btn" id="ny-retry">Try payment again</button><button type="button" class="btn ghost" id="ny-switch">Switch to Cash on Delivery</button></div>
      <p class="oerr" id="co-err" role="alert" hidden></p>
      <div class="step-acts"><button class="btn ghost" type="button" data-back>Back</button><button class="btn" type="submit" id="co-pay">Pay securely</button></div>
      <p class="muted" style="font-size:.78rem;margin-top:8px">Your details are used only to deliver this order. See our <a href="/privacy-policy/">privacy policy</a>.</p></div>
  </div>
  </form>
</div>
<aside class="panel"><h2 style="font-size:1.6rem;margin-bottom:12px">Your order</h2><div id="co-lines"></div><div class="sum" id="co-sum" style="margin-top:12px"></div></aside>
</div>'''
page('/checkout/', 'Checkout | GlutaNex', 'Secure checkout for GlutaNex orders.', checkout, index=False)


# ---------------- Google Merchant Center feed ----------------
# Price is the regular price every customer pays (no sale_price / MRP games, to avoid misrepresentation flags).
FEED_META = {
    'cream': dict(cat='Health &amp; Beauty &gt; Personal Care &gt; Cosmetics &gt; Skin Care &gt; Lotion &amp; Moisturizer', ptype='Skin Care &gt; Night Cream', grams=120,
                  desc='GlutaNex Glutathione Night Cream, 30 g jar. A night cream with glutathione, niacinamide (vitamin B3), vitamin C, hyaluronic acid, retinol, ceramides, salicylic acid, peptides, aloe vera, turmeric and neem, made for brighter-looking, more even-looking skin. Use at night, start 2 to 3 nights a week, and use sunscreen every morning. Not for use during pregnancy or breastfeeding unless a doctor approves. Patch test before use. Cosmetic product; results vary. Free shipping across India, Cash on Delivery available.'),
    'wash': dict(cat='Health &amp; Beauty &gt; Personal Care &gt; Cosmetics &gt; Skin Care &gt; Facial Cleansers', ptype='Skin Care &gt; Face Wash', grams=140,
                 desc='GlutaNex Gluta Boost Face Wash, 100 ml pump bottle. A gentle glutathione face wash for daily cleansing that cleans without stripping, the first step before a night cream. Use morning and night. Cosmetic product; results vary. Free shipping across India, Cash on Delivery available.'),
    'duo': dict(cat='Health &amp; Beauty &gt; Personal Care &gt; Cosmetics &gt; Skin Care', ptype='Skin Care &gt; Skin Care Sets', grams=260, bundle=True,
                desc='GlutaNex Glow Duo: GlutaNex Glutathione Night Cream 30 g and Gluta Boost Face Wash 100 ml together. Cleanse with the face wash, then apply the night cream; use sunscreen every morning. The night cream contains retinol and salicylic acid: start 2 to 3 nights a week, and avoid during pregnancy or breastfeeding unless a doctor approves. Cosmetic products; results vary. Free shipping across India, Cash on Delivery available.'),
}
FEED_TITLES = {'cream': 'GlutaNex Glutathione Night Cream 30 g - with Niacinamide, Vitamin C and Hyaluronic Acid',
               'wash': 'GlutaNex Gluta Boost Glutathione Face Wash 100 ml',
               'duo': 'GlutaNex Glow Duo - Glutathione Night Cream 30 g + Face Wash 100 ml'}
_fi = []
for p in PRODUCTS:
    m = FEED_META[p['id']]
    imgs = [SITE + im(i, 'jpg') for i in p['imgs']]
    _fi.append('''<item>
  <g:id>%s</g:id>
  <title>%s</title>
  <description>%s</description>
  <link>%s%s</link>
  <g:image_link>%s</g:image_link>%s
  <g:availability>in_stock</g:availability>
  <g:price>%d.00 INR</g:price>
  <g:brand>GlutaNex</g:brand>
  <g:condition>new</g:condition>
  <g:identifier_exists>no</g:identifier_exists>%s
  <g:google_product_category>%s</g:google_product_category>
  <g:product_type>%s</g:product_type>
  <g:size>%s</g:size>
  <g:shipping><g:country>IN</g:country><g:service>Standard</g:service><g:price>0.00 INR</g:price></g:shipping>
  <g:shipping_weight>%d g</g:shipping_weight>
</item>''' % (p['sku'], html.escape(FEED_TITLES[p['id']]), html.escape(m['desc']), SITE, url(p), imgs[0],
                ''.join('\n  <g:additional_image_link>%s</g:additional_image_link>' % u for u in imgs[1:]), p['price'],
                '\n  <g:is_bundle>yes</g:is_bundle>' if m.get('bundle') else '', m['cat'], m['ptype'], html.escape(p['size']), m['grams']))
os.makedirs(os.path.join(ROOT, 'feeds'), exist_ok=True)
open(os.path.join(ROOT, 'feeds', 'products.xml'), 'w', encoding='utf-8').write(
    '<?xml version="1.0" encoding="UTF-8"?>\n<rss version="2.0" xmlns:g="http://base.google.com/ns/1.0">\n<channel>\n<title>GlutaNex</title><link>%s/</link><description>GlutaNex product feed</description>\n%s\n</channel>\n</rss>\n' % (SITE, '\n'.join(_fi)))

exec(open(os.path.join(B, 'content.py'), encoding='utf-8').read())

# ---------------- Knowledge file for the question assistant (api/ask.js) ----------------
def _txt(h):
    h = re.sub(r'<(script|style)[^>]*>.*?</\1>', ' ', h, flags=re.S)
    h = re.sub(r'<a [^>]*href="([^"]+)"[^>]*>(.*?)</a>', r'\2', h)
    h = re.sub(r'</(p|li|tr|h3|div)>', '\n', h)
    h = re.sub(r'<(td|th)[^>]*>', ' | ', h)
    return re.sub(r'[ \t]+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', h))).replace(' \n', '\n').strip()
KB = [{'t': 'GlutaNex products, prices and policies', 'u': '/shop/', 's': '', 'always': True, 'x': '\n'.join([
    '%s (%s): %s, MRP %s. %s' % (p['name'], p['size'], rs(p['price']), rs(p['mrp']), _txt(p['summary'])) for p in PRODUCTS] + [
    'Glow Duo is %s, %s less than buying the Night Cream and Face Wash separately; the cart upgrades them automatically.' % (rs(BYID['duo']['price']), rs(BYID['cream']['price'] + BYID['wash']['price'] - BYID['duo']['price'])),
    'Night Cream ingredients: ' + ', '.join(n for n, d in INGREDIENTS) + '. The complete list is printed on the pack.',
    'Night Cream use: ' + _txt(CREAM_USE),
    'Shipping: free across India, packed in 1 to 2 business days, delivered in 3 to 7 business days. Track orders at /track-order/.',
    'Payment: pay online (UPI, cards, netbanking), Cash on Delivery with a %s refundable advance, or order on WhatsApp at %s.' % (rs(ADVANCE), WA_SHOW),
    'Returns: sealed products within 7 days of delivery; damaged or wrong items replaced or refunded if reported within 48 hours; opened products cannot be returned for hygiene reasons.',
    'Seller: %s, %s.' % (OWNER, ADDR)])}]
for g in GUIDES:
    body = g['body'] % P
    parts = re.split(r'<h2[^>]*>(.*?)</h2>', body)
    intro = _txt(parts[0])
    if intro:
        KB.append({'t': g['title'], 'u': guide_url(g), 's': '', 'x': intro[:1500]})
    for k in range(1, len(parts), 2):
        KB.append({'t': g['title'], 'u': guide_url(g), 's': _txt(parts[k]), 'x': _txt(parts[k + 1])[:1500]})
    for q_, a_ in g.get('faq', []):
        KB.append({'t': g['title'], 'u': guide_url(g), 's': q_ % P, 'x': _txt(a_ % P)})
for h_ in HI:
    for q_, a_ in h_['faq']:
        KB.append({'t': h_['title'], 'u': '/hi/%s/' % h_['slug'], 's': q_ % P, 'x': _txt(a_ % P)})
for q_, a_ in FAQ_ALL:
    KB.append({'t': 'GlutaNex FAQ', 'u': '/faq/', 's': q_, 'x': _txt(a_)})
open(os.path.join(ROOT, 'api', '_kb.json'), 'w', encoding='utf-8').write(json.dumps(KB, ensure_ascii=False))

# ---------------- Owner page: unfinished checkouts ----------------
page('/leads/', 'Unfinished checkouts | GlutaNex', 'Owner page.', top('Owner', 'Unfinished checkouts', 'Customers who started checkout, agreed to a WhatsApp follow-up, and did not finish. Entries disappear after 30 days.') + \
     '<section style="padding-top:20px"><div class="wrap"><form class="form leads-login" id="leads-login" autocomplete="off"><div class="f"><label for="owner-code">Owner code</label>'
     '<input id="owner-code" type="password" autocomplete="current-password" placeholder="Enter your owner code"></div><button class="btn" type="submit">Show list</button><p class="oerr" id="leads-err" hidden></p></form>'
     '<div id="leads-out"></div></div></section>', index=False, js='store.js,leads.js')

# ---------------- Offline page (shown by the app when there is no internet) ----------------
page('/offline/', 'You are offline | GlutaNex', 'No internet connection.', top('Offline', 'You are offline', 'Check your internet connection and try again. Pages you opened before still work.') +
     '<section style="padding-top:20px"><div class="wrap"><button class="btn" type="button" onclick="location.reload()">Try again</button></div></section>', index=False)

# ---------------- Assets, sitemap, robots, vercel ----------------
os.makedirs(os.path.join(ROOT, 'assets'), exist_ok=True)
for f in ['site.css', 'store.js', 'jar3d.js', 'owner.js', 'leads.js']:
    if os.path.exists(os.path.join(B, f)):
        shutil.copy(os.path.join(B, f), os.path.join(ROOT, 'assets', f))
open(os.path.join(ROOT, 'assets', 'products.json'), 'w').write(json.dumps({p['id']: {'name': p['name'], 'short': p['short'], 'price': p['price'], 'mrp': p['mrp'], 'img': im(p['imgs'][0]), 'url': url(p)} for p in PRODUCTS}, ensure_ascii=False))
sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for pth in pages:
    sm.append('  <url><loc>%s%s</loc><lastmod>%s</lastmod></url>' % (SITE, pth, TODAY))
sm.append('</urlset>')
open(os.path.join(ROOT, 'sitemap.xml'), 'w').write('\n'.join(sm) + '\n')
open(os.path.join(ROOT, 'robots.txt'), 'w').write(('User-agent: *\nDisallow: /\n' if PREVIEW else 'User-agent: *\nDisallow: /cart/\nDisallow: /checkout/\nDisallow: /reorder/\nDisallow: /leads/\nDisallow: /offline/\nDisallow: /api/\nAllow: /\n\nSitemap: %s/sitemap.xml\n' % SITE))
vercel = {'cleanUrls': False, 'headers': [{'source': '/assets/(.*)\\.(webp|jpg|png|svg)', 'headers': [{'key': 'Cache-Control', 'value': 'public, max-age=86400, stale-while-revalidate=604800'}]},
                                         {'source': '/(cart|checkout|reorder|leads|offline)/(.*)', 'headers': [{'key': 'X-Robots-Tag', 'value': 'noindex'}]},
                                         {'source': '/sw.js', 'headers': [{'key': 'Cache-Control', 'value': 'no-cache'}]},
                                         {'source': '/site.webmanifest', 'headers': [{'key': 'Content-Type', 'value': 'application/manifest+json'}]}]}
open(os.path.join(ROOT, 'vercel.json'), 'w').write(json.dumps(vercel, indent=2) + '\n')
# ---------------- Install as an app: manifest + service worker ----------------
import hashlib
_ver = hashlib.md5(b''.join(open(os.path.join(ROOT, 'assets', f), 'rb').read() for f in ['site.css', 'store.js', 'jar3d.js', 'products.json'])).hexdigest()[:10]
open(os.path.join(ROOT, 'site.webmanifest'), 'w').write(json.dumps({
    'name': 'GlutaNex – Glutathione Skincare', 'short_name': 'GlutaNex', 'description': 'GlutaNex glutathione night cream and face wash. Free shipping and Cash on Delivery across India.',
    'id': '/', 'start_url': '/?source=app', 'scope': '/', 'display': 'standalone', 'orientation': 'portrait',
    'background_color': '#FBF7F1', 'theme_color': '#FBF7F1', 'lang': 'en-IN', 'categories': ['shopping', 'beauty', 'lifestyle'],
    'icons': [{'src': '/icon-192.png', 'sizes': '192x192', 'type': 'image/png', 'purpose': 'any'}, {'src': '/icon-512.png', 'sizes': '512x512', 'type': 'image/png', 'purpose': 'any'}, {'src': '/icon-maskable-512.png', 'sizes': '512x512', 'type': 'image/png', 'purpose': 'maskable'}],
    'shortcuts': [{'name': 'Shop', 'url': '/shop/', 'icons': [{'src': '/icon-192.png', 'sizes': '192x192'}]},
                  {'name': 'Track order', 'url': '/track-order/', 'icons': [{'src': '/icon-192.png', 'sizes': '192x192'}]},
                  {'name': 'Glutathione guide', 'url': '/glutathione/', 'icons': [{'src': '/icon-192.png', 'sizes': '192x192'}]}]}, ensure_ascii=False, indent=1))
PRECACHE = ['/', '/offline/', '/shop/', '/glutathione/', '/assets/site.css', '/assets/store.js', '/assets/jar3d.js', '/assets/products.json',
            '/assets/img/jar-cut.webp', '/assets/img/glutanex-logo-dark.png', '/assets/img/glutanex-logo-light.png', '/assets/whatsapp-glyph-green.svg', '/icon-192.png']
open(os.path.join(ROOT, 'sw.js'), 'w').write('''/* GlutaNex app: keeps the shop fast and usable on weak connections. Version %s */
var V='gn-%s', CORE=%s;
self.addEventListener('install',function(e){e.waitUntil(caches.open(V).then(function(c){return c.addAll(CORE);}).then(function(){return self.skipWaiting();}));});
self.addEventListener('activate',function(e){e.waitUntil(caches.keys().then(function(ks){return Promise.all(ks.filter(function(k){return k!==V;}).map(function(k){return caches.delete(k);}));}).then(function(){return self.clients.claim();}));});
self.addEventListener('fetch',function(e){
  var r=e.request,u=new URL(r.url);
  if(r.method!=='GET'){return;}
  if(u.origin===location.origin&&(u.pathname.indexOf('/api/')===0||/^\\/(checkout|leads)\\//.test(u.pathname))){return;}
  if(u.origin!==location.origin&&!/fonts\\.(googleapis|gstatic)\\.com$/.test(u.hostname)){return;}
  if(r.mode==='navigate'){
    e.respondWith(fetch(r).then(function(res){var cp=res.clone();caches.open(V).then(function(c){c.put(r,cp);});return res;}).catch(function(){return caches.match(r).then(function(m){return m||caches.match('/offline/');});}));
    return;}
  e.respondWith(caches.match(r).then(function(m){var net=fetch(r).then(function(res){if(res&&(res.ok||res.type==='opaque')){var cp=res.clone();caches.open(V).then(function(c){c.put(r,cp);});}return res;}).catch(function(){return m;});return m||net;}));
});
''' % (_ver, _ver, json.dumps(PRECACHE)))
open(os.path.join(ROOT, '.vercelignore'), 'w').write('_build\nREADME.md\n')
print('built', len(pages), 'indexed pages', '(PREVIEW: noindex everywhere)' if PREVIEW else '')
