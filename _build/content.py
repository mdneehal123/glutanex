# Guides, information pages and policies. Read by build.py with exec(), so it uses the helpers defined there.
STUDY = '<a href="https://www.dovepress.com/skin-whitening-and-skin-condition-improving-effects-of-topical-oxidize-peer-reviewed-fulltext-article-CCID" rel="noopener">Watanabe et al., 2014</a>'
FDA = '<a href="https://www.medestheticsmag.com/fda-warns-against-skin-lightening-injectables" rel="noopener">US FDA warning, 2015</a>'
CREAM = '<a href="%s">GlutaNex Glutathione Night Cream</a>' % url(BYID['cream'])
WASH = '<a href="%s">Gluta Boost Face Wash</a>' % url(BYID['wash'])

GUIDES = [
    dict(slug='glutathione-cream', title='Glutathione cream: what it is and how to choose one', short='Glutathione cream guide',
         blurb='What glutathione cream does, what the research says, and what to look for.',
         seo='What Is Glutathione Cream? Benefits, Uses & How to Choose',
         desc='What glutathione cream is, what a glutathione face cream can and cannot do, uses and benefits, what research shows, and how to choose one safely.',
         body='''<p>A glutathione cream is a skincare cream that contains glutathione, an antioxidant the body makes naturally. It is used in products made for <b>brighter-looking, more even skin</b>. It is a cosmetic, not a medicine, and it works gradually. Most are made as a <b>glutathione face cream</b> for night use, like the <a href="/product/glutanex-glutathione-night-cream/">GlutaNex glutathione face cream</a>.</p>
<h2>What is glutathione?</h2><p>Glutathione is a small molecule made of three amino acids (cysteine, glutamic acid and glycine). Inside the body it acts as an antioxidant, helping cells deal with everyday stress from things like UV light and pollution. In skincare, it is added to creams, serums and face washes, often together with niacinamide or vitamin C.</p>
<h2>What can a glutathione cream do?</h2><ul><li>Help skin look <b>brighter and more even</b> with regular use.</li><li>Support the look of <b>dark spots and tan</b> fading, alongside daily sunscreen.</li><li>Add an antioxidant step to a simple night routine.</li></ul>
<h2>What it cannot do</h2><ul><li>Change your natural skin colour. No cream can.</li><li>Work overnight. Expect weeks, not days.</li><li>Replace sunscreen or treatment for medical conditions like <a href="/glutathione-for-melasma/">melasma</a>.</li></ul>
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
         desc='Glutathione side effects explained: what is normal with glutathione creams, the risks of injections, who should ask a doctor first, and how to patch test.',
         body='''<p>Glutathione creams and face washes are generally well tolerated, but any skincare product can irritate some skin. The bigger safety concerns are with <b>glutathione injections</b>, not creams.</p>
<h2>Creams and face washes</h2><ul><li><b>Mild tingling, redness or dryness</b> in the first days can happen with new products and usually settles.</li><li><b>Redness, itching or burning that lasts</b> is a reaction: stop using the product.</li><li><b>Rash or swelling</b>: stop at once and see a doctor.</li></ul><p>In the 10-week study of a 2%% glutathione lotion (%(study)s), one of 30 participants had mild redness for two days, which settled without stopping.</p>
<h2>Glutathione injections</h2><p>Injections are a medical procedure, not skincare. The %(fda)s said injectable skin-lightening products may be unsafe, may contain unknown substances, and carry risks from unsafe injection practices, and that no injectable skin-lightening drug is approved. Never take glutathione injections from salons or unlicensed sellers.</p>
<h2>How to patch test</h2><ol><li>Apply a little product behind the ear or on the inner arm.</li><li>Leave it for 24 hours.</li><li>No reaction? Start on the face, once a day.</li></ol>
<h2>Ask a doctor first if you</h2><ul><li>are pregnant or breastfeeding;</li><li>have eczema, rosacea or very sensitive skin;</li><li>use prescription skin treatments;</li><li>have patchy pigmentation that may be <a href="/glutathione-for-melasma/">melasma</a>.</li></ul>
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
exec(open(os.path.join(B, 'hinglish.py'), encoding='utf-8').read())
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
for _g in [PILLAR] + GUIDES + NEW_GUIDES:
    if QA_EXTRA.get(_g['slug']):
        _g['qa'] = QA_EXTRA[_g['slug']]
    if _g.get('qa'):
        _g['body'] = ''.join('<h2>%s</h2><p class="answer">%s</p>%s' % (q, a, d) for q, a, d in _g['qa']) + _g['body']
        _g['faq_ld'] = [(q, a) for q, a, d in _g['qa']] + list(_g.get('faq', []))
        _g['faq'] = []
GUIDES = [PILLAR] + GUIDES + NEW_GUIDES + [QA_PAGE]
EN2HI = {h['en']: '/hi/%s/' % h['slug'] for h in HI}


GSH_THING = {'@type': 'Thing', 'name': 'Glutathione', 'sameAs': ['https://en.wikipedia.org/wiki/Glutathione', 'https://pubchem.ncbi.nlm.nih.gov/compound/GSH', 'https://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI:16856']}


def guide_url(g):
    return '/%s/' % g['slug']


def slugify(t):
    return re.sub(r'[^a-z0-9\u0900-\u0963\u0966-\u0dff]+', '-', re.sub(r'<[^>]+>', '', t).lower()).strip('-')[:80] or 'section'


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


NO_CARD = {'glutathione-in-pregnancy', 'glutathione-vs-hydroquinone', 'glutathione-for-underarms-and-body', 'glutathione-for-dark-circles'}
def mid_card(slug, body):
    if slug in NO_CARD:
        return body
    idx = [m.start() for m in re.finditer(r'<h2 ', body)]
    if len(idx) < 4:
        return body
    card = ('<aside class="midcard"><img src="%s" alt="GlutaNex Glutathione Night Cream 30 g" width="80" height="80" loading="lazy"><div><b>Try it: GlutaNex Night Cream</b>'
            '<span>Glutathione + niacinamide + vitamin C · 30 g · %s · free shipping · COD</span></div><a class="btn sm" href="%s">View</a></aside>') % (im('cream-square'), rs(BYID['cream']['price']), url(BYID['cream']))
    k = idx[len(idx) // 2]
    return body[:k] + card + body[k:]


def tldr_box(slug, src=None, label='Key takeaways'):
    pts = (src if src is not None else TLDR).get(slug)
    if not pts:
        return ''
    return '<div class="tldr"><b>%s</b><ul>%s</ul></div>' % (label, ''.join('<li>%s</li>' % html.escape(x) for x in pts))


def faq_block(items, head='Frequently asked questions'):
    return '<h2 id="faq">%s</h2>' % head + faq_html(items) if items else ''


def sources_block(refs, head='Sources'):
    if not refs:
        return ''
    return '<div class="sources"><b>%s</b><ol>%s</ol></div>' % (head, ''.join('<li>%s</li>' % html.escape(SOURCES[r]) for r in refs if r in SOURCES))


def hreflang_cluster(en_path):
    alts = [('en-IN', en_path)]
    if en_path in EN2HI:
        alts.append(('hi-IN', EN2HI[en_path]))
    if en_path in EN2HL:
        alts.append(('hi-Latn', EN2HL[en_path]))
    alts += [(r['code'], '/%s/%s/' % (r['lang'], r['slug'])) for r in REG if en_path == '/glutathione-cream/']
    if len(alts) < 2:
        return ''
    return ''.join('<link rel="alternate" hreflang="%s" href="%s%s">\n' % (c, SITE, u) for c, u in alts) + '<link rel="alternate" hreflang="x-default" href="%s%s">\n' % (SITE, en_path)


def hreflang(en_path, hi_path):
    return ('<link rel="alternate" hreflang="en-IN" href="%s%s">\n<link rel="alternate" hreflang="hi-IN" href="%s%s">\n'
            '<link rel="alternate" hreflang="x-default" href="%s%s">\n') % (SITE, en_path, SITE, hi_path, SITE, en_path)



def gcard(g):
    keys = ' '.join([g['title'], g['blurb'], g.get('short', '')] + [q for q, a, d in g.get('qa', [])] + [q for q, a in g.get('faq', [])])
    return '<a class="reveal" href="%s" data-k="%s"><span class="eyebrow">Guide</span><h3>%s</h3><p>%s</p></a>' % (guide_url(g), html.escape(re.sub(r'<[^>]+>', '', keys).lower()), g['title'], g['blurb'])
hub = top('Glutathione guides', 'Everything about <span class="gold">glutathione</span>', 'Plain, accurate guides on glutathione for skin: what it does, how to use it, and how to stay safe.') + \
    '<section style="padding-top:30px"><div class="wrap"><div class="gsearch"><input type="search" id="guide-search" placeholder="Search guides: side effects, tablets, price, men, pregnancy…" aria-label="Search glutathione guides"><p class="muted" id="guide-count" aria-live="polite"></p></div><a class="pillar-card reveal" href="/glutathione/"><span class="eyebrow">Start here</span><h2>%s</h2><p>%s</p><span class="btn sm">Read the complete guide</span></a>' \
    '<div class="guides" style="margin-top:22px">%s</div>' \
    '<div class="sec-h" style="margin-top:48px"><span class="eyebrow">हिंदी में पढ़ें</span><h2>Hindi guides</h2></div><div class="guides">%s</div>' \
    '<p class="note">These guides are general information about cosmetic skincare and do not replace advice from a dermatologist.</p></div></section>' % (
        PILLAR['title'], PILLAR['blurb'], ''.join(gcard(g) for g in GUIDES[1:]),
        ''.join('<a class="reveal" href="/hi/%s/" lang="hi"><span class="eyebrow">हिंदी</span><h3>%s</h3><p>%s</p></a>' % (h['slug'], h['title'], h['desc'].split(':')[0]) for h in HI))
page('/glutathione-guides/', 'Glutathione Guides: Benefits, Side Effects, Price, Use | GlutaNex', 'All GlutaNex glutathione guides: what glutathione is, benefits for skin, side effects, price in India, face wash, kojic acid, foods and Hindi guides.',
     hub, crumbs=[('Glutathione guides', '/glutathione-guides/')], ptype='CollectionPage', schema=[{'@type': 'ItemList', 'itemListElement': [{'@type': 'ListItem', 'position': i + 1, 'url': SITE + guide_url(g), 'name': g['title']} for i, g in enumerate(GUIDES)]}])

RELATED = {'glutathione': ['glutathione-cream-questions', 'glutathione-cream', 'is-glutathione-safe-for-skin'], 'glutathione-cream-questions': ['glutathione', 'retinol-vs-glutathione', 'glutathione-night-cream']}
RELATED.update(RELATED_MORE)
for i, g in enumerate(GUIDES):
    if g['slug'] in RELATED:
        more = sorted([x for x in GUIDES if x['slug'] in RELATED[g['slug']]], key=lambda x: RELATED[g['slug']].index(x['slug']))
    else:
        more = [GUIDES[0]] + [GUIDES[(i + j) % len(GUIDES)] for j in (1, 2) if GUIDES[(i + j) % len(GUIDES)]['slug'] != 'glutathione']
        more = more[:3]
    faq = [(q % P, a % P) for q, a in g.get('faq', [])]
    body = top('Glutathione guide', g['title'], g['blurb']) + \
        '<section style="padding-top:22px"><div class="wrap article"><div class="prose"><p class="byline">By the GlutaNex team · Updated 11 October 2026 · %d sources cited</p>%s%s%s<p class="note">General information about cosmetic skincare, not medical advice. Results vary from person to person. See a dermatologist for persistent or changing pigmentation.</p></div>' \
        '<aside class="side-cta"><img src="%s" alt="GlutaNex Glutathione Night Cream" width="800" height="800" loading="lazy"><b>GlutaNex Night Cream</b><span>Glutathione + niacinamide + vitamin C · %s · Cash on Delivery</span><button class="btn block" type="button" data-buy="cream">Buy now</button><a class="btn ghost block sm" href="%s">View product</a></aside></div></section>' \
        '<section style="padding-top:10px"><div class="wrap"><div class="sec-h"><span class="eyebrow">Keep reading</span><h2>More glutathione guides</h2></div><div class="guides">%s</div></div></section>' % (
            len(g['refs']), mid_card(g['slug'], tldr_box(g['slug']) + with_toc(g['body'] % P)), faq_block(faq), sources_block(g['refs']), im('cream-square'), rs(BYID['cream']['price']), url(BYID['cream']),
            ''.join(gcard(m) for m in more))
    sch = [{'@type': 'Article', 'headline': g['title'], 'description': g['desc'], 'datePublished': TODAY, 'dateModified': TODAY, 'mainEntityOfPage': SITE + guide_url(g),
            'author': {'@id': SITE + '/#org'}, 'publisher': {'@id': SITE + '/#org'}, 'image': SITE + im('cream-square', 'jpg'), 'inLanguage': 'en-IN',
            'about': GSH_THING,
            'citation': [{'@type': 'CreativeWork', 'name': SOURCES[r], 'url': re.search(r'href="([^"]+)"', (REFS.get(r) or (FDA if r == 'fda' else ''))).group(1)} for r in g['refs'] if r in SOURCES and re.search(r'href="([^"]+)"', (REFS.get(r) or (FDA if r == 'fda' else '')))],
            'speakable': {'@type': 'SpeakableSpecification', 'cssSelector': ['.tldr', '.answer']}}]
    if g['slug'] == 'how-to-use-glutathione-cream':
        sch.append({'@type': 'HowTo', '@id': SITE + guide_url(g) + '#howto', 'name': 'How to use glutathione cream at night', 'inLanguage': 'en-IN', 'totalTime': 'PT3M',
                    'supply': [{'@type': 'HowToSupply', 'name': 'Gentle face wash'}, {'@type': 'HowToSupply', 'name': 'Glutathione night cream'}, {'@type': 'HowToSupply', 'name': 'Sunscreen SPF 30 or higher'}],
                    'step': [{'@type': 'HowToStep', 'position': i + 1, 'name': n, 'text': t} for i, (n, t) in enumerate([
                        ('Cleanse', 'Wash your face with a gentle face wash and pat it dry.'),
                        ('Take a pea-sized amount', 'Dot a pea-sized amount of glutathione cream on the forehead, cheeks, chin and neck.'),
                        ('Spread thinly', 'Spread it in thin, upward strokes, avoiding the eyes and lips.'),
                        ('Start slowly', 'If the cream has retinol, use it 2 to 3 nights a week for the first two weeks, then build up.'),
                        ('Sunscreen every morning', 'Every morning, apply SPF 30 or higher sunscreen and reapply when outdoors.')])]})
    if g['slug'] == 'glutathione-skincare-glossary':
        sch.append({'@type': 'DefinedTermSet', '@id': SITE + guide_url(g) + '#terms', 'name': 'Glutathione skincare glossary', 'inLanguage': 'en-IN',
                    'hasDefinedTerm': [{'@type': 'DefinedTerm', 'name': t, 'description': d, 'url': SITE + guide_url(g) + '#' + re.sub(r'[^a-z0-9]+', '-', t.lower()).strip('-')} for t, d, u in GLOSSARY]})
    if g.get('faq_ld'):
        sch.append(faq_ld([(q % P, re.sub(r'<[^>]+>', '', a % P)) for q, a in g['faq_ld']]))
    elif faq:
        sch.append(faq_ld([(q, re.sub(r'<[^>]+>', '', a)) for q, a in faq]))
    hp = EN2HI.get(guide_url(g))
    page(guide_url(g), g['seo'], g['desc'], body, og='article', crumbs=[('Glutathione guides', '/glutathione-guides/'), (g['short'], guide_url(g))], schema=sch,
         extra=hreflang_cluster(guide_url(g)))

# ---------------- Hindi pages ----------------
for h in HI:
    path = '/hi/%s/' % h['slug']
    _qa = HI_QA.get(h['slug'], [])
    if _qa and not h.get('_qa_done'):
        h['body'] = ''.join('<h2>%s</h2><p class="answer">%s</p>%s' % (q, a, d) for q, a, d in _qa) + h['body']
        h['_qa_done'] = True
    faq = [(q % P, a % P) for q, a in h['faq']]
    _qa_ld = [(q % P, re.sub(r'<[^>]+>', '', a % P)) for q, a, d in _qa]
    body = top('हिंदी गाइड', h['title'], h['desc'].split(':', 1)[-1].strip()) + \
        '<section style="padding-top:22px"><div class="wrap article"><div class="prose" lang="hi"><p class="byline">GlutaNex टीम द्वारा · अपडेट: 11 अक्टूबर 2026 · <a href="%s" lang="en">Read in English</a></p>%s%s%s<p class="note">यह सामान्य कॉस्मेटिक स्किनकेयर जानकारी है, चिकित्सा सलाह नहीं। परिणाम हर व्यक्ति में अलग हो सकते हैं।</p></div>' \
        '<aside class="side-cta"><img src="%s" alt="GlutaNex Glutathione Night Cream" width="800" height="800" loading="lazy"><b>GlutaNex Night Cream</b><span>ग्लूटाथियोन नाइट क्रीम · %s · कैश ऑन डिलीवरी</span><button class="btn block" type="button" data-buy="cream">अभी खरीदें</button></aside></div></section>' \
        '<section style="padding-top:10px"><div class="wrap"><div class="sec-h"><h2>और पढ़ें</h2></div><div class="guides">%s</div></div></section>' % (
            h['en'], tldr_box(h['slug'], TLDR_HI, 'मुख्य बातें') + with_toc(h['body'] % P, 'इस पेज पर'), faq_block(faq, 'अक्सर पूछे जाने वाले सवाल'), sources_block(['study', 'ijdvl', 'fda'], 'स्रोत'),
            im('cream-square'), rs(BYID['cream']['price']),
            ''.join('<a href="/hi/%s/" lang="hi"><span class="eyebrow">हिंदी</span><h3>%s</h3></a>' % (x['slug'], x['title']) for x in HI if x is not h) +
            '<a href="/glutathione/"><span class="eyebrow">English</span><h3>Glutathione: the complete guide</h3></a>')
    page(path, h['seo'], h['desc'], body, og='article', lang='hi-IN', crumbs=[('हिंदी गाइड', '/hi/'), (h['short'], path)], extra=hreflang_cluster(h['en']),
         schema=[{'@type': 'Article', 'headline': h['title'], 'description': h['desc'], 'datePublished': TODAY, 'dateModified': TODAY, 'mainEntityOfPage': SITE + path,
                  'author': {'@id': SITE + '/#org'}, 'publisher': {'@id': SITE + '/#org'}, 'image': SITE + im('cream-square', 'jpg'), 'inLanguage': 'hi-IN', 'about': GSH_THING},
                 faq_ld(_qa_ld + faq)])
page('/hi/', 'Glutathione Hindi Guide: ग्लूटाथियोन की जानकारी हिंदी में', 'ग्लूटाथियोन की जानकारी हिंदी में: ग्लूटाथियोन क्रीम के फायदे, नुकसान और लगाने का सही तरीका।',
     top('हिंदी गाइड', 'ग्लूटाथियोन की जानकारी <span class="gold">हिंदी में</span>', 'आसान और सही जानकारी: फायदे, नुकसान और उपयोग का तरीका।') +
     '<section style="padding-top:30px"><div class="wrap" lang="hi"><div class="guides">%s</div></div></section>' % ''.join(
         '<a class="reveal" href="/hi/%s/"><span class="eyebrow">गाइड</span><h3>%s</h3><p>%s</p></a>' % (x['slug'], x['title'], x['desc'].split(':', 1)[-1].strip()) for x in HI),
     lang='hi-IN', crumbs=[('हिंदी गाइड', '/hi/')])

# ---------------- Hinglish pages (Hindi in English letters) ----------------
for h in HL:
    path = '/hinglish/%s/' % h['slug']
    u = HL_UI
    qa_html = ''.join('<h2>%s</h2><p class="answer">%s</p>%s' % (q, a, d) for q, a, d in h['qa'])
    strip = lambda t: re.sub(r'<[^>]+>', '', t % P)
    ld_qa = [(q, strip(a)) for q, a, d in h['qa']] + [(q, strip(a)) for q, a in h['faq']]
    hi_link = (' · <a href="%s" lang="hi">हिंदी में पढ़ें</a>' % EN2HI[h['en']]) if h['en'] in EN2HI else ''
    body = top(u['hub'], h['title'], h['desc'].split(':', 1)[0]) + \
        '<section style="padding-top:22px"><div class="wrap article"><div class="prose"><p class="byline">%s · <a href="%s" lang="en-IN">Read in English</a>%s</p>%s%s%s<p class="note">%s</p></div>' \
        '<aside class="side-cta"><img src="%s" alt="GlutaNex Glutathione Night Cream" width="800" height="800" loading="lazy"><b>GlutaNex Night Cream</b><span>Glutathione night cream · %s · Cash on Delivery</span><button class="btn block" type="button" data-buy="cream">%s</button></aside></div></section>' \
        '<section style="padding-top:10px"><div class="wrap"><div class="sec-h"><h2>%s</h2></div><div class="guides">%s</div></div></section>' % (
            u['by'], h['en'], hi_link, tldr_box(h['slug'], TLDR_HL, 'Mukhya baatein') + with_toc((qa_html + h['body']) % P, u['toc']), faq_block([(q, a % P) for q, a in h['faq']], u['faq']),
            sources_block(['study', 'fda'], u['src']), u['note'], im('cream-square'), rs(BYID['cream']['price']), u['buy'], u['more'],
            ''.join('<a href="/hinglish/%s/"><span class="eyebrow">Hinglish</span><h3>%s</h3></a>' % (x['slug'], x['title']) for x in HL if x is not h))
    page(path, h['seo'], h['desc'], body, og='article', lang='hi-Latn', crumbs=[(u['hub'], '/hinglish/'), (h['short'], path)], extra=hreflang_cluster(h['en']),
         schema=[{'@type': 'Article', 'headline': h['title'], 'description': h['desc'], 'datePublished': TODAY, 'dateModified': TODAY, 'mainEntityOfPage': SITE + path,
                  'author': {'@id': SITE + '/#org'}, 'publisher': {'@id': SITE + '/#org'}, 'image': SITE + im('cream-square', 'jpg'), 'inLanguage': 'hi-Latn', 'about': GSH_THING,
                  'speakable': {'@type': 'SpeakableSpecification', 'cssSelector': ['.answer']}},
                 faq_ld(ld_qa)])
page('/hinglish/', 'Glutathione Ki Jaankari Hinglish Mein: Fayde, Nuksan, Use',
     'Glutathione ki poori jaankari aasan Hinglish mein: glutathione kya hai, cream ke fayde, nuksan, kaise lagaye, tablet, injection aur price.',
     top('Hinglish guides', 'Glutathione ki jaankari <span class="gold">Hinglish mein</span>', 'Aasan bhasha mein sach aur kaam ki baatein.') +
     '<section style="padding-top:30px"><div class="wrap"><div class="guides">%s</div></div></section>' % ''.join(
         '<a class="reveal" href="/hinglish/%s/"><span class="eyebrow">Guide</span><h3>%s</h3><p>%s</p></a>' % (x['slug'], x['title'], html.escape(x['desc'].split(':', 1)[0])) for x in HL),
     lang='hi-Latn', crumbs=[('Hinglish guides', '/hinglish/')])

# ---------------- Regional language pages ----------------
for r in REG:
    path = '/%s/%s/' % (r['lang'], r['slug'])
    u = r['ui']
    body = top(u['guide'], r['title'], r['desc'].split(':', 1)[-1].strip()) + \
        '<section style="padding-top:22px"><div class="wrap article"><div class="prose"><p class="byline">%s · <a href="/glutathione-cream/" lang="en">%s</a></p>%s%s<p class="note">%s</p></div>' \
        '<aside class="side-cta"><img src="%s" alt="GlutaNex Glutathione Night Cream" width="800" height="800" loading="lazy"><b>GlutaNex Night Cream</b><span>%s · COD</span><button class="btn block" type="button" data-buy="cream">%s</button></aside></div></section>' % (
            u['by'], u['en'], with_toc(r['body'], u['toc']), faq_block(r['faq'], u['faq']), u['note'], im('cream-square'), rs(BYID['cream']['price']), u['buy'])
    page(path, r['seo'], r['desc'], body, og='article', lang=r['code'], crumbs=[(u['guide'], path)], extra=hreflang_cluster('/glutathione-cream/'),
         schema=[{'@type': 'Article', 'headline': r['title'], 'description': r['desc'], 'datePublished': TODAY, 'dateModified': TODAY, 'mainEntityOfPage': SITE + path,
                  'author': {'@id': SITE + '/#org'}, 'publisher': {'@id': SITE + '/#org'}, 'image': SITE + im('cream-square', 'jpg'), 'inLanguage': r['code'], 'about': GSH_THING}, faq_ld(r['faq'])])

# ---------------- Information pages ----------------
page('/about/', 'About GlutaNex | Glutathione Skincare', 'About GlutaNex: glutathione skincare for a simple night routine, sold and shipped by %s.' % OWNER,
     top('About', 'About <span class="gold">GlutaNex</span>', 'Glutathione skincare for a simple, consistent night routine.') + '''<section style="padding-top:24px"><div class="wrap prose">
<p>GlutaNex makes glutathione skincare for people who want a short routine they can keep: a gentle face wash and a night cream, with sunscreen in the morning.</p>
<h2>What we believe</h2><ul><li><b>Honest claims.</b> Glutathione works gradually and does not change your natural skin colour. We say so.</li><li><b>Clear information.</b> Full ingredient lists, clear prices, no hidden charges.</li><li><b>Safety first.</b> We recommend creams, not injections, and we explain why.</li></ul>
<h2>Who we are</h2><p>GlutaNex products on this website are sold and shipped by %s, %s. You can reach us on WhatsApp at %s. See the official <a href="/glutanex/">GlutaNex brand facts</a>.</p>
<p style="margin-top:24px"><a class="btn" href="/shop/">Shop GlutaNex</a></p></div></section>''' % (OWNER, ADDR, WA_SHOW), crumbs=[('About', '/about/')])

# brand facts page: the page for searches of the brand name itself, so search engines and AI tools get one clear, official answer
_BRAND_FAQ = [('Is GlutaNex an Indian brand?', 'Yes. GlutaNex is an Indian skincare brand from %s, based in Bhatkal, Karnataka.' % OWNER),
              ('What is the official GlutaNex website?', 'The official website is glutanex.co.in. GlutaNex is also sold on Amazon, Flipkart and Myntra, and the official listings are linked on this page.'),
              ('What products does GlutaNex make?', 'GlutaNex makes a Glutathione Night Cream (30 g), a Gluta Boost Face Wash (100 ml) and the Glow Duo, which combines both.'),
              ('How do I know my GlutaNex product is genuine?', 'Buy from glutanex.co.in or the official marketplace listings linked on this page, check that the pack is sealed and the name reads GlutaNex, and send us a photo on WhatsApp if you are unsure.'),
              ('Does GlutaNex sell glutathione injections or tablets?', 'No. GlutaNex makes only skincare you apply to the skin: a Night Cream and a Face Wash. Glutanex glutathione injections and tablets from Korea, sometimes sold online in India, are made by other companies and are not GlutaNex products.'),
              ('Is GlutaNex the same as the Korean brand Glutanex?', 'GlutaNex (India, glutanex.co.in) makes only skincare you apply to the skin. It does not make or sell glutathione injections, drips or tablets. GlutaNex is an Indian brand. "Glutanex" products from Korea, including glutathione injections, tablets and skincare sold online in India, are made by other companies and are not connected with GlutaNex India.')]
_bp_rows = ''.join('<tr><td>%s</td><td>%s</td></tr>' % r for r in [
    ('Brand', 'GlutaNex'), ('Company', OWNER), ('Based in', 'Bhatkal, Uttara Kannada, Karnataka, India'),
    ('Products', ', '.join('<a href="%s">%s</a> (%s, %s)' % (url(x), html.escape(x['short']), html.escape(x['size']), rs(x['price'])) for x in PRODUCTS)),
    ('Key ingredient', '<a href="/glutathione/">Glutathione</a>, with niacinamide, vitamin C and hyaluronic acid'),
    ('Official website', '<a href="/">glutanex.co.in</a>'), ('Instagram', '<a href="%s" target="_blank" rel="noopener">@glutanexofficial</a>' % INSTAGRAM),
    ('Customer support', 'WhatsApp %s, Monday to Saturday, 10 am to 7 pm' % WA_SHOW)])
_bp_mkts = ''.join('<li><a href="%s" target="_blank" rel="noopener">GlutaNex on %s</a></li>' % (html.escape(u), n) for n, u in MARKET_LINKS)
page('/glutanex/', 'GlutaNex: Official Brand Information | Glutathione Skincare India',
     'Official facts about GlutaNex, the Indian glutathione skincare brand: who makes it, products and prices, official website and marketplaces, and how to buy genuine.',
     top('Brand facts', '<span class="gold">GlutaNex</span>: official brand information', 'Who we are, what we make and where to buy genuine GlutaNex.') + """<section style="padding-top:24px"><div class="wrap prose">
<p class="answer"><b>GlutaNex</b> is an Indian glutathione skincare brand from %s, Bhatkal, Karnataka. It makes a Glutathione Night Cream and a Gluta Boost Face Wash, sold on its official website glutanex.co.in and on Amazon, Flipkart and Myntra.</p>
<h2>GlutaNex at a glance</h2><div class="tbl"><table class="facts"><tbody>%s</tbody></table></div>
<h2>Where to buy genuine GlutaNex</h2><ul><li><a href="/shop/">glutanex.co.in</a>: free shipping and Cash on Delivery across India</li>%s</ul>
<h2>How to check your product is genuine</h2><ul><li>Buy from this website or the official listings above.</li><li>The pack should be sealed, and the name should read <b>GlutaNex</b>.</li><li>Not sure? Send a photo of the pack to us on WhatsApp at %s and we will check it.</li></ul>
<h2>GlutaNex (India) is not the Korean Glutanex</h2><p>GlutaNex (India, glutanex.co.in) makes only skincare you apply to the skin. It does not make or sell glutathione injections, drips or tablets. GlutaNex is an Indian brand. "Glutanex" products from Korea, including glutathione injections, tablets and skincare sold online in India, are made by other companies and are not connected with GlutaNex India. We advise against glutathione injections for skin lightening: read <a href="/glutathione-cream-vs-tablets-vs-injections/">cream vs tablets vs injections</a>. If a product is not listed on this page, we cannot vouch for it.</p>
<h2>What we stand for</h2><p>Honest claims: glutathione works gradually and does not change natural skin colour, and we do not recommend injections. Read <a href="/our-standards/">our standards</a> and <a href="/about/">about us</a>.</p>
</div></section>""" % (OWNER, _bp_rows, _bp_mkts, WA_SHOW) + faq_block(_BRAND_FAQ),
     crumbs=[('GlutaNex', '/glutanex/')],
     schema=[{'@type': 'AboutPage', '@id': SITE + '/glutanex/#page', 'url': SITE + '/glutanex/', 'name': 'GlutaNex: official brand information',
              'mainEntity': {'@id': SITE + '/#org'}, 'about': {'@id': SITE + '/#brand'}, 'speakable': {'@type': 'SpeakableSpecification', 'cssSelector': ['.answer']}},
             faq_ld(_BRAND_FAQ)])

page('/image-licence/', 'GlutaNex Image Licence: Using Our Glutathione Cream Photos', 'How you may use GlutaNex product photos: free for reviews, press and authorised sellers with credit to GlutaNex; other uses need permission.',
     top('Image licence', 'Using <span class="gold">GlutaNex</span> photos', 'Product photos on this website belong to GlutaNex.') + """<section style="padding-top:24px"><div class="wrap prose">
<p class="answer">GlutaNex product photos are © 2026 GlutaNex (%s). You may use them free of charge for product reviews, news and press, and for selling genuine GlutaNex products, as long as you credit <b>GlutaNex</b> and link to glutanex.co.in where possible.</p>
<h2>Allowed with credit</h2><ul><li>Reviews, blog posts, news and press articles about GlutaNex</li><li>Listings by authorised sellers of genuine GlutaNex products</li><li>Social media posts about GlutaNex products</li></ul>
<h2>Not allowed</h2><ul><li>Editing the photos to change the product, its label or its claims</li><li>Using them for other brands, look-alike or fake products</li><li>Using them to suggest GlutaNex endorses something it does not</li></ul>
<h2>How to credit</h2><p>Write <b>Photo: GlutaNex</b>, with a link to <a href="/">glutanex.co.in</a> where you can.</p>
<h2>Other uses</h2><p>For any other use, ask us first on WhatsApp at %s.</p>
</div></section>""" % (OWNER, WA_SHOW), crumbs=[('Image licence', '/image-licence/')])

page('/contact/', 'Contact GlutaNex | WhatsApp Support', 'Contact GlutaNex on WhatsApp at %s for help with orders, delivery and products.' % WA_SHOW,
     top('Contact', 'Contact us', 'The fastest way to reach us is WhatsApp.') + '''<section style="padding-top:24px"><div class="wrap prose">
<p><a class="btn wa" href="https://wa.me/%s" target="_blank" rel="noopener">%s Chat on WhatsApp</a></p>
<h2>Details</h2><ul><li><b>Instagram:</b> <a href="https://www.instagram.com/glutanexofficial/" rel="noopener">@glutanexofficial</a></li><li><b>WhatsApp and phone:</b> %s</li><li><b>Seller:</b> %s</li><li><b>Address:</b> %s</li><li><b>Hours:</b> Monday to Saturday, 10 am to 7 pm</li></ul>
<p>Please share your order number or the mobile number used on the order. You can also check your parcel on the <a href="/track-order/">Track Order</a> page.</p></div></section>''' % (WA, WA_IMG, WA_SHOW, OWNER, ADDR), crumbs=[('Contact', '/contact/')], ptype='ContactPage')

page('/our-standards/', 'Our Standards: How GlutaNex Writes and Sells | GlutaNex', 'How GlutaNex writes its glutathione guides, checks facts, makes claims and sells its products: cited research, honest claims, clear labels and easy returns.',
     top('Our standards', 'Our <span class="gold">standards</span>', 'How we write about glutathione, what we will and will not claim, and how we sell.') + '''<section style="padding-top:24px"><div class="wrap prose">
<h2>How we write our guides</h2><ul><li><b>Research first.</b> Claims about glutathione are based on published studies and dermatology reviews, which we cite and list as sources at the end of each guide.</li><li><b>Plain language.</b> We explain what studies found, including their limits, such as small size or short duration.</li><li><b>Kept up to date.</b> Each guide shows when it was last updated. When new research changes the picture, we update the page.</li><li><b>General information.</b> Our guides are cosmetic skincare information, not medical advice. For skin conditions, pregnancy or reactions, we always point readers to a doctor or dermatologist.</li></ul>
<h2>What we will and will not claim</h2><ul><li>We say glutathione can help skin look <b>brighter and more even</b> over weeks, with sunscreen.</li><li>We do <b>not</b> claim it changes natural skin colour, works overnight, or treats any disease.</li><li>We do <b>not</b> recommend glutathione injections for skin lightening, and we explain why.</li><li>We do <b>not</b> publish fake reviews, ratings, before-and-after photos or customer numbers.</li></ul>
<h2>How we sell</h2><ul><li><b>Clear prices.</b> The price shown includes taxes, with free shipping and no hidden charges.</li><li><b>Full ingredient lists</b> printed on every pack, and the key ingredients listed on each product page.</li><li><b>Sealed packs</b> with batch number and expiry date.</li><li><b>Easy returns</b> on sealed products within 7 days, and replacements for damaged items. See our <a href="/refund-policy/">returns policy</a>.</li><li><b>Real people.</b> GlutaNex is sold by %s, %s. Reach us on WhatsApp at %s or on <a href="https://www.instagram.com/glutanexofficial/" rel="noopener">Instagram</a>.</li></ul>
<h2>Spotted a mistake?</h2><p>If anything on our site looks wrong or out of date, message us on WhatsApp and we will check and correct it.</p></div></section>''' % (OWNER, ADDR, WA_SHOW), crumbs=[('Our standards', '/our-standards/')])

FAQ_ALL = HOME_FAQ + [
    ('What is the price of GlutaNex Glutathione Night Cream?', 'The Night Cream is %s, the Gluta Boost Face Wash is %s and the Glow Duo is %s. Prices include taxes and shipping is free.' % (rs(BYID['cream']['price']), rs(BYID['wash']['price']), rs(BYID['duo']['price']))),
    ('How long does delivery take?', 'Orders are packed in 1 to 2 business days and usually delivered in 3 to 7 business days after dispatch.'),
    ('Can I return a product?', 'Sealed, unopened products can be returned within 7 days of delivery. Damaged or wrong items are replaced or refunded in full. See the <a href="/refund-policy/">returns policy</a>.'),
    ('Can men use GlutaNex?', 'Yes. GlutaNex products are for anyone who wants a simple night skincare routine.'),
    ('Is it safe during pregnancy?', 'Ask your doctor before using any new skincare product during pregnancy or breastfeeding.'),
]
page('/faq/', 'GlutaNex FAQ | Glutathione Cream Questions', 'Answers about GlutaNex glutathione cream and face wash: how to use, results, safety, price, delivery, Cash on Delivery and returns.',
     top('FAQ', 'Questions, answered') + '<section style="padding-top:24px"><div class="wrap">%s</div></section>' % faq_html(FAQ_ALL), crumbs=[('FAQ', '/faq/')], schema=[faq_ld(FAQ_ALL)])

page('/track-order/', 'Track Your Order | GlutaNex', 'Track your GlutaNex order with your mobile number and pincode, your order number, payment ID or tracking number.',
     top('Track order', 'Track your order', 'Use the mobile number and pincode from your order, or your order number, payment ID or tracking number.') + '''<section style="padding-top:20px"><div class="wrap track">
<form class="form" id="track-form" novalidate>
  <div class="track-by"><button type="button" id="by-phone" class="on">Mobile number</button><button type="button" id="by-id">Payment ID / AWB</button></div>
  <div id="by-phone-box" class="form"><div class="f"><label for="t-phone">Mobile number</label><input id="t-phone" type="tel" inputmode="numeric" maxlength="16"></div><div class="f"><label for="t-pin">Delivery pincode</label><input id="t-pin" inputmode="numeric" maxlength="6"></div></div>
  <div id="by-id-box" class="form" hidden><div class="f"><label for="t-id">Order number, payment ID or tracking number</label><input id="t-id" autocomplete="off" placeholder="GX12345678 or pay_XXXXXXXXXXXX"></div></div>
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
<h2>Orders</h2><p>An online order is confirmed when the payment succeeds. A Cash on Delivery order is confirmed when it is placed. If we cannot fulfil an order, we refund any amount paid in full.</p>
<h2>Cash on Delivery</h2><p>Cash on Delivery orders need nothing paid in advance: you pay the full amount in cash to the courier when the parcel arrives. There is no Cash on Delivery fee. Cash on Delivery is available for pincodes our courier serves for it.</p>
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
        body % dict(o=OWNER, biz=BIZ)), crumbs=[(h, path)])

page('/404', 'Page not found | GlutaNex', 'This page could not be found.', top('404', 'Page not found', 'The link may be old or mistyped.') + '<section style="padding-top:20px"><div class="wrap"><a class="btn" href="/shop/">Go to the shop</a></div></section>', index=False)
