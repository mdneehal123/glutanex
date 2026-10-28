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
TODAY = '2026-10-11'
INDEXNOW_KEY = 'a7f3c9e15b2d4086b1e8d3f0c62a97e4'

PRODUCTS = [
    dict(id='cream', slug='glutanex-glutathione-night-cream', short='Night Cream', sku='GNX-CREAM',
         name='GlutaNex Glutathione Night Cream', size='30 g jar', price=2499, mrp=3000,  # confirmed 11 Oct 2026
         tag='Bestseller',
         imgs=['cream-square', 'jar-night', 'jar-hand', 'jar-bag'], og='cream-square',
         summary='A rich night cream that pairs glutathione with niacinamide, vitamin C, retinol, hyaluronic acid, ceramides and peptides, plus aloe, turmeric and neem. Made for skin that looks brighter, smoother and more even by morning.',
         title='Glutathione Face Cream for Night, 30 g | GlutaNex Night Cream',
         sub='Glutathione face cream · night formula with niacinamide and vitamin C',
         alt_names=['GlutaNex Glutathione Face Cream', 'Glutathione Cream for Face'],
         desc='GlutaNex glutathione face cream for night with niacinamide, vitamin C, retinol and hyaluronic acid, for brighter, more even-looking skin. COD across India.'),
    dict(id='wash', slug='glutanex-gluta-boost-face-wash', short='Face Wash', sku='GNX-WASH-100',
         name='GlutaNex Gluta Boost Face Wash', size='100 ml pump bottle', price=399, mrp=599,  # confirmed 11 Oct 2026
         tag='Launching soon', soon=True,
         imgs=['facewash-square', 'facewash', 'facewash-foam'], og='facewash-square',
         summary='A daily foaming gel face wash made with glutathione and copper peptide, plus niacinamide, aloe, chamomile and panthenol. It lifts away dirt, oil and the day\'s build-up and leaves skin feeling fresh and soft, and it is the first step before your glutathione night cream.',
         title='Gluta Boost Face Wash 100 ml | Glutathione & Copper Peptide',
         sub='Glutathione face wash · foaming gel with copper peptide and niacinamide',
         alt_names=['GlutaNex Glutathione Face Wash', 'Gluta Boost Glutathione Face Wash'],
         desc='GlutaNex Gluta Boost Face Wash, 100 ml: a foaming glutathione face wash with copper peptide, niacinamide, aloe and panthenol for daily cleansing. For all skin types. COD across India.',
         meta_desc='GlutaNex Gluta Boost Face Wash 100 ml: foaming glutathione face wash with copper peptide, niacinamide, aloe and panthenol. All skin types. COD across India.'),
    dict(id='duo', slug='glutanex-glow-duo-night-cream-face-wash', short='Glow Duo', sku='GNX-DUO',
         name='GlutaNex Glow Duo: Night Cream + Face Wash', size='Night Cream 30 g + Face Wash 100 ml', price=2699, mrp=3599,  # duo: MRP = 3000 + 599; saves 199 vs buying both separately (2898)
         tag='Launching soon', soon=True,
         imgs=['duo-square', 'cream-square', 'facewash-square'], og='duo-square',
         summary='The full GlutaNex ritual: cleanse with Gluta Boost Face Wash, then finish with the Glutathione Night Cream. Launching soon.',
         title='GlutaNex Glow Duo: Glutathione Night Cream + Face Wash',
         desc='GlutaNex Glow Duo: Glutathione Night Cream with Gluta Boost Face Wash at one price. A complete glutathione night routine. Cash on Delivery.'),
    dict(id='gel', slug='glutanex-aqua-fresh-shower-gel', short='Shower Gel', sku='GNX-GEL-100', soon=True, price=0, mrp=0,
         name='GlutaNex Aqua Fresh Shower Gel', size='100 ml pump bottle', tag='Launching soon',
         imgs=['gel-square', 'washgel-square'], og='gel-square',
         summary='A refreshing glutathione shower gel with hyaluronic acid and aloe vera. It cleanses, refreshes and leaves skin feeling moisturised, for all skin types. Launching soon.',
         title='Glutathione Shower Gel 100 ml | GlutaNex Aqua Fresh',
         sub='Glutathione shower gel · with hyaluronic acid and aloe vera',
         alt_names=['GlutaNex Glutathione Body Wash', 'Aqua Fresh Glutathione Shower Gel'],
         desc='GlutaNex Aqua Fresh Shower Gel, 100 ml: a glutathione shower gel with hyaluronic acid and aloe vera that cleanses, refreshes and moisturises. For all skin types. Launching soon.',
         meta_desc='GlutaNex Aqua Fresh Shower Gel 100 ml: a glutathione shower gel with hyaluronic acid and aloe vera that cleanses and refreshes. All skin types. Launching soon.'),
    dict(id='washgel', slug='glutanex-face-wash-shower-gel-combo', short='Wash + Gel Combo', sku='GNX-WASHGEL', soon=True, price=0, mrp=0,
         name='GlutaNex Face Wash + Shower Gel Combo', size='Face Wash 100 ml + Shower Gel 100 ml', tag='Launching soon',
         imgs=['washgel-square', 'gel-square', 'facewash-square'], og='washgel-square',
         summary='Two glutathione cleansers in one set: Gluta Boost Face Wash for your face and Aqua Fresh Shower Gel for your bath. A daily cleansing combo from GlutaNex. Launching soon.',
         title='Glutathione Face Wash + Shower Gel Combo | GlutaNex',
         sub='Glutathione face wash and shower gel combo · 100 ml + 100 ml',
         alt_names=['GlutaNex Glutathione Cleansing Combo'],
         desc='GlutaNex Face Wash + Shower Gel combo: Gluta Boost Face Wash 100 ml with Aqua Fresh Shower Gel 100 ml, a glutathione cleansing set for face and body. Launching soon.',
         meta_desc='GlutaNex Face Wash + Shower Gel combo: Gluta Boost Face Wash 100 ml and Aqua Fresh Shower Gel 100 ml, a glutathione set for face and body. Launching soon.'),
    dict(id='creamgel', slug='glutanex-night-cream-shower-gel-combo', short='Cream + Gel Combo', sku='GNX-CREAMGEL', soon=True, price=0, mrp=0,
         name='GlutaNex Night Cream + Shower Gel Combo', size='Night Cream 30 g + Shower Gel 100 ml', tag='Launching soon',
         imgs=['creamgel-square', 'cream-square', 'gel-square'], og='creamgel-square',
         summary='The Glutathione Night Cream for your night routine and the Aqua Fresh Shower Gel for your daily bath, together in one GlutaNex set. Launching soon.',
         title='Glutathione Night Cream + Shower Gel Combo | GlutaNex',
         sub='Glutathione night cream 30 g and shower gel 100 ml set',
         alt_names=['GlutaNex Night Cream and Shower Gel Set'],
         desc='GlutaNex Night Cream + Shower Gel combo: Glutathione Night Cream 30 g with Aqua Fresh Shower Gel 100 ml. A glutathione skincare set for night care and daily bathing. Launching soon.',
         meta_desc='GlutaNex Night Cream + Shower Gel combo: Glutathione Night Cream 30 g with Aqua Fresh Shower Gel 100 ml, for night care and daily bathing. Launching soon.'),
    dict(id='trio', slug='glutanex-glow-trio-night-cream-face-wash-shower-gel', short='Glow Trio', sku='GNX-TRIO', soon=True, price=0, mrp=0,
         name='GlutaNex Glow Trio: Night Cream + Face Wash + Shower Gel', size='Night Cream 30 g + Face Wash 100 ml + Shower Gel 100 ml', tag='Launching soon',
         imgs=['trio-square', 'trio-sun', 'cream-square'], og='trio-square',
         summary='The complete GlutaNex range in one set: Gluta Boost Face Wash, Aqua Fresh Shower Gel and the Glutathione Night Cream. Launching soon.',
         title='GlutaNex Glow Trio: Glutathione Skincare Set of 3',
         sub='Glutathione night cream + face wash + shower gel set',
         alt_names=['GlutaNex Glutathione Skincare Combo Pack', 'GlutaNex 3-in-1 Skincare Set'],
         desc='GlutaNex Glow Trio: Glutathione Night Cream 30 g, Gluta Boost Face Wash 100 ml and Aqua Fresh Shower Gel 100 ml together. The full GlutaNex glutathione skincare set. Launching soon.',
         meta_desc='GlutaNex Glow Trio: Glutathione Night Cream 30 g, Gluta Boost Face Wash 100 ml and Aqua Fresh Shower Gel 100 ml. The full GlutaNex set. Launching soon.'),
]
BYID = {p['id']: p for p in PRODUCTS}


def url(p):
    return '/product/%s/' % p['slug']


def rs(n):
    return '₹{:,}'.format(n)


def pct(p):
    return round((p['mrp'] - p['price']) * 100 / p['mrp']) if p['mrp'] > p['price'] else 0


def wl_form(product, cls='', named=False):
    return ('<form class="wl %s" data-waitlist data-product="%s" hidden novalidate><div class="wl-t"><b>🎁 Join the waitlist · get 10%% off at launch</b><span>Your personal code works for 7 days from launch day.</span></div>'
            '<div class="wl-row">%s<input name="phone" type="tel" inputmode="numeric" maxlength="16" autocomplete="tel" placeholder="Mobile number" aria-label="Mobile number"><button class="btn" type="submit">Join waitlist</button></div>'
            '<label class="wl-c"><input type="checkbox" name="consent"><span>You may message me on WhatsApp about this launch and related offers.</span></label><p class="wl-msg" aria-live="polite" hidden></p></form>') % (
        cls, product, '<input name="name" autocomplete="name" placeholder="Your name (optional)" aria-label="Your name">' if named else '')


def notify_url(p):
    return 'https://wa.me/%s?text=%s' % (WA, urllib.parse.quote('Hi GlutaNex, please message me when %s is available.' % p['name']))


def notify_btn(p, cls='btn wa'):
    return '<a class="%s" href="%s" target="_blank" rel="noopener">%s Notify me on WhatsApp</a>' % (cls, notify_url(p), WA_IMG)


# Search-friendly file names for Google Images (source files keep their short names in assets/img and are copied at build time)
SEO_IMG = {'cream-square': 'glutanex-glutathione-night-cream-30g', 'jar-night': 'glutathione-night-cream-jar-glutanex',
           'jar-hand': 'glutanex-glutathione-cream-in-hand', 'jar-bag': 'glutanex-glutathione-night-cream-travel',
           'jar-marble': 'glutanex-glutathione-face-cream', 'facewash-square': 'glutanex-gluta-boost-glutathione-face-wash-100ml',
           'facewash': 'gluta-boost-face-wash-carton-glutanex', 'facewash-foam': 'gluta-boost-face-wash-foam-glutanex', 'gel-square': 'glutanex-aqua-fresh-glutathione-shower-gel-100ml', 'washgel-square': 'glutanex-face-wash-and-shower-gel-combo', 'creamgel-square': 'glutanex-night-cream-and-shower-gel-combo', 'trio-square': 'glutanex-glow-trio-night-cream-face-wash-shower-gel', 'trio-sun': 'glutanex-glutathione-skincare-trio-set', 'duo-square': 'glutanex-glow-duo-glutathione-cream-face-wash',
           'night-shift-banner': 'glutathione-night-cream-routine-glutanex', 'jar-cut': 'glutanex-glutathione-night-cream-jar'}


def im(name, ext='webp'):
    return '/assets/img/%s.%s' % (SEO_IMG.get(name, name), ext)


# Real customer review images, added on the owner's confirmation (22 Oct 2026) that Priya S., Sneha K., Anjali M. and Riya P.
# wrote these words and agreed to them (and, for Anjali, her photo) being shown.
REVIEW_SEC = '<section style="padding-top:0"><div class="wrap"><div class="sec-h reveal"><span class="eyebrow">From our customers</span><h2>What customers say</h2></div><div class="revs rail-m reveal"><figure><img src="/assets/img/glutanex-night-cream-customer-review.webp" alt="Customer review of GlutaNex Night Cream by Priya S.: made my skin smoother, brighter and more even, woke up with healthy, glowing skin every morning" width="720" height="720" loading="lazy" decoding="async"></figure><figure><img src="/assets/img/glutanex-night-cream-customer-review-sneha.webp" alt="Customer review of GlutaNex Night Cream by Sneha K.: skin feels soft, smooth and hydrated, gives a natural glow and keeps skin fresh all day" width="720" height="720" loading="lazy" decoding="async"></figure><figure><img src="/assets/img/glutanex-night-cream-customer-review-anjali.webp" alt="Customer review of GlutaNex Night Cream by Anjali M.: after 3 weeks dark spots look lighter and skin looks fresh and radiant" width="720" height="720" loading="lazy" decoding="async"></figure><figure><img src="/assets/img/glutanex-night-cream-customer-review-riya.webp" alt="Customer review of GlutaNex Night Cream by Riya P.: improved skin texture, reduced dullness and gives a visible glow" width="720" height="720" loading="lazy" decoding="async"></figure></div><p class="muted" style="font-size:.85rem;margin-top:10px;text-align:center">Reviews shared by GlutaNex customers, shown with their permission. Results vary from person to person.</p></div></section>\n'


NAV = [('/', 'Home'), ('/shop/', 'Shop'), ('/glutathione/', 'Glutathione'), ('/glutathione-cream/', 'Cream Guide'), ('/glutathione-guides/', 'Guides'),
       ('/about/', 'About'), ('/faq/', 'FAQ'), ('/track-order/', 'Track Order')]
POLICIES = [('/privacy-policy/', 'Privacy Policy'), ('/terms/', 'Terms'), ('/refund-policy/', 'Returns & Refunds'), ('/shipping-policy/', 'Shipping')]
SVG_BAG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 7h14l-1.2 11.2a2 2 0 0 1-2 1.8H8.2a2 2 0 0 1-2-1.8L5 7Z"/><path d="M9 7V6a3 3 0 0 1 6 0v1"/></svg>'
SVG_MENU = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg>'
SVG_X = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6 6 18"/></svg>'
INSTAGRAM = 'https://www.instagram.com/glutanexofficial/'
# marketplace stores, shown in the footer. Logos: put the OFFICIAL file at assets/img/market-<name>.svg (or .png);
# until a file is there, a text badge is shown. Never draw these logos by hand: they are the marketplaces' trademarks.
MARKET_LINKS = [('Amazon', 'https://amzn.in/d/0a1LcDUz'), ('Flipkart', 'https://dl.flipkart.com/s/nLf9OfNNNN'),
                ('Myntra', 'https://www.myntra.com/mailers/night-cream/glutanex/glutanex-skin-whitening-cream-with-glutathione-restore-your-youthful-glow--30g/30981116/buy')]


def _market_badge(n, u):
    for ext in ('svg', 'png', 'webp'):
        f = 'assets/img/market-%s.%s' % (n.lower(), ext)
        if os.path.exists(os.path.join(ROOT, f)):
            return '<a class="mkt" href="%s" target="_blank" rel="noopener" aria-label="GlutaNex on %s"><img src="/%s" alt="%s" height="22" loading="lazy"></a>' % (html.escape(u), n, f, n)
    return '<a class="mkt" href="%s" target="_blank" rel="noopener">%s</a>' % (html.escape(u), n)
WA_IMG = '<img src="/assets/whatsapp-glyph-green.svg" alt="" width="20" height="20">'

pages = []
# asset version: changes whenever the stylesheet or any script changes, so browsers can cache them for a year
import hashlib as _hl, glob as _glob
AV = _hl.md5(b''.join(open(f, 'rb').read() for f in sorted(_glob.glob(os.path.join(B, '*.js')) + [os.path.join(B, 'site.css')]))).hexdigest()[:10]


def mincss(c):
    # careful minifier: drops comments and spacing only; selectors and values are untouched otherwise
    c = re.sub(r'/\*.*?\*/', '', c, flags=re.S)
    c = re.sub(r'\s+', ' ', c)
    c = re.sub(r'\s*([{};,>])\s*', r'\1', c)
    c = re.sub(r':\s+', ':', c)
    return c.replace(';}', '}').strip()
SEARCH = []  # site search index, written to assets/search.json


# extra official profiles (YouTube, Pinterest, LinkedIn, marketplace brand stores) go here as they are created
BRAND_PROFILES = []
BRAND_DESC = ('GlutaNex is an Indian glutathione skincare brand (Glutathione Night Cream and Gluta Boost Face Wash) from %s, Bhatkal, Karnataka. '
              'Official website glutanex.co.in; also sold on Amazon, Flipkart and Myntra. GlutaNex does not make or sell glutathione injections or tablets.' % OWNER)


def graph_base():
    addr = {'@type': 'PostalAddress', 'streetAddress': 'Azad Nagar 4th Cross, near Anfa Park', 'addressLocality': 'Bhatkal', 'addressRegion': 'Karnataka',
            'postalCode': '581320', 'addressCountry': 'IN'}
    logo = {'@type': 'ImageObject', '@id': SITE + '/#logo', 'url': SITE + '/assets/img/glutanex-logo-dark.png', 'contentUrl': SITE + '/assets/img/glutanex-logo-dark.png',
            'width': 515, 'height': 150, 'caption': 'GlutaNex'}
    return [{'@type': 'OnlineStore', '@id': SITE + '/#org', 'name': 'GlutaNex', 'alternateName': ['Glutanex', 'GlutaNex India', 'GlutaNex Skincare'],
             'url': SITE + '/', 'logo': logo, 'image': {'@id': SITE + '/#logo'}, 'description': BRAND_DESC,
             'sameAs': [INSTAGRAM] + BRAND_PROFILES, 'publishingPrinciples': SITE + '/our-standards/', 'address': addr, 'areaServed': 'IN',
             'brand': {'@id': SITE + '/#brand'}, 'parentOrganization': {'@type': 'Organization', 'name': OWNER, 'address': addr},
             'knowsAbout': ['Glutathione', 'Glutathione cream', 'Skincare', 'Tan removal', 'Niacinamide'],
             'hasMerchantReturnPolicy': {'@type': 'MerchantReturnPolicy', 'applicableCountry': 'IN', 'returnPolicyCategory': 'https://schema.org/MerchantReturnFiniteReturnWindow',
                                         'merchantReturnDays': 7, 'returnMethod': 'https://schema.org/ReturnByMail', 'returnFees': 'https://schema.org/ReturnFeesCustomerResolution',
                                         'merchantReturnLink': SITE + '/refund-policy/'},
             'contactPoint': {'@type': 'ContactPoint', 'telephone': '+' + WA, 'contactType': 'customer service', 'areaServed': 'IN', 'availableLanguage': ['English', 'Hindi']}},
            {'@type': 'Brand', '@id': SITE + '/#brand', 'name': 'GlutaNex', 'alternateName': 'Glutanex', 'url': SITE + '/glutanex/', 'logo': {'@id': SITE + '/#logo'}},
            {'@type': 'WebSite', '@id': SITE + '/#site', 'url': SITE + '/', 'name': 'GlutaNex', 'alternateName': ['Glutanex', 'glutanex.co.in'], 'inLanguage': 'en-IN',
             'publisher': {'@id': SITE + '/#org'}}]


def img_ld(u, caption=''):
    # credit and licence details, so Google Images can show 'Licensable' and the credit line
    d = {'@type': 'ImageObject', 'url': u, 'contentUrl': u, 'creator': {'@type': 'Organization', 'name': 'GlutaNex', '@id': SITE + '/#org'}, 'creditText': 'GlutaNex',
         'copyrightNotice': '© 2026 GlutaNex (%s)' % OWNER, 'license': SITE + '/image-licence/', 'acquireLicensePage': SITE + '/image-licence/'}
    if caption:
        d['caption'] = caption
    return d


def product_ld(p):
    d = _product_ld(p)
    if p.get('soon'):
        d.pop('offers', None)
    return d


def _product_ld(p):
    extra_p = {'cream': {'additionalProperty': [{'@type': 'PropertyValue', 'name': 'Key ingredients', 'value': ', '.join(n for n, d in INGREDIENTS)}, {'@type': 'PropertyValue', 'name': 'When to use', 'value': 'Night'}]},
               'wash': {'additionalProperty': [{'@type': 'PropertyValue', 'name': 'Key ingredients', 'value': 'Glutathione, copper peptide, niacinamide, aloe, chamomile, panthenol'}, {'@type': 'PropertyValue', 'name': 'Skin type', 'value': 'All skin types'}, {'@type': 'PropertyValue', 'name': 'When to use', 'value': 'Morning and night'}]},
               'gel': {'additionalProperty': [{'@type': 'PropertyValue', 'name': 'Key ingredients', 'value': 'Glutathione, hyaluronic acid, aloe vera'}, {'@type': 'PropertyValue', 'name': 'Skin type', 'value': 'All skin types'}]},
               'duo': {'isRelatedTo': [{'@id': SITE + url(BYID['cream']) + '#product'}, {'@id': SITE + url(BYID['wash']) + '#product'}]}}.get(p['id'], {})
    return dict({'@type': 'Product', '@id': SITE + url(p) + '#product', 'name': p['name'], **({'alternateName': p['alt_names']} if p.get('alt_names') else {}), 'sku': p['sku'], 'mpn': p['sku'], 'size': p['size'], 'category': 'Health & Beauty > Personal Care > Cosmetics > Skin Care', 'brand': {'@type': 'Brand', '@id': SITE + '/#brand', 'name': 'GlutaNex'},
            'image': [img_ld(SITE + im(i, 'jpg'), p['name']) for i in p['imgs']], 'description': p['desc'],
            'offers': {'@type': 'Offer', 'url': SITE + url(p), 'price': str(p['price']), 'priceCurrency': 'INR', 'priceValidUntil': '2027-12-31', 'availability': 'https://schema.org/InStock',
                       'itemCondition': 'https://schema.org/NewCondition', 'seller': {'@id': SITE + '/#org'},
                       'shippingDetails': {'@type': 'OfferShippingDetails', 'shippingRate': {'@type': 'MonetaryAmount', 'value': '0', 'currency': 'INR'},
                                           'shippingDestination': {'@type': 'DefinedRegion', 'addressCountry': 'IN'},
                                           'deliveryTime': {'@type': 'ShippingDeliveryTime', 'handlingTime': {'@type': 'QuantitativeValue', 'minValue': 1, 'maxValue': 2, 'unitCode': 'DAY'},
                                                            'transitTime': {'@type': 'QuantitativeValue', 'minValue': 3, 'maxValue': 7, 'unitCode': 'DAY'}}},
                       'hasMerchantReturnPolicy': {'@type': 'MerchantReturnPolicy', 'applicableCountry': 'IN', 'returnPolicyCategory': 'https://schema.org/MerchantReturnFiniteReturnWindow',
                                                   'merchantReturnDays': 7, 'returnMethod': 'https://schema.org/ReturnByMail', 'returnFees': 'https://schema.org/ReturnFeesCustomerResolution'}}}, **extra_p)


def faq_ld(items):
    return {'@type': 'FAQPage', 'mainEntity': [{'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in items]}


def faq_html(items):
    return '<div class="faq">' + ''.join('<details><summary>%s</summary><p>%s</p></details>' % qa for qa in items) + '</div>'


SVG_SEARCH = '<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.6-3.6"/></svg>'
SVG_HOME = '<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" aria-hidden="true"><path d="M3.5 10.5 12 3.8l8.5 6.7V20a1 1 0 0 1-1 1H15v-6.5H9V21H4.5a1 1 0 0 1-1-1z"/></svg>'
SVG_GRID = '<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><rect x="3.5" y="3.5" width="7" height="7" rx="1.6"/><rect x="13.5" y="3.5" width="7" height="7" rx="1.6"/><rect x="3.5" y="13.5" width="7" height="7" rx="1.6"/><rect x="13.5" y="13.5" width="7" height="7" rx="1.6"/></svg>'
SVG_TRUCK = '<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" aria-hidden="true"><path d="M2.5 6.5h11v9.5h-11zM13.5 9.5h4l3 3.2V16h-7z"/><circle cx="6.5" cy="17.5" r="1.8" fill="#fff"/><circle cx="17" cy="17.5" r="1.8" fill="#fff"/></svg>'


def range_strip():
    items = ''.join('<a href="%s"><img src="%s" alt="%s" width="120" height="120" loading="lazy" decoding="async"><b>%s</b><span>%s</span></a>' % (
        url(x), im(x['imgs'][0]), html.escape(x['name']), html.escape(x['short']), 'Launching soon' if x.get('soon') else 'Available now') for x in PRODUCTS)
    return '<section class="range-strip"><div class="wrap"><h2>The GlutaNex range</h2><div class="rs-grid">%s</div></div></section>' % items


def page(path, title, desc, body, schema=None, crumbs=None, index=True, og='website', ogimg='night-shift-banner', extra='', js='store.js', jar=False, lang='en-IN', ptype='WebPage', main=None):
    full = SITE + path
    if 'class="side-cta"' in body and 'range-strip' not in body:
        body += range_strip()
    nav = ''.join('<a href="%s"%s>%s</a>' % (h, ' aria-current="page"' if h == path else '', t) for h, t in NAV)
    graph = graph_base()
    if crumbs:
        graph.append({'@type': 'BreadcrumbList', '@id': full + '#breadcrumb', 'itemListElement': [{'@type': 'ListItem', 'position': 1, 'name': 'Home', 'item': SITE + '/'}] +
                      [{'@type': 'ListItem', 'position': i + 2, 'name': n, 'item': SITE + u} for i, (n, u) in enumerate(crumbs)]})
        body = '<div class="wrap"><nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a> / ' + ' / '.join(
            ('<a href="%s">%s</a>' % (u, html.escape(n)) if i < len(crumbs) - 1 else html.escape(n)) for i, (n, u) in enumerate(crumbs)) + '</nav></div>' + body
    if schema:
        graph += schema
    # one WebPage node per page, tied to the site, its breadcrumb, language and main subject
    if index and path != '/404' and not any(x.get('@type') == 'AboutPage' for x in graph):
        wp = {'@type': ptype, '@id': full + '#webpage', 'url': full, 'name': re.sub(r'\s*\|\s*GlutaNex.*$', '', title), 'description': desc, 'inLanguage': lang,
              'isPartOf': {'@id': SITE + '/#site'}, 'publisher': {'@id': SITE + '/#org'}}
        if crumbs:
            wp['breadcrumb'] = {'@id': full + '#breadcrumb'}
        art = next((x for x in graph if x.get('@type') == 'Article'), None)
        if main:
            wp['mainEntity'] = {'@id': main}
        elif art:
            art['@id'] = full + '#article'
            wp['mainEntity'] = {'@id': full + '#article'}
        if art and art.get('about'):
            wp['about'] = art['about']
        graph.append(wp)
    robots = 'noindex, nofollow' if (PREVIEW or not index) else 'index, follow, max-image-preview:large'
    scripts = ''.join('<script src="/assets/%s?v=%s" defer></script>' % (j, AV) for j in (['jar3d.js'] if jar else []) + js.split(',') + (['talk.js'] if '[data-talk]' in body or 'data-talk' in body else []) + (['waitlist.js'] if 'data-waitlist' in body else []))
    doc = '''<!doctype html>
<html lang="%(lang)s">
<head>
<meta charset="utf-8">
<script>(function(){try{var d=document.documentElement,q=location.search,n=new Date(),h=n.getHours(),p=function(x){return (x<10?'0':'')+x;},
t=(/[?&]theme=(night|morning|day)/.exec(q)||[])[1]||(h>=19||h<5?'night':h<11?'morning':'day'),ds=n.getFullYear()+'-'+p(n.getMonth()+1)+'-'+p(n.getDate()),md=ds.slice(5),
F=[['diwali','2026-10-29','2026-11-12'],['sankranti','2027-01-13','2027-01-16']],f=(/[?&]fest=(diwali|christmas|newyear|sankranti)/.exec(q)||[])[1]||'';
if(!f){F.forEach(function(x){if(ds>=x[1]&&ds<=x[2]){f=x[0];}});if(!f&&md>='12-23'&&md<='12-26'){f='christmas';}if(!f&&(md==='12-31'||md==='01-01')){f='newyear';}}
d.className+=' t-'+t+(f?' fest-'+f:'');d.setAttribute('data-today',ds);}catch(e){}})();</script>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(title)s</title>
<meta name="description" content="%(desc)s">
<meta name="robots" content="%(robots)s">
<link rel="canonical" href="%(url)s">
<meta name="theme-color" content="#FBF7F1">
<meta property="og:type" content="%(og)s"><meta property="og:site_name" content="GlutaNex"><meta property="og:title" content="%(title)s">
<meta property="og:description" content="%(desc)s"><meta property="og:url" content="%(url)s"><meta property="og:image" content="%(site)s%(ogsrc)s">
<meta name="twitter:card" content="summary_large_image">
%(extra)s<link rel="manifest" href="/site.webmanifest"><link rel="icon" href="/favicon.ico" sizes="48x48"><link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
<link rel="preload" href="/assets/fonts/manrope.woff" as="font" type="font/woff" crossorigin><link rel="preload" href="/assets/fonts/cormorant.woff" as="font" type="font/woff" crossorigin>
<link rel="stylesheet" href="/assets/site.css?v=%(av)s">
<script type="application/ld+json">%(ld)s</script>
</head>
<body%(bodycls)s><div class="progress" aria-hidden="true"></div>
<a class="skip" href="#main">Skip to content</a>
%(ribbon)s<div class="strip">Free shipping across India<span> · </span><b>Cash on Delivery</b><span> · </span>WhatsApp support</div>
<header class="head"><div class="wrap head-in">
  <a class="brand" href="/" aria-label="GlutaNex home"><img src="/assets/img/glutanex-logo-dark.png" alt="GlutaNex – Restore your youthness" width="515" height="150"></a>
  <nav class="nav" id="nav" aria-label="Main">%(nav)s</nav>
  <button class="icon-btn search-btn" type="button" aria-label="Search" data-search>%(srch)s</button>
  <button class="icon-btn menu-btn" type="button" aria-controls="nav" aria-expanded="false" aria-label="Menu">%(menu)s</button>
  <button class="icon-btn cart-btn" type="button" aria-label="Open cart" data-open-cart>%(bag)s<span class="cart-count" hidden>0</span></button>
</div></header>
<main id="main">
%(body)s
</main>
<footer><div class="wrap">
  <div class="fgrid">
    <div><a class="brand" href="/"><img src="/assets/img/glutanex-logo-light.png" alt="GlutaNex" width="515" height="150" style="height:36px;width:auto"></a>
      <p class="about">Glutathione skincare for your night ritual. Sold and shipped by %(owner)s, %(addr)s.</p><a class="social" href="%(insta)s" target="_blank" rel="noopener">Instagram · @glutanexofficial</a></div>
    <div><h4>Shop</h4>%(shop)s</div>
    <div><h4>Glutathione guides</h4><a href="/glutathione/">What is glutathione?</a><a href="/glutathione-cream-questions/">Glutathione questions</a><a href="/glutathione-cream/">Glutathione cream</a><a href="/glutathione-benefits-for-skin/">Benefits for skin</a><a href="/glutathione-side-effects/">Side effects</a><a href="/how-to-use-glutathione-cream/">How to use</a><a href="/hi/">हिंदी गाइड</a><a href="/hinglish/">Hinglish guide</a><span class="langs"><a href="/ta/glutathione-cream/" lang="ta">தமிழ்</a><a href="/te/glutathione-cream/" lang="te">తెలుగు</a><a href="/mr/glutathione-cream/" lang="mr">मराठी</a><a href="/bn/glutathione-cream/" lang="bn">বাংলা</a><a href="/kn/glutathione-cream/" lang="kn">ಕನ್ನಡ</a></span><a href="/glutathione-guides/">All guides</a></div>
    <div><h4>Help</h4><a href="/skin-quiz/">Skin quiz</a><a href="/wholesale/">Wholesale</a><a href="/glutanex/">Brand facts</a><a href="/our-standards/">Our standards</a><a href="/image-licence/">Image licence</a><a href="/contact/">Contact</a><a href="/track-order/">Track order</a><a href="/reminders/">Reminders</a><a href="/web-stories/">Web Stories</a>%(pol)s</div>
  </div>
  <div class="markets"><span>Also available on</span>%(markets)s</div>
  <div class="markets"><span>Also from our family</span><a href="https://mircglow.com/" target="_blank" rel="noopener">Mirc Glow avocado night creams</a></div>
  <div class="install" id="install-app" hidden><img src="/icon-192.png" alt="" width="40" height="40"><div><b>Get the GlutaNex app</b><span id="install-hint">Add GlutaNex to your home screen for quick access.</span></div><button class="btn sm" type="button" id="install-btn">Install</button></div>
  <div class="legal"><span>© 2026 GlutaNex · %(owner)s · %(addr)s</span><span>Cosmetic products. Results vary from person to person. Payments secured by Razorpay.</span></div>
</div></footer>
<div class="drawer-bg" data-close-cart></div>
<div class="drawer-wrap" aria-hidden="true"><aside class="drawer" role="dialog" aria-label="Your cart">
  <div class="drawer-h"><h2>Your cart</h2><button class="icon-btn" type="button" data-close-cart aria-label="Close cart">%(x)s</button></div>
  <div class="drawer-body" id="drawer-lines"></div>
  <div class="drawer-foot"><div class="sum" id="drawer-sum"></div><a class="btn block" href="/checkout/" id="drawer-go">Checkout</a><a class="btn wa block" id="drawer-wa" href="https://wa.me/%(wa)s" target="_blank" rel="noopener">%(waimg)s Order on WhatsApp</a></div>
</aside></div>
<nav class="tabbar" aria-label="Quick menu">
  <a href="/"%(t_home)s>%(i_home)s<span>Home</span></a>
  <button type="button" data-search>%(srch)s<span>Search</span></button>
  <a href="/shop/"%(t_shop)s>%(i_shop)s<span>Shop</span></a>
  <a href="/track-order/"%(t_track)s>%(i_track)s<span>Track</span></a>
  <button type="button" data-open-cart>%(bag)s<span>Cart</span><b class="tb-count" hidden>0</b></button>
</nav>
<div class="sov" id="sov" hidden role="dialog" aria-modal="true" aria-label="Search GlutaNex"><div class="sov-in">
  <div class="sov-top"><div class="sov-box">%(srch)s<input id="sov-q" type="search" placeholder="Search: night cream, side effects, हिंदी…" autocomplete="off" enterkeyhint="search" aria-label="Search"></div><button type="button" class="sov-x" data-close-search>Cancel</button></div>
  <div class="sov-res" id="sov-res" aria-live="polite"></div>
</div></div>
<a class="wa-float" href="https://wa.me/%(wa)s?text=%(watext)s" target="_blank" rel="noopener" aria-label="Chat with GlutaNex on WhatsApp"><img src="/assets/whatsapp-glyph-green.svg" alt="" width="58" height="58"></a>
%(scripts)s
</body>
</html>
''' % dict(lang=lang, insta=INSTAGRAM, ogsrc=im(ogimg, 'jpg'), title=html.escape(title), desc=html.escape(desc), robots=robots, url=full, og=og, site=SITE, ogimg=ogimg, extra=extra,
           ld=json.dumps({'@context': 'https://schema.org', '@graph': graph}, ensure_ascii=False),
           ribbon='<div class="preview-ribbon">PREVIEW · prices, business details and product facts are samples until confirmed</div>' if PREVIEW else '',
           nav=nav, menu=SVG_MENU, bag=SVG_BAG, x=SVG_X, body=body, owner=OWNER, addr=ADDR, wa=WA, waimg=WA_IMG,
           watext=urllib.parse.quote('Hi GlutaNex, I have a question.'),
           shop=''.join('<a href="%s">%s</a>' % (url(p), p['short']) for p in PRODUCTS),
           av=AV, bodycls=' class="checkout-page"' if path == '/checkout/' else '', srch=SVG_SEARCH, i_home=SVG_HOME, i_shop=SVG_GRID, i_track=SVG_TRUCK, t_home=' aria-current="page"' if path == '/' else '', t_shop=' aria-current="page"' if path == '/shop/' or path.startswith('/product/') else '', t_track=' aria-current="page"' if path == '/track-order/' else '', pol=''.join('<a href="%s">%s</a>' % x for x in POLICIES), markets=''.join(_market_badge(n, u) for n, u in MARKET_LINKS), scripts=scripts)
    out = os.path.join(ROOT, '404.html') if path == '/404' else os.path.join(ROOT, path.strip('/'), 'index.html')
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, 'w').write(doc)
    if index:
        pages.append(path)
        SEARCH.append({'u': path, 't': re.sub(r'\s*\|\s*GlutaNex.*$', '', title), 'd': desc[:180], 'l': lang[:2]})


def top(eyebrow, h1, lead=''):
    return '<div class="wrap page-top"><span class="eyebrow">%s</span><h1>%s</h1>%s</div>' % (eyebrow, h1, '<p>%s</p>' % lead if lead else '')


def card(p, h='h3'):
    off = pct(p)
    if p.get('soon'):
        return '''<article class="card tilt reveal soon"><span class="tag">Launching soon</span><a class="ph" href="%s"><img src="%s" alt="%s" width="800" height="800" loading="lazy"></a>
  <div class="bd"><%s><a href="%s">%s</a></%s><span class="size">%s</span>
  <div class="price"><b class="soon-txt">Launching soon</b></div>
  <div class="acts"><a class="btn ghost" href="%s">View details</a>%s</div></div></article>''' % (
            url(p), im(p['imgs'][0]), html.escape(p['name']), h, url(p), p['name'], h, p['size'], url(p), notify_btn(p))
    return '''<article class="card tilt reveal"><span class="tag">%s</span><a class="ph" href="%s"><img src="%s" alt="%s" width="800" height="800" loading="lazy"></a>
  <div class="bd"><%s><a href="%s">%s</a></%s><span class="size">%s</span>
  <div class="price"><b>%s</b>%s%s</div>
  <div class="acts"><button class="btn ghost" type="button" data-add="%s">Add to cart</button><button class="btn" type="button" data-buy="%s">Buy now</button></div></div></article>''' % (
        p['tag'], url(p), im(p['imgs'][0]), html.escape(p['name']), h, url(p), p['name'], h, p['size'], rs(p['price']),
        '<s>MRP %s</s>' % rs(p['mrp']) if off else '', '<span class="off">%d%% off</span>' % off if off else '', p['id'], p['id'])


# ---------------- Home ----------------
HOME_FAQ = [
    ('What is glutathione?', 'Glutathione is an antioxidant made of three amino acids, found naturally in the body. In skincare it is used in creams and face washes made for brighter-looking, more even skin.'),
    ('How do I use the GlutaNex Night Cream?', 'At night, wash your face with a gentle cleanser (the Gluta Boost Face Wash is launching soon), pat dry and apply a small amount of the cream to the face and neck. Use sunscreen every morning.'),
    ('When will I see a difference?', 'Skin changes slowly. Use your routine every night for at least 6 to 8 weeks, with daily sunscreen, before judging. Results vary from person to person.'),
    ('Is Cash on Delivery available?', 'Yes. Choose Cash on Delivery at checkout and pay the full amount in cash when your parcel arrives: nothing to pay in advance and no COD fee. You can also pay online or order on WhatsApp.'),
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
HOME_STORIES = [('glutathione-benefits-for-skin', 'Glutathione for skin: 5 honest facts', ''), ('how-to-use-glutathione-cream', 'How to use glutathione cream', ''),
                ('glutathione-side-effects', 'Glutathione side effects', ''), ('glutathione-before-wedding', 'Before your wedding: 12-week plan', ''),
                ('glutathione-cream-vs-tablets-vs-injections', 'Cream vs tablets vs injections', ''), ('glutathione-cream-ke-fayde', 'ग्लूटाथियोन क्रीम के फायदे', 'hi')]
_soonp = [x for x in PRODUCTS if x.get('soon')]
SOONBAND = ('<section style="padding-top:0"><div class="wrap"><div class="soonband reveal"><figure class="sb-media"><img src="%s" alt="GlutaNex Gluta Boost Face Wash, Aqua Fresh Shower Gel and Glutathione Night Cream on satin" width="900" height="900" loading="lazy" decoding="async"></figure>'
            '<div class="sb-copy"><span class="eyebrow">Launching soon</span><h2>The complete range in one set: <span class="gold">the Glow Trio</span></h2>'
            '<p>Gluta Boost Face Wash, Aqua Fresh Shower Gel and the Glutathione Night Cream together. Tell us once and we will message you on WhatsApp the day it is ready. No payment, no commitment.</p>'
            '<div class="cta">%s<a class="btn ghost" href="%s">See the Glow Trio</a></div></div></div></div></section>\n') % (
    im('trio-square'), notify_btn(BYID['trio']), url(BYID['trio']))
RANGE_FEATURE = ('<article class="range-feat reveal"><a class="rf-ph" href="%s"><img src="%s" alt="%s" width="800" height="800" loading="lazy"><span class="tag">Bestseller · Available now</span></a>'
                 '<div class="rf-body"><span class="eyebrow">Glutathione Night Cream · %s</span><h3><a href="%s">%s</a></h3>'
                 '<p>%s</p><ul class="rf-pts"><li>Glutathione with niacinamide, vitamin C and hyaluronic acid</li><li>Night use: start 2 to 3 nights a week, sunscreen every morning</li><li>Free shipping across India · Cash on Delivery · 7-day returns on sealed packs</li></ul>'
                 '<div class="price"><b>%s</b>%s%s</div><div class="acts"><button class="btn" type="button" data-buy="cream">Buy now</button><button class="btn ghost" type="button" data-add="cream">Add to cart</button><a class="btn ghost" href="%s">Details</a></div></div></article>') % (
    url(c), im(c['imgs'][0]), html.escape(c['name']), html.escape(c['size']), url(c), html.escape(c['name']), html.escape(c['summary']), rs(c['price']),
    '<s>MRP %s</s>' % rs(c['mrp']), '<span class="off">%d%% off</span>' % pct(c), url(c))
RANGE_CARDS = ''.join('<article class="rcard reveal"><a class="rc-ph" href="%s"><img src="%s" alt="%s" width="800" height="800" loading="lazy"><span class="tag">Launching soon</span></a><div class="rc-bd"><h4><a href="%s">%s</a></h4><span class="size">%s</span>%s</div></article>' % (
    url(x), im(x['imgs'][0]), html.escape(x['name']), url(x), html.escape(x['name']), html.escape(x['size']), notify_btn(x, 'btn wa sm')) for x in PRODUCTS if x.get('soon'))
home = '''<section class="dban" data-dban aria-roledescription="carousel" aria-label="GlutaNex highlights"><div class="db-track"><div class="db-s"><picture><source type="image/webp" srcset="/assets/img/banner-night-cream-1600.webp 1600w, /assets/img/banner-night-cream.webp 2400w" sizes="100vw"><img src="/assets/img/banner-night-cream.jpg" alt="GlutaNex Glutathione Night Cream jar on black stone with a swatch of cream" width="2400" height="1000" fetchpriority="high" decoding="async"></picture><div class="db-t"><span class="db-e">Available now</span><p class="db-h">Your skin's <em>night shift</em> starts here.</p><p class="db-p">Glutathione Night Cream, 30 g. Free shipping across India and Cash on Delivery.</p><div class="db-c"><button class="btn" type="button" data-buy="cream">Buy the Night Cream · ₹2,499</button><a class="btn ghost" href="/glutathione-cream/">What is glutathione cream?</a></div></div></div><div class="db-s"><picture><source type="image/webp" srcset="/assets/img/banner-glow-trio-1600.webp 1600w, /assets/img/banner-glow-trio.webp 2400w" sizes="100vw"><img src="/assets/img/banner-glow-trio.jpg" alt="GlutaNex Glow Trio: face wash, shower gel and night cream on satin" width="2400" height="1000" loading="lazy" decoding="async"></picture><div class="db-t"><span class="db-e">Launching soon</span><p class="db-h">Face. Body. <em>Night.</em></p><p class="db-p">The Glow Trio: Night Cream, Gluta Boost Face Wash and Aqua Fresh Shower Gel, together.</p><div class="db-c"><a class="btn" href="/product/glutanex-glow-trio-night-cream-face-wash-shower-gel/">See the Glow Trio</a><a class="btn ghost" href="/shop/">Shop all</a></div></div></div><div class="db-s"><picture><source type="image/webp" srcset="/assets/img/banner-face-wash-1600.webp 1600w, /assets/img/banner-face-wash.webp 2400w" sizes="100vw"><img src="/assets/img/banner-face-wash.jpg" alt="GlutaNex Gluta Boost Face Wash bottle on satin" width="2400" height="1000" loading="lazy" decoding="async"></picture><div class="db-t"><span class="db-e">Launching soon</span><p class="db-h">Cleanse with <em>Gluta Boost.</em></p><p class="db-p">A foaming gel face wash with glutathione, copper peptide and niacinamide.</p><div class="db-c"><a class="btn" href="/product/glutanex-gluta-boost-face-wash/">Meet the Face Wash</a><a class="btn ghost" href="/skin-quiz/">Take the skin quiz</a></div></div></div><div class="db-s"><picture><source type="image/webp" srcset="/assets/img/banner-shower-gel-1600.webp 1600w, /assets/img/banner-shower-gel.webp 2400w" sizes="100vw"><img src="/assets/img/banner-shower-gel.jpg" alt="GlutaNex Aqua Fresh Shower Gel bottle on satin" width="2400" height="1000" loading="lazy" decoding="async"></picture><div class="db-t"><span class="db-e">Launching soon</span><p class="db-h">Aqua Fresh, <em>neck to toe.</em></p><p class="db-p">A glutathione shower gel with hyaluronic acid and aloe vera for fresh, soft skin.</p><div class="db-c"><a class="btn" href="/product/glutanex-aqua-fresh-shower-gel/">Meet the Shower Gel</a><a class="btn ghost" href="/glutathione-shower-gel/">Read the guide</a></div></div></div></div><button class="db-nav db-prev" type="button" aria-label="Previous banner">&#8249;</button><button class="db-nav db-next" type="button" aria-label="Next banner">&#8250;</button><div class="db-dots" aria-hidden="true"></div></section>
<section class="hero" style="padding:0"><div class="aurora" aria-hidden="true"><i></i><i></i><i></i></div><div class="sky" aria-hidden="true"><i class="orb"></i></div><div class="fest" aria-hidden="true"></div><div class="spot" aria-hidden="true"></div><div class="hero-word" aria-hidden="true">Glutathione</div><div class="wrap hero-in">
  %(wlhero_m)s
  <div class="reveal">
    %(wlhero)s
    <a class="hero-pill" href="#shop"><b>New</b> Face Wash, Shower Gel and 4 sets launching soon <i aria-hidden="true">→</i></a>
    <h1><span class="h1-brand">GlutaNex Glutathione Night Cream</span>Your skin's <span class="gold">night shift</span> starts here.</h1>
    <p class="lead">A glutathione face cream that works while you sleep: cleanse with Gluta Boost, finish with the Night Cream, wake up to skin that looks brighter and more even.</p>
    <div class="price-line"><b>%(cprice)s</b><span>Glutathione Night Cream · about %(pernight)s a night · free shipping · Cash on Delivery</span></div>
    <div class="cta"><button class="btn" type="button" data-buy="cream">Buy the Night Cream</button><a class="btn ghost" href="/glutathione-cream/">What is glutathione cream?</a></div>
    <button class="jar-talk hero-talk" type="button" data-talk hidden><span class="jt-dot"></span>🎙️ Talk to the jar<small>Ask out loud in English, हिंदी, Hinglish, தமிழ்…</small></button>
    <div class="badges"><span>Glutathione care</span><span>Night routine</span><span>Ships across India</span><span>7-day returns on sealed packs</span></div>
  </div>
  <div class="hero-stage">
    <div class="hs" data-hs role="region" aria-roledescription="carousel" aria-label="GlutaNex products"><div class="hs-track"><figure class="hs-s"><picture><source srcset="/assets/img/glutathione-night-cream-routine-glutanex.webp" type="image/webp"><img fetchpriority="high" src="/assets/img/glutathione-night-cream-routine-glutanex.jpg" alt="GlutaNex Night Cream: your skin's night shift starts here" width="1254" height="1254" decoding="async"></picture><figcaption><b>Glutathione Night Cream</b><span>Your night ritual · 30 g</span></figcaption></figure><figure class="hs-s"><picture><source srcset="/assets/img/glutanex-gluta-boost-glutathione-face-wash-100ml.webp" type="image/webp"><img loading="lazy" src="/assets/img/glutanex-gluta-boost-glutathione-face-wash-100ml.jpg" alt="GlutaNex Gluta Boost Face Wash 100 ml" width="1200" height="1200" decoding="async"></picture><figcaption><b>Gluta Boost Face Wash</b><span>Launching soon · 100 ml</span></figcaption></figure><figure class="hs-s"><picture><source srcset="/assets/img/glutanex-glow-duo-glutathione-cream-face-wash.webp" type="image/webp"><img loading="lazy" src="/assets/img/glutanex-glow-duo-glutathione-cream-face-wash.jpg" alt="GlutaNex Glow Duo: night cream and face wash" width="900" height="900" decoding="async"></picture><figcaption><b>Glow Duo</b><span>Night cream + face wash · launching soon</span></figcaption></figure><figure class="hs-s"><picture><source srcset="/assets/img/glutanex-glow-trio-night-cream-face-wash-shower-gel.webp" type="image/webp"><img loading="lazy" src="/assets/img/glutanex-glow-trio-night-cream-face-wash-shower-gel.jpg" alt="GlutaNex Glow Trio: night cream, face wash and shower gel" width="900" height="900" decoding="async"></picture><figcaption><b>Glow Trio</b><span>Face + body set · launching soon</span></figcaption></figure><figure class="hs-s"><picture><source srcset="/assets/img/glutanex-glutathione-cream-in-hand.webp" type="image/webp"><img loading="lazy" src="/assets/img/glutanex-glutathione-cream-in-hand.jpg" alt="Hand holding a GlutaNex night cream jar" width="1024" height="682" decoding="async"></picture><figcaption><b>A small night ritual</b><span>Pea-sized, every evening</span></figcaption></figure></div><button class="hs-nav hs-prev" type="button" aria-label="Previous photo">&#8249;</button><button class="hs-nav hs-next" type="button" aria-label="Next photo">&#8250;</button><div class="hs-dots" aria-hidden="true"></div></div>
  </div>
</div></section>
<div class="marquee" aria-hidden="true"><div>%(mq)s%(mq)s</div></div>
<section class="ritual" aria-labelledby="h-ritual"><div class="wrap"><div class="rit-h reveal"><span class="eyebrow">The GlutaNex ritual</span><h2 id="h-ritual">Three steps. One <span class="gold">quiet glow.</span></h2><p>A simple routine, from face to body, built around glutathione.</p></div>
<div class="rit-grid">
<article class="rit reveal"><span class="rit-n">I</span><div class="rit-ph"><img src="/assets/img/gluta-boost-face-wash-carton-glutanex.jpg" alt="GlutaNex Gluta Boost Face Wash with its carton" width="600" height="600" loading="lazy" decoding="async"></div><span class="rit-k">Cleanse</span><h3>Gluta Boost Face Wash</h3><p>A foaming gel with glutathione, copper peptide and niacinamide that lifts away the day.</p><em>Launching soon</em></article>
<article class="rit reveal"><span class="rit-n">II</span><div class="rit-ph"><img src="/assets/img/glutathione-night-cream-jar-glutanex.jpg" alt="GlutaNex Glutathione Night Cream with a swatch of cream" width="600" height="600" loading="lazy" decoding="async"></div><span class="rit-k">Treat</span><h3>Glutathione Night Cream</h3><p>Glutathione with niacinamide, hyaluronic acid and aloe vera, pressed in as the last step of your night.</p><em>Available now</em></article>
<article class="rit reveal"><span class="rit-n">III</span><div class="rit-ph"><img src="/assets/img/glutanex-aqua-fresh-glutathione-shower-gel-100ml.jpg" alt="GlutaNex Aqua Fresh Shower Gel" width="600" height="600" loading="lazy" decoding="async"></div><span class="rit-k">Refresh</span><h3>Aqua Fresh Shower Gel</h3><p>Glutathione, hyaluronic acid and aloe vera for skin that feels fresh and soft from neck to toe.</p><em>Launching soon</em></article>
</div><p class="rit-note">Gradual results, best with daily sunscreen. Cosmetic products, not medicines.</p></div></section>
<section id="shop" class="range"><div class="wrap">
  <div class="sec-h reveal"><span class="eyebrow">The collection</span><h2>Glutathione care, <span class="gold">made simple</span></h2><p>Start with the Night Cream, available now. The Face Wash, the Aqua Fresh Shower Gel and four ready-made sets are launching soon: tap Notify me and we will message you on WhatsApp when they are ready.</p></div>
  %(rangefeature)s
  <div class="range-head reveal"><h3>Launching soon</h3><a href="/shop/">See all products →</a></div>
  <div class="range-rail">%(rangecards)s</div>
  <a class="quizcta reveal" href="/skin-quiz/"><b>Not sure which one?</b><span>Take the 30-second skin quiz →</span></a>
</div></section>
%(soonband)s
<section class="promise-sec" style="padding-top:0"><div class="wrap"><ul class="promise reveal">
  <li><b>Clear ingredients</b><span>Know what goes on your skin: ingredients are printed on every pack.</span></li>
  <li><b>Honest claims</b><span>Gradual results with sunscreen. No "fair in 7 days" promises.</span></li>
  <li><b>COD + 7-day returns</b><span>Pay at your door; sealed packs can be returned within 7 days.</span></li>
  <li><b>Real people on WhatsApp</b><span>Questions before or after you order, Monday to Saturday.</span></li>
</ul></div></section>
<section style="padding-top:0"><div class="wrap split">
  <div class="reveal hide-m"><img src="%(img_marble)s" alt="GlutaNex glutathione cream jar on a marble stand" width="586" height="645" loading="lazy"></div>
  <div class="prose reveal"><span class="eyebrow">The ingredient</span><h2 style="font-size:clamp(2.2rem,4.4vw,3.2rem);margin-top:12px">What is a glutathione cream?</h2>
    <p>Glutathione is an antioxidant made of three amino acids that the body produces naturally. In skincare, it is added to creams and face washes made for <b>brighter-looking, more even skin</b>, often alongside ingredients like niacinamide. A <b>glutathione face cream</b> is a leave-on cream, the format used in research, which is why it does more than a wash-off product.</p>
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
  <ol class="ritual"><li class="reveal"><h3>Cleanse</h3><p>Massage a gentle face wash such as Gluta Boost (launching soon) onto damp skin and rinse. Pat dry.</p></li><li class="reveal"><h3>Apply</h3><p>Smooth a small amount of Glutathione Night Cream over face and neck.</p></li><li class="reveal"><h3>Protect</h3><p>Every morning, finish with a broad-spectrum sunscreen. It protects the work of the night.</p></li></ol>
</div></section>
<section style="padding-top:0"><div class="wrap">
  <div class="sec-h reveal"><span class="eyebrow">What to expect</span><h2>Your first <span class="gold">12 weeks</span></h2><p>Glutathione works gradually. Here is an honest timeline with nightly use and daily sunscreen.</p></div>
  <ol class="timeline">
    <li class="reveal"><span class="wk">Weeks 1–2</span><b>Start slowly</b><p>Use the Night Cream 2–3 nights a week. A little tingling at first is normal.</p></li>
    <li class="reveal"><span class="wk">Weeks 3–4</span><b>Build up</b><p>Every other night. Skin feels smoother and looks fresher.</p></li>
    <li class="reveal"><span class="wk">Weeks 5–8</span><b>Every night</b><p>Tan and dullness start to look lighter; tone looks more even.</p></li>
    <li class="reveal"><span class="wk">Weeks 8–12</span><b>Keep it going</b><p>The most even-looking result, kept with sunscreen every morning.</p></li>
  </ol>
  <p class="muted reveal" style="margin-top:14px;font-size:.88rem">Results vary from person to person. Glutathione does not change your natural skin colour. <a href="/how-to-use-glutathione-cream/">Full routine</a></p>
</div></section>
<section style="padding-top:0"><div class="wrap"><div class="gallery rail-m">
  <figure class="tilt reveal"><img src="%(img_night)s" alt="GlutaNex glutathione night cream on a black stone with a swatch of cream" width="1134" height="680" loading="lazy"></figure>
  <figure class="tilt reveal"><img src="%(img_hand)s" alt="Hand holding a GlutaNex glutathione night cream jar" width="1024" height="682" loading="lazy"></figure>
  <figure class="tilt reveal"><img src="%(img_bag)s" alt="GlutaNex glutathione night cream 30 g jar in a handbag" width="1024" height="684" loading="lazy"></figure>
</div></div></section>
%(review)s<section style="padding-top:0"><div class="wrap">
  <div class="sec-h reveal"><span class="eyebrow">Glutathione guides</span><h2>Know before you buy</h2></div>
  <div class="guides rail-m">
    <a class="reveal" href="/glutathione-benefits-for-skin/"><span class="eyebrow">Guide</span><h3>Glutathione benefits for skin</h3><p>What it can and cannot do, and what the research says.</p></a>
    <a class="reveal" href="/glutathione-side-effects/"><span class="eyebrow">Guide</span><h3>Glutathione side effects</h3><p>Who should be careful, and how to use creams safely.</p></a>
    <a class="reveal" href="/glutathione-cream-vs-tablets-vs-injections/"><span class="eyebrow">Guide</span><h3>Cream vs tablets vs injections</h3><p>The honest differences, including the safety warnings.</p></a>
  </div>
</div></section>
<section style="padding-top:0"><div class="wrap">
  <div class="sec-h reveal"><span class="eyebrow">Web Stories</span><h2>Glutathione in <span class="gold">one minute</span></h2></div>
  <div class="srail">%(storycards)s</div>
</div></section>
<section style="padding-top:0"><div class="wrap"><div class="langband reveal"><b>Read about glutathione in your language</b><div>
  <a href="/hi/" lang="hi">हिंदी</a><a href="/hinglish/">Hinglish</a><a href="/ta/glutathione-cream/" lang="ta">தமிழ்</a><a href="/te/glutathione-cream/" lang="te">తెలుగు</a><a href="/mr/glutathione-cream/" lang="mr">मराठी</a><a href="/bn/glutathione-cream/" lang="bn">বাংলা</a><a href="/kn/glutathione-cream/" lang="kn">ಕನ್ನಡ</a>
</div></div></div></section>
<section style="padding-top:0"><div class="wrap">
  <div class="sec-h reveal"><span class="eyebrow">Questions</span><h2>Before you order</h2></div>%(faq)s
  <p style="margin-top:20px"><a class="btn ghost" href="/glutathione-cream-questions/">More glutathione cream questions answered</a></p>
</div></section>
<section style="padding-top:0"><div class="wrap"><div class="band2 reveal">
  <div class="b2-copy">
    <span class="eyebrow">Order your way</span>
    <h2>Pay online, on delivery, <span class="gold">or on WhatsApp</span></h2>
    <p>Choose whatever feels easiest. Every order ships free across India.</p>
    <ul class="ways">
      <li><i aria-hidden="true">₹</i><div><b>Pay online</b><span class="l">UPI, cards or net banking</span><span class="s">UPI · cards</span></div></li>
      <li><i aria-hidden="true">⌂</i><div><b>Cash on Delivery</b><span class="l">Nothing to pay now, pay at your door</span><span class="s">Pay at door</span></div></li>
      <li><i aria-hidden="true">✆</i><div><b>WhatsApp order</b><span class="l">Message us and we will confirm it for you</span><span class="s">We confirm it</span></div></li>
    </ul>
    <div class="b2-cta"><a class="btn" href="%(duourl)s"><span class="l">Glow Duo · launching soon</span><span class="s">Glow Duo · soon</span></a><a class="btn wa" href="https://wa.me/%(wa)s?text=%(watext)s" target="_blank" rel="noopener">%(waimg)s WhatsApp<span class="l">&nbsp;us</span></a></div>
  </div>
  <figure class="b2-media"><img src="%(img_night)s" alt="GlutaNex Glutathione Night Cream jar beside a swirl of cream" loading="lazy" width="1134" height="680"></figure>
</div></div></section>''' % dict(cprice=rs(c['price']), pernight=rs(-(-c['price'] // 56)), storycards=''.join('<a class="scard" href="%s/web-stories/%s/"%s><img src="/assets/img/web-story-%s.jpg" alt="" width="640" height="853" loading="lazy" decoding="async"><span>%s</span></a>' % ('/hi' if l else '', sl, ' lang="hi"' if l else '', sl, t) for sl, t, l in HOME_STORIES), duourl=url(d), wlhero=wl_form('all', 'wl-hero wl-d'), wlhero_m=wl_form('all', 'wl-hero wl-m'), soonband=SOONBAND, rangefeature=RANGE_FEATURE, rangecards=RANGE_CARDS, faq=faq_html(HOME_FAQ), jarimg=im('jar-cut'), ing=ing_html(), spots=html.escape(json.dumps([dict(n=INGREDIENTS[i][0], d=INGREDIENTS[i][1], x=x, y=y) for i, x, y in [(0, 50, 9), (1, 17, 31), (3, 83, 29), (2, 27, 50), (4, 76, 47), (5, 50, 88)]], ensure_ascii=False)),
                                      mq=''.join('<span>%s</span><i>✦</i>' % t for t in ['Glutathione night cream', 'Gluta Boost face wash', 'Aqua Fresh shower gel', 'Free shipping', 'Cash on Delivery', 'Restore your youthness']),
                                      img_marble=im('jar-marble'), img_night=im('jar-night'), img_hand=im('jar-hand'), img_bag=im('jar-bag'), review=REVIEW_SEC, img_banner=im('night-shift-banner'),
                                      wa=WA, watext=urllib.parse.quote('Hi GlutaNex, I want to order.'), waimg=WA_IMG)
# duo url for the band
page('/', 'Glutathione Cream for Face in India | GlutaNex', 'GlutaNex glutathione face cream: a night cream with glutathione, niacinamide and vitamin C for brighter, more even-looking skin. %s, free shipping, COD.' % rs(c['price']),
     home, jar=False, extra='<link rel="preload" as="image" href="/assets/img/glutathione-night-cream-routine-glutanex.webp" type="image/webp" fetchpriority="high">\n', schema=[{'@type': 'ItemList', 'itemListElement': [{'@type': 'ListItem', 'position': i + 1, 'url': SITE + url(p)} for i, p in enumerate(PRODUCTS)]}, faq_ld(HOME_FAQ)])

# ---------------- Shop ----------------
# phone-only luxury showcase for the shop page: the Night Cream featured on a pedestal, the other two as tiles
_c, _w, _d = BYID['cream'], BYID['wash'], BYID['duo']
def _mrp(p):
    return '<s>%s</s>' % rs(p['mrp']) if p['mrp'] > p['price'] else ''
SHOWCASE = ('<div class="lux" aria-label="GlutaNex products">'
    '<article class="lux-hero"><a class="lux-link" href="%s" aria-label="%s"></a><div class="lux-txt"><span class="lux-eb">Bestseller</span><h2>Glutathione<br>Night Cream</h2><span class="lux-sz">%s</span>'
    '<div class="lux-pr"><b>%s</b>%s</div><button class="lux-btn" type="button" data-add="cream">Add to bag</button></div>'
    '<div class="lux-stage"><i class="lux-glow"></i><img src="%s" alt="%s" width="650" height="614"><i class="lux-ped"></i></div></article>'
    '<div class="lux-row">%s</div></div>') % (
    url(_c), html.escape(_c['name']), html.escape(_c['size']), rs(_c['price']), _mrp(_c), im('jar-cut'), html.escape(_c['name']),
    ''.join('<article class="lux-tile"><a class="lux-link" href="%s" aria-label="%s"></a><div class="lux-ph"><img src="%s" alt="%s" width="800" height="800" loading="lazy"><i class="lux-ped"></i></div><span class="lux-eb">Launching soon</span><h3>%s</h3><div class="lux-pr"><b>Notify me</b></div></article>' % (url(x), html.escape(x['name']), im(x['imgs'][0]), html.escape(x['name']), html.escape(x['short'])) for x in PRODUCTS if x.get('soon')))

page('/shop/', 'Shop Glutathione Face Cream & Face Wash | GlutaNex', 'Shop GlutaNex glutathione skincare: Glutathione Night Cream, Gluta Boost Face Wash and the Glow Duo. Free shipping and Cash on Delivery across India.',
     top('Shop', 'Shop <span class="gold">GlutaNex</span>', 'Glutathione skincare for your night routine. Free shipping and Cash on Delivery on every order.') +
     '<section class="shop-sec" style="padding-top:30px"><div class="wrap">' + SHOWCASE + '<div class="grid shop-grid">' + ''.join(card(p, 'h2') for p in PRODUCTS) + '</div>'
     '<div class="sec-h" style="margin-top:56px"><span class="eyebrow">Compare</span><h2>Which one is right for you?</h2></div>'
     '<div class="tbl"><table class="cmp"><thead><tr><th></th><th>Night Cream</th><th>Face Wash</th><th>Shower Gel</th></tr></thead><tbody>'
     '<tr><td>Size</td><td>30 g jar</td><td>100 ml pump</td><td>100 ml pump</td></tr>'
     '<tr><td>Price</td><td>' + rs(BYID['cream']['price']) + '</td><td>Launching soon</td><td>Launching soon</td></tr>'
     '<tr><td>What it does</td><td>Night care for a brighter, more even-looking tone</td><td>Daily foaming cleanse for your face</td><td>Cleanses, refreshes and moisturises in the shower</td></tr>'
     '<tr><td>Key ingredients</td><td>Glutathione, niacinamide, vitamin C, hyaluronic acid, retinol, ceramides</td><td>Glutathione, copper peptide, niacinamide, aloe, chamomile, panthenol</td><td>Glutathione, hyaluronic acid, aloe vera</td></tr>'
     '<tr><td>When to use</td><td>Night (start 2–3 nights a week)</td><td>Morning and night</td><td>In your daily shower</td></tr>'
     '<tr><td>Best for</td><td>Tan, dullness, uneven tone</td><td>Clean, fresh skin before your cream</td><td>A fresh, moisturised feel after your bath</td></tr>'
     '<tr><td></td><td><button class="btn sm" type="button" data-add="cream">Add</button></td><td>' + notify_btn(BYID['wash'], 'btn wa sm') + '</td><td>' + notify_btn(BYID['gel'], 'btn wa sm') + '</td></tr>'
     '</tbody></table></div></div></section>', crumbs=[('Shop', '/shop/')], ptype='CollectionPage', main=SITE + '/shop/#products', schema=[{'@type': 'ItemList', '@id': SITE + '/shop/#products', 'name': 'GlutaNex products', 'numberOfItems': len(PRODUCTS), 'itemListElement': [{'@type': 'ListItem', 'position': n + 1, 'item': {'@id': SITE + url(x) + '#product'}, 'url': SITE + url(x), 'name': x['name']} for n, x in enumerate(PRODUCTS)]}] + [product_ld(x) for x in PRODUCTS])

# ---------------- Product pages ----------------
WASH_ING = ('<ul class="ing ing-sm"><li><b>Glutathione</b><span>The antioxidant this brand is built around, used here for fresher, brighter-looking skin.</span></li>'
            '<li><b>Copper peptide</b><span>A skin-conditioning ingredient used in skincare for the look of smoother, healthier skin.</span></li>'
            '<li><b>Niacinamide</b><span>Vitamin B3, used for the look of even tone and smoother texture.</span></li>'
            '<li><b>Aloe and chamomile</b><span>Soothing plant ingredients that help the wash feel gentle.</span></li>'
            '<li><b>Panthenol</b><span>Provitamin B5, a hydrating ingredient that helps skin feel soft after rinsing.</span></li></ul>')
GEL_ING = ('<ul class="ing ing-sm"><li><b>Glutathione</b><span>The antioxidant GlutaNex is built around, here in a wash-off shower gel.</span></li>'
           '<li><b>Hyaluronic acid</b><span>A hydrating ingredient that helps skin feel soft and moisturised after your bath.</span></li>'
           '<li><b>Aloe vera</b><span>A familiar, soothing plant ingredient that helps the gel feel gentle on skin.</span></li></ul>')
GEL_USE = '<p>Apply a small amount to wet skin or a bath sponge, lather and massage gently, then rinse well. Keep it away from the eyes. For daily use in the shower.</p>'
SOON_NOTE = '<p class="muted" style="margin-top:12px;font-size:.88rem">The complete ingredient list will be printed on the pack.</p>'
TABS = {
    'cream': [('Key ingredients', ing_html('ing ing-sm') + '<p class="muted" style="margin-top:12px;font-size:.88rem">The complete ingredient list is printed on the pack.</p>'),
              ('How to use', CREAM_USE)],
    'wash': [('How to use', '<ol class="steps"><li>Take a small amount on your palm.</li><li>Lather it and massage gently on a wet face in circular motions.</li><li>Rinse thoroughly with water.</li></ol><p>Use morning and night. At night, follow with your glutathione night cream; in the morning, finish with sunscreen.</p>'),
             ('Key ingredients', WASH_ING + '<p class="muted" style="margin-top:12px;font-size:.88rem">The complete ingredient list is printed on the pack.</p>')],
    'gel': [('How to use', GEL_USE), ('Key ingredients', GEL_ING + SOON_NOTE)],
    'washgel': [('What you get', '<p>1 × GlutaNex Gluta Boost Face Wash 100 ml and 1 × GlutaNex Aqua Fresh Shower Gel 100 ml.</p>'),
                ('How to use', '<p>Face: use the Face Wash morning and night. Lather on a wet face, massage gently in circles and rinse well. Body: use a small amount of the Shower Gel on wet skin, lather and rinse.</p>'),
                ('Key ingredients', '<h4>Face Wash</h4>' + WASH_ING + '<h4 style="margin-top:14px">Shower Gel</h4>' + GEL_ING + SOON_NOTE)],
    'creamgel': [('What you get', '<p>1 × GlutaNex Glutathione Night Cream 30 g and 1 × GlutaNex Aqua Fresh Shower Gel 100 ml.</p>'),
                 ('How to use', '<p>Shower Gel: use daily on wet skin, lather and rinse. Night Cream: at night, on a clean, dry face, a pea-sized amount over face and neck. It contains retinol and salicylic acid, so start 2 to 3 nights a week and use sunscreen every morning.</p>'),
                 ('Key ingredients', '<h4>Night Cream</h4>' + ing_html('ing ing-sm') + '<h4 style="margin-top:14px">Shower Gel</h4>' + GEL_ING + SOON_NOTE)],
    'trio': [('What you get', '<p>1 × GlutaNex Glutathione Night Cream 30 g, 1 × GlutaNex Gluta Boost Face Wash 100 ml and 1 × GlutaNex Aqua Fresh Shower Gel 100 ml.</p>'),
             ('How to use', '<p>Morning: cleanse with the Face Wash, then sunscreen. Night: cleanse with the Face Wash, pat dry, then the Night Cream (start 2 to 3 nights a week, as it contains retinol and salicylic acid). In the shower: Aqua Fresh Shower Gel for your body.</p>'),
             ('Key ingredients', '<h4>Night Cream</h4>' + ing_html('ing ing-sm') + '<h4 style="margin-top:14px">Face Wash</h4>' + WASH_ING + '<h4 style="margin-top:14px">Shower Gel</h4>' + GEL_ING + SOON_NOTE)],
    'duo': [('What you get', '<p>1 × GlutaNex Glutathione Night Cream 30 g and 1 × GlutaNex Gluta Boost Face Wash 100 ml.</p>'),
            ('How to use', '<p>Night: cleanse with Gluta Boost Face Wash, pat dry, then apply the Night Cream (start with 2 to 3 nights a week, as it contains retinol and salicylic acid). Morning: cleanse and finish with sunscreen.</p>'),
            ('Night Cream key ingredients', ing_html('ing ing-sm'))],
}
SHIP_TAB = ('Shipping & returns', '<p>Free shipping across India. Pay online, or choose Cash on Delivery and pay in cash when the parcel arrives (nothing to pay in advance). Orders are packed in 1 to 2 business days and delivered in 3 to 7 business days. Sealed packs can be returned within 7 days of delivery.</p>')
CREAM_FAQ = [('Can I use it during pregnancy?', 'The Night Cream contains retinol (vitamin A) and salicylic acid. Do not use it during pregnancy or breastfeeding unless your doctor says it is fine.'),
             ('Why start 2 to 3 nights a week?', 'Retinol and salicylic acid can cause mild dryness or tingling while skin gets used to them. Starting slowly and using sunscreen every morning keeps it comfortable.')]
PDP_FAQ = [('Can I pay Cash on Delivery?', 'Yes. Choose Cash on Delivery at checkout and pay the full amount in cash when your parcel arrives. Nothing is paid in advance.'),
           ('When will I see results?', 'Use it every night with daily sunscreen for at least 6 to 8 weeks before judging. Results vary from person to person.'),
           ('Is it safe for sensitive skin?', 'Patch test first on a small area for 24 hours. If redness, itching or burning continues, stop and speak to a dermatologist.')]
WASH_FAQ = [('Can I pay Cash on Delivery?', 'Yes. Choose Cash on Delivery at checkout and pay the full amount in cash when your parcel arrives. Nothing is paid in advance.'),
            ('How often can I use it?', 'The pack says morning and night. If your skin feels tight, wash once at night and just rinse with water in the morning.'),
            ('Is it suitable for all skin types?', 'It is made for all skin types, as printed on the pack. As with any new product, patch test first on a small area for 24 hours. If redness, itching or burning continues, stop and speak to a dermatologist.'),
            ('Does a face wash work like a glutathione cream?', 'No. A wash stays on your skin for under a minute and is rinsed off, so its main job is cleansing and keeping skin fresh. The leave-on step, such as a night cream, does the longer work. Read <a href="/glutathione-face-wash/">what a glutathione face wash can and cannot do</a>.'),
            ('What does the pack say it is free from?', 'The carton states paraben-free, sulfate-free and cruelty-free.')]
def _soon_faq(p, qa):
    return [('When will it be available?', 'It is launching soon. Tap "Notify me on WhatsApp" and we will message you when it is ready to order. There is no payment and no commitment.')] + qa + [
        ('Can I buy anything from GlutaNex right now?', 'Yes. The <a href="/product/glutanex-glutathione-night-cream/">Glutathione Night Cream</a> is available now with free shipping and Cash on Delivery.')]
SOON_FAQ = {
    'gel': _soon_faq(None, [('Is the Aqua Fresh Shower Gel for all skin types?', 'It is made for all skin types, as printed on the pack. Patch test first on a small area, and stop using it if redness, itching or burning continues.'),
                            ('What is in it?', 'The pack says it is enriched with glutathione, hyaluronic acid and aloe vera. The complete ingredient list will be printed on the pack.'),
                            ('Is a glutathione shower gel the same as a glutathione cream?', 'No. A shower gel is rinsed off within a minute or two, so its job is cleansing and a fresh, moisturised feel. Leave-on products such as a night cream do the longer work.')]),
    'washgel': _soon_faq(None, [('What is in the Face Wash + Shower Gel combo?', 'One Gluta Boost Face Wash (100 ml) for your face and one Aqua Fresh Shower Gel (100 ml) for your bath.'),
                                ('Can I use the shower gel on my face?', 'Use the Face Wash for your face and the Shower Gel for your body. That is what each one is made for.')]),
    'creamgel': _soon_faq(None, [('What is in the Night Cream + Shower Gel combo?', 'One Glutathione Night Cream (30 g) and one Aqua Fresh Shower Gel (100 ml).'),
                                 ('Can I use the Night Cream during pregnancy?', 'The Night Cream contains retinol (vitamin A) and salicylic acid. Do not use it during pregnancy or breastfeeding unless your doctor says it is fine.')]),
    'trio': _soon_faq(None, [('What is in the Glow Trio?', 'One Glutathione Night Cream (30 g), one Gluta Boost Face Wash (100 ml) and one Aqua Fresh Shower Gel (100 ml): the complete GlutaNex range.'),
                             ('Why does the Night Cream start at 2 to 3 nights a week?', 'It contains retinol and salicylic acid, which can cause mild dryness or tingling while skin gets used to them. Start slowly and use sunscreen every morning.')]),
    'wash': _soon_faq(None, [('How often can I use it?', 'The pack says morning and night. If your skin feels tight, wash once at night and just rinse with water in the morning.'),
                             ('Is it suitable for all skin types?', 'It is made for all skin types, as printed on the pack. Patch test first on a small area for 24 hours. If redness, itching or burning continues, stop and speak to a dermatologist.'),
                             ('Does a face wash work like a glutathione cream?', 'No. A wash stays on your skin for under a minute and is rinsed off, so its main job is cleansing and keeping skin fresh. Read <a href="/glutathione-face-wash/">what a glutathione face wash can and cannot do</a>.'),
                             ('What does the pack say it is free from?', 'The carton states paraben-free, sulfate-free and cruelty-free.')]),
    'duo': _soon_faq(None, [('What is in the Glow Duo?', 'One Glutathione Night Cream (30 g) and one Gluta Boost Face Wash (100 ml): cleanse, then treat.'),
                            ('Can I use the Night Cream during pregnancy?', 'The Night Cream contains retinol (vitamin A) and salicylic acid. Do not use it during pregnancy or breastfeeding unless your doctor says it is fine.')]),
}
def _about(title, intro, who, fit, links=''):
    return '<section style="padding-top:10px"><div class="wrap"><div class="prose pdp-about"><h2>%s</h2>%s<h3>Who it is for</h3><ul>%s</ul><h3>How it fits your routine</h3>%s%s</div></div></section>' % (title, intro, ''.join('<li>%s</li>' % w for w in who), fit, links)
ABOUT_SOON = {
 'gel': _about('About the Aqua Fresh Shower Gel',
   '<p>The GlutaNex Aqua Fresh Shower Gel is a <b>glutathione shower gel</b> in a 100 ml pump bottle. It is a clear blue gel enriched with glutathione, hyaluronic acid and aloe vera, made to cleanse, refresh and leave skin feeling moisturised.</p><p>Because a shower gel is rinsed off, it is there for a clean, fresh, comfortable bath rather than to treat skin. For longer-contact care, pair it with a leave-on step such as the <a href="/product/glutanex-glutathione-night-cream/">Night Cream</a>.</p>',
   ['Anyone who wants a daily shower gel from the same brand as their glutathione skincare.', 'All skin types, as printed on the pack.', 'People who like a light gel that rinses off cleanly.'],
   '<p>Use it in the shower on wet skin, then rinse well. Want the face routine too? See the <a href="/product/glutanex-gluta-boost-face-wash/">Gluta Boost Face Wash</a> and the <a href="/product/glutanex-glow-trio-night-cream-face-wash-shower-gel/">Glow Trio</a>.</p>',
   '<p class="muted">New to glutathione? Start with <a href="/glutathione/">what glutathione is</a>.</p>'),
 'washgel': _about('About the Face Wash + Shower Gel combo',
   '<p>This set pairs the <a href="/product/glutanex-gluta-boost-face-wash/">Gluta Boost Face Wash</a> for your face with the <a href="/product/glutanex-aqua-fresh-shower-gel/">Aqua Fresh Shower Gel</a> for your bath. Both are 100 ml pump bottles in the new GlutaNex pack design, so one order covers face and body cleansing.</p>',
   ['Anyone who wants a matching cleansing set from one brand.', 'A simple gift for someone who already likes GlutaNex.', 'Normal, combination and oily skin that likes a fresh, foaming clean; dry skin can wash once a day.'],
   '<p>Face Wash morning and night, Shower Gel in your bath. Add the <a href="/product/glutanex-glutathione-night-cream/">Night Cream</a> as your leave-on night step.</p>'),
 'creamgel': _about('About the Night Cream + Shower Gel combo',
   '<p>This set combines the <a href="/product/glutanex-glutathione-night-cream/">Glutathione Night Cream</a> with the <a href="/product/glutanex-aqua-fresh-shower-gel/">Aqua Fresh Shower Gel</a>: a leave-on night step for your face and a rinse-off shower gel for your body.</p>',
   ['Anyone starting a glutathione night routine who also wants a matching shower gel.', 'Normal, combination and oily skin; dry skin can add a moisturiser on top of the cream.'],
   '<p>Shower Gel in your bath. Night: cleanse, pat dry, then a pea-sized amount of the Night Cream. It contains retinol and salicylic acid, so start 2 to 3 nights a week, use sunscreen every morning, and avoid it during pregnancy or breastfeeding unless your doctor approves.</p>'),
 'trio': _about('About the Glow Trio',
   '<p>The GlutaNex Glow Trio is the full range in one set: the <a href="/product/glutanex-glutathione-night-cream/">Glutathione Night Cream</a> (30 g), the <a href="/product/glutanex-gluta-boost-face-wash/">Gluta Boost Face Wash</a> (100 ml) and the <a href="/product/glutanex-aqua-fresh-shower-gel/">Aqua Fresh Shower Gel</a> (100 ml).</p>',
   ['Anyone who wants to try the whole GlutaNex range together.', 'A gift set for someone who loves skincare.', 'Normal, combination and oily skin; dry skin can use the wash once a day and add a moisturiser.'],
   '<p>Morning: Face Wash, then sunscreen. Night: Face Wash, pat dry, then the Night Cream (start 2 to 3 nights a week). In the shower: Aqua Fresh Shower Gel.</p>',
   '<p class="muted">Learn the routine: <a href="/how-to-use-glutathione-cream/">how to use glutathione cream</a>.</p>'),
}
ABOUT = {'wash': '''<section style="padding-top:10px"><div class="wrap"><div class="prose pdp-about"><h2>About the Gluta Boost Face Wash</h2>
<p>The GlutaNex Gluta Boost Face Wash is a <b>glutathione face wash</b> in a 100 ml pump bottle, launching soon. It is a clear, foaming gel that lathers into a rich, creamy foam and rinses off cleanly, so it fits easily into a daily routine.</p>
<h3>What is in it</h3><p>Glutathione and copper peptide lead the formula, backed by niacinamide, aloe, chamomile and panthenol. Because a wash is rinsed off, these ingredients are there to support a fresh, soft, comfortable feel after cleansing rather than to treat skin.</p>
<h3>Who it is for</h3><ul><li>Anyone who wants a daily cleanser to go with a <a href="/glutathione-cream/">glutathione cream</a> routine.</li><li>Normal, combination and oily skin that likes a fresh, foaming wash; dry skin can wash once at night.</li><li>People who want one brand across the routine: wash, then <a href="/product/glutanex-glutathione-night-cream/">Night Cream</a>.</li></ul>
<h3>How it fits your routine</h3><p>Morning: wash, then sunscreen. Night: wash, pat dry, then the Night Cream. Prefer a set? The <a href="/product/glutanex-glow-duo-night-cream-face-wash/">Glow Duo</a> pairs it with the Night Cream, and it is launching soon.</p>
<p class="muted">Want the full picture of what a wash can do? Read our guide to <a href="/glutathione-face-wash/">glutathione face wash</a>.</p></div></div></section>''',
         'cream': '''<section style="padding-top:10px"><div class="wrap"><div class="prose pdp-about"><h2>About this glutathione face cream</h2>
<p>The GlutaNex Night Cream is a <b>glutathione face cream</b> made for night use. Glutathione is paired with niacinamide (vitamin B3) and vitamin C, which also help the look of uneven tone, plus retinol for smoother-looking skin and hyaluronic acid and ceramides for moisture.</p>
<h3>Who it is for</h3><ul><li>Women and men with <a href="/glutathione-cream-for-summer-tan/">tan</a>, dullness or uneven-looking tone.</li><li>Flat <a href="/glutathione-for-acne-marks/">acne marks</a> left after pimples heal.</li><li>Normal, combination and oily skin; dry skin can add a moisturiser on top.</li></ul>
<h3>What to expect</h3><p>A smoother feel in 2 to 4 weeks, a fresher look in 4 to 8 weeks, and lighter-looking tan and marks in 8 to 12 weeks, with sunscreen every morning. It does not change your natural skin colour. See <a href="/how-long-does-glutathione-take-to-work/">how long glutathione cream takes to work</a>.</p>
<h3>Who should not use it</h3><p>It contains retinol and salicylic acid, so avoid it during pregnancy or breastfeeding unless your doctor approves, and ask a dermatologist first if you use prescription creams or have <a href="/glutathione-for-melasma/">melasma</a>.</p>
<p class="muted">Comparing creams? Use our <a href="/best-glutathione-cream-in-india/">checklist for the best glutathione cream in India</a>.</p></div></div></section>'''}
BUY_TPL = '''    <div class="qty-row"><div class="qty" data-qty><button type="button" data-dec aria-label="Less">−</button><output>1</output><button type="button" data-inc aria-label="More">+</button></div><span class="muted" style="font-size:.88rem">In stock</span></div>
    <div class="acts"><button class="btn ghost" type="button" data-add="%(id)s" data-useqty>Add to cart</button><button class="btn" type="button" data-buy="%(id)s" data-useqty>Buy now</button><a class="btn wa" href="https://wa.me/%(wa)s?text=%(watext)s" target="_blank" rel="noopener">%(waimg)s Order on WhatsApp</a></div>
    <p class="eta" data-eta hidden></p>
    <form class="pinchk" data-pinchk hidden><label for="pc-pin">Check delivery to your pincode</label><div><input id="pc-pin" inputmode="numeric" maxlength="6" autocomplete="postal-code" placeholder="6-digit pincode"><button class="btn sm" type="submit">Check</button></div><p class="pc-out" aria-live="polite" hidden></p></form>
    <ul class="perks"><li>Cash on Delivery: nothing to pay in advance</li><li>Free shipping across India</li><li>Sealed packs: 7-day returns</li></ul>'''
SOON_TPL = '''<div class="soon-box"><span class="soon-badge">🚀 Launching soon</span><p><b>Not on sale yet.</b> Join the waitlist for 10%% off at launch, or just tap the button and we will message you on WhatsApp the moment %(short)s is ready. No payment, no commitment.</p>%(wlform)s<div class="acts">%(notify)s</div><p class="soon-alt">Want to start today? <a href="/product/glutanex-glutathione-night-cream/">Buy the Glutathione Night Cream</a>: free shipping and Cash on Delivery.</p></div>'''
for p in PRODUCTS:
    off = pct(p)
    thumbs = ''.join('<button type="button" data-src="%s"%s aria-label="Picture %d"><img src="%s" alt="" width="78" height="78" loading="lazy"></button>' % (
        im(i), ' class="on"' if n == 0 else '', n + 1, im(i)) for n, i in enumerate(p['imgs']))
    tabs = TABS[p['id']] + [SHIP_TAB]
    faq_items = SOON_FAQ[p['id']] if p.get('soon') else PDP_FAQ + (CREAM_FAQ if p['id'] in ('cream', 'duo') else [])
    others = [q for q in PRODUCTS if q['id'] != p['id']]
    body = '''<div class="wrap pdp">
  <div class="pdp-media"><div class="pdp-main tilt"><img id="pdp-img" src="%(main)s" alt="%(alt)s" width="800" height="800" fetchpriority="high"></div><div class="thumbs">%(thumbs)s</div></div>
  <div>
    <span class="eyebrow">GlutaNex · %(tag)s</span>
    <h1>%(name)s</h1>%(sub)s
    %(pricehtml)s
    <p class="summary">%(summary)s</p>
    %(buyhtml)s
    <button class="jar-talk sm" type="button" data-talk hidden><span class="jt-dot"></span>🎙️ Ask the jar a question<small>Speak in English, हिंदी, Hinglish, தமிழ்…</small></button>
    <a class="quizcta sm" href="/skin-quiz/"><b>Not sure it suits your skin?</b><span>Take the 30-second quiz →</span></a>
    <div class="tabs">%(tabs)s</div>
  </div>
</div>
%(about)s%(review)s<section style="padding-top:10px"><div class="wrap"><div class="sec-h"><h2>Questions</h2></div>%(faq)s
<p style="margin-top:22px" class="muted">Learn more: <a href="/glutathione-cream/">Glutathione cream guide</a> · <a href="/glutathione-side-effects/">Side effects</a> · <a href="/how-to-use-glutathione-cream/">How to use</a></p></div></section>
<section style="padding-top:10px"><div class="wrap"><div class="sec-h"><span class="eyebrow">Complete the ritual</span><h2>You may also like</h2></div><div class="grid">%(rel)s</div></div></section>
%(buybar)s''' % dict(
        buybar=('<div class="buybar" id="buybar" aria-hidden="true"><img src="%s" alt="" width="44" height="44"><div class="bb-t"><b>%s</b><span>Launching soon</span></div>%s</div>' % (im(p['imgs'][0]), html.escape(p['short']), notify_btn(p, 'btn wa sm')) if p.get('soon') else
                '<div class="buybar" id="buybar" aria-hidden="true"><img src="%s" alt="" width="44" height="44"><div class="bb-t"><b>%s</b><span>%s · Free shipping · COD</span></div><button class="icon-btn bb-add" type="button" data-add="%s" aria-label="Add to cart">%s</button><button class="btn" type="button" data-buy="%s">Buy now</button></div>' % (im(p['imgs'][0]), html.escape(p['short']), rs(p['price']), p['id'], SVG_BAG, p['id'])),
        pricehtml=('<p class="tax"><b>Launching soon</b> · %s</p>' % html.escape(p['size']) if p.get('soon') else '<div class="price"><b>%s</b>%s%s</div>\n    <p class="tax">Inclusive of all taxes · Free shipping · %s</p>' % (rs(p['price']), '<s>MRP %s</s>' % rs(p['mrp']) if off else '', '<span class="off">%d%% off</span>' % off if off else '', p['size'])),
        buyhtml=(SOON_TPL % dict(short=html.escape(p['short']), notify=notify_btn(p), wlform=wl_form(p['id'], named=True)) if p.get('soon') else BUY_TPL % dict(id=p['id'], wa=WA, watext=urllib.parse.quote('Hi GlutaNex, I want to order: %s' % p['name']), waimg=WA_IMG)),
        main=im(p['imgs'][0]), alt=html.escape(p['name']), thumbs=thumbs, tag=p['tag'], name=html.escape(p['name']),
        mrp='<s>MRP %s</s>' % rs(p['mrp']) if off else '', off='<span class="off">%d%% off</span>' % off if off else '', size=p['size'], summary=p['summary'], id=p['id'],
        wa=WA, watext=urllib.parse.quote('Hi GlutaNex, I want to order: %s' % p['name']), waimg=WA_IMG,
        tabs=''.join('<details%s><summary>%s</summary><div class="in">%s</div></details>' % (' open' if n == 0 else '', t, x) for n, (t, x) in enumerate(tabs)),
        faq=faq_html(faq_items), rel=''.join(card(q) for q in others),
        sub='<p class="pdp-sub">%s</p>' % html.escape(p['sub']) if p.get('sub') else '', about=(ABOUT_SOON.get(p['id']) or ABOUT.get(p['id'], '')), review=REVIEW_SEC if p['id'] in ('cream', 'duo') else '')
    page(url(p), p['title'], p.get('meta_desc', p['desc']), body, og='product', ogimg=p['og'], crumbs=[('Shop', '/shop/'), (p['short'], url(p))], schema=[product_ld(p), faq_ld(faq_items)], ptype='ItemPage', main=SITE + url(p) + '#product',
         extra=('' if p.get('soon') else '<meta property="product:price:amount" content="%d"><meta property="product:price:currency" content="INR">\n' % p['price']))

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
      <label class="consent" id="consent-row" hidden><input type="checkbox" id="co-consent"><span>You may message me on WhatsApp about this order and related offers, even if I don't complete it.</span></label>
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
        <label><input type="radio" name="pay" value="cod"><span>Cash on Delivery<small id="cod-note">Nothing to pay now · pay in cash when it arrives</small></span><b id="amt-cod"></b></label>
        <label><input type="radio" name="pay" value="wa"><span>Order on WhatsApp<small>Send your order, we confirm on chat</small></span><b id="amt-wa"></b></label>
      </fieldset>
      <p class="muted" id="cod-terms" style="font-size:.82rem" hidden>Delivered by Delhivery. Please keep the exact amount ready; there is no Cash on Delivery fee. You get a Delhivery tracking number as soon as the order is placed.</p>
      <div class="notyet" id="not-yet" hidden><p><b>Your order isn't placed yet.</b> The payment window closed before it finished. Your details are saved.</p><button type="button" class="btn" id="ny-retry">Try payment again</button><button type="button" class="btn ghost" id="ny-switch">Switch to Cash on Delivery</button></div>
      <p class="oerr" id="co-err" role="alert" hidden></p>
      <div class="step-acts"><button class="btn ghost" type="button" data-back>Back</button><button class="btn" type="submit" id="co-pay">Pay securely</button></div>
      <p class="muted" style="font-size:.78rem;margin-top:8px">Your details are used only to deliver this order. See our <a href="/privacy-policy/">privacy policy</a>.</p></div>
  </div>
  </form>
</div>
<aside class="panel"><h2 style="font-size:1.6rem;margin-bottom:12px">Your order</h2><div id="co-lines"></div><div class="sum" id="co-sum" style="margin-top:12px"></div><div class="cpn" id="co-cpn" hidden><button type="button" class="cpn-open" id="cpn-open">Have a reward code?</button><div class="cpn-row" id="cpn-row" hidden><input id="cpn-in" placeholder="GNX-XXXXXX" maxlength="12" autocapitalize="characters" autocomplete="off" spellcheck="false" aria-label="Reward code"><button type="button" class="btn sm" id="cpn-apply">Apply</button></div><p class="cpn-msg" id="cpn-msg" hidden></p></div></aside>
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
FEED_TITLES = {'cream': 'GlutaNex Glutathione Face Cream for Night, 30 g - with Niacinamide, Vitamin C and Hyaluronic Acid',
               'wash': 'GlutaNex Gluta Boost Glutathione Face Wash 100 ml',
               'duo': 'GlutaNex Glow Duo - Glutathione Night Cream 30 g + Face Wash 100 ml'}
_fi = []
for p in PRODUCTS:
    if p.get('soon'):
        continue
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
exec(open(os.path.join(B, 'stories.py'), encoding='utf-8').read())

# ---------------- Knowledge file for the question assistant (api/ask.js) ----------------
def _txt(h):
    h = re.sub(r'<(script|style)[^>]*>.*?</\1>', ' ', h, flags=re.S)
    h = re.sub(r'<a [^>]*href="([^"]+)"[^>]*>(.*?)</a>', r'\2', h)
    h = re.sub(r'</(p|li|tr|h3|div)>', '\n', h)
    h = re.sub(r'<(td|th)[^>]*>', ' | ', h)
    return re.sub(r'[ \t]+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', h))).replace(' \n', '\n').strip()
KB = [{'t': 'GlutaNex products, prices and policies', 'u': '/shop/', 's': '', 'always': True, 'x': '\n'.join([
    ('%s (%s): %s. %s' % (p['name'], p['size'], 'launching soon, not yet available to order; customers can ask to be notified on WhatsApp' if p.get('soon') else '%s, MRP %s' % (rs(p['price']), rs(p['mrp'])), _txt(p['summary']))) for p in PRODUCTS] + [
    'Only the Glutathione Night Cream can be ordered right now. The Face Wash, Shower Gel, Glow Duo and the other combo sets are launching soon.',
    'Night Cream ingredients: ' + ', '.join(n for n, d in INGREDIENTS) + '. The complete list is printed on the pack.',
    'Night Cream use: ' + _txt(CREAM_USE),
    'Shipping: free across India, packed in 1 to 2 business days, delivered in 3 to 7 business days. Track orders at /track-order/.',
    'Payment: pay online (UPI, cards, netbanking), Cash on Delivery (pay in cash at delivery, nothing in advance), or order on WhatsApp at %s.' % WA_SHOW,
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

# ---------------- Files for AI assistants (llmstxt.org format) ----------------
def _g(slug):
    return next(x for x in GUIDES if x['slug'] == slug)
_core = ['glutathione', 'glutathione-cream-questions', 'glutathione-cream', 'glutathione-benefits-for-skin', 'glutathione-side-effects', 'is-glutathione-safe-for-skin',
         'how-to-use-glutathione-cream', 'glutathione-for-skin-whitening', 'glutathione-cream-vs-tablets-vs-injections', 'glutathione-tablets']
_line = lambda u, t, d: '- [%s](%s%s): %s' % (t, SITE, u, d)
LLMS = ['# GlutaNex', '',
        '> GlutaNex is an Indian skincare brand selling a glutathione night cream (30 g) and a glutathione face wash (100 ml) at glutanex.co.in, '
        'sold and shipped by %s, %s. The site also publishes research-cited guides on glutathione for skin, written to be accurate: glutathione can help tan '
        'and uneven tone look lighter and more even over 8 to 12 weeks with daily sunscreen; it does not change natural skin colour; injections for skin '
        'lightening are not recommended.' % (OWNER, ADDR), '',
        '## Brand facts', '',
        '- Brand name: GlutaNex (also written Glutanex). Official website: https://glutanex.co.in. Company: %s, Bhatkal, Karnataka, India.' % OWNER,
        '- Official channels: this website, Instagram @glutanexofficial (%s), WhatsApp %s. Official marketplace listings: ' % (INSTAGRAM, WA_SHOW) + ', '.join('%s (%s)' % (n, u) for n, u in MARKET_LINKS) + '.',
        '- GlutaNex (India, glutanex.co.in) makes only skincare you apply to the skin. It does not make or sell glutathione injections, drips or tablets. GlutaNex is an Indian brand. "Glutanex" products from Korea, including glutathione injections, tablets and skincare sold online in India, are made by other companies and are not connected with GlutaNex India. Brand page: %s/glutanex/' % SITE, '',
        'Key facts:', '',
        '- Products: ' + '; '.join(('%s (%s) launching soon' % (x['name'], x['size'])) if x.get('soon') else '%s (%s) %s, MRP %s' % (x['name'], x['size'], rs(x['price']), rs(x['mrp'])) for x in PRODUCTS) + '. Prices include taxes. Only the Night Cream can be ordered now.',
        '- Night Cream ingredients: ' + ', '.join(n for n, d in INGREDIENTS) + '. Contains retinol and salicylic acid: night use, start 2-3 nights a week, sunscreen every morning, not for pregnancy or breastfeeding unless a doctor approves.',
        '- Shipping: free across India; packed in 1-2 business days; delivered in 3-7 business days. Payment: online (UPI, cards), Cash on Delivery (nothing paid in advance), or WhatsApp order.',
        '- Returns: sealed products within 7 days of delivery; damaged or wrong items replaced or refunded. Contact: WhatsApp %s, Instagram @glutanexofficial.' % WA_SHOW, '',
        '## Shop', '',
        _line('/shop/', 'Shop', 'all GlutaNex products with prices')] + [_line(url(x), x['name'], x['desc']) for x in PRODUCTS] + [
        '', '## Glutathione guides', ''] + [_line(guide_url(_g(sl)), _g(sl)['title'], _g(sl)['desc']) for sl in _core] + [
        '', '## Policies', '', _line('/our-standards/', 'Our standards', 'how GlutaNex writes its guides and what it will and will not claim'),
        _line('/refund-policy/', 'Returns and refunds', '7-day returns on sealed products'), _line('/shipping-policy/', 'Shipping', 'free shipping across India, delivery times'),
        '', '## Optional', '', _line('/llms-full.txt', 'Full text', 'all product facts and guides as plain text')] + \
       [_line(guide_url(x), x['title'], x['desc']) for x in GUIDES if x['slug'] not in _core] + \
       [_line('/hi/%s/' % h['slug'], h['title'], h['desc']) for h in HI] + [_line('/%s/%s/' % (r['lang'], r['slug']), r['title'], r['desc']) for r in REG]
open(os.path.join(ROOT, 'llms.txt'), 'w', encoding='utf-8').write('\n'.join(LLMS) + '\n')
_full = ['# GlutaNex: full text for AI assistants', '', 'Source: %s. Cosmetic skincare information, not medical advice.' % SITE, '']
for c in KB:
    _full.append('## %s%s' % (c['t'], (' — ' + c['s']) if c['s'] else ''))
    _full.append('URL: %s%s' % (SITE, c['u']))
    _full.append(c['x'])
    _full.append('')
_full.append('## Sources cited on this site')
_full += ['- ' + v for v in SOURCES.values()]
open(os.path.join(ROOT, 'llms-full.txt'), 'w', encoding='utf-8').write('\n'.join(_full) + '\n')

# ---------------- Owner page: unfinished checkouts ----------------
page('/leads/', 'Unfinished checkouts | GlutaNex', 'Owner page.', top('Owner', 'Unfinished checkouts', 'Customers who started checkout, agreed to a WhatsApp follow-up, and did not finish. Entries disappear after 30 days.') + \
     '<section style="padding-top:20px"><div class="wrap"><form class="form leads-login" id="leads-login" autocomplete="off"><div class="f"><label for="owner-code">Owner code</label>'
     '<input id="owner-code" type="password" autocomplete="current-password" placeholder="Enter your owner code"></div><button class="btn" type="submit">Show list</button><p class="oerr" id="leads-err" hidden></p></form>'
     '<div id="leads-out"></div>'
     '<div class="otools" id="owner-tools"><div class="panel"><h2>Create a reward code</h2><p class="muted">For an unboxing Reel or to say sorry. Linked to the customer\'s mobile, single use, 60 days.</p>'
     '<div class="f"><label for="ot-phone">Customer mobile</label><input id="ot-phone" type="tel" inputmode="numeric" maxlength="14"></div>'
     '<div class="two"><div class="f"><label for="ot-off">Amount</label><select id="ot-off"><option value="150">₹150</option><option value="100">₹100</option><option value="200">₹200</option><option value="50">₹50</option></select></div>'
     '<div class="f"><label for="ot-note">Reason</label><select id="ot-note"><option>Unboxing Reel</option><option>Sorry for the trouble</option><option>Other</option></select></div></div>'
     '<button class="btn" type="button" id="ot-code-go">Create code</button><p class="ot-msg" id="ot-code-msg" hidden></p></div>'
     '<div class="panel"><h2>Packed-parcel photo</h2><p class="muted">One photo of the sealed parcel. The customer sees it on the tracking page.</p>'
     '<div class="f"><label for="ot-order">Order number</label><input id="ot-order" placeholder="pay_… or order_… (paid orders)" autocomplete="off" spellcheck="false"></div>'
     '<div class="f"><label for="ot-file">Photo</label><input id="ot-file" type="file" accept="image/*" capture="environment"></div>'
     '<button class="btn" type="button" id="ot-photo-go">Upload photo</button><p class="ot-msg" id="ot-photo-msg" hidden></p></div></div>'
     '</div></section>', index=False, js='store.js,leads.js,owner-tools.js')

# ---------------- App reminders page ----------------
page('/reminders/', 'Routine reminders | GlutaNex', 'Turn on GlutaNex routine and refill reminders on your phone.', top('Reminders', 'Gentle <span class="gold">reminders</span>', 'A nudge on your phone at 9:30 pm on Night Cream nights, and when it is time to reorder. Turn them off any time.') +
     '''<section style="padding-top:20px"><div class="wrap"><div class="panel rem" id="rem">
  <label class="rem-row"><span><b>Night routine</b><small>Weeks 1–2: 2–3 nights a week. Then every other night, then nightly. Ends after 8 weeks.</small></span><input type="checkbox" id="rem-routine" checked></label>
  <label class="rem-row"><span><b>Refill reminder</b><small id="rem-refill-note">One message about 40 days after your order, when a 30 g jar is running low.</small></span><input type="checkbox" id="rem-refill" checked></label>
  <button class="btn block" type="button" id="rem-save">Turn on reminders</button>
  <p class="muted" id="rem-status" role="status" style="font-size:.88rem"></p>
  <div class="note" id="rem-ios" hidden><b>On iPhone:</b> reminders work in the GlutaNex app. Tap the Share button in Safari, then <b>Add to Home Screen</b>, open GlutaNex from your home screen, and come back to this page.</div>
</div><p class="muted" style="font-size:.82rem;margin-top:14px">We only send what you choose here: no ads, no spam. Your phone's notification settings always come first.</p></div></section>''', index=False, js='store.js,reminders.js', crumbs=[('Reminders', '/reminders/')])

exec(open(os.path.join(B, 'features.py'), encoding='utf-8').read())

# ---------------- Offline page (shown by the app when there is no internet) ----------------
page('/offline/', 'You are offline | GlutaNex', 'No internet connection.', top('Offline', 'You are offline', 'Check your internet connection and try again. Pages you opened before still work.') +
     '<section style="padding-top:20px"><div class="wrap"><button class="btn" type="button" onclick="location.reload()">Try again</button></div></section>', index=False)

# ---------------- Assets, sitemap, robots, vercel ----------------
os.makedirs(os.path.join(ROOT, 'assets'), exist_ok=True)
open(os.path.join(ROOT, 'assets', 'site.css'), 'w', encoding='utf-8').write(mincss(open(os.path.join(B, 'site.css'), encoding='utf-8').read()))
for f in ['store.js', 'waitlist.js', 'jar3d.js', 'owner.js', 'leads.js', 'reminders.js', 'quiz.js', 'features.js', 'routine.js', 'owner-tools.js', 'talk.js']:
    if os.path.exists(os.path.join(B, f)):
        shutil.copy(os.path.join(B, f), os.path.join(ROOT, 'assets', f))
_pj = {p['id']: {'name': p['name'], 'short': p['short'], 'price': p['price'], 'mrp': p['mrp'], 'img': im(p['imgs'][0]), 'url': url(p)} for p in PRODUCTS if not p.get('soon')}
# the ₹1 test product used by /sample-test/ to check live payments (kept in products.json, not listed in the shop)
_pj['sample'] = {'name': 'GlutaNex Test Sample (₹1)', 'short': 'Test Sample', 'price': 1, 'mrp': 1, 'img': im(BYID['cream']['imgs'][0]), 'url': '/sample-test/'}
open(os.path.join(ROOT, 'assets', 'products.json'), 'w').write(json.dumps(_pj, ensure_ascii=False))
# photo credit + licence data inside every image (Google Images shows it); lossless and only once per file
import sys as _sys
_sys.path.insert(0, B)
import imgmeta
imgmeta.stamp_dir(os.path.join(ROOT, 'assets', 'img'), SITE, OWNER)
# copy the photos to their search-friendly names
for _src, _dst in SEO_IMG.items():
    for _ext in ('webp', 'jpg', 'png'):
        _a = os.path.join(ROOT, 'assets', 'img', '%s.%s' % (_src, _ext))
        if os.path.exists(_a):
            shutil.copy(_a, os.path.join(ROOT, 'assets', 'img', '%s.%s' % (_dst, _ext)))
# sitemap with image entries, so Google Images can find the product photos
IMG_FOR = {'/': ['jar-cut', 'jar-night', 'jar-hand', 'jar-bag', 'night-shift-banner'], '/shop/': ['cream-square', 'facewash-square', 'duo-square']}
for _p in PRODUCTS:
    IMG_FOR[url(_p)] = _p['imgs']
def _imgs(pth):
    names = IMG_FOR.get(pth, ['cream-square'] if pth.startswith('/glutathione') or pth.startswith('/hi/') or '-glutathione' in pth or 'glutathione-' in pth else [])
    return ''.join('<image:image><image:loc>%s%s</image:loc></image:image>' % (SITE, im(n, 'jpg' if n != 'jar-cut' else 'png')) for n in names)
# real per-page dates: a page's date only moves when its content changes (search engines ignore a lastmod that is always "today")
import hashlib, re as _re, datetime as _dt
_DATES_F = os.path.join(B, 'pagedates.json')
try:
    _dates = json.load(open(_DATES_F))
except Exception:
    _dates = {}
_now = (_dt.datetime.now(_dt.timezone.utc) + _dt.timedelta(hours=5, minutes=30)).strftime('%Y-%m-%d')
_DRE = _re.compile(r'"(datePublished|dateModified)": "\d{4}-\d{2}-\d{2}"')
for pth in pages:
    _f = os.path.join(ROOT, pth.strip('/'), 'index.html') if pth != '/' else os.path.join(ROOT, 'index.html')
    if not os.path.exists(_f):
        continue
    _h = open(_f, encoding='utf-8').read()
    _main = re.search(r'<main id="main">(.*)</main>', _h, re.S)
    _sig = hashlib.sha256(_DRE.sub('', (_main.group(1) if _main else _h) + re.sub(r'<script type="application/ld\+json">.*?</script>', '', re.search(r'<head>(.*?)</head>', _h, re.S).group(1) if '<head>' in _h else '', flags=re.S)[:0]).encode()).hexdigest()[:16]
    _d = _dates.get(pth)
    if not _d:
        _d = _dates[pth] = {'h': _sig, 'pub': _now, 'mod': _now}
    elif _d['h'] != _sig:
        _d['h'] = _sig; _d['mod'] = _now
    _h2 = _h.replace('"datePublished": "%s"' % TODAY, '"datePublished": "%s"' % _d['pub']).replace('"dateModified": "%s"' % TODAY, '"dateModified": "%s"' % _d['mod'])
    # visible "Updated" lines match the real last-changed date (AI engines and Google compare them with the markup)
    _y, _m, _dd = [int(x) for x in _d['mod'].split('-')]
    _EN = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    _HIM = ['जनवरी', 'फरवरी', 'मार्च', 'अप्रैल', 'मई', 'जून', 'जुलाई', 'अगस्त', 'सितंबर', 'अक्टूबर', 'नवंबर', 'दिसंबर']
    _h2 = _h2.replace('Updated 11 October 2026', 'Updated %d %s %d' % (_dd, _EN[_m - 1], _y)).replace('Updated: 12 Oct 2026', 'Updated: %d %s %d' % (_dd, _EN[_m - 1][:3], _y)).replace('अपडेट: 11 अक्टूबर 2026', 'अपडेट: %d %s %d' % (_dd, _HIM[_m - 1], _y))
    if _h2 != _h:
        open(_f, 'w', encoding='utf-8').write(_h2)
open(_DATES_F, 'w').write(json.dumps(_dates, indent=1, sort_keys=True) + '\n')
# page list + fingerprints for the IndexNow job (tells Bing/Yandex/Seznam/Naver which pages changed)
open(os.path.join(ROOT, 'api', '_pages.json'), 'w').write(json.dumps({SITE + k: v['h'] for k, v in _dates.items() if k in pages}))
open(os.path.join(ROOT, INDEXNOW_KEY + '.txt'), 'w').write(INDEXNOW_KEY)
sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">']
for pth in pages:
    sm.append('  <url><loc>%s%s</loc><lastmod>%s</lastmod>%s</url>' % (SITE, pth, _dates.get(pth, {}).get('mod', TODAY), _imgs(pth)))
sm.append('</urlset>')
open(os.path.join(ROOT, 'sitemap.xml'), 'w').write('\n'.join(sm) + '\n')
# Google Search Console ownership file (HTML file method). Must stay at the site root.
open(os.path.join(ROOT, 'google68c163c347b9f153.html'), 'w').write('google-site-verification: google68c163c347b9f153.html')
open(os.path.join(ROOT, 'robots.txt'), 'w').write(('User-agent: *\nDisallow: /\n' if PREVIEW else 'User-agent: OAI-SearchBot\nUser-agent: ChatGPT-User\nUser-agent: GPTBot\nUser-agent: PerplexityBot\nUser-agent: Perplexity-User\nUser-agent: ClaudeBot\nUser-agent: Claude-SearchBot\nUser-agent: Claude-User\nUser-agent: Google-Extended\nUser-agent: Applebot-Extended\nUser-agent: Bingbot\nDisallow: /cart/\nDisallow: /checkout/\nDisallow: /leads/\nDisallow: /api/\nAllow: /\n\nUser-agent: *\nDisallow: /cart/\nDisallow: /checkout/\nDisallow: /reorder/\nDisallow: /leads/\nDisallow: /offline/\nDisallow: /reminders/\nDisallow: /api/\nAllow: /\n\nSitemap: %s/sitemap.xml\n' % SITE))
vercel = {'cleanUrls': False, 'rewrites': [{'source': '/api/:fn(addon|indexnow|coupon|scratch|routine|parcel-photo|cod-order|delhivery-check)', 'destination': '/api/hub?fn=:fn'}], 'crons': [{'path': '/api/push-cron', 'schedule': '0 16 * * *'}, {'path': '/api/hub?fn=indexnow', 'schedule': '30 3 * * *'}], 'headers': [{'source': '/(.*)', 'headers': [{'key': 'X-Content-Type-Options', 'value': 'nosniff'}, {'key': 'Referrer-Policy', 'value': 'strict-origin-when-cross-origin'},
                {'key': 'Permissions-Policy', 'value': 'camera=(self), microphone=(self), geolocation=(), browsing-topics=()'}, {'key': 'Strict-Transport-Security', 'value': 'max-age=63072000; includeSubDomains'}]},
               {'source': '/((?!web-stories|hi/web-stories).*)', 'headers': [{'key': 'X-Frame-Options', 'value': 'SAMEORIGIN'}]},
               {'source': '/assets/(.*)\\.(webp|jpg|png|svg)', 'headers': [{'key': 'Cache-Control', 'value': 'public, max-age=86400, stale-while-revalidate=604800'}]},
                                         {'source': '/assets/(.*)\\.(css|js)', 'headers': [{'key': 'Cache-Control', 'value': 'public, max-age=31536000, immutable'}]}, {'source': '/assets/fonts/(.*)', 'headers': [{'key': 'Cache-Control', 'value': 'public, max-age=31536000, immutable'}]},
                                         {'source': '/(cart|checkout|reorder|leads|offline|reminders)/(.*)', 'headers': [{'key': 'X-Robots-Tag', 'value': 'noindex'}]},
                                         {'source': '/sw.js', 'headers': [{'key': 'Cache-Control', 'value': 'no-cache'}]},
                                         {'source': '/(llms.txt|llms-full.txt)', 'headers': [{'key': 'Content-Type', 'value': 'text/plain; charset=utf-8'}, {'key': 'Cache-Control', 'value': 'public, max-age=3600'}]},
                                         {'source': '/site.webmanifest', 'headers': [{'key': 'Content-Type', 'value': 'application/manifest+json'}]}]}
open(os.path.join(ROOT, 'vercel.json'), 'w').write(json.dumps(vercel, indent=2) + '\n')
# ---------------- Install as an app: manifest + service worker ----------------
import hashlib
# llms.txt: add every indexable page that is not listed yet (Hinglish, regional, tools, newer pages)
_lt = open(os.path.join(ROOT, 'llms.txt'), encoding='utf-8').read()
_more = [x for x in SEARCH if ('](' + SITE + x['u'] + ')') not in _lt and x['u'] not in ('/404',)]
if _more:
    _lt = _lt.rstrip('\n') + '\n\n## More pages\n\n' + '\n'.join('- [%s](%s%s): %s' % (x['t'], SITE, x['u'], x['d']) for x in _more) + '\n'
    open(os.path.join(ROOT, 'llms.txt'), 'w', encoding='utf-8').write(_lt)
open(os.path.join(ROOT, 'assets', 'search.json'), 'w', encoding='utf-8').write(json.dumps(SEARCH, ensure_ascii=False, separators=(',', ':')))
_ver = hashlib.md5(b''.join(open(os.path.join(ROOT, 'assets', f), 'rb').read() for f in ['site.css', 'store.js', 'jar3d.js', 'products.json'])).hexdigest()[:10]
open(os.path.join(ROOT, 'site.webmanifest'), 'w').write(json.dumps({
    'name': 'GlutaNex – Glutathione Skincare', 'short_name': 'GlutaNex', 'description': 'GlutaNex glutathione night cream and face wash. Free shipping and Cash on Delivery across India.',
    'id': '/', 'start_url': '/?source=app', 'scope': '/', 'display': 'standalone', 'orientation': 'portrait',
    'background_color': '#FBF7F1', 'theme_color': '#FBF7F1', 'lang': 'en-IN', 'categories': ['shopping', 'beauty', 'lifestyle'],
    'icons': [{'src': '/icon-192.png', 'sizes': '192x192', 'type': 'image/png', 'purpose': 'any'}, {'src': '/icon-512.png', 'sizes': '512x512', 'type': 'image/png', 'purpose': 'any'}, {'src': '/icon-maskable-512.png', 'sizes': '512x512', 'type': 'image/png', 'purpose': 'maskable'}],
    'shortcuts': [{'name': 'Shop', 'url': '/shop/', 'icons': [{'src': '/icon-192.png', 'sizes': '192x192'}]},
                  {'name': 'Track order', 'url': '/track-order/', 'icons': [{'src': '/icon-192.png', 'sizes': '192x192'}]},
                  {'name': 'Glutathione guide', 'url': '/glutathione/', 'icons': [{'src': '/icon-192.png', 'sizes': '192x192'}]}]}, ensure_ascii=False, indent=1))
PRECACHE = ['/', '/offline/', '/shop/', '/glutathione/', '/assets/site.css?v=' + AV, '/assets/store.js?v=' + AV, '/assets/jar3d.js?v=' + AV, '/assets/products.json',
            im('jar-cut'), '/assets/img/glutanex-logo-dark.png', '/assets/img/glutanex-logo-light.png', '/assets/whatsapp-glyph-green.svg', '/icon-192.png', '/assets/fonts/manrope.woff', '/assets/fonts/cormorant.woff']
open(os.path.join(ROOT, 'sw.js'), 'w').write('''/* GlutaNex app: keeps the shop fast and usable on weak connections. Version %s */
var V='gn-%s', CORE=%s;
self.addEventListener('install',function(e){e.waitUntil(caches.open(V).then(function(c){return c.addAll(CORE);}).then(function(){return self.skipWaiting();}));});
self.addEventListener('activate',function(e){e.waitUntil(caches.keys().then(function(ks){return Promise.all(ks.filter(function(k){return k!==V;}).map(function(k){return caches.delete(k);}));}).then(function(){return self.clients.claim();}));});
self.addEventListener('push',function(e){var d={};try{d=e.data?e.data.json():{};}catch(x){d={body:e.data?e.data.text():''};}
  e.waitUntil(self.registration.showNotification(d.title||'GlutaNex',{body:d.body||'',icon:'/icon-192.png',badge:'/icon-192.png',tag:d.tag||'gn',data:{url:d.url||'/'}}));});
self.addEventListener('notificationclick',function(e){e.notification.close();var url=(e.notification.data&&e.notification.data.url)||'/';
  e.waitUntil(clients.matchAll({type:'window',includeUncontrolled:true}).then(function(cs){for(var i=0;i<cs.length;i++){if('focus' in cs[i]){cs[i].navigate(url);return cs[i].focus();}}return clients.openWindow(url);}));});
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
open(os.path.join(ROOT, '.vercelignore'), 'w').write('_build\nREADME.md\n.github\n')
print('built', len(pages), 'indexed pages', '(PREVIEW: noindex everywhere)' if PREVIEW else '')
