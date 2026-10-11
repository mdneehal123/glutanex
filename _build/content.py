# Guides, information pages and policies. Read by build.py with exec(), so it uses the helpers defined there.
STUDY = '<a href="https://www.dovepress.com/skin-whitening-and-skin-condition-improving-effects-of-topical-oxidize-peer-reviewed-fulltext-article-CCID" rel="noopener">Watanabe et al., 2014</a>'
FDA = '<a href="https://www.medestheticsmag.com/fda-warns-against-skin-lightening-injectables" rel="noopener">US FDA warning, 2015</a>'
CREAM = '<a href="%s">GlutaNex Glutathione Night Cream</a>' % url(BYID['cream'])
WASH = '<a href="%s">Gluta Boost Face Wash</a>' % url(BYID['wash'])

GUIDES = [
    dict(slug='glutathione-cream', title='Glutathione cream: what it is and how to choose one', short='Glutathione cream guide',
         blurb='What glutathione cream does, what the research says, and what to look for.',
         seo='Glutathione Cream for Face: Benefits, Research & How to Choose',
         desc='Glutathione cream explained: what glutathione is, what a glutathione face cream can and cannot do, what the research shows, and how to choose and use one safely.',
         body='''<p>A glutathione cream is a skincare cream that contains glutathione, an antioxidant the body makes naturally. It is used in products made for <b>brighter-looking, more even skin</b>. It is a cosmetic, not a medicine, and it works gradually.</p>
<h2>What is glutathione?</h2><p>Glutathione is a small molecule made of three amino acids (cysteine, glutamic acid and glycine). Inside the body it acts as an antioxidant, helping cells deal with everyday stress from things like UV light and pollution. In skincare, it is added to creams, serums and face washes, often together with niacinamide or vitamin C.</p>
<h2>What can a glutathione cream do?</h2><ul><li>Help skin look <b>brighter and more even</b> with regular use.</li><li>Support the look of <b>dark spots and tan</b> fading, alongside daily sunscreen.</li><li>Add an antioxidant step to a simple night routine.</li></ul>
<h2>What it cannot do</h2><ul><li>Change your natural skin colour. No cream can.</li><li>Work overnight. Expect weeks, not days.</li><li>Replace sunscreen or treatment for medical conditions like melasma.</li></ul>
<h2>What the research says</h2><p>Studies on glutathione applied to the skin are few and small. In one double-blind, placebo-controlled study (%(study)s), 30 women applied a 2%% oxidized glutathione lotion to one side of the face twice a day for 10 weeks. The glutathione side showed a modest but steady reduction in melanin index compared with placebo, and the lotion was well tolerated. The study was small and partly run by the ingredient's maker, so results should be read with care.</p>
<h2>How to choose a glutathione cream</h2><ol><li><b>Read the ingredient list.</b> Glutathione should be listed, and the full list should be printed on the pack.</li><li><b>Avoid big promises.</b> "Fair in 7 days" or "permanent whitening" are red flags for harsh or banned ingredients.</li><li><b>Check the seller.</b> A real business name, address, return policy and contact number.</li><li><b>Pick a routine you will keep.</b> A gentle cleanser, the cream at night, sunscreen in the morning.</li></ol>
<h2>How to use it</h2><p>At night, cleanse with a gentle face wash such as %(wash)s, pat dry and apply a small amount of cream to the face and neck. Use sunscreen every morning. Patch test first. See the full guide: <a href="/how-to-use-glutathione-cream/">how to use glutathione cream</a>.</p>
<p>%(cream)s is GlutaNex's glutathione cream for the night routine.</p>'''),
    dict(slug='glutathione-benefits-for-skin', title='Glutathione benefits for skin', short='Benefits for skin',
         blurb='What glutathione can do for skin, and what it cannot.',
         seo='Glutathione Benefits for Skin: What It Does & What Research Shows',
         desc='Glutathione benefits for skin explained simply: antioxidant support, brighter and more even-looking skin, what the studies show, and realistic timelines.',
         body='''<p>Glutathione's main benefit in skincare is helping skin look <b>brighter and more even</b> over time, as part of a routine with daily sunscreen. Here is what that means in practice.</p>
<h2>1. Antioxidant support</h2><p>Glutathione is one of the body's own antioxidants. In skincare, antioxidants are used to help skin cope with daily stress from sun and pollution, which contributes to dullness and uneven tone.</p>
<h2>2. Brighter, more even-looking skin</h2><p>Glutathione is studied for its effect on melanin, the pigment behind tan and dark spots. In a small placebo-controlled study (%(study)s), a 2%% glutathione lotion used twice daily gave a modest, gradual improvement in skin tone over 10 weeks.</p>
<h2>3. Smoother-feeling skin</h2><p>The same study also reported better skin moisture and smoothness in later weeks. Much of this also comes from the cream base itself and from regular moisturising.</p>
<h2>What to expect, realistically</h2><div class="tbl"><table><thead><tr><th>Time</th><th>What you may notice</th></tr></thead><tbody><tr><td>Week 1–2</td><td>Skin feels softer and more comfortable</td></tr><tr><td>Week 4–6</td><td>Skin may look a little brighter and more even</td></tr><tr><td>Week 8+</td><td>Dark spots and tan may look lighter, with daily sunscreen</td></tr></tbody></table></div>
<p>Results vary from person to person. Glutathione does not change your natural skin colour.</p>
<h2>Getting the most from it</h2><ul><li>Use it every night, not occasionally.</li><li>Wear sunscreen every morning; without it, new tan and spots keep forming.</li><li>Pair it with gentle cleansing, such as %(wash)s.</li></ul>
<p>Read next: <a href="/glutathione-side-effects/">glutathione side effects</a> · <a href="/glutathione-cream/">how to choose a glutathione cream</a></p>'''),
    dict(slug='glutathione-side-effects', title='Glutathione side effects and safe use', short='Side effects',
         blurb='Who should be careful, and how to use glutathione creams safely.',
         seo='Glutathione Side Effects: Is Glutathione Cream Safe?',
         desc='Glutathione side effects explained: what is normal with glutathione creams, the risks of glutathione injections, who should ask a doctor first, and how to patch test.',
         body='''<p>Glutathione creams and face washes are generally well tolerated, but any skincare product can irritate some skin. The bigger safety concerns are with <b>glutathione injections</b>, not creams.</p>
<h2>Creams and face washes</h2><ul><li><b>Mild tingling, redness or dryness</b> in the first days can happen with new products and usually settles.</li><li><b>Redness, itching or burning that lasts</b> is a reaction: stop using the product.</li><li><b>Rash or swelling</b>: stop at once and see a doctor.</li></ul><p>In the 10-week study of a 2%% glutathione lotion (%(study)s), one of 30 participants had mild redness for two days, which settled without stopping.</p>
<h2>Glutathione injections</h2><p>Injections are a medical procedure, not skincare. The %(fda)s said injectable skin-lightening products may be unsafe, may contain unknown substances, and carry risks from unsafe injection practices, and that no injectable skin-lightening drug is approved. Never take glutathione injections from salons or unlicensed sellers.</p>
<h2>How to patch test</h2><ol><li>Apply a little product behind the ear or on the inner arm.</li><li>Leave it for 24 hours.</li><li>No reaction? Start on the face, once a day.</li></ol>
<h2>Ask a doctor first if you</h2><ul><li>are pregnant or breastfeeding;</li><li>have eczema, rosacea or very sensitive skin;</li><li>use prescription skin treatments;</li><li>have patchy pigmentation that may be melasma.</li></ul>
<p>See also: <a href="/glutathione-cream-vs-tablets-vs-injections/">cream vs tablets vs injections</a></p>'''),
    dict(slug='how-to-use-glutathione-cream', title='How to use glutathione cream', short='How to use',
         blurb='A simple night routine, step by step.',
         seo='How to Use Glutathione Cream: Simple Night Routine',
         desc='How to use glutathione cream on the face: a simple step-by-step night routine, how much to apply, what to pair it with, and mistakes to avoid.',
         body='''<p>Use glutathione cream at night on clean, dry skin, and use sunscreen every morning. That's the whole routine.</p>
<h2>Night routine</h2><ol><li><b>Cleanse:</b> wash your face with a gentle cleanser such as %(wash)s and pat dry.</li><li><b>Apply:</b> take a pea-sized amount and dot it on forehead, cheeks and chin, then smooth over face and neck. Avoid the eyes.</li><li><b>Let it absorb:</b> give it a few minutes before lying down.</li></ol>
<h2>Morning</h2><p>Cleanse, then apply a broad-spectrum sunscreen (SPF 30 or higher). Sun exposure keeps creating new tan and dark spots, so this step protects the work of the night.</p>
<h2>Good pairings</h2><ul><li><b>Niacinamide:</b> a gentle, well-studied ingredient often used with glutathione.</li><li><b>Vitamin C:</b> another antioxidant; use it in the morning if you have it.</li><li><b>A simple moisturiser:</b> if your skin feels dry.</li></ul>
<h2>Mistakes to avoid</h2><ul><li>Using a thick layer: more cream does not work faster.</li><li>Skipping sunscreen.</li><li>Layering extra strong products on top. The GlutaNex Night Cream already contains retinol and salicylic acid, so skip other retinol, AHA/BHA or peel products on the same night.</li><li>Going every night from day one: start 2 to 3 nights a week for the first two weeks.</li><li>Changing products every week: give one routine 6 to 8 weeks.</li></ul>
<p>Products: %(cream)s · %(wash)s</p>'''),
    dict(slug='glutathione-cream-vs-tablets-vs-injections', title='Glutathione cream vs tablets vs injections', short='Cream vs tablets vs injections',
         blurb='The honest differences, including the safety warnings.',
         seo='Glutathione Cream vs Tablets vs Injections: Which Is Safe?',
         desc='Glutathione cream vs tablets vs injections compared: how each is used, what the evidence says, safety warnings on injections, and which makes sense for skincare.',
         body='''<p>For everyday skincare, a <b>glutathione cream or face wash</b> is the simple, low-risk option. Tablets are supplements with mixed evidence, and injections carry real safety risks.</p>
<div class="tbl"><table><thead><tr><th></th><th>Cream / face wash</th><th>Tablets</th><th>Injections</th></tr></thead><tbody>
<tr><td>What it is</td><td>Cosmetic applied to skin</td><td>Oral supplement</td><td>Medical procedure</td></tr>
<tr><td>Evidence for skin</td><td>Small studies show modest, gradual effects</td><td>Mixed; the body breaks much of it down</td><td>Not approved for skin lightening</td></tr>
<tr><td>Main risks</td><td>Skin irritation in some people</td><td>Stomach upset; ask a doctor first</td><td>Infection, unknown ingredients, serious reactions</td></tr>
<tr><td>Who should use it</td><td>Most adults, after a patch test</td><td>Only with medical advice</td><td>Avoid for cosmetic use</td></tr>
</tbody></table></div>
<h2>Why we recommend against injections for skin</h2><p>The %(fda)s stated that injectable skin-lightening products may be unsafe and ineffective, may contain unknown substances, and that unsafe injections can spread infection. No injectable product is approved for skin lightening.</p>
<h2>What about tablets?</h2><p>Glutathione supplements are widely sold, but evidence for visible skin changes is mixed. If you are considering them, talk to a doctor, especially if you take other medicines or are pregnant.</p>
<h2>The simple approach</h2><p>A gentle face wash, a glutathione cream at night and sunscreen every morning. See <a href="/how-to-use-glutathione-cream/">how to use glutathione cream</a>.</p>'''),
    dict(slug='glutathione-and-niacinamide', title='Glutathione with niacinamide and vitamin C', short='Glutathione + niacinamide',
         blurb='How these ingredients work together in a routine.',
         seo='Glutathione and Niacinamide Together: Benefits & How to Use',
         desc='Can you use glutathione with niacinamide and vitamin C? How these brightening ingredients work together, how to layer them, and what to avoid.',
         body='''<p>Yes, glutathione can be used with niacinamide and vitamin C. They are often combined in products made for brighter, more even-looking skin.</p>
<h2>How they differ</h2><div class="tbl"><table><thead><tr><th>Ingredient</th><th>Used for</th><th>Good to know</th></tr></thead><tbody>
<tr><td>Glutathione</td><td>Antioxidant support, brighter-looking skin</td><td>Works gradually</td></tr>
<tr><td>Niacinamide (vitamin B3)</td><td>Even-looking tone, smoother texture, skin barrier</td><td>May tingle briefly at first</td></tr>
<tr><td>Vitamin C</td><td>Antioxidant, brightness</td><td>Best in the morning, under sunscreen</td></tr>
</tbody></table></div>
<h2>A simple way to layer</h2><ul><li><b>Morning:</b> cleanser → vitamin C (optional) → sunscreen.</li><li><b>Night:</b> cleanser → glutathione cream (with niacinamide if your product has it).</li></ul>
<h2>Keep it gentle</h2><p>Add one new product at a time, patch test, and avoid stacking strong acids or retinol on the same night. Read <a href="/glutathione-side-effects/">side effects and safe use</a>.</p>'''),
    dict(slug='glutathione-for-dark-spots-and-tan', title='Glutathione for dark spots and tan', short='Dark spots and tan',
         blurb='What helps tan and dark spots fade, and how long it takes.',
         seo='Glutathione for Dark Spots and Tan: Does It Work?',
         desc='Does glutathione help dark spots and tan? What causes them, how glutathione creams fit in, the role of sunscreen, realistic timelines and when to see a doctor.',
         body='''<p>Glutathione creams can support the look of tan and dark spots fading, but <b>sunscreen does most of the work</b>. Without it, new tan and spots keep forming.</p>
<h2>What causes them</h2><ul><li><b>Tan:</b> the skin's response to UV light.</li><li><b>Marks after pimples:</b> very common on Indian skin.</li><li><b>Sun spots:</b> from years of sun exposure.</li><li><b>Melasma:</b> patchy brown areas linked to hormones and sun; needs a dermatologist.</li></ul>
<h2>A routine that helps</h2><ol><li>Sunscreen every morning, reapplied if you are outdoors for long.</li><li>A glutathione cream every night, such as %(cream)s.</li><li>No squeezing pimples, no harsh scrubs or lemon juice.</li></ol>
<h2>How long it takes</h2><p>Tan usually lightens over a few weeks once you protect your skin. Dark spots take longer: often 8 to 12 weeks, and older spots may only lighten partly.</p>
<h2>When to see a doctor</h2><p>Patchy pigmentation on both cheeks, spots that change shape or colour, or no change after 3 months of care.</p>'''),
]

exec(open(os.path.join(B, 'content_more.py'), encoding='utf-8').read())
P = dict(REFS, fda=FDA, cream=CREAM, wash=WASH, uduo=url(BYID['duo']),
         pcream=rs(BYID['cream']['price']), mcream=rs(BYID['cream']['mrp']), pwash=rs(BYID['wash']['price']), mwash=rs(BYID['wash']['mrp']),
         pduo=rs(BYID['duo']['price']), mduo=rs(BYID['duo']['mrp']))
for g in GUIDES:
    ex = EXPAND.get(g['slug'])
    g.setdefault('refs', ['study', 'fda'] if '%(fda)s' in g['body'] else ['study'])
    if ex:
        g['body'] += ex['body']; g['faq'] = ex['faq']
        g['refs'] = list(dict.fromkeys(g['refs'] + ex['refs']))
# the Q&A page: each question becomes an H2 with a short direct answer, and the FAQ schema
QA_PAGE['body'] = ''.join('<h2>%s</h2><p class="answer">%s</p>%s' % (q, a, d) for q, a, d in QA_PAGE['qa'])
QA_PAGE['faq_ld'] = [(q, a) for q, a, d in QA_PAGE['qa']]
P['owner'] = OWNER
# guides with a 'qa' list (exact Google questions): questions go first as H2s with a short answer, and into the FAQ schema
for _g in [PILLAR]:
    if _g.get('qa'):
        _g['body'] = ''.join('<h2>%s</h2><p class="answer">%s</p>%s' % (q, a, d) for q, a, d in _g['qa']) + _g['body']
        _g['faq_ld'] = [(q, a) for q, a, d in _g['qa']] + list(_g.get('faq', []))
        _g['faq'] = []
GUIDES = [PILLAR] + GUIDES + NEW_GUIDES + [QA_PAGE]
EN2HI = {h['en']: '/hi/%s/' % h['slug'] for h in HI}


def guide_url(g):
    return '/%s/' % g['slug']


def slugify(t):
    return re.sub(r'[^a-z0-9]+', '-', re.sub(r'<[^>]+>', '', t).lower()).strip('-')[:60] or 'section'


def with_toc(body, label='On this page'):
    heads = []
    def sub(m):
        txt = m.group(1); i = slugify(txt)
        if i in [x[0] for x in heads]: i += '-%d' % len(heads)
        heads.append((i, re.sub(r'<[^>]+>', '', txt)))
        return '<h2 id="%s">%s</h2>' % (i, txt)
    body = re.sub(r'<h2>(.*?)</h2>', sub, body)
    if len(heads) < 4:
        return body
    toc = '<nav class="toc" aria-label="%s"><b>%s</b><ol>%s</ol></nav>' % (label, label, ''.join('<li><a href="#%s">%s</a></li>' % (i, html.escape(t)) for i, t in heads))
    return toc + body


def faq_block(items, head='Frequently asked questions'):
    return '<h2 id="faq">%s</h2>' % head + faq_html(items) if items else ''


def sources_block(refs, head='Sources'):
    if not refs:
        return ''
    return '<div class="sources"><b>%s</b><ol>%s</ol></div>' % (head, ''.join('<li>%s</li>' % html.escape(SOURCES[r]) for r in refs if r in SOURCES))


def hreflang(en_path, hi_path):
    return ('<link rel="alternate" hreflang="en-IN" href="%s%s">\n<link rel="alternate" hreflang="hi-IN" href="%s%s">\n'
            '<link rel="alternate" hreflang="x-default" href="%s%s">\n') % (SITE, en_path, SITE, hi_path, SITE, en_path)



def gcard(g):
    return '<a class="reveal" href="%s"><span class="eyebrow">Guide</span><h3>%s</h3><p>%s</p></a>' % (guide_url(g), g['title'], g['blurb'])
hub = top('Glutathione guides', 'Everything about <span class="gold">glutathione</span>', 'Plain, accurate guides on glutathione for skin: what it does, how to use it, and how to stay safe.') + \
    '<section style="padding-top:30px"><div class="wrap"><a class="pillar-card reveal" href="/glutathione/"><span class="eyebrow">Start here</span><h2>%s</h2><p>%s</p><span class="btn sm">Read the complete guide</span></a>' \
    '<div class="guides" style="margin-top:22px">%s</div>' \
    '<div class="sec-h" style="margin-top:48px"><span class="eyebrow">हिंदी में पढ़ें</span><h2>Hindi guides</h2></div><div class="guides">%s</div>' \
    '<p class="note">These guides are general information about cosmetic skincare and do not replace advice from a dermatologist.</p></div></section>' % (
        PILLAR['title'], PILLAR['blurb'], ''.join(gcard(g) for g in GUIDES[1:]),
        ''.join('<a class="reveal" href="/hi/%s/" lang="hi"><span class="eyebrow">हिंदी</span><h3>%s</h3><p>%s</p></a>' % (h['slug'], h['title'], h['desc'].split(':')[0]) for h in HI))
page('/glutathione-guides/', 'Glutathione Guides: Benefits, Side Effects, Price & Use | GlutaNex', 'All GlutaNex glutathione guides: what glutathione is, benefits for skin, side effects, price in India, face wash, kojic acid, foods and Hindi guides.',
     hub, crumbs=[('Glutathione guides', '/glutathione-guides/')], schema=[{'@type': 'ItemList', 'itemListElement': [{'@type': 'ListItem', 'position': i + 1, 'url': SITE + guide_url(g), 'name': g['title']} for i, g in enumerate(GUIDES)]}])

RELATED = {'glutathione': ['glutathione-cream-questions', 'glutathione-cream', 'is-glutathione-safe-for-skin'], 'glutathione-cream-questions': ['glutathione', 'retinol-vs-glutathione', 'glutathione-night-cream']}
for i, g in enumerate(GUIDES):
    if g['slug'] in RELATED:
        more = [x for x in GUIDES if x['slug'] in RELATED[g['slug']]]
    else:
        more = [GUIDES[0]] + [GUIDES[(i + j) % len(GUIDES)] for j in (1, 2) if GUIDES[(i + j) % len(GUIDES)]['slug'] != 'glutathione']
        more = more[:3]
    faq = [(q % P, a % P) for q, a in g.get('faq', [])]
    body = top('Glutathione guide', g['title'], g['blurb']) + \
        '<section style="padding-top:22px"><div class="wrap article"><div class="prose"><p class="byline">By the GlutaNex team · Updated 11 October 2026 · %d sources cited</p>%s%s%s<p class="note">General information about cosmetic skincare, not medical advice. Results vary from person to person. See a dermatologist for persistent or changing pigmentation.</p></div>' \
        '<aside class="side-cta"><img src="%s" alt="GlutaNex Glutathione Night Cream" width="800" height="800" loading="lazy"><b>GlutaNex Night Cream</b><span>Glutathione + niacinamide + vitamin C · %s · Cash on Delivery</span><button class="btn block" type="button" data-buy="cream">Buy now</button><a class="btn ghost block sm" href="%s">View product</a></aside></div></section>' \
        '<section style="padding-top:10px"><div class="wrap"><div class="sec-h"><span class="eyebrow">Keep reading</span><h2>More glutathione guides</h2></div><div class="guides">%s</div></div></section>' % (
            len(g['refs']), with_toc(g['body'] % P), faq_block(faq), sources_block(g['refs']), im('cream-square'), rs(BYID['cream']['price']), url(BYID['cream']),
            ''.join(gcard(m) for m in more))
    sch = [{'@type': 'Article', 'headline': g['title'], 'description': g['desc'], 'datePublished': TODAY, 'dateModified': TODAY, 'mainEntityOfPage': SITE + guide_url(g),
            'author': {'@id': SITE + '/#org'}, 'publisher': {'@id': SITE + '/#org'}, 'image': SITE + im('cream-square', 'jpg'), 'inLanguage': 'en-IN',
            'about': {'@type': 'Thing', 'name': 'Glutathione', 'sameAs': 'https://en.wikipedia.org/wiki/Glutathione'}}]
    if g.get('faq_ld'):
        sch.append(faq_ld([(q % P, re.sub(r'<[^>]+>', '', a % P)) for q, a in g['faq_ld']]))
    elif faq:
        sch.append(faq_ld([(q, re.sub(r'<[^>]+>', '', a)) for q, a in faq]))
    hp = EN2HI.get(guide_url(g))
    page(guide_url(g), g['seo'], g['desc'], body, og='article', crumbs=[('Glutathione guides', '/glutathione-guides/'), (g['short'], guide_url(g))], schema=sch,
         extra=hreflang(guide_url(g), hp) if hp else '')

# ---------------- Hindi pages ----------------
for h in HI:
    path = '/hi/%s/' % h['slug']
    faq = [(q % P, a % P) for q, a in h['faq']]
    body = top('हिंदी गाइड', h['title'], h['desc'].split(':', 1)[-1].strip()) + \
        '<section style="padding-top:22px"><div class="wrap article"><div class="prose" lang="hi"><p class="byline">GlutaNex टीम द्वारा · अपडेट: 11 अक्टूबर 2026 · <a href="%s" lang="en">Read in English</a></p>%s%s%s<p class="note">यह सामान्य कॉस्मेटिक स्किनकेयर जानकारी है, चिकित्सा सलाह नहीं। परिणाम हर व्यक्ति में अलग हो सकते हैं।</p></div>' \
        '<aside class="side-cta"><img src="%s" alt="GlutaNex Glutathione Night Cream" width="800" height="800" loading="lazy"><b>GlutaNex Night Cream</b><span>ग्लूटाथियोन नाइट क्रीम · %s · कैश ऑन डिलीवरी</span><button class="btn block" type="button" data-buy="cream">अभी खरीदें</button></aside></div></section>' \
        '<section style="padding-top:10px"><div class="wrap"><div class="sec-h"><h2>और पढ़ें</h2></div><div class="guides">%s</div></div></section>' % (
            h['en'], with_toc(h['body'] % P, 'इस पेज पर'), faq_block(faq, 'अक्सर पूछे जाने वाले सवाल'), sources_block(['study', 'ijdvl', 'fda'], 'स्रोत'),
            im('cream-square'), rs(BYID['cream']['price']),
            ''.join('<a href="/hi/%s/" lang="hi"><span class="eyebrow">हिंदी</span><h3>%s</h3></a>' % (x['slug'], x['title']) for x in HI if x is not h) +
            '<a href="/glutathione/"><span class="eyebrow">English</span><h3>Glutathione: the complete guide</h3></a>')
    page(path, h['seo'], h['desc'], body, og='article', lang='hi-IN', crumbs=[('हिंदी गाइड', '/hi/'), (h['short'], path)], extra=hreflang(h['en'], path),
         schema=[{'@type': 'Article', 'headline': h['title'], 'description': h['desc'], 'datePublished': TODAY, 'dateModified': TODAY, 'mainEntityOfPage': SITE + path,
                  'author': {'@id': SITE + '/#org'}, 'publisher': {'@id': SITE + '/#org'}, 'image': SITE + im('cream-square', 'jpg'), 'inLanguage': 'hi-IN'},
                 faq_ld(faq)])
page('/hi/', 'Glutathione Hindi Guide: ग्लूटाथियोन की पूरी जानकारी हिंदी में | GlutaNex', 'ग्लूटाथियोन की जानकारी हिंदी में: ग्लूटाथियोन क्रीम के फायदे, नुकसान और लगाने का सही तरीका।',
     top('हिंदी गाइड', 'ग्लूटाथियोन की जानकारी <span class="gold">हिंदी में</span>', 'आसान और सही जानकारी: फायदे, नुकसान और उपयोग का तरीका।') +
     '<section style="padding-top:30px"><div class="wrap" lang="hi"><div class="guides">%s</div></div></section>' % ''.join(
         '<a class="reveal" href="/hi/%s/"><span class="eyebrow">गाइड</span><h3>%s</h3><p>%s</p></a>' % (x['slug'], x['title'], x['desc'].split(':', 1)[-1].strip()) for x in HI),
     lang='hi-IN', crumbs=[('हिंदी गाइड', '/hi/')])

# ---------------- Information pages ----------------
page('/about/', 'About GlutaNex | Glutathione Skincare', 'About GlutaNex: glutathione skincare for a simple night routine, sold and shipped by %s.' % OWNER,
     top('About', 'About <span class="gold">GlutaNex</span>', 'Glutathione skincare for a simple, consistent night routine.') + '''<section style="padding-top:24px"><div class="wrap prose">
<p>GlutaNex makes glutathione skincare for people who want a short routine they can keep: a gentle face wash and a night cream, with sunscreen in the morning.</p>
<h2>What we believe</h2><ul><li><b>Honest claims.</b> Glutathione works gradually and does not change your natural skin colour. We say so.</li><li><b>Clear information.</b> Full ingredient lists, clear prices, no hidden charges.</li><li><b>Safety first.</b> We recommend creams, not injections, and we explain why.</li></ul>
<h2>Who we are</h2><p>GlutaNex products on this website are sold and shipped by %s, %s. You can reach us on WhatsApp at %s.</p>
<p style="margin-top:24px"><a class="btn" href="/shop/">Shop GlutaNex</a></p></div></section>''' % (OWNER, ADDR, WA_SHOW), crumbs=[('About', '/about/')])

page('/contact/', 'Contact GlutaNex | WhatsApp Support', 'Contact GlutaNex on WhatsApp at %s for help with orders, delivery and products.' % WA_SHOW,
     top('Contact', 'Contact us', 'The fastest way to reach us is WhatsApp.') + '''<section style="padding-top:24px"><div class="wrap prose">
<p><a class="btn wa" href="https://wa.me/%s" target="_blank" rel="noopener">%s Chat on WhatsApp</a></p>
<h2>Details</h2><ul><li><b>WhatsApp and phone:</b> %s</li><li><b>Seller:</b> %s</li><li><b>Address:</b> %s</li><li><b>Hours:</b> Monday to Saturday, 10 am to 7 pm</li></ul>
<p>Please share your order number or the mobile number used on the order. You can also check your parcel on the <a href="/track-order/">Track Order</a> page.</p></div></section>''' % (WA, WA_IMG, WA_SHOW, OWNER, ADDR), crumbs=[('Contact', '/contact/')])

FAQ_ALL = HOME_FAQ + [
    ('What is the price of GlutaNex Glutathione Night Cream?', 'The Night Cream is %s, the Gluta Boost Face Wash is %s and the Glow Duo is %s. Prices include taxes and shipping is free.' % (rs(BYID['cream']['price']), rs(BYID['wash']['price']), rs(BYID['duo']['price']))),
    ('How long does delivery take?', 'Orders are packed in 1 to 2 business days and usually delivered in 3 to 7 business days after dispatch.'),
    ('Can I return a product?', 'Sealed, unopened products can be returned within 7 days of delivery. Damaged or wrong items are replaced or refunded in full. See the <a href="/refund-policy/">returns policy</a>.'),
    ('Can men use GlutaNex?', 'Yes. GlutaNex products are for anyone who wants a simple night skincare routine.'),
    ('Is it safe during pregnancy?', 'Ask your doctor before using any new skincare product during pregnancy or breastfeeding.'),
]
page('/faq/', 'GlutaNex FAQ | Glutathione Cream Questions', 'Answers about GlutaNex glutathione cream and face wash: how to use, results, safety, price, delivery, Cash on Delivery and returns.',
     top('FAQ', 'Questions, answered') + '<section style="padding-top:24px"><div class="wrap">%s</div></section>' % faq_html(FAQ_ALL), crumbs=[('FAQ', '/faq/')], schema=[faq_ld(FAQ_ALL)])

page('/track-order/', 'Track Your Order | GlutaNex', 'Track your GlutaNex order with your mobile number and pincode, or your payment ID.',
     top('Track order', 'Track your order', 'Use the mobile number and pincode from your order, or your payment ID.') + '''<section style="padding-top:20px"><div class="wrap track">
<form class="form" id="track-form" novalidate>
  <div class="track-by"><button type="button" id="by-phone" class="on">Mobile number</button><button type="button" id="by-id">Payment ID / AWB</button></div>
  <div id="by-phone-box" class="form"><div class="f"><label for="t-phone">Mobile number</label><input id="t-phone" type="tel" inputmode="numeric" maxlength="16"></div><div class="f"><label for="t-pin">Delivery pincode</label><input id="t-pin" inputmode="numeric" maxlength="6"></div></div>
  <div id="by-id-box" class="form" hidden><div class="f"><label for="t-id">Payment ID or tracking number</label><input id="t-id" autocomplete="off" placeholder="pay_XXXXXXXXXXXX"></div></div>
  <button class="btn block" type="submit" id="t-go">Track order</button>
</form><div class="track-out" id="t-out" role="status" aria-live="polite" hidden></div></div></section>''', crumbs=[('Track order', '/track-order/')])

# ---------------- Policies ----------------
BIZ = '<div class="note"><b>Seller:</b> %s · %s · WhatsApp %s · For complaints, message us on WhatsApp.</div>' % (OWNER, ADDR, WA_SHOW)
POL = {
    '/privacy-policy/': ('Privacy Policy', 'How GlutaNex collects, uses and protects your information, and how cookies and ads work on this site.', '''
<p>This policy explains what information GlutaNex (sold by %(o)s) collects and how it is used.</p>%(biz)s
<h2>What we collect</h2><p>When you order: your name, mobile number, delivery address, city, pincode and the products you choose. Payments are processed by Razorpay; we never see your card or UPI details.</p>
<h2>How we use it</h2><p>Only to process, ship and support your order, send order updates and reply on WhatsApp. If a payment does not complete, we may contact you once to help. We do not sell your information.</p>
<h2>Who we share it with</h2><p>Razorpay (payments), Shiprocket and courier partners (delivery), Vercel (hosting), and authorities when required by law.</p>
<h2>Cookies and ads</h2><p>The site may use advertising and analytics tools such as Google or Meta to measure visits and orders. You can opt out of personalised ads at <a href="https://adssettings.google.com" rel="noopener">Google Ads Settings</a> and in your Facebook ad preferences.</p>
<h2>Help with unfinished orders</h2><p>At checkout you can tick a box to let us message you on WhatsApp if you do not finish your order. Only if you tick it, we save your name, mobile number, address and cart for up to 30 days, and delete it as soon as you order or ask us to. If you do not tick it, nothing is saved.</p>
<h2>Question assistant</h2><p>The "Ask" assistant answers questions using our guides. Your questions are sent to our AI provider (Anthropic) to write the answer and are not used to identify you; please do not type personal or medical details. We keep only a daily count of questions, not the questions themselves.</p>
<h2>App reminders</h2><p>If you turn on reminders, your phone's notification address and your chosen reminders (routine and refill dates) are stored so we can send them. No name or number is attached. Turn them off on the Reminders page or in your phone settings, and they are deleted.</p>
<h2>Saved on your device</h2><p>Your cart and checkout details are saved in your browser so you don't have to type them again. You can clear them any time.</p>
<h2>Your choices</h2><p>To access, correct or delete your information, message us on WhatsApp. We respond within 30 days.</p>'''),
    '/terms/': ('Terms & Conditions', 'Terms for buying GlutaNex products on this website: orders, prices, payment, Cash on Delivery and product use.', '''
<p>By using this website and placing an order you agree to these terms. Products are sold by %(o)s.</p>%(biz)s
<h2>Products</h2><p>GlutaNex products are cosmetics, not medicines. Results vary and are not guaranteed. Patch test before use and follow the directions on the pack.</p>
<h2>Prices</h2><p>Prices are in Indian rupees and include taxes. Shipping is free. The total shown at checkout is the total you pay.</p>
<h2>Orders</h2><p>An order is confirmed when payment, or the Cash on Delivery advance, succeeds. If we cannot fulfil an order, we refund any amount paid in full.</p>
<h2>Cash on Delivery</h2><p>Cash on Delivery orders are confirmed with a %(adv)s advance paid online. It is part of the price and is refunded in full if the order is cancelled, refused at delivery or cannot be delivered.</p>
<h2>Liability and law</h2><p>Our liability is limited to the amount paid for the order. These terms are governed by the laws of India. Nothing here limits your rights under the Consumer Protection Act, 2019.</p>'''),
    '/refund-policy/': ('Returns & Refunds', 'GlutaNex returns: 7 days for sealed products, free replacement or refund for damaged or wrong items, refunds within 7 working days.', '''
%(biz)s<h2>Returns</h2><p>Sealed, unopened products can be returned within <b>7 days of delivery</b>. Message us on WhatsApp first. Return shipping for a change of mind is paid by you; we refund the product price once we receive it sealed.</p>
<h2>Damaged or wrong items</h2><p>Message us within 48 hours of delivery with photos. We replace the item free or refund you in full, including shipping.</p>
<h2>Opened products</h2><p>For hygiene reasons, opened products cannot be returned unless they arrived damaged, defective or wrong.</p>
<h2>Cancellations</h2><p>Cancel any time before dispatch for a full refund.</p>
<h2>Refunds</h2><p>Approved refunds are credited to your original payment method, or your bank or UPI for cash amounts, within 7 working days.</p>'''),
    '/shipping-policy/': ('Shipping', 'GlutaNex shipping: free across India, packed in 1 to 2 business days, delivered in 3 to 7 business days, Cash on Delivery available.', '''
%(biz)s<h2>Where we ship</h2><p>Across India, to serviceable pincodes.</p><h2>Cost</h2><p>Free on every order, with no Cash on Delivery fee.</p>
<h2>Timing</h2><p>Packed in 1 to 2 business days; delivered in 3 to 7 business days after dispatch.</p>
<h2>Tracking</h2><p>Use the <a href="/track-order/">Track Order</a> page with your mobile number and pincode.</p>'''),
}
for path, (h, d_, body) in POL.items():
    page(path, '%s | GlutaNex' % h, d_, top('Policy', h, 'Last updated: 11 October 2026') + '<section style="padding-top:20px"><div class="wrap prose">%s</div></section>' % (
        body % dict(o=OWNER, biz=BIZ, adv=rs(ADVANCE))), crumbs=[(h, path)])

page('/404', 'Page not found | GlutaNex', 'This page could not be found.', top('404', 'Page not found', 'The link may be old or mistyped.') + '<section style="padding-top:20px"><div class="wrap"><a class="btn" href="/shop/">Go to the shop</a></div></section>', index=False)
