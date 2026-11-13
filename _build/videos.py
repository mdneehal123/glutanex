# GlutaNex videos: one watch page each under /videos/<slug>/ (video is the main content, so Google can index it),
# a /videos/ hub, a video sitemap, and the same video embedded on the product/guide pages listed in 'on'.
# Honesty: the person in the AI videos is an AI-generated model, not a customer. Say so on every page that shows one.
# No before/after, no results claims. Night-only + retinol rules stay as on the rest of the site.

AI_NOTE = ('Made with AI tools: the woman shown is an AI-generated model, not a customer, and the scenes were created from photos of the real GlutaNex jar. '
           'It shows how the cream is used, not results.')
REAL_NOTE = 'Real footage of GlutaNex Night Cream jars from a fresh batch, filmed by the GlutaNex team.'

VIDEOS = [
    dict(slug='glutanex-night-cream-night-routine', dur='PT32S', secs=32,
         name='GlutaNex Night Cream: a simple night routine (32 sec)',
         seo='GlutaNex Night Cream Night Routine Video (32 sec)',
         desc='Watch a 32-second night routine with GlutaNex Glutathione Night Cream: the texture, how much to use, how to blend it in and when to apply it.',
         ai=True, on=['/how-to-use-glutathione-cream/', '/product/glutanex-glutathione-night-cream/'],
         transcript=['Let me show you my night ritual.', 'Meet GlutaNex night cream.', 'Look at this texture. Rich, creamy, and never greasy.',
                     'A little goes a long way. It blends in fast, and feels so light.', 'I put it on before bed, then lights off, and off to sleep.',
                     'Your skin deserves this. Get yours on glutanex.co.in.'],
         about='''<p>This short video walks through where GlutaNex Night Cream fits in an evening routine: open the jar, take a small amount on a clean fingertip, dab it on the cheeks, forehead and chin, and blend it in with light circular motions. Let it absorb, and go to bed.</p>
<p>Two things the video does not show, but you should know: the cream contains retinol and salicylic acid, so it is for night use only, and it is best to start on 2 to 3 nights a week while your skin gets used to it. Use sunscreen every morning. The full steps are in <a href="/how-to-use-glutathione-cream/">how to use glutathione cream</a>, and the timing question is answered in <a href="/glutathione-cream-morning-or-night/">glutathione cream: morning or night?</a></p>''',
         links=[('/how-to-use-glutathione-cream/', 'How to use glutathione cream'), ('/glutathione-night-cream/', 'Glutathione night cream guide'),
                ('/can-i-use-glutathione-cream-daily/', 'Can I use glutathione cream daily?')]),
    dict(slug='glutanex-night-cream-3-key-ingredients', dur='PT22S', secs=22,
         name='3 ingredients to check in a night cream: GlutaNex (22 sec)',
         seo='3 Night Cream Ingredients to Check (Video)',
         desc='A 22-second video on three ingredient groups to look for in a glutathione night cream: glutathione with vitamin C, niacinamide, and hyaluronic acid with ceramides.',
         ai=True, on=['/glutathione-cream-ingredients/'],
         transcript=['Three things I check in every night cream.', 'One. Glutathione and vitamin C, for a brighter-looking glow.',
                     'Two. Niacinamide, for a more even-looking tone.', 'Three. Hyaluronic acid and ceramides, for soft, hydrated skin.',
                     'GlutaNex has all of them, in one jar. Get yours on glutanex.co.in.'],
         about='''<p>The video picks three of the eleven ingredients in GlutaNex Night Cream and says, in one line each, what they are used for in skincare. Glutathione and vitamin C are antioxidants used for a brighter-looking glow. Niacinamide (vitamin B3) is used for a more even-looking tone. Hyaluronic acid and ceramides help skin hold water and feel soft.</p>
<p>The cream also contains retinol, salicylic acid, peptides, aloe vera, turmeric and neem extracts. Because of the retinol and salicylic acid it is a night-only cream. Ingredient percentages are not published. Read the full list and what each one does in <a href="/glutathione-cream-ingredients/">glutathione cream ingredients</a>, or see how two of them work together in <a href="/glutathione-and-niacinamide/">glutathione and niacinamide</a>.</p>''',
         links=[('/glutathione-cream-ingredients/', 'Glutathione cream ingredients'), ('/glutathione-and-niacinamide/', 'Glutathione and niacinamide'),
                ('/glutathione-and-hyaluronic-acid/', 'Glutathione and hyaluronic acid')]),
    dict(slug='glutanex-get-unready-with-me-night-routine', dur='PT17S', secs=17,
         name='Get unready with me: 5-step night routine with GlutaNex (17 sec)',
         seo='Get Unready With Me: 5-Step Night Routine Video',
         desc='A 17-second get-unready-with-me video: unbox, check the texture, blend GlutaNex Night Cream, and lights off. A calm 5-step night skincare routine.',
         ai=True, on=['/glutathione-night-cream/'],
         transcript=['(No speech. On-screen text.)', 'Get unready with me.', 'Step 1: unbox the good stuff.', 'Step 2: this texture though.',
                     'Step 3: blend. Zero grease.', 'Step 4: GlutaNex, every night.', 'Step 5: lights off. Sleep.'],
         about='''<p>A quick, music-only version of an evening routine. In real life the order is: cleanse with a gentle face wash, pat your face dry, apply a pea-sized amount of night cream to the face and neck, and sleep. In the morning, wash and use sunscreen.</p>
<p>The on-screen text says "every night", but if you are new to retinol, start on 2 to 3 nights a week and build up as your skin allows. More on this in the <a href="/glutathione-night-cream/">glutathione night cream guide</a> and <a href="/retinol-night-cream-for-beginners/">retinol night cream for beginners</a>.</p>''',
         links=[('/glutathione-night-cream/', 'Glutathione night cream guide'), ('/retinol-night-cream-for-beginners/', 'Retinol night cream for beginners'),
                ('/night-cream-vs-day-cream/', 'Night cream vs day cream')]),
    dict(slug='glutanex-night-cream-fresh-batch-texture', dur='PT13S', secs=13,
         name='GlutaNex Night Cream: fresh batch and real texture (13 sec)',
         seo='GlutaNex Night Cream Texture: Fresh Batch Video',
         desc='Real 13-second footage of a fresh batch of GlutaNex Night Cream jars, showing the light green cream texture up close before the jars are closed and packed.',
         ai=False, on=['/product/glutanex-glutathione-night-cream/', '/genuine-glutanex/'],
         transcript=['(No speech. Background music.)'],
         about='''<p>This is real footage of filled GlutaNex Night Cream jars before they are closed and packed. The cream is light green and soft, the colour you should see when you open a genuine jar.</p>
<p>If a jar you bought looks or smells very different, or the seal is broken, contact us on WhatsApp before using it. See <a href="/genuine-glutanex/">how to check a genuine GlutaNex jar</a> and <a href="/how-to-store-glutathione-cream/">how to store glutathione cream</a> so the texture stays as it should.</p>''',
         links=[('/genuine-glutanex/', 'Genuine GlutaNex'), ('/how-to-store-glutathione-cream/', 'How to store glutathione cream'),
                ('/how-to-spot-fake-glutathione-cream/', 'How to spot fake glutathione cream')]),
]
BYSLUG = {v['slug']: v for v in VIDEOS}
UPLOAD = '2026-11-13T18:00:00+05:30'


def vurl(v):
    return '/videos/%s/' % v['slug']


def video_ld(site, v, page_url):
    return {'@type': 'VideoObject', '@id': site + vurl(v) + '#video', 'name': v['name'], 'description': v['desc'],
            'thumbnailUrl': [site + '/assets/video/%s.jpg' % v['slug']], 'uploadDate': UPLOAD, 'duration': v['dur'],
            'contentUrl': site + '/assets/video/%s.mp4' % v['slug'], 'embedUrl': site + vurl(v), 'inLanguage': 'en-IN',
            'publisher': {'@id': site + '/#org'}, 'isFamilyFriendly': True,
            **({'transcript': ' '.join(t for t in v['transcript'] if not t.startswith('('))} if any(not t.startswith('(') for t in v['transcript']) else {})}


def player(v, lazy=True):
    return ('<video class="vid-el" controls playsinline preload="%s" poster="/assets/video/%s.jpg" width="360" height="640">'
            '<source src="/assets/video/%s.mp4" type="video/mp4"></video>') % ('none' if lazy else 'metadata', v['slug'], v['slug'])


def note(v):
    return AI_NOTE if v['ai'] else REAL_NOTE


def embed_block(slugs):
    """Supplementary video section for a product/guide page (the watch page is the canonical video page)."""
    items = ''.join('<figure class="vid-card">%s<figcaption><a href="%s">%s</a><span>%s</span></figcaption></figure>' % (
        player(BYSLUG[s]), vurl(BYSLUG[s]), BYSLUG[s]['name'], note(BYSLUG[s])) for s in slugs)
    return '<section class="vid-sec"><div class="wrap"><h2>Watch</h2><div class="vid-row">%s</div><p class="muted" style="font-size:.85rem"><a href="/videos/">All GlutaNex videos</a></p></div></section>' % items


EMBEDS = {}
for _v in VIDEOS:
    for _p in _v['on']:
        EMBEDS.setdefault(_p, []).append(_v['slug'])
