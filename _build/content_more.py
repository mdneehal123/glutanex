# Extra glutathione content: the pillar page, new guides, expansions for existing guides, and Hindi pages.
# Read by content.py with exec(). Bodies use %(name)s placeholders filled in content.py, so a literal percent sign is written %%.

REFS = dict(
    study='<a href="https://www.dovepress.com/skin-whitening-and-skin-condition-improving-effects-of-topical-oxidize-peer-reviewed-fulltext-article-CCID" rel="noopener">Watanabe et al., 2014</a>',
    oral='<a href="https://clinicaltrials.gov/study/NCT01016080" rel="noopener">Arjinpathana &amp; Asawanonda, 2012</a>',
    wesch='<a href="https://www.dovepress.com/glutathione-and-its-antiaging-and-antimelanogenic-effects-peer-reviewed-fulltext-article-CCID" rel="noopener">Weschawalit et al., 2017</a>',
    ijdvl='<a href="https://ijdvl.com/glutathione-as-a-skin-whitening-agent-facts-myths-evidence-and-controversies/" rel="noopener">Sonthalia, Daulatabad &amp; Sarkar, IJDVL 2016</a>',
    review='<a href="https://jcadonline.com/efficacy-safety-topical-glutathione/" rel="noopener">Khanna et al., J Clin Aesthet Dermatol 2025</a>',
)
SOURCES = {
    'study': 'Watanabe F, et al. Skin-whitening and skin-condition-improving effects of topical oxidized glutathione: a double-blind and placebo-controlled clinical trial in healthy women. Clin Cosmet Investig Dermatol. 2014.',
    'oral': 'Arjinpathana N, Asawanonda P. Glutathione as an oral whitening agent: a randomized, double-blind, placebo-controlled study. J Dermatolog Treat. 2012 (trial NCT01016080).',
    'wesch': 'Weschawalit S, Thongthip S, Phutrakool P, Asawanonda P. Glutathione and its antiaging and antimelanogenic effects. Clin Cosmet Investig Dermatol. 2017;10.',
    'ijdvl': 'Sonthalia S, Daulatabad D, Sarkar R. Glutathione as a skin whitening agent: facts, myths, evidence and controversies. Indian J Dermatol Venereol Leprol. 2016;82(3):262-272.',
    'review': 'Khanna R, Rambhia P, Chapas A. Systematic review of the efficacy and safety of topical glutathione in dermatology. J Clin Aesthet Dermatol. 2025;18(9):51-54.',
    'fda': 'US Food and Drug Administration warning on injectable skin-lightening products, 2015 (as reported by MedEsthetics).',
}

PILLAR = dict(
    slug='glutathione', title='Glutathione: what it is, what it does for skin, and how to use it safely', short='Glutathione',
    blurb='The complete guide: what glutathione is, how it affects skin, every form compared, and the research.',
    seo='Glutathione: Benefits for Skin, Uses, Side Effects & Forms',
    desc='Glutathione explained: what it is, how it works in body and skin, benefits, cream vs tablets vs injections, side effects, foods, and what research shows.',
    refs=['study', 'oral', 'wesch', 'ijdvl', 'review', 'fda'],
    body='''<p><b>Glutathione</b> is a small antioxidant molecule that your body makes every day, mostly in the liver. It is often called the body's "master antioxidant" because it helps protect cells from damage and recycles other antioxidants such as vitamin C and vitamin E. In skincare, glutathione is used in creams, serums and face washes made for <b>brighter-looking, more even skin</b>.</p>
<p>This guide covers everything in one place: what glutathione is, how it affects skin, the different forms you can buy, what the research shows, and how to use it safely.</p>

<h2>What is glutathione?</h2>
<p>Glutathione (often written GSH) is a <b>tripeptide</b>, a chain of three amino acids:</p>
<ul><li><b>Glutamic acid</b> (glutamate)</li><li><b>Cysteine</b>, which carries the sulphur group that makes glutathione such an effective antioxidant</li><li><b>Glycine</b></li></ul>
<p>It exists in two forms. <b>Reduced glutathione (GSH)</b> is the active form that neutralises free radicals. When it does that job it becomes <b>oxidised glutathione (GSSG)</b>, which the body then converts back. Skincare products may use either form (<a href="/reduced-vs-oxidized-glutathione/">reduced vs oxidised glutathione</a>).</p>
<p>Glutathione levels naturally fall with age, stress, poor sleep, smoking, alcohol and heavy sun exposure, which is one reason it has become popular in skincare.</p>

<h2>What does glutathione do in the body?</h2>
<ul><li><b>Antioxidant defence:</b> it neutralises free radicals produced by everyday metabolism, UV light and pollution.</li><li><b>Recycles other antioxidants:</b> it helps regenerate vitamin C and vitamin E.</li><li><b>Detoxification:</b> the liver uses it to process and remove many substances.</li><li><b>Immune support:</b> immune cells rely on it to work properly.</li></ul>

<h2>How glutathione affects skin colour and tone</h2>
<p>Skin colour comes from <b>melanin</b>, made in cells called melanocytes. There are two main types: dark brown-black <b>eumelanin</b> and lighter red-yellow <b>pheomelanin</b>. According to a review in the Indian Journal of Dermatology (%(ijdvl)s), glutathione may influence melanin in a few ways:</p>
<ol><li><b>Slowing tyrosinase</b>, the key enzyme the skin uses to make melanin.</li><li><b>Shifting production</b> from darker eumelanin towards lighter pheomelanin.</li><li><b>Antioxidant action</b>, which reduces the oxidative stress that triggers extra pigment after sun exposure.</li></ol>
<p>In everyday terms, this is why glutathione is used in products for <b>tan, dullness and uneven-looking tone</b>. It does not change your natural, genetic skin colour, and no honest product should claim it does.</p>

<h2>Benefits of glutathione for skin</h2>
<ul><li><b>Brighter, more even-looking skin</b> with regular use and daily sunscreen.</li><li><b>Support for fading tan and dark marks</b>, gradually, over weeks.</li><li><b>Antioxidant protection</b> against daily stress from sun and pollution.</li><li><b>Smoother, more hydrated feel</b>, reported in the topical study below, partly thanks to the cream base itself.</li></ul>
<p>Read the full guide: <a href="/glutathione-benefits-for-skin/">glutathione benefits for skin</a>.</p>

<h2>What the research says</h2>
<p>Glutathione is widely used, but the number of good clinical studies is still small. Here are the main ones, in plain words:</p>
<div class="tbl"><table><thead><tr><th>Study</th><th>Form and dose</th><th>Who and how long</th><th>Result</th></tr></thead><tbody>
<tr><td>%(study)s</td><td>2%% oxidised glutathione lotion, twice daily, on one side of the face</td><td>30 healthy women, 10 weeks</td><td>Melanin index fell more on the glutathione side than the placebo side; moisture and smoothness also improved. Well tolerated.</td></tr>
<tr><td>%(oral)s</td><td>500 mg glutathione capsules daily</td><td>60 healthy medical students, 4 weeks</td><td>Melanin index fell at all six measured sites compared with placebo.</td></tr>
<tr><td>%(wesch)s</td><td>250 mg/day reduced or oxidised glutathione</td><td>60 women aged 20–50, 12 weeks</td><td>Trends towards lower melanin and better elasticity, mostly not statistically significant; some wrinkle improvement with the reduced form.</td></tr>
</tbody></table></div>
<p>A 2025 systematic review of topical glutathione (%(review)s) concluded that it "shows promise", but that studies are few, small and short, and that more and larger trials are needed. The Indian review (%(ijdvl)s) reached a similar view: the evidence is encouraging for creams and tablets in the short term, but not strong enough to call glutathione a treatment for pigmentation disorders such as <a href="/glutathione-for-melasma/">melasma</a>. See <a href="/how-long-does-glutathione-take-to-work/">how long glutathione takes to work</a>.</p>
<p><b>Our honest summary:</b> glutathione can help skin look brighter and more even over time, as part of a routine with sunscreen. Expect gradual, modest change, not dramatic results.</p>

<h2>Forms of glutathione compared</h2>
<div class="tbl"><table><thead><tr><th></th><th>Cream / serum / face wash</th><th>Tablets / capsules</th><th>Injections (IV drips)</th></tr></thead><tbody>
<tr><td>How it works</td><td>Applied directly to skin</td><td>Swallowed as a supplement</td><td>Injected into a vein</td></tr>
<tr><td>Evidence for skin</td><td>Small controlled studies, modest gradual effect</td><td>Small studies, mixed results</td><td>No clinical trial for skin lightening</td></tr>
<tr><td>Safety</td><td>Generally well tolerated; patch test</td><td>Usually well tolerated short term; ask a doctor</td><td>Serious safety warnings from regulators</td></tr>
<tr><td>Best for</td><td>Everyday skincare</td><td>Only with medical advice</td><td>Not recommended for cosmetic use</td></tr>
</tbody></table></div>
<p>More detail: <a href="/glutathione-cream-vs-tablets-vs-injections/">glutathione cream vs tablets vs injections</a>.</p>

<h2>Glutathione side effects and safety</h2>
<p>Creams and face washes are generally well tolerated. As with any new product, some people get mild tingling, redness or dryness at first; stop if it lasts. Injections are a different matter: the %(fda)s said injectable skin-lightening products may be unsafe and contain unknown substances, and the Indian dermatology review advises doctors not to give IV glutathione for skin lightening. Full guide: <a href="/glutathione-side-effects/">glutathione side effects</a> and <a href="/is-glutathione-safe-for-skin/">is glutathione safe for skin?</a></p>

<h2>Foods that support glutathione</h2>
<p>Your body builds glutathione from amino acids, so diet matters. Foods rich in sulphur and in glutathione's building blocks include garlic, onion, broccoli, cabbage, cauliflower, spinach, okra (bhindi), avocado, eggs, lentils and dairy. Vitamin C-rich foods such as amla, guava, oranges and lemons help keep glutathione in its active form. See <a href="/glutathione-rich-foods/">glutathione-rich foods</a>.</p>

<h2>How to use glutathione in your routine</h2>
<ol><li><b>Night:</b> cleanse with a gentle face wash such as %(wash)s, then apply a glutathione cream such as %(cream)s.</li><li><b>Morning:</b> cleanse and apply broad-spectrum sunscreen, SPF 30 or higher.</li><li><b>Be patient:</b> give the routine 8 to 12 weeks before judging.</li></ol>
<p>Step by step: <a href="/how-to-use-glutathione-cream/">how to use glutathione cream</a>.</p>

<h2>Who should be careful</h2>
<ul><li>Pregnant or breastfeeding women, especially with products that also contain retinol.</li><li>People with eczema, rosacea or very sensitive skin.</li><li>Anyone with patchy pigmentation that may be <a href="/glutathione-for-melasma/">melasma</a>, or spots that change shape or colour: see a dermatologist first.</li></ul>''',
    faq=[
        ('What is glutathione in simple words?', 'Glutathione is an antioxidant your body makes from three amino acids (glutamic acid, cysteine and glycine). It protects cells from damage and is used in skincare for brighter, more even-looking skin.'),
        ('Does glutathione lighten skin permanently?', 'No. Glutathione may help tan and uneven tone look lighter over time, but it does not change your natural skin colour, and any effect fades if you stop sun protection and regular care.'),
        ('Which form of glutathione is best for skin?', 'For everyday skincare, a glutathione cream or face wash is the simplest and lowest-risk option. Tablets should be taken only with medical advice, and injections are not recommended for cosmetic use.'),
        ('How long does glutathione take to show results?', 'Studies ran for 4 to 12 weeks. With a cream, most people should give it at least 8 weeks of regular use with daily sunscreen before judging.'),
        ('Is glutathione safe?', 'Glutathione creams are generally well tolerated; patch test first. Glutathione injections for skin lightening carry serious safety warnings and should be avoided.'),
        ('Can men use glutathione?', 'Yes. Glutathione skincare works the same way for men and women.'),
    ])

NEW_GUIDES = [
    dict(slug='glutathione-cream-price-in-india', title='Glutathione cream price in India: what you are paying for', short='Price in India',
         blurb='Why glutathione creams cost what they do, and how to judge value.',
         seo='Glutathione Cream Price in India (2026): What Affects It',
         desc='Glutathione cream price in India explained: what drives the price, how to compare value per gram, red flags with very cheap creams, and GlutaNex prices.',
         refs=['ijdvl', 'review'],
         body='''<p>Glutathione creams in India range from a few hundred rupees to several thousand. The price depends less on the word "glutathione" on the label and more on <b>what else is in the formula, how much you get, and who stands behind it</b>.</p>
<h2>GlutaNex prices</h2>
<div class="tbl"><table><thead><tr><th>Product</th><th>Price</th><th>MRP</th><th>Shipping</th></tr></thead><tbody>
<tr><td>%(cream)s</td><td>%(pcream)s</td><td>%(mcream)s</td><td>Free</td></tr>
<tr><td>%(wash)s</td><td>%(pwash)s</td><td>%(mwash)s</td><td>Free</td></tr>
<tr><td><a href="%(uduo)s">Glow Duo (cream + face wash)</a></td><td>%(pduo)s</td><td>%(mduo)s</td><td>Free</td></tr>
</tbody></table></div>
<p>Prices include taxes. Cash on Delivery is available with nothing to pay in advance.</p>
<h2>What affects the price of a glutathione cream</h2>
<ol><li><b>The full formula.</b> A cream that combines glutathione with proven partners such as niacinamide, vitamin C, hyaluronic acid, ceramides and peptides costs more to make than a basic cream with a trace of glutathione.</li><li><b>Quantity.</b> Always compare price per gram, not price per jar.</li><li><b>Packaging.</b> Airless pumps and opaque jars protect sensitive ingredients from light and air.</li><li><b>Testing and transparency.</b> A full ingredient list, batch number, expiry date and a real company address on the pack.</li><li><b>Support.</b> Returns, a working contact number and a clear refund policy cost money to run, and protect you.</li></ol>
<h2>How to compare value</h2>
<p>Work out the <b>price per gram</b> (price ÷ grams), then check whether the formula has the ingredients you want. A slightly more expensive cream that you use consistently for 3 months is better value than a cheap one you abandon after two weeks.</p>
<h2>Red flags with very cheap or "miracle" creams</h2>
<ul><li>Promises like "fair in 7 days" or "permanent whitening".</li><li>No full ingredient list, or only "glutathione + herbal extracts".</li><li>No manufacturer address, licence or batch details.</li><li>A burning feeling followed by fast lightening: some illegal "fairness" creams contain steroids, hydroquinone or mercury, which can seriously damage skin.</li></ul>
<h2>Is a more expensive glutathione cream always better?</h2>
<p>No. Research on topical glutathione is still limited (%(review)s), so no price guarantees results. Pay for a sensible formula, honest labelling and a seller you can reach, then use it consistently with sunscreen.</p>''',
         faq=[('What is the price of glutathione cream in India?', 'Glutathione creams range from a few hundred to several thousand rupees. GlutaNex Glutathione Night Cream is %(pcream)s with free shipping.'),
              ('Why are some glutathione creams so cheap?', 'They may contain very little glutathione, skip other useful ingredients, or in the worst cases contain banned substances. Check the full ingredient list and the seller details.'),
              ('Is the Glow Duo cheaper than buying separately?', 'Yes. The Glow Duo is %(pduo)s, less than the Night Cream and Face Wash bought separately.')]),

    dict(slug='best-glutathione-cream-in-india', title='How to choose the best glutathione cream in India', short='Best glutathione cream',
         blurb='A simple checklist to judge any glutathione cream before you buy.',
         seo='Best Glutathione Cream in India: How to Choose (Checklist)',
         desc='Looking for the best glutathione cream in India? Use this checklist: ingredients that matter, safe concentrations, red flags, skin type advice and a simple routine.',
         refs=['study', 'review', 'ijdvl'],
         body='''<p>The "best" glutathione cream is the one that suits your skin, has an honest, sensible formula, and that you will use every night for at least two months. Rather than a paid ranking, here is a checklist you can apply to <b>any</b> glutathione cream, including ours.</p>
<h2>The 7-point checklist</h2>
<ol><li><b>Glutathione is clearly listed</b> in the full ingredient list printed on the pack.</li><li><b>It has useful partners.</b> Niacinamide (vitamin B3), vitamin C, hyaluronic acid and ceramides support even tone, hydration and the skin barrier.</li><li><b>Night or day use is clear.</b> Creams with retinol or exfoliating acids belong at night.</li><li><b>Realistic claims.</b> "Brighter-looking" and "more even" are honest; "fair in 7 days" is not.</li><li><b>Safe packaging.</b> Sealed, with batch number, manufacturing and expiry dates.</li><li><b>A real seller.</b> Company name, address, phone or WhatsApp, and a return policy.</li><li><b>Fits your skin type</b> (see below).</li></ol>
<h2>Choosing by skin type</h2>
<div class="tbl"><table><thead><tr><th>Skin type</th><th>Look for</th><th>Be careful with</th></tr></thead><tbody>
<tr><td>Oily or acne-prone</td><td>Light texture, niacinamide, salicylic acid</td><td>Heavy oils and thick butters</td></tr>
<tr><td>Dry</td><td>Ceramides, hyaluronic acid, a richer cream</td><td>Strong acids used every night</td></tr>
<tr><td>Sensitive</td><td>Short ingredient list, soothing aloe vera</td><td>Retinol and acids at first; patch test</td></tr>
<tr><td>Combination</td><td>Balanced cream, niacinamide</td><td>Layering many actives</td></tr>
</tbody></table></div>
<h2>How GlutaNex Night Cream measures up</h2>
<p>%(cream)s pairs glutathione with niacinamide, vitamin C, hyaluronic acid, retinol, ceramides, salicylic acid, peptides, aloe vera, turmeric and neem. Because it contains retinol and salicylic acid, it is a <b>night cream</b>: start 2 to 3 nights a week and use sunscreen every morning. It is not suitable during pregnancy or breastfeeding unless your doctor approves.</p>
<h2>What the evidence can and cannot tell you</h2>
<p>The best-known topical study used a 2%% oxidised glutathione lotion for 10 weeks (%(study)s) and found a modest improvement in skin tone. A 2025 systematic review (%(review)s) called topical glutathione promising but under-studied. So be wary of any brand that claims clinical proof of dramatic results.</p>''',
         faq=[('Which glutathione cream is best for Indian skin?', 'Choose one with glutathione clearly listed, supporting ingredients like niacinamide and hyaluronic acid, realistic claims and a seller you can contact. Use it nightly with daily sunscreen.'),
              ('Is a glutathione cream with niacinamide better?', 'Niacinamide is well studied for even-looking tone and the skin barrier, so it is a sensible partner for glutathione.'),
              ('Can I use a glutathione cream in the day?', 'Some are for day use, but creams with retinol or exfoliating acids, such as the GlutaNex Night Cream, should be used at night.')]),

    dict(slug='glutathione-face-wash', title='Glutathione face wash: does it work and how to use it', short='Glutathione face wash',
         blurb='What a glutathione face wash can do, and how it fits your routine.',
         seo='Glutathione Face Wash: Benefits, How to Use & What to Expect',
         desc='Glutathione face wash explained: what it can and cannot do in a short contact time, how to use it, who it suits, and how to pair it with a glutathione cream.',
         refs=['review'],
         body='''<p>A glutathione face wash is a gentle cleanser that contains glutathione. Because a face wash is rinsed off within a minute, it is best thought of as the <b>first step of a glutathione routine</b>, not the whole treatment.</p>
<h2>What a glutathione face wash can do</h2><ul><li><b>Clean without stripping</b>, removing oil, sweat, sunscreen and pollution.</li><li><b>Prepare the skin</b> so your night cream spreads evenly.</li><li>Leave skin feeling <b>fresh and soft</b>, especially with hydrating ingredients.</li></ul>
<h2>What it cannot do on its own</h2><p>Ingredients in a wash have only a short time on the skin. The research on glutathione for skin tone used leave-on lotions applied for weeks (%(review)s). For visible change in tone, pair the face wash with a leave-on cream and daily sunscreen.</p>
<h2>How to use a glutathione face wash</h2><ol><li>Wet your face with lukewarm water.</li><li>Lather a small amount between your palms.</li><li>Massage gently in circles for 30 to 60 seconds.</li><li>Rinse well and pat dry with a clean towel.</li><li>Use morning and night.</li></ol>
<h2>The simple routine</h2><ul><li><b>Morning:</b> %(wash)s, then sunscreen.</li><li><b>Night:</b> %(wash)s, then %(cream)s.</li></ul><p>Or get both together in the <a href="%(uduo)s">Glow Duo</a>.</p>
<h2>Who it suits</h2><p>Most skin types. If your skin is very dry or sensitive, use it once a day and patch test first.</p>''',
         faq=[('Does glutathione face wash lighten skin?', 'A face wash is rinsed off quickly, so on its own it mainly cleans and refreshes. For brighter-looking skin, pair it with a leave-on glutathione cream and daily sunscreen.'),
              ('Can I use glutathione face wash twice a day?', 'Yes, most people can use it morning and night. If your skin feels tight or dry, use it once a day.'),
              ('Can men use a glutathione face wash?', 'Yes. It suits men and women.')]),

    dict(slug='is-glutathione-safe-for-skin', title='Is glutathione safe for skin?', short='Is it safe?',
         blurb='Creams, tablets and injections: what is safe and what is not.',
         seo='Is Glutathione Safe for Skin? Creams vs Injections Explained',
         desc='Is glutathione safe? What the research says about glutathione creams, tablets and injections, who should avoid it, how to patch test, and warning signs to watch for.',
         refs=['study', 'review', 'ijdvl', 'fda'],
         body='''<p><b>Short answer:</b> glutathione creams and face washes are generally safe for most adults when used as directed. Glutathione <b>injections</b> for skin lightening are not considered safe and should be avoided.</p>
<h2>Glutathione creams</h2><p>In the 10-week study of a 2%% glutathione lotion (%(study)s), only one of 30 women had mild redness, which cleared within two days without stopping. A 2025 systematic review (%(review)s) found topical glutathione generally well tolerated, but noted that safety data are still limited. As with any skincare, irritation is possible, especially in products that also contain retinol or acids.</p>
<h2>Glutathione tablets</h2><p>Short studies of oral glutathione reported mostly mild effects, but they were small and short. Tablets are supplements, so talk to a doctor first, especially if you take other medicines, have a medical condition or are pregnant.</p>
<h2>Glutathione injections</h2><p>The %(fda)s warned that injectable skin-lightening products may be unsafe or ineffective and may contain unknown ingredients. The Indian Journal of Dermatology review (%(ijdvl)s) noted that no clinical trial supports IV glutathione for skin lightening, listed reported concerns, and advised dermatologists against using it for this purpose. Fake or contaminated injections sold online or in salons add further risk.</p>
<h2>Who should be careful</h2><ul><li>Pregnant or breastfeeding women (and avoid retinol products unless a doctor approves).</li><li>People with eczema, rosacea, or very sensitive or broken skin.</li><li>Anyone using prescription creams for acne or pigmentation.</li></ul>
<h2>How to patch test</h2><ol><li>Apply a little behind the ear or on the inner arm.</li><li>Wait 24 hours.</li><li>No redness or itching? Start on the face, slowly.</li></ol>
<h2>Stop and see a doctor if</h2><ul><li>Redness, burning or itching does not settle within a few days.</li><li>You develop swelling, a rash or blisters.</li><li>Your skin becomes patchy, much lighter in areas, or thin and sensitive.</li></ul>''',
         faq=[('Is glutathione cream safe for daily use?', 'For most adults, yes, when used as directed. Patch test first. Creams that also contain retinol should be introduced slowly and used at night.'),
              ('Are glutathione injections safe?', 'Regulators have warned against injectable skin-lightening products, and no clinical trial supports IV glutathione for skin lightening. Avoid them for cosmetic use.'),
              ('Can I use glutathione cream during pregnancy?', 'Ask your doctor first. The GlutaNex Night Cream contains retinol and salicylic acid and should not be used during pregnancy or breastfeeding unless a doctor approves.')]),

    dict(slug='glutathione-vs-kojic-acid', title='Glutathione vs kojic acid: which is better for your skin?', short='Glutathione vs kojic acid',
         blurb='How the two brightening ingredients compare, and whether to combine them.',
         seo='Glutathione vs Kojic Acid: Differences, Benefits & Which to Use',
         desc='Glutathione vs kojic acid compared: how each works on pigmentation, gentleness, evidence, who each suits, and whether you can use them together.',
         refs=['ijdvl', 'review'],
         body='''<p>Glutathione and kojic acid are both used in products for <b>tan, dark spots and uneven-looking tone</b>. They work in related ways but feel different on the skin.</p>
<div class="tbl"><table><thead><tr><th></th><th>Glutathione</th><th>Kojic acid</th></tr></thead><tbody>
<tr><td>What it is</td><td>Antioxidant tripeptide the body makes naturally</td><td>Compound produced by certain fungi, often from fermented rice</td></tr>
<tr><td>How it works</td><td>Slows tyrosinase, shifts melanin to lighter forms, antioxidant</td><td>Slows tyrosinase by binding the copper it needs</td></tr>
<tr><td>Gentleness</td><td>Generally gentle</td><td>Can irritate or cause allergic reactions in some people</td></tr>
<tr><td>Extra benefits</td><td>Antioxidant protection, recycles vitamins C and E</td><td>Mild antibacterial properties</td></tr>
<tr><td>Best for</td><td>Overall dullness and uneven tone, sensitive skin</td><td>Stubborn spots, in people who tolerate it</td></tr>
</tbody></table></div>
<h2>Which is better?</h2><p>Neither is "stronger" in every way. Glutathione is usually the gentler choice for everyday use and adds antioxidant protection. Kojic acid may suit stubborn spots but is more likely to irritate. Evidence for both comes mostly from small studies (%(ijdvl)s, %(review)s).</p>
<h2>Can you use them together?</h2><p>Yes, many products combine them. If you use separate products, introduce one at a time, patch test, and avoid layering several strong actives on the same night.</p>
<h2>Whatever you choose</h2><p>Sunscreen every morning matters more than any single ingredient. Without it, new tan and spots keep forming.</p>
<p>GlutaNex uses glutathione with niacinamide and vitamin C: %(cream)s.</p>''',
         faq=[('Is glutathione better than kojic acid?', 'Glutathione is usually gentler and adds antioxidant protection; kojic acid may help stubborn spots but irritates some skin. The better choice depends on your skin.'),
              ('Can I use kojic acid and glutathione together?', 'Yes, but introduce one product at a time, patch test and avoid stacking many strong actives on the same night.')]),

    dict(slug='glutathione-for-skin-whitening', title='Glutathione for skin whitening: what is true and what is hype', short='Glutathione and skin whitening',
         blurb='The honest answer to the most searched glutathione question.',
         seo='Glutathione for Skin Whitening: What Is True & What Is Hype',
         desc='Does glutathione whiten skin? An honest look at what glutathione can do for tan and uneven tone, what it cannot do, the injection risks, and safer routines.',
         refs=['study', 'oral', 'ijdvl', 'review', 'fda'],
         body='''<p>Glutathione is often marketed for "skin whitening". The honest answer: glutathione may help <b>tan, dullness and uneven tone look lighter and more even</b> over time. It <b>does not change your natural skin colour</b>, and claims that it does are hype.</p>
<h2>Where the "whitening" idea comes from</h2><p>Glutathione slows tyrosinase, the enzyme that makes melanin, and may shift production towards lighter pheomelanin (%(ijdvl)s). Small studies found modest drops in melanin index with a 2%% topical lotion over 10 weeks (%(study)s) and with 500 mg oral capsules over 4 weeks (%(oral)s).</p>
<h2>What glutathione can realistically do</h2><ul><li>Help a recent <b>tan</b> fade faster, with sun protection.</li><li>Make <b>dark marks</b> after pimples look lighter over weeks.</li><li>Give a <b>brighter, more even</b> look to dull skin.</li></ul>
<h2>What it cannot do</h2><ul><li>Change your genetic skin tone.</li><li>Give permanent results without sunscreen.</li><li>Treat melasma or other pigment disorders on its own; see a dermatologist.</li></ul>
<h2>The injection problem</h2><p>The fastest "whitening" promises usually involve glutathione injections or drips. The %(fda)s warned about injectable skin-lightening products, and Indian dermatologists have advised against IV glutathione for skin lightening because no clinical trial supports it (%(ijdvl)s). Avoid them.</p>
<h2>Beware of "fairness" creams that work too fast</h2><p>Creams that lighten skin dramatically within days may contain steroids, hydroquinone or mercury, which can cause thinning, acne, stretch marks and patchy skin. Fast is not safe.</p>
<h2>Healthy skin, in every shade</h2><p>Every skin tone can be healthy and glowing. A good goal is <b>even, clear, well-protected skin</b> in your own shade: gentle cleansing, a glutathione cream at night, and sunscreen every morning.</p>''',
         faq=[('Does glutathione whiten skin permanently?', 'No. It may help tan and uneven tone look lighter over time, but it does not change your natural skin colour, and results depend on continued sun protection.'),
              ('How much glutathione is needed for skin whitening?', 'There is no proven dose that whitens skin. Studies used a 2%% lotion or 250–500 mg tablets and found only modest changes in skin tone. Tablets should be taken only with medical advice.'),
              ('Are glutathione whitening injections safe?', 'No clinical trial supports them for skin lightening and regulators have issued warnings. Avoid them.')]),

    dict(slug='glutathione-rich-foods', title='Glutathione-rich foods: how to support your body\'s glutathione naturally', short='Glutathione-rich foods',
         blurb='Indian foods that help your body make and recycle glutathione.',
         seo='Glutathione-Rich Foods: 15 Indian Foods That Support Glutathione',
         desc='Glutathione-rich foods and how to boost glutathione naturally: sulphur vegetables, vitamin C foods, protein sources, everyday Indian options and lifestyle habits.',
         refs=['ijdvl'],
         body='''<p>Your body makes its own glutathione from three amino acids: glutamic acid, cysteine and glycine. You can support that process with everyday foods, especially those rich in <b>sulphur</b>, <b>protein</b> and <b>vitamin C</b>.</p>
<h2>Foods that contain glutathione or its building blocks</h2><div class="tbl"><table><thead><tr><th>Group</th><th>Everyday Indian examples</th><th>Why it helps</th></tr></thead><tbody>
<tr><td>Sulphur-rich vegetables</td><td>Garlic, onion, broccoli, cabbage, cauliflower</td><td>Provide sulphur compounds the body uses to make cysteine</td></tr>
<tr><td>Green vegetables</td><td>Spinach (palak), okra (bhindi), asparagus</td><td>Contain glutathione directly</td></tr>
<tr><td>Fruits</td><td>Avocado, tomato</td><td>Contain glutathione</td></tr>
<tr><td>Vitamin C foods</td><td>Amla, guava, oranges, lemon, papaya</td><td>Help keep glutathione in its active form</td></tr>
<tr><td>Protein</td><td>Eggs, dal and lentils, paneer, curd, milk, chicken, fish</td><td>Supply cysteine, glycine and glutamate</td></tr>
<tr><td>Seeds and nuts</td><td>Sunflower seeds, almonds, walnuts</td><td>Provide vitamin E and selenium, which work with glutathione</td></tr>
</tbody></table></div>
<p>Cooking reduces the glutathione in vegetables, so include some raw or lightly cooked options, such as salads, kachumber and fruit.</p>
<h2>Habits that protect glutathione</h2><ul><li><b>Sleep</b> 7 to 8 hours.</li><li><b>Exercise</b> regularly, without overtraining.</li><li><b>Limit alcohol and avoid smoking</b>, both of which use up glutathione.</li><li><b>Protect your skin from the sun</b> to reduce oxidative stress.</li></ul>
<h2>Food, skin and realistic expectations</h2><p>A good diet supports your body's antioxidant defences, but food alone will not visibly change pigmentation. For skin, combine a balanced diet with a topical routine: a glutathione cream at night such as %(cream)s and sunscreen every morning.</p>''',
         faq=[('Which food has the most glutathione?', 'Spinach, okra, asparagus and avocado contain glutathione directly, while garlic, onion, broccoli and protein foods supply its building blocks.'),
              ('Does eating glutathione-rich food lighten skin?', 'A healthy diet supports overall skin health, but food alone will not noticeably change pigmentation.')]),
]

# Extra sections appended to the existing guides (plus a FAQ for each).
EXPAND = {
    'glutathione-cream': dict(refs=['study', 'review', 'ijdvl'], body='''
<h2>Glutathione cream ingredients that work well together</h2><div class="tbl"><table><thead><tr><th>Ingredient</th><th>Why it is paired with glutathione</th></tr></thead><tbody>
<tr><td>Niacinamide (vitamin B3)</td><td>Helps with uneven-looking tone and strengthens the skin barrier</td></tr>
<tr><td>Vitamin C</td><td>Antioxidant partner that helps keep glutathione active</td></tr>
<tr><td>Hyaluronic acid</td><td>Hydration, so skin looks plumper and smoother</td></tr>
<tr><td>Ceramides</td><td>Support the barrier and reduce dryness from active ingredients</td></tr>
<tr><td>Retinol</td><td>Smoother texture; night use only, introduce slowly</td></tr>
<tr><td>Aloe vera</td><td>Soothes and calms</td></tr>
</tbody></table></div>
<h2>Glutathione cream for different concerns</h2><ul><li><b>Tan:</b> nightly cream plus daily sunscreen; tan usually fades over a few weeks.</li><li><b>Dark spots and acne marks:</b> 8 to 12 weeks of regular use; older marks may lighten only partly.</li><li><b>Dullness:</b> many people notice a fresher look within a few weeks.</li><li><b>Melasma:</b> needs a dermatologist; a cream alone is not a treatment.</li></ul>
<h2>What the wider research says</h2><p>A 2025 systematic review (%(review)s) found five clinical trials of topical glutathione: results were promising for hyperpigmentation, but studies were small, short and sometimes uncontrolled. India's own dermatology journal (%(ijdvl)s) reached a similar conclusion. That is why we describe results as gradual and modest.</p>''',
        faq=[('Which glutathione cream is good for the face?', 'Look for glutathione clearly listed with supporting ingredients such as niacinamide and hyaluronic acid, realistic claims, and a seller you can contact.'),
             ('Should glutathione cream be used at night or in the day?', 'Night is usually best, especially for creams with retinol or acids. Use sunscreen every morning.'),
             ('How long does glutathione cream take to work?', 'Expect gradual changes over 8 to 12 weeks of regular use with daily sunscreen.')]),
    'glutathione-benefits-for-skin': dict(refs=['study', 'oral', 'wesch', 'review'], body='''
<h2>4. Support for an anti-ageing routine</h2><p>In a 12-week study of oral glutathione (%(wesch)s), the reduced form showed some improvement in wrinkles and a trend towards better elasticity, though most results were not statistically significant. In skincare, glutathione is best seen as a supporting antioxidant alongside proven anti-ageing basics: sunscreen, retinoids and moisturiser.</p>
<h2>5. A gentler option for sensitive skin</h2><p>Compared with some stronger brightening ingredients, glutathione is generally well tolerated in creams (%(review)s), which makes it a good everyday option.</p>
<h2>Glutathione benefits: summary</h2><div class="tbl"><table><thead><tr><th>Benefit</th><th>Strength of evidence</th></tr></thead><tbody>
<tr><td>Antioxidant protection</td><td>Strong (well established in biology)</td></tr>
<tr><td>Brighter, more even-looking tone</td><td>Moderate: small controlled studies (%(study)s, %(oral)s)</td></tr>
<tr><td>Hydration and smoothness</td><td>Limited: reported in one topical study</td></tr>
<tr><td>Wrinkles and elasticity</td><td>Limited: mixed oral results</td></tr>
</tbody></table></div>''',
        faq=[('What are the main benefits of glutathione for skin?', 'Antioxidant protection, a brighter and more even-looking tone with regular use, and a smoother, more hydrated feel.'),
             ('Is glutathione good for oily skin?', 'Yes. Choose a lightweight cream and pair it with a gentle face wash.')]),
    'glutathione-side-effects': dict(refs=['study', 'wesch', 'ijdvl', 'review', 'fda'], body='''
<h2>Side effects of glutathione tablets</h2><p>Short studies of oral glutathione reported mostly mild effects such as itching or tiredness, which also appeared in placebo groups; in one 12-week study, two people had temporary changes in liver tests that settled (%(wesch)s). Tablets are supplements: speak to a doctor before taking them.</p>
<h2>Reported concerns with injections</h2><p>The Indian dermatology review (%(ijdvl)s) listed concerns reported or suspected with IV glutathione used for skin lightening, including patchy loss of colour on sun-exposed skin, possible effects on the liver's own glutathione, and risks from counterfeit products. It advised doctors not to use IV glutathione for skin lightening.</p>
<h2>Side effects from other ingredients</h2><p>Many glutathione creams also contain retinol, salicylic acid or vitamin C. These can cause dryness, peeling or tingling at first. Start 2 to 3 nights a week and use sunscreen every morning.</p>''',
        faq=[('What are the side effects of glutathione cream?', 'Most people have none. Some may get mild tingling, redness or dryness at first, especially if the cream also contains retinol or acids. Stop if it lasts.'),
             ('Does glutathione damage the liver?', 'Creams are applied to the skin and are not linked to liver problems. Concerns relate mainly to high-dose injections; talk to a doctor before any oral or injected use.')]),
    'how-to-use-glutathione-cream': dict(refs=['study'], body='''
<h2>How much glutathione cream to use</h2><p>A pea-sized amount covers the face; add a little more for the neck. Using more does not give faster results and can increase irritation.</p>
<h2>A sample 8-week plan</h2><div class="tbl"><table><thead><tr><th>Weeks</th><th>Night</th><th>Morning</th></tr></thead><tbody>
<tr><td>1–2</td><td>Cream on 2 to 3 nights, gentle cleanser every night</td><td>Cleanser + sunscreen</td></tr>
<tr><td>3–4</td><td>Cream every other night if comfortable</td><td>Cleanser + sunscreen</td></tr>
<tr><td>5–8</td><td>Cream every night</td><td>Cleanser + sunscreen, reapply outdoors</td></tr>
</tbody></table></div>
<h2>Glutathione cream for men</h2><p>The routine is the same. Apply after shaving only once the skin has settled, as freshly shaved skin can sting.</p>''',
        faq=[('Can I apply glutathione cream every day?', 'Yes, once your skin is used to it. With creams containing retinol, start 2 to 3 nights a week.'),
             ('Should I wash off glutathione cream in the morning?', 'Yes, cleanse in the morning and apply sunscreen.')]),
    'glutathione-cream-vs-tablets-vs-injections': dict(refs=['study', 'oral', 'wesch', 'ijdvl'], body='''
<h2>What the studies used</h2><ul><li><b>Cream:</b> a 2%% oxidised glutathione lotion for 10 weeks (%(study)s).</li><li><b>Tablets:</b> 500 mg a day for 4 weeks (%(oral)s), and 250 mg a day for 12 weeks (%(wesch)s).</li><li><b>Injections:</b> no clinical trial for skin lightening (%(ijdvl)s).</li></ul>
<h2>Cost and convenience</h2><p>Creams are the most affordable and simplest to use every day. Injections are expensive, need repeated visits, and cheap versions may be counterfeit.</p>''',
        faq=[('Which is better, glutathione tablets or cream?', 'For skincare, a cream is the simple, low-risk choice. Tablets have mixed evidence and should be taken only with medical advice.'),
             ('Are glutathione injections approved in India for skin whitening?', 'They are not supported by clinical trials for skin lightening, and Indian dermatologists have advised against using them for this purpose.')]),
    'glutathione-and-niacinamide': dict(refs=['review'], body='''
<h2>Why niacinamide and glutathione pair well</h2><p>Niacinamide helps reduce the transfer of pigment to the skin's surface cells and strengthens the barrier, while glutathione works earlier in melanin production and adds antioxidant protection. Together they target uneven tone from two directions, and both are generally gentle.</p>
<h2>Can I add vitamin C and retinol too?</h2><p>Yes, with care. Vitamin C is ideal in the morning under sunscreen. Retinol belongs at night and should be introduced slowly. If your glutathione cream already contains retinol, such as %(cream)s, do not add another retinol product.</p>''',
        faq=[('Can I use glutathione and niacinamide together every day?', 'Yes. They are often combined in one product and are generally gentle.'),
             ('Can I use glutathione with vitamin C?', 'Yes. Vitamin C helps keep glutathione active. Use vitamin C in the morning under sunscreen.')]),
    'glutathione-for-dark-spots-and-tan': dict(refs=['study', 'ijdvl'], body='''
<h2>Tan vs dark spots vs melasma</h2><div class="tbl"><table><thead><tr><th></th><th>Looks like</th><th>Typical timeline with care</th></tr></thead><tbody>
<tr><td>Tan</td><td>Even darkening on sun-exposed areas</td><td>A few weeks</td></tr>
<tr><td>Acne marks</td><td>Flat brown spots where pimples were</td><td>8–12 weeks or more</td></tr>
<tr><td>Sun spots</td><td>Small brown spots, often on cheeks and hands</td><td>Months; may lighten only partly</td></tr>
<tr><td>Melasma</td><td>Patchy brown areas on both cheeks, forehead or upper lip</td><td>Needs a dermatologist</td></tr>
</tbody></table></div>
<h2>Home remedies to avoid</h2><p>Lemon juice, baking soda, toothpaste and harsh scrubs can irritate the skin and make marks darker. Stick to gentle care and sunscreen.</p>''',
        faq=[('Does glutathione remove dark spots?', 'It may help dark spots look lighter over 8 to 12 weeks with daily sunscreen. Older spots may lighten only partly.'),
             ('How fast does glutathione remove tan?', 'With daily sunscreen, a recent tan usually fades over a few weeks.')]),
}

# ---------------- Hindi pages ----------------
HI = [
    dict(slug='glutathione-cream-ke-fayde', en='/glutathione-benefits-for-skin/',
         title='ग्लूटाथियोन क्रीम के फायदे: त्वचा के लिए क्या करती है', short='ग्लूटाथियोन क्रीम के फायदे',
         seo='Glutathione Cream Ke Fayde: ग्लूटाथियोन क्रीम के फायदे और उपयोग',
         desc='Glutathione cream ke fayde हिंदी में: ग्लूटाथियोन क्या है, त्वचा के लिए फायदे, रिसर्च क्या कहती है, कितने दिन में असर दिखता है और सही तरीके से कैसे लगाएं।',
         body='''<p><b>ग्लूटाथियोन (Glutathione)</b> एक एंटीऑक्सीडेंट है जिसे हमारा शरीर खुद बनाता है। स्किनकेयर में इसका उपयोग <b>त्वचा को चमकदार और एक-समान दिखाने</b> के लिए किया जाता है। यह एक कॉस्मेटिक है, दवा नहीं, और इसका असर धीरे-धीरे दिखता है।</p>
<h2>ग्लूटाथियोन क्या है?</h2><p>ग्लूटाथियोन तीन अमीनो एसिड (ग्लूटामिक एसिड, सिस्टीन और ग्लाइसिन) से बना एक छोटा अणु है। यह कोशिकाओं को धूप, प्रदूषण और तनाव से होने वाले नुकसान से बचाने में मदद करता है।</p>
<h2>ग्लूटाथियोन क्रीम के फायदे</h2><ul><li><b>चमकदार और एक-समान दिखने वाली त्वचा</b>, नियमित उपयोग और सनस्क्रीन के साथ।</li><li><b>टैन और दाग-धब्बों</b> को हल्का दिखाने में सहायता, कुछ हफ्तों में।</li><li><b>एंटीऑक्सीडेंट सुरक्षा</b>, धूप और प्रदूषण से।</li><li><b>मुलायम और नमीयुक्त त्वचा</b> का एहसास।</li></ul>
<h2>रिसर्च क्या कहती है?</h2><p>एक छोटी, प्लेसीबो-नियंत्रित स्टडी (%(study)s) में 30 महिलाओं ने 10 हफ्तों तक 2%% ग्लूटाथियोन लोशन लगाया। ग्लूटाथियोन वाली तरफ त्वचा का मेलानिन थोड़ा कम हुआ और त्वचा अधिक नम और मुलायम रही। भारतीय डर्मेटोलॉजी जर्नल की समीक्षा (%(ijdvl)s) के अनुसार सबूत उत्साहजनक हैं, लेकिन अभी बड़ी स्टडी की जरूरत है।</p>
<h2>ग्लूटाथियोन क्या नहीं कर सकता</h2><ul><li>आपका प्राकृतिक रंग नहीं बदल सकता। कोई भी क्रीम ऐसा नहीं कर सकती।</li><li>रातों-रात असर नहीं दिखाता; हफ्तों का समय लगता है।</li><li>मेलाज्मा जैसी समस्या का इलाज नहीं है; उसके लिए डर्मेटोलॉजिस्ट से मिलें।</li></ul>
<h2>कितने दिन में असर दिखता है?</h2><div class="tbl"><table><thead><tr><th>समय</th><th>आप क्या महसूस कर सकते हैं</th></tr></thead><tbody><tr><td>1–2 हफ्ते</td><td>त्वचा मुलायम और आरामदायक</td></tr><tr><td>4–6 हफ्ते</td><td>त्वचा थोड़ी चमकदार और एक-समान दिख सकती है</td></tr><tr><td>8 हफ्ते+</td><td>टैन और दाग हल्के दिख सकते हैं (रोज सनस्क्रीन के साथ)</td></tr></tbody></table></div>
<h2>GlutaNex Night Cream में क्या है?</h2><p>%(cream)s में ग्लूटाथियोन के साथ नियासिनामाइड (विटामिन B3), विटामिन C, हायलूरोनिक एसिड, रेटिनॉल, सेरामाइड्स, सैलिसिलिक एसिड, पेप्टाइड्स, एलोवेरा, हल्दी और नीम हैं। इसमें रेटिनॉल और सैलिसिलिक एसिड है, इसलिए इसे केवल रात में लगाएं, पहले 2 हफ्ते हफ्ते में 2–3 बार से शुरू करें, और गर्भावस्था या स्तनपान के दौरान डॉक्टर की सलाह के बिना उपयोग न करें।</p>''',
         faq=[('ग्लूटाथियोन क्रीम के क्या फायदे हैं?', 'नियमित उपयोग और सनस्क्रीन के साथ यह त्वचा को चमकदार और एक-समान दिखाने, टैन और दाग-धब्बों को हल्का दिखाने और एंटीऑक्सीडेंट सुरक्षा देने में मदद करती है।'),
              ('क्या ग्लूटाथियोन से रंग गोरा होता है?', 'नहीं। यह टैन और असमान रंगत को हल्का दिखाने में मदद कर सकता है, लेकिन आपका प्राकृतिक रंग नहीं बदलता।'),
              ('ग्लूटाथियोन क्रीम कितने दिन में असर करती है?', 'आमतौर पर 8 से 12 हफ्तों के नियमित उपयोग और रोज सनस्क्रीन के साथ बदलाव दिखता है।')]),
    dict(slug='glutathione-ke-nuksan', en='/glutathione-side-effects/',
         title='ग्लूटाथियोन के नुकसान और साइड इफेक्ट्स: क्या यह सुरक्षित है?', short='ग्लूटाथियोन के नुकसान',
         seo='Glutathione Ke Nuksan: ग्लूटाथियोन के साइड इफेक्ट्स और सुरक्षा',
         desc='Glutathione ke nuksan हिंदी में: ग्लूटाथियोन क्रीम, टैबलेट और इंजेक्शन के साइड इफेक्ट्स, किसे सावधान रहना चाहिए और पैच टेस्ट कैसे करें।',
         body='''<p>ग्लूटाथियोन <b>क्रीम और फेस वॉश</b> आमतौर पर ज्यादातर लोगों के लिए सुरक्षित माने जाते हैं। सबसे बड़ी चिंता <b>ग्लूटाथियोन इंजेक्शन</b> को लेकर है, क्रीम को लेकर नहीं।</p>
<h2>क्रीम के संभावित साइड इफेक्ट्स</h2><ul><li>शुरुआत में हल्की झुनझुनी, लालिमा या रूखापन, जो अक्सर ठीक हो जाता है।</li><li>लालिमा, खुजली या जलन लगातार रहे तो उपयोग बंद करें।</li><li>रैश या सूजन हो तो तुरंत बंद करें और डॉक्टर से मिलें।</li></ul><p>10 हफ्ते की स्टडी (%(study)s) में 30 में से केवल एक महिला को दो दिन हल्की लालिमा हुई, जो अपने आप ठीक हो गई।</p>
<h2>ग्लूटाथियोन इंजेक्शन से बचें</h2><p>%(fda)s के अनुसार त्वचा गोरी करने वाले इंजेक्शन असुरक्षित हो सकते हैं और उनमें अज्ञात पदार्थ हो सकते हैं। भारतीय डर्मेटोलॉजी समीक्षा (%(ijdvl)s) ने भी डॉक्टरों को त्वचा गोरी करने के लिए IV ग्लूटाथियोन न देने की सलाह दी है, क्योंकि इसके समर्थन में कोई क्लिनिकल ट्रायल नहीं है।</p>
<h2>किसे सावधान रहना चाहिए</h2><ul><li>गर्भवती या स्तनपान कराने वाली महिलाएं (रेटिनॉल वाली क्रीम डॉक्टर की सलाह के बिना नहीं)।</li><li>एक्जिमा, रोसेशिया या बहुत संवेदनशील त्वचा वाले लोग।</li><li>जो पहले से कोई प्रिस्क्रिप्शन क्रीम लगा रहे हैं।</li></ul>
<h2>पैच टेस्ट कैसे करें</h2><ol><li>कान के पीछे या बांह के अंदर थोड़ी क्रीम लगाएं।</li><li>24 घंटे इंतजार करें।</li><li>कोई प्रतिक्रिया न हो तो चेहरे पर धीरे-धीरे शुरू करें।</li></ol>''',
         faq=[('क्या ग्लूटाथियोन क्रीम सुरक्षित है?', 'ज्यादातर वयस्कों के लिए हां, जब निर्देशों के अनुसार उपयोग करें। पहले पैच टेस्ट करें।'),
              ('क्या ग्लूटाथियोन इंजेक्शन सुरक्षित हैं?', 'त्वचा गोरी करने के लिए इनके समर्थन में कोई क्लिनिकल ट्रायल नहीं है और नियामकों ने चेतावनी दी है। इनसे बचें।')]),
    dict(slug='glutathione-cream-kaise-lagaye', en='/how-to-use-glutathione-cream/',
         title='ग्लूटाथियोन क्रीम कैसे लगाएं: आसान नाइट रूटीन', short='ग्लूटाथियोन क्रीम कैसे लगाएं',
         seo='Glutathione Cream Kaise Lagaye: सही तरीका और नाइट रूटीन',
         desc='Glutathione cream kaise lagaye हिंदी में: रात का आसान रूटीन, कितनी मात्रा लगाएं, सुबह सनस्क्रीन क्यों जरूरी है और किन गलतियों से बचें।',
         body='''<p>ग्लूटाथियोन क्रीम को <b>रात में साफ और सूखी त्वचा</b> पर लगाएं और <b>सुबह सनस्क्रीन</b> जरूर लगाएं। यही पूरा रूटीन है।</p>
<h2>रात का रूटीन</h2><ol><li><b>चेहरा साफ करें:</b> %(wash)s जैसे हल्के फेस वॉश से चेहरा धोकर थपथपाकर सुखाएं।</li><li><b>क्रीम लगाएं:</b> मटर के दाने जितनी क्रीम माथे, गालों और ठोड़ी पर लगाकर पूरे चेहरे और गर्दन पर फैलाएं। आंखों से दूर रखें।</li><li><b>सोखने दें:</b> सोने से पहले कुछ मिनट रुकें।</li></ol>
<h2>सुबह</h2><p>चेहरा धोएं और SPF 30 या उससे अधिक वाला सनस्क्रीन लगाएं। धूप से नया टैन और दाग बनते रहते हैं, इसलिए यह कदम सबसे जरूरी है।</p>
<h2>धीरे शुरू करें</h2><p>%(cream)s में रेटिनॉल और सैलिसिलिक एसिड है, इसलिए पहले 2 हफ्ते इसे हफ्ते में 2–3 रात लगाएं, फिर त्वचा आरामदायक हो तो रोज। उसी रात दूसरा रेटिनॉल या एसिड प्रोडक्ट न लगाएं।</p>
<h2>इन गलतियों से बचें</h2><ul><li>बहुत ज्यादा क्रीम लगाना; इससे असर तेज नहीं होता।</li><li>सनस्क्रीन छोड़ देना।</li><li>नींबू, बेकिंग सोडा या टूथपेस्ट जैसे घरेलू नुस्खे।</li><li>हर हफ्ते प्रोडक्ट बदलना; एक रूटीन को 8 हफ्ते दें।</li></ul>''',
         faq=[('ग्लूटाथियोन क्रीम कब लगानी चाहिए?', 'रात में, चेहरा धोने के बाद। सुबह सनस्क्रीन लगाएं।'),
              ('क्या ग्लूटाथियोन क्रीम रोज लगा सकते हैं?', 'हां, जब त्वचा इसकी आदी हो जाए। रेटिनॉल वाली क्रीम को पहले हफ्ते में 2–3 बार से शुरू करें।')]),
]

# ---------------- "People also ask" pages ----------------
# Each question is written exactly as Google shows it, followed by a short direct answer (what Google lifts into the box)
# and then the detail. Rendered by content.py: qa items become H2 + answer, and FAQPage schema.
QA_PAGE = dict(
    slug='glutathione-cream-questions', title='Glutathione cream: answers to the most-asked questions', short='Glutathione cream questions',
    blurb='Straight answers to what people ask Google about glutathione cream: does it work, daily use, whitening, the best one, retinol and more.',
    seo='Glutathione Cream Questions: Does It Work, Daily Use, Best One',
    desc='Honest answers to the most-asked glutathione cream questions: what it is used for, does it work, can you use it daily, whitening, best brand, retinol vs glutathione.',
    refs=['study', 'review', 'ijdvl', 'fda'],
    qa=[
        ('What is glutathione cream used for?',
         'Glutathione cream is used to help skin look brighter and more even. It is applied to the face to support fading of tan, dullness and dark marks, and to add antioxidant protection against daily sun and pollution stress. It works gradually, alongside daily sunscreen.',
         '<p>Most glutathione creams combine glutathione with partners such as niacinamide, vitamin C and hyaluronic acid. See <a href="/glutathione-cream/">glutathione cream: what it is and how to choose one</a>.</p>'),
        ('Do glutathione creams really work?',
         'They can help, modestly. In a 10-week placebo-controlled study, a 2%% glutathione lotion reduced skin melanin more than placebo and was well tolerated. Reviews call topical glutathione promising but say studies are small, so expect gradual change over 8 to 12 weeks, not dramatic results.',
         '<p>Details: %(study)s; systematic review %(review)s. Daily sunscreen matters as much as the cream. Read <a href="/glutathione-benefits-for-skin/">glutathione benefits for skin</a>.</p>'),
        ('Can I use glutathione cream daily?',
         'Yes, most people can use a glutathione cream every day, usually at night on clean skin, with sunscreen every morning. If the cream also contains retinol or exfoliating acids, start 2 to 3 nights a week for two weeks, then increase if your skin is comfortable.',
         '<p>Patch test first. The GlutaNex Night Cream contains retinol and salicylic acid, so it follows the start-slow plan. Step by step: <a href="/how-to-use-glutathione-cream/">how to use glutathione cream</a>.</p>'),
        ('Is glutathione cream good for skin whitening?',
         'Glutathione cream can help tan, dark marks and uneven tone look lighter over weeks, but it does not change your natural skin colour. Any honest product will say so. Results depend on regular use and daily sunscreen, and fade if sun protection stops.',
         '<p>Avoid creams promising fast "whitening": some illegal fairness creams contain steroids, hydroquinone or mercury. Full guide: <a href="/glutathione-for-skin-whitening/">glutathione for skin whitening: what is true</a>.</p>'),
        ('Which night cream is best for whitening?',
         'No night cream safely changes natural skin colour. For tan and uneven tone, choose a night cream with proven brightening partners such as glutathione, niacinamide and vitamin C, a full ingredient list on the pack, realistic claims, and use sunscreen every morning.',
         '<p>Be wary of night creams that lighten very fast or sting badly. Use our <a href="/best-glutathione-cream-in-india/">7-point checklist</a> to judge any cream.</p>'),
        ('Which glutathione night cream is best?',
         'The best glutathione night cream is one with glutathione clearly listed, supporting ingredients such as niacinamide, hyaluronic acid and ceramides, clear night-use directions, honest claims and a seller you can contact. Use it consistently for at least 8 weeks with daily sunscreen.',
         '<p>%(cream)s combines glutathione with niacinamide, vitamin C, hyaluronic acid, retinol, ceramides, salicylic acid, peptides, aloe vera, turmeric and neem. Compare options with the <a href="/glutathione-night-cream/">glutathione night cream guide</a>.</p>'),
        ('Which brand of glutathione cream is best?',
         'There is no single best brand for everyone. Pick a brand that prints the full ingredient list, a batch number and expiry date, makes realistic claims, gives a real company address and return policy, and has a formula that suits your skin type.',
         '<p>Price is not proof of quality; see <a href="/glutathione-cream-price-in-india/">glutathione cream price in India</a> and the <a href="/best-glutathione-cream-in-india/">buying checklist</a>.</p>'),
        ('Which is better, retinol or glutathione?',
         'They do different jobs. Retinol has stronger evidence for smoother texture, fine lines and acne marks but can irritate. Glutathione is a gentler antioxidant used for brighter, more even-looking tone. Many routines use both, introduced slowly, at night, with daily sunscreen.',
         '<p>Full comparison: <a href="/retinol-vs-glutathione/">retinol vs glutathione</a>.</p>'),
        ('Is glutathione cream safe?',
         'Glutathione creams are generally well tolerated by most adults. Patch test first and stop if redness or burning lasts. Glutathione injections for skin lightening are different: they are not supported by clinical trials and regulators have issued warnings, so avoid them.',
         '<p>More: <a href="/is-glutathione-safe-for-skin/">is glutathione safe for skin?</a> and <a href="/glutathione-side-effects/">side effects</a>.</p>'),
        ('What do dermatologists say about glutathione cream?',
         'Dermatology reviews describe topical glutathione as promising and reasonably safe in short-term studies, but say the evidence is still limited and not enough to treat pigment disorders like melasma. They advise against glutathione injections for skin lightening.',
         '<p>Source: %(ijdvl)s and %(review)s. For melasma or patchy pigmentation, see a dermatologist.</p>'),
        ('How do I know if a glutathione cream is original?',
         'Buy from the brand\'s own website or an authorised seller, and check for a sealed pack, printed batch number, manufacturing and expiry dates, a full ingredient list and the manufacturer\'s address. Very low prices and blurry printing are warning signs of fakes.',
         '<p>GlutaNex is sold directly on this website by %(owner)s and ships sealed.</p>'),
        ('Is glutathione cream good for oily or sensitive skin?',
         'Yes, with the right formula. Oily skin suits a light, non-greasy texture, often with niacinamide or salicylic acid. Sensitive skin should start slowly, patch test, and avoid using retinol or acids every night at first.',
         '<p>See choosing by skin type in the <a href="/best-glutathione-cream-in-india/">buying guide</a>.</p>'),
    ])

NEW_GUIDES += [
    dict(slug='retinol-vs-glutathione', title='Retinol vs glutathione: which is better for your skin?', short='Retinol vs glutathione',
         blurb='What each one does, how they compare, and how to use both safely.',
         seo='Retinol vs Glutathione: Which Is Better & Can You Use Both?',
         desc='Retinol vs glutathione compared: what each does, evidence, irritation, who each suits, and how to use retinol and glutathione together safely at night.',
         refs=['study', 'review'],
         body='''<p><b>Short answer:</b> retinol and glutathione do different jobs. Retinol has stronger evidence for smoother texture, fine lines and acne marks, but it can irritate. Glutathione is a gentler antioxidant used for brighter, more even-looking tone. Many routines use both.</p>
<div class="tbl"><table><thead><tr><th></th><th>Retinol (vitamin A)</th><th>Glutathione</th></tr></thead><tbody>
<tr><td>Main use</td><td>Texture, fine lines, acne marks, clogged pores</td><td>Brighter, more even-looking tone; antioxidant support</td></tr>
<tr><td>How it works</td><td>Speeds up skin cell turnover</td><td>Slows melanin production and neutralises free radicals</td></tr>
<tr><td>Evidence</td><td>Strong, decades of research on retinoids</td><td>Promising but small studies (%(review)s)</td></tr>
<tr><td>Irritation</td><td>Common at first: dryness, peeling, redness</td><td>Generally gentle</td></tr>
<tr><td>When to use</td><td>Night only</td><td>Night or day, depending on the product</td></tr>
<tr><td>Pregnancy</td><td>Avoid unless your doctor approves</td><td>Ask your doctor</td></tr>
</tbody></table></div>
<h2>Which should you choose?</h2><ul><li><b>Mainly dull skin, tan or uneven tone:</b> start with glutathione.</li><li><b>Mainly texture, fine lines or acne marks:</b> retinol is the stronger option.</li><li><b>Both:</b> a routine with both, introduced slowly.</li></ul>
<h2>Using retinol and glutathione together</h2><ol><li>Use them at night, on clean dry skin.</li><li>Start 2 to 3 nights a week for two weeks, then every other night, then nightly if comfortable.</li><li>Moisturise if skin feels dry.</li><li>Sunscreen every morning: retinol makes skin more sun-sensitive.</li><li>Do not add another retinol or exfoliating acid product on the same night.</li></ol>
<p>%(cream)s already combines glutathione with retinol, niacinamide and soothing ingredients, so you do not need separate products.</p>''',
         faq=[('Can I use retinol and glutathione together?', 'Yes. Use them at night, start 2 to 3 nights a week, and use sunscreen every morning. Do not add another retinol product on the same night.'),
              ('Is glutathione gentler than retinol?', 'Generally yes. Retinol often causes dryness and peeling at first, while glutathione is usually well tolerated.')]),
    dict(slug='glutathione-night-cream', title='Glutathione night cream: how to choose and use one', short='Glutathione night cream',
         blurb='Why night is the best time for glutathione, what to look for, and options for oily and sensitive skin.',
         seo='Glutathione Night Cream: Benefits, How to Choose & Use (2026)',
         desc='Glutathione night cream guide: why use it at night, ingredients to look for, choosing for oily or sensitive skin, how to apply, and what results to expect.',
         refs=['study', 'review'],
         body='''<p>A <b>glutathione night cream</b> is a leave-on cream with glutathione designed for your evening routine. Night is a good time for brightening care: there is no sun exposure, and creams with retinol or exfoliating acids must be used at night anyway.</p>
<h2>Why use glutathione at night?</h2><ul><li>Skin repairs itself overnight, without sun and pollution.</li><li>Night creams can be richer and more nourishing.</li><li>Partners such as retinol and salicylic acid belong at night.</li></ul>
<h2>What to look for</h2><div class="tbl"><table><thead><tr><th>Ingredient</th><th>Why it helps at night</th></tr></thead><tbody>
<tr><td>Glutathione</td><td>Antioxidant for brighter, more even-looking tone</td></tr>
<tr><td>Niacinamide</td><td>Even tone and a stronger skin barrier</td></tr>
<tr><td>Hyaluronic acid and ceramides</td><td>Overnight hydration, less dryness from actives</td></tr>
<tr><td>Retinol</td><td>Smoother texture; start slowly</td></tr>
<tr><td>Peptides</td><td>Firmer, smoother-looking skin</td></tr>
</tbody></table></div>
<h2>Glutathione night cream for oily skin</h2><p>Choose a light, non-greasy texture. Niacinamide and salicylic acid help with shine and clogged pores. Apply a thin layer.</p>
<h2>Glutathione night cream for sensitive skin</h2><p>Patch test, start 2 to 3 nights a week, and avoid layering other actives. A soothing ingredient such as aloe vera helps. Stop if burning lasts.</p>
<h2>How to apply</h2><ol><li>Cleanse with a gentle face wash such as %(wash)s and pat dry.</li><li>Use a pea-sized amount on face and neck, avoiding eyes and lips.</li><li>Sunscreen every morning.</li></ol>
<h2>Results to expect</h2><p>Softer skin within days; a brighter, more even look over 4 to 8 weeks; tan and marks lighter over 8 to 12 weeks with daily sunscreen. The topical study used a 2%% glutathione lotion for 10 weeks (%(study)s).</p>
<p>Our pick: %(cream)s (30 g), made for night use.</p>''',
         faq=[('Is glutathione cream better at night or in the day?', 'Night is usually best, especially if the cream contains retinol or acids. Use sunscreen every morning.'),
              ('Which glutathione night cream is good for oily skin?', 'Look for a light texture with niacinamide or salicylic acid, applied as a thin layer.')]),
]

# "People also ask" for the search "glutathione" (11 Oct 2026), placed at the top of the pillar page.
PILLAR['qa'] = [
    ('What is glutathione used for?',
     'Glutathione is the body\'s own antioxidant. It protects cells from oxidative stress, recycles vitamins C and E, and helps the liver process toxins. In skincare it is used in creams and face washes for brighter, more even-looking skin, alongside daily sunscreen.',
     '<p>It is made from three amino acids: glutamic acid, cysteine and glycine. Levels fall with age, stress, smoking and sun exposure.</p>'),
    ('What does glutathione do for the skin?',
     'Glutathione slows tyrosinase, the enzyme that makes melanin, shifts pigment towards lighter forms and adds antioxidant protection. With regular use and sunscreen it can help tan, dullness and uneven tone look lighter over 8 to 12 weeks, but it does not change natural skin colour.',
     '<p>A 10-week study of a 2%% glutathione lotion found a modest drop in melanin index versus placebo (%(study)s). More: <a href="/glutathione-benefits-for-skin/">glutathione benefits for skin</a>.</p>'),
    ('Is glutathione permanent skin whitening?',
     'No. Glutathione does not permanently whiten skin. Any lightening of tan or uneven tone is gradual and fades if you stop or skip sunscreen, because skin keeps making melanin. Claims of permanent whitening, especially from injections, are not supported by clinical trials.',
     '<p>Regulators have warned against skin-lightening injections (%(fda)s). Read <a href="/glutathione-for-skin-whitening/">glutathione for skin whitening: what is true</a>.</p>'),
    ('What food is highest in glutathione?',
     'Among everyday foods, spinach, avocado, asparagus and okra (bhindi) contain the most glutathione. Garlic, onion, broccoli, cabbage, eggs, lentils and dairy supply the sulphur and amino acids your body uses to make it, and vitamin C foods like amla help keep it active.',
     '<p>Cooking lowers glutathione in vegetables, so include some raw or lightly cooked options. Full list: <a href="/glutathione-rich-foods/">glutathione-rich foods</a>.</p>'),
]

# "People also ask" / related searches for "glutathione benefits" (11 Oct 2026)
QA_EXTRA = {
    'glutathione-benefits-for-skin': [
        ('What are the benefits of glutathione?',
         'Glutathione is the body\'s main antioxidant: it protects cells from oxidative damage, recycles vitamins C and E, supports liver detoxification and immune cells. For skin, it can help tan, dullness and uneven tone look lighter and more even over weeks, used with daily sunscreen.',
         '<p>The skin benefits are modest and gradual in studies (%(study)s, %(oral)s).</p>'),
        ('Which diseases is glutathione good for?',
         'Glutathione is not a proven cure for any disease. Researchers study it in conditions linked to oxidative stress, such as some liver conditions, and doctors sometimes give it under medical supervision. Do not use glutathione to self-treat an illness; speak to a doctor first.',
         '<p>For skincare, glutathione is a cosmetic ingredient, not a medicine.</p>'),
    ],
    'glutathione-cream-vs-tablets-vs-injections': [
        ('What is the best glutathione supplement for skin?',
         'No glutathione supplement is proven best for skin. Small studies used 250 to 500 mg a day for 4 to 12 weeks and found modest, mixed changes in skin tone. Supplements are not regulated like medicines, so speak to a doctor before taking any, especially if pregnant.',
         '<p>For skincare, a glutathione cream is the simpler, lower-risk option. Studies: %(oral)s; %(wesch)s.</p>'),
        ('What is liposomal glutathione?',
         'Liposomal glutathione is glutathione wrapped in tiny fat-like bubbles called liposomes, designed to protect it from digestion and improve absorption. It is usually more expensive, and evidence that it gives better skin results than ordinary glutathione is still limited.',
         '<p>Ask a doctor before starting any supplement.</p>'),
        ('What is the recommended dose of glutathione for skin whitening?',
         'There is no officially recommended dose of glutathione for skin whitening. Published studies used 250 to 500 mg by mouth daily for 4 to 12 weeks, with only modest changes in skin tone. It does not permanently whiten skin. Ask a doctor before taking supplements, and avoid injections.',
         '<p>Regulators have warned against skin-lightening injections (%(fda)s). See <a href="/glutathione-for-skin-whitening/">glutathione and skin whitening: what is true</a>.</p>'),
        ('What is L-glutathione?',
         'L-glutathione is simply the natural form of glutathione, the same one your body makes. The "L" refers to the form of the amino acids it is built from. Most products labelled L-glutathione or reduced glutathione contain this active form.',
         '<p>In creams it may appear as glutathione or oxidised glutathione (GSSG). See <a href="/glutathione/">what is glutathione</a>.</p>'),
    ],
}

# "People also ask" / related searches for "glutathione side effects" (11 Oct 2026)
QA_EXTRA['glutathione-side-effects'] = [
    ('What are the serious side effects of glutathione?',
     'Serious side effects are rare and usually signs of an allergic reaction: breathing problems or wheezing, a racing heart, rash or swelling, fever and swollen lymph nodes. The highest risk is with glutathione injections. Stop using it and get medical help straight away if these happen.',
     '<p>People with asthma should not inhale glutathione, as it can trigger wheezing. Concerns reported with skin-lightening injections are covered by %(ijdvl)s.</p>'),
    ('What are the risks of taking glutathione?',
     'Glutathione creams and short courses of tablets are usually well tolerated. Possible risks include stomach upset, bloating and allergic reactions. Injections carry the biggest risks: unknown ingredients, infection and serious reactions. Long-term safety of high doses, and safety in pregnancy, are not well studied.',
     '<p>The %(fda)s covers injectable skin-lightening products. Talk to a doctor before taking any supplement.</p>'),
    ('Is glutathione safe for your liver?',
     'Your liver naturally makes and uses glutathione, and short studies of oral glutathione found it generally safe. In one 12-week study, two people had temporary rises in liver tests that settled. Glutathione creams are not linked to liver problems. If you have liver disease, ask your doctor first.',
     '<p>Study: %(wesch)s.</p>'),
    ('What will happen if I take glutathione daily?',
     'Daily use of a glutathione cream is fine for most people and may gradually help skin look brighter and more even, with sunscreen. Daily oral doses in studies were well tolerated for 4 to 12 weeks, but long-term effects are not well known, so check with a doctor.',
     '<p>Results fade if you stop and skip sun protection. See <a href="/how-to-use-glutathione-cream/">how to use glutathione cream</a>.</p>'),
    ('What to avoid when taking glutathione?',
     'Avoid glutathione injections from salons or unlicensed sellers, high-dose supplements without medical advice, and inhaled glutathione if you have asthma. With creams, avoid layering other retinol or acid products the same night and never skip sunscreen. Tell your doctor if you are pregnant or on chemotherapy.',
     '<p>Smoking and heavy drinking also use up the body\'s own glutathione.</p>'),
    ('What are the side effects of glutathione tablets?',
     'Glutathione tablets usually cause no problems in short courses. When side effects happen they are mild: stomach cramps, bloating, loose stools or, rarely, an allergic reaction such as rash or itching. Stop taking them if you react, and speak to a doctor before starting.',
     '<p>Compare forms: <a href="/glutathione-cream-vs-tablets-vs-injections/">cream vs tablets vs injections</a>.</p>'),
    ('What are the side effects of glutathione on skin?',
     'On skin, glutathione creams can cause mild tingling, redness or dryness at first, especially when combined with retinol or acids, and rarely a rash. Patch test before use and stop if irritation lasts. Patchy loss of skin colour has been reported with injections, not creams.',
     '<p>How to patch test is explained below.</p>'),
]

# "glutathione tablets" (11 Oct 2026): its own page, questions first
NEW_GUIDES.append(dict(slug='glutathione-tablets', title='Glutathione tablets: benefits, safety, dose and do they work for skin?', short='Glutathione tablets',
    blurb='What glutathione tablets can and cannot do for skin, what the studies used, safety, and how they compare with a cream.',
    seo='Glutathione Tablets: Benefits, Safety, Dose & Do They Work?',
    desc='Glutathione tablets explained: skin benefits, doses used in studies, daily safety, kidneys and liver, 1000 mg tablets, spotting originals, and tablets vs cream.',
    refs=['oral', 'wesch', 'ijdvl', 'review', 'fda'],
    body='''<h2>How glutathione tablets compare with a cream</h2><div class="tbl"><table><thead><tr><th></th><th>Tablets</th><th>Cream</th></tr></thead><tbody>
<tr><td>How it reaches skin</td><td>Swallowed; much is broken down in digestion</td><td>Applied directly where you want it</td></tr>
<tr><td>Evidence for skin</td><td>Small studies, mixed results (%(oral)s, %(wesch)s)</td><td>Small studies, modest gradual effect (%(review)s)</td></tr>
<tr><td>Main risks</td><td>Stomach upset; ask a doctor first</td><td>Mild irritation in some people</td></tr>
<tr><td>Who decides</td><td>Best with medical advice</td><td>Most adults, after a patch test</td></tr>
</tbody></table></div>
<h2>Who should not take glutathione tablets without a doctor</h2><ul><li>Pregnant or breastfeeding women.</li><li>People with liver or kidney disease, asthma, or on chemotherapy or other regular medicines.</li><li>Children and teenagers.</li></ul>
<h2>A simpler option for skin</h2><p>If your goal is brighter, more even-looking skin, a leave-on cream puts glutathione where you want it, with no pills to swallow. %(cream)s pairs glutathione with niacinamide, vitamin C and hyaluronic acid. Use it at night with sunscreen every morning.</p>''',
    faq=[]))
QA_EXTRA['glutathione-tablets'] = [
    ('What are the benefits of glutathione tablets?',
     'Glutathione tablets are taken to support the body\'s antioxidant defences, and some people use them for skin tone. Small studies found modest drops in skin melanin with 250 to 500 mg a day over 4 to 12 weeks, but results were mixed. They do not permanently change skin colour.',
     '<p>Studies: %(oral)s (500 mg/day, 4 weeks) and %(wesch)s (250 mg/day, 12 weeks).</p>'),
    ('Is glutathione safe to take daily?',
     'Short courses of daily glutathione tablets, 4 to 12 weeks in studies, were generally well tolerated, with mostly mild side effects. Long-term daily use has not been well studied. Speak to a doctor before taking it every day, especially if pregnant, on medicines or with a health condition.',
     '<p>Glutathione creams can be used daily by most adults after a patch test.</p>'),
    ('Which glutathione tablet is best for skin whitening?',
     'No glutathione tablet is proven best for skin whitening, and none permanently whitens skin. Studies used 250 to 500 mg a day and found only modest changes in tone. If you consider tablets, choose a reputable brand with full labelling, and ask a doctor first.',
     '<p>For tan and uneven tone, daily sunscreen and a leave-on cream are the simplest start. See <a href="/glutathione-for-skin-whitening/">glutathione and skin whitening: what is true</a>.</p>'),
    ('Is glutathione safe for the kidneys and liver?',
     'In short studies, oral glutathione was generally safe; one 12-week study saw temporary liver test rises in two people that settled. Kidney problems were not reported, but research is limited. If you have liver or kidney disease, do not take glutathione without your doctor\'s advice.',
     '<p>Study: %(wesch)s. Creams are not linked to liver or kidney problems.</p>'),
    ('Are glutathione tablets 1000 mg better for skin whitening?',
     'There is no evidence that 1000 mg glutathione tablets work better for skin than lower doses. Published skin studies used 250 to 500 mg a day with modest results. Higher doses may increase side effects and cost. Ask a doctor before taking high-dose supplements.',
     '<p>More is not faster: skin tone changes slowly whatever the dose.</p>'),
    ('How do I choose glutathione tablets in India?',
     'Choose tablets with an FSSAI licence number, the glutathione amount per tablet clearly stated, batch number, manufacturing and expiry dates, and the manufacturer\'s address. Avoid products promising "fair in 7 days". Buy from authorised sellers, and check with a doctor that tablets are right for you.',
     '<p>Supplements in India are regulated as foods, not medicines, so labels matter.</p>'),
    ('How can I tell if glutathione tablets are original?',
     'Original glutathione tablets come sealed with a printed batch number, manufacturing and expiry dates, an FSSAI licence number and the manufacturer\'s address. Check that these match the brand\'s website. Very low prices, spelling mistakes and missing details are warning signs of fakes.',
     '<p>Buy from the brand or an authorised seller.</p>'),
]

# "glutathione face wash" (11 Oct 2026)
QA_EXTRA['glutathione-face-wash'] = [
    ('Is glutathione face wash good for skin?',
     'Yes, a gentle glutathione face wash is good for most skin types. It cleans away oil, sweat and pollution without stripping, and prepares skin for a leave-on cream. Because it is rinsed off quickly, it mainly cleans and refreshes; visible brightening needs a cream and daily sunscreen.',
     '<p>Our %(wash)s (100 ml) is designed as the first step before the Night Cream.</p>'),
    ('Which glutathione face wash is best for skin whitening?',
     'No face wash can whiten skin, because it stays on for under a minute. Choose a gentle, non-drying glutathione face wash with a clear ingredient list, then follow with a leave-on glutathione cream at night and sunscreen every morning for tan and uneven tone.',
     '<p>Avoid washes that leave skin tight or squeaky: over-cleansing can make dullness and marks worse. See <a href="/glutathione-for-skin-whitening/">glutathione and skin whitening: what is true</a>.</p>'),
    ('Is glutathione good for your face?',
     'Yes. Glutathione is a gentle antioxidant that suits facial skin. Used in a cream with daily sunscreen, it can help tan, dullness and uneven tone look lighter and more even over 8 to 12 weeks. Patch test first, and avoid injections.',
     '<p>More: <a href="/glutathione-benefits-for-skin/">glutathione benefits for skin</a>.</p>'),
    ('How to use glutathione for skin whitening?',
     'Use glutathione as a routine, not a quick fix: cleanse with a gentle face wash, apply a glutathione cream at night, and use SPF 30 or higher every morning. Give it 8 to 12 weeks. It can lighten tan and uneven tone, but it does not change natural skin colour.',
     '<p>Step by step: <a href="/how-to-use-glutathione-cream/">how to use glutathione cream</a>. If your cream contains retinol, start 2 to 3 nights a week.</p>'),
    ('Is glutathione face wash good for oily and acne-prone skin?',
     'A gentle glutathione face wash suits oily and acne-prone skin when used twice a day and followed by a light, non-greasy moisturiser. It helps clear oil and grime without over-drying. For active acne, pair it with proven acne care and see a dermatologist if breakouts persist.',
     '<p>Do not scrub hard or wash more than twice a day: it can trigger more oil.</p>'),
]

# "best glutathione cream in india" (11 Oct 2026)
QA_EXTRA['best-glutathione-cream-in-india'] = [
    ('Which glutathione brand is best in India?',
     'No single glutathione brand is best for everyone in India. The right one prints its full ingredient list, batch and expiry details and company address, makes realistic claims, offers returns, and suits your skin type. Use it nightly for 8 weeks with daily sunscreen before judging.',
     '<p>Use the 7-point checklist below to compare any brand, including ours.</p>'),
    ('Which cream is no. 1 for skin whitening in India?',
     'There is no officially "no. 1" skin whitening cream in India, and no safe cream changes natural skin colour. For tan and uneven tone, look for gentle brightening ingredients such as glutathione, niacinamide and vitamin C, avoid creams that lighten within days, and use sunscreen daily.',
     '<p>Creams that work "too fast" may contain steroids, hydroquinone or mercury. Read <a href="/glutathione-for-skin-whitening/">glutathione and skin whitening: what is true</a>.</p>'),
    ('Is glutathione cream good for skin whitening?',
     'Glutathione cream can help tan and uneven tone look lighter and more even over 8 to 12 weeks, especially with daily sunscreen, but it will not change your natural skin colour. Small studies show modest, gradual effects. Be wary of any cream promising fast or permanent whitening.',
     '<p>More answers: <a href="/glutathione-cream-questions/">glutathione cream questions</a>.</p>'),
    ('What brand of glutathione is best?',
     'The best glutathione brand is one that is transparent and suits your needs: a full ingredient list, clear glutathione content, sealed packs with batch and expiry dates, honest claims and a contactable seller. For skin, a leave-on cream is the simplest choice; for supplements, ask a doctor.',
     '<p>See also <a href="/glutathione-tablets/">glutathione tablets</a> and <a href="/glutathione-cream-price-in-india/">glutathione cream price in India</a>.</p>'),
    ('Is there a good glutathione cream under ₹200?',
     'Some basic glutathione creams cost under ₹200, but they are usually small tubes with short ingredient lists and little or unstated glutathione. Compare price per gram and the full formula, and avoid unbranded creams with no address or batch number, which may contain banned ingredients.',
     '<p>How prices work: <a href="/glutathione-cream-price-in-india/">glutathione cream price in India</a>.</p>'),
]

# Google "People also ask" for "glutathione cream ke fayde" (Hindi, 11 Oct 2026)
HI_QA = {
    'glutathione-cream-ke-fayde': [
        ('ग्लूटाथियोन को त्वचा को गोरा करने में कितना समय लगता है?',
         'ग्लूटाथियोन आपका प्राकृतिक रंग गोरा नहीं करता। क्रीम के नियमित उपयोग और रोज सनस्क्रीन के साथ टैन और असमान रंगत आमतौर पर 8 से 12 हफ्तों में हल्की दिखने लगती है। स्टडी में 4 से 12 हफ्तों में हल्का बदलाव दिखा। कुछ दिनों में गोरा करने के दावों से बचें।',
         '<p>स्टडी: %(study)s।</p>'),
        ('त्वचा को गोरा करने के लिए सबसे अच्छी ग्लूटाथियोन गोलियाँ कौन सी हैं?',
         'कोई भी ग्लूटाथियोन गोली त्वचा को स्थायी रूप से गोरा नहीं करती, और कोई भी "सबसे अच्छी" साबित नहीं है। स्टडी में रोज 250 से 500 mg लेने पर रंगत में केवल हल्का बदलाव दिखा। गोलियां लेने से पहले डॉक्टर से सलाह लें, खासकर गर्भावस्था या किसी बीमारी में।',
         '<p>अधिक जानकारी (अंग्रेजी में): <a href="/glutathione-tablets/" lang="en">Glutathione tablets</a>।</p>'),
        ('गोरा चेहरा साफ करने के लिए कौन सी क्रीम अच्छी है?',
         'साफ और चमकदार चेहरे के लिए हल्के फेस वॉश के बाद रात में ग्लूटाथियोन, नियासिनामाइड या विटामिन C वाली क्रीम और सुबह सनस्क्रीन एक अच्छा रूटीन है। ऐसी क्रीम से बचें जो कुछ दिनों में रंग बहुत तेजी से बदल दे, उनमें स्टेरॉयड या मरकरी हो सकता है।',
         '<p>GlutaNex Night Cream में ग्लूटाथियोन, नियासिनामाइड और विटामिन C हैं: %(cream)s।</p>'),
    ],
    'glutathione-ke-nuksan': [
        ('ग्लूटाथिओन के क्या नुकसान हैं?',
         'ग्लूटाथियोन क्रीम आमतौर पर सुरक्षित है; कुछ लोगों को शुरुआत में हल्की जलन, लालिमा या रूखापन हो सकता है। गोलियों से पेट खराब या एलर्जी हो सकती है। सबसे ज्यादा खतरा इंजेक्शन से है। सांस फूलना, सूजन या रैश हो तो तुरंत डॉक्टर से मिलें।',
         '<p>नियामकों ने त्वचा गोरी करने वाले इंजेक्शन के बारे में चेतावनी दी है: %(fda)s।</p>'),
    ],
    'glutathione-cream-kaise-lagaye': [
        ('त्वचा को गोरा करने के लिए ग्लूटाथियोन क्रीम का उपयोग कैसे करें?',
         'रात में चेहरा धोकर सुखाएं, मटर के दाने जितनी ग्लूटाथियोन क्रीम चेहरे और गर्दन पर लगाएं, और सुबह SPF 30 या उससे अधिक वाला सनस्क्रीन लगाएं। 8 से 12 हफ्ते नियमित उपयोग करें। यह टैन और असमान रंगत हल्की कर सकती है, लेकिन प्राकृतिक रंग नहीं बदलती।',
         '<p>रेटिनॉल वाली क्रीम को पहले 2 हफ्ते, हफ्ते में 2–3 रात ही लगाएं।</p>'),
    ],
}

# ---------------- Comparison pages ----------------
def _cmp(slug, other, short_other, rows, body_extra, faq, seo, desc):
    head = ''.join('<tr><td>%s</td><td>%s</td><td>%s</td></tr>' % r for r in rows)
    return dict(slug=slug, title='Glutathione vs %s: which is better for your skin?' % other, short='Glutathione vs %s' % short_other,
                blurb='How glutathione and %s compare, who each suits, and whether to use them together.' % other.lower() if other[0].isupper() and other not in ('Vitamin C',) else 'How glutathione and %s compare, who each suits, and whether to use them together.' % other,
                seo=seo, desc=desc, refs=['ijdvl', 'review'],
                body='<div class="tbl"><table><thead><tr><th></th><th>Glutathione</th><th>%s</th></tr></thead><tbody>%s</tbody></table></div>%s' % (other, head, body_extra),
                faq=faq)

NEW_GUIDES += [
    _cmp('glutathione-vs-vitamin-c', 'Vitamin C', 'vitamin C',
         [('What it is', 'Antioxidant tripeptide the body makes', 'Antioxidant vitamin (ascorbic acid and its forms)'),
          ('Main skin use', 'Brighter, more even-looking tone', 'Brightness, antioxidant protection, firmer-looking skin'),
          ('How it works', 'Slows tyrosinase; shifts melanin to lighter forms', 'Slows tyrosinase; neutralises free radicals; supports collagen'),
          ('Evidence', 'Small studies, modest effect', 'Well studied in skincare'),
          ('Best time', 'Night (or as directed)', 'Morning, under sunscreen'),
          ('Watch out for', 'Mild irritation in some people', 'Can sting; pure forms oxidise and turn brown')],
         '''<h2>Which is better?</h2><p>Neither replaces the other. Vitamin C has stronger evidence as a daytime antioxidant and brightener; glutathione is a gentle option for tan and uneven tone, often used at night. They also work together: vitamin C helps keep glutathione in its active form.</p>
<h2>How to use both</h2><ul><li><b>Morning:</b> cleanser → vitamin C serum (optional) → sunscreen.</li><li><b>Night:</b> cleanser → glutathione cream.</li></ul><p>%(cream)s already includes vitamin C alongside glutathione and niacinamide.</p>''',
         [('Can I use glutathione and vitamin C together?', 'Yes. Vitamin C helps keep glutathione active. Many products combine them; if you use separate ones, vitamin C in the morning and glutathione at night is a simple split.'),
          ('Is vitamin C better than glutathione for skin?', 'Vitamin C has more research behind it as a brightening antioxidant, while glutathione is a gentle option for tan and uneven tone. Using both often works best.')],
         'Glutathione vs Vitamin C: Which Is Better & Can You Use Both?', 'Glutathione vs vitamin C compared: how each brightens skin, evidence, best time to use, irritation, and how to use glutathione and vitamin C together.'),
    _cmp('glutathione-vs-niacinamide', 'niacinamide', 'niacinamide',
         [('What it is', 'Antioxidant tripeptide', 'Vitamin B3'),
          ('Main skin use', 'Brighter, more even-looking tone', 'Even tone, smaller-looking pores, oil control, stronger barrier'),
          ('How it works', 'Works early in melanin production', 'Reduces pigment transfer to surface skin cells'),
          ('Evidence', 'Small studies, modest effect', 'Well studied at 2–5%%'),
          ('Gentleness', 'Generally gentle', 'Generally gentle; may tingle at first'),
          ('Best for', 'Tan, dullness', 'Oily skin, uneven tone, sensitive barrier')],
         '''<h2>Which is better?</h2><p>They complement each other: glutathione acts early in melanin production, niacinamide reduces how much pigment reaches the skin surface. Together they target uneven tone from two directions, and both suit most skin types.</p>
<h2>Using them together</h2><p>Yes, they are often combined in one product, such as %(cream)s. Apply at night on clean skin and use sunscreen every morning.</p>''',
         [('Can I use glutathione and niacinamide together?', 'Yes. They work in different ways on pigment and are both generally gentle, which is why many creams combine them.'),
          ('Which is better for oily skin, glutathione or niacinamide?', 'Niacinamide is better known for oil control and pores; glutathione adds brightening. A light cream with both suits oily skin well.')],
         'Glutathione vs Niacinamide: Differences & Using Them Together', 'Glutathione vs niacinamide compared: how each evens skin tone, evidence, oily and sensitive skin, and why glutathione and niacinamide work well together.'),
    _cmp('glutathione-vs-alpha-arbutin', 'alpha arbutin', 'alpha arbutin',
         [('What it is', 'Antioxidant tripeptide', 'Plant-derived brightening ingredient related to hydroquinone, but much gentler'),
          ('Main skin use', 'Overall brighter, even-looking tone', 'Dark spots and patches'),
          ('How it works', 'Slows tyrosinase; antioxidant', 'Slows tyrosinase'),
          ('Evidence', 'Small studies', 'Small to moderate studies'),
          ('Gentleness', 'Generally gentle', 'Generally gentle at usual cosmetic levels'),
          ('Best for', 'Dullness, tan, antioxidant support', 'Targeted dark spots')],
         '''<h2>Which is better?</h2><p>Alpha arbutin is often chosen for specific dark spots, while glutathione suits overall dullness and tan and adds antioxidant protection. Both are gentle options compared with prescription lighteners.</p>
<h2>Can you combine them?</h2><p>Yes, many brightening products contain both. Introduce one new product at a time, patch test, and keep using sunscreen daily.</p>''',
         [('Is alpha arbutin better than glutathione for dark spots?', 'Alpha arbutin is often used for targeted dark spots, while glutathione suits overall tone. Both work gradually with daily sunscreen.'),
          ('Can I use alpha arbutin and glutathione together?', 'Yes, they are commonly combined. Patch test first and add one new product at a time.')],
         'Glutathione vs Alpha Arbutin: Which Is Better for Dark Spots?', 'Glutathione vs alpha arbutin compared: how each works on dark spots and uneven tone, gentleness, evidence, and whether to use them together.'),
    _cmp('glutathione-vs-hydroquinone', 'hydroquinone', 'hydroquinone',
         [('What it is', 'Cosmetic antioxidant', 'Strong skin-lightening medicine'),
          ('Availability in India', 'Sold in cosmetics', 'Sold as a prescription medicine'),
          ('Strength', 'Gentle, gradual', 'Strong; used for conditions like melasma'),
          ('Main risks', 'Mild irritation in some people', 'Irritation; with long misuse, a bluish-dark discolouration (ochronosis)'),
          ('Use', 'Everyday skincare', 'Only under a dermatologist, for a limited time'),
          ('In cosmetics', 'Allowed', 'Not allowed in cosmetics in many countries')],
         '''<h2>Which is better?</h2><p>They are not alternatives for everyday care. Hydroquinone is a prescription treatment that a dermatologist may use for a limited time for conditions such as melasma. Glutathione is a gentle cosmetic ingredient for everyday brightening.</p>
<h2>Watch out for hidden hydroquinone</h2><p>Some unbranded "fairness" creams sold in India contain hydroquinone, often mixed with steroids, without saying so. Misuse can cause thinning, acne and patchy, darker skin. Avoid creams that lighten very fast or have no full ingredient list.</p>
<p>Prefer a gentle, clearly labelled routine: %(cream)s at night and sunscreen every morning.</p>''',
         [('Is glutathione safer than hydroquinone?', 'For everyday use, yes. Glutathione is a gentle cosmetic ingredient, while hydroquinone is a strong prescription medicine that should be used only under a dermatologist.'),
          ('Can I use hydroquinone without a prescription?', 'In India hydroquinone is a prescription medicine. Use it only if a dermatologist prescribes it, for the time they advise.')],
         'Glutathione vs Hydroquinone: Safety, Strength & Which to Use', 'Glutathione vs hydroquinone compared: strength, safety, prescription status in India, risks of misuse, and why gentle glutathione suits everyday care.'),
]

# ---------------- "Who is it for" pages ----------------
NEW_GUIDES += [
    dict(slug='glutathione-cream-for-men', title='Glutathione cream for men: does it work and how to use it', short='For men',
         blurb='Why men use glutathione cream, how to fit it around shaving, and what to expect.',
         seo='Glutathione Cream for Men: Skin Brightening Cream Guide', desc='Glutathione cream for men: benefits for tan, dullness and oily skin, how to use it around shaving, a simple routine and realistic results.',
         refs=['study'],
         body='''<p>Glutathione cream works the same way for men as for women. Men often have oilier skin, more sun exposure from commuting and sport, and razor irritation, so a few adjustments help.</p>
<h2>Why men use it</h2><ul><li>Tan from bikes, sport and outdoor work.</li><li>Dull, tired-looking skin.</li><li>Dark marks after pimples or ingrown hairs.</li></ul>
<h2>A simple routine for men</h2><ol><li><b>Night:</b> wash with a gentle face wash such as %(wash)s, then a pea-sized amount of %(cream)s.</li><li><b>Morning:</b> wash and apply a light, non-greasy sunscreen.</li></ol>
<h2>Around shaving</h2><p>Freshly shaved skin can sting. Shave in the morning and apply the night cream at night, or wait a few hours after shaving. Skip the cream on any nicks.</p>
<h2>What to expect</h2><p>Softer skin within days; a brighter, more even look over 4 to 8 weeks; tan lighter over 8 to 12 weeks with daily sunscreen.</p>''',
         faq=[('Can men use glutathione cream?', 'Yes. It works the same for men; use it at night and sunscreen every morning.'), ('Can I use glutathione cream after shaving?', 'Wait until the skin has settled, ideally apply at night if you shave in the morning, and avoid nicks.')]),
    dict(slug='glutathione-for-acne-marks', title='Glutathione for acne marks: does it help?', short='Acne marks',
         blurb='What causes dark marks after pimples, how glutathione fits in, and how long they take to fade.',
         seo='Glutathione for Acne Marks & Pimple Spots: Does It Help?', desc='Does glutathione help acne marks? What causes dark spots after pimples, how glutathione, niacinamide and sunscreen help, timelines and when to see a dermatologist.',
         refs=['study', 'ijdvl'],
         body='''<p>The flat brown marks left after pimples are called post-inflammatory hyperpigmentation. They are very common on Indian skin and usually fade on their own, slowly. A glutathione routine with daily sunscreen can help them look lighter sooner.</p>
<h2>Marks vs scars</h2><ul><li><b>Marks:</b> flat brown or dark spots. Brightening care helps.</li><li><b>Scars:</b> dents or raised bumps. Creams do not fix these; a dermatologist can.</li></ul>
<h2>A routine that helps</h2><ol><li>Do not pick or squeeze pimples; it makes marks darker and longer-lasting.</li><li>At night, a cream with glutathione, niacinamide and salicylic acid, such as %(cream)s.</li><li>Sunscreen every morning: sun makes marks darker.</li></ol>
<h2>How long it takes</h2><p>New marks often lighten in 6 to 12 weeks; older ones may take months and may fade only partly.</p>
<h2>When to see a dermatologist</h2><p>If you still get many new pimples, or have painful, deep acne, treat the acne first with a doctor's help.</p>''',
         faq=[('Does glutathione remove pimple marks?', 'It can help flat dark marks look lighter over 6 to 12 weeks with daily sunscreen; it does not fix dented or raised scars.'), ('Is glutathione cream good for acne-prone skin?', 'A light formula with niacinamide or salicylic acid suits acne-prone skin; introduce it slowly and patch test.')]),
    dict(slug='glutathione-for-oily-skin', title='Glutathione for oily skin: how to choose and use it', short='Oily skin',
         blurb='The right texture and partners for oily, shiny skin, and mistakes to avoid.',
         seo='Glutathione Cream for Oily Skin: How to Choose & Use', desc='Glutathione for oily skin: choosing a light texture, helpful partners like niacinamide and salicylic acid, how much to apply, and mistakes that make oiliness worse.',
         refs=['review'],
         body='''<p>Oily skin can use glutathione happily; the key is a light, non-greasy formula and not over-washing.</p>
<h2>What to look for</h2><ul><li>A light cream or gel-cream texture.</li><li><b>Niacinamide</b> for shine and pores.</li><li><b>Salicylic acid</b> to keep pores clear.</li><li>Hyaluronic acid for oil-free hydration.</li></ul>
<h2>How to use</h2><ol><li>Cleanse with a gentle face wash, such as %(wash)s, morning and night.</li><li>Apply a thin layer of glutathione cream at night.</li><li>Use a light, matte sunscreen every morning.</li></ol>
<h2>Mistakes to avoid</h2><ul><li>Washing more than twice a day or scrubbing hard, which triggers more oil.</li><li>Skipping moisturiser: dehydrated skin can look oilier.</li><li>Layering many actives at once.</li></ul>''',
         faq=[('Is glutathione good for oily skin?', 'Yes, in a light, non-greasy formula, ideally with niacinamide or salicylic acid.'), ('Will glutathione cream make my face oily?', 'A thin layer of a light formula should not. Apply at night and use a matte sunscreen in the morning.')]),
    dict(slug='glutathione-cream-for-summer-tan', title='Glutathione cream for summer tan: a simple routine', short='Summer tan',
         blurb='How to protect your skin in Indian summers and help tan fade faster.',
         seo='Glutathione Cream for Summer Tan: Routine & Sun Protection Tips', desc='How to remove summer tan with a glutathione routine: sunscreen that works in Indian heat, reapplying, night care, how long tan takes to fade and what to avoid.',
         refs=['study'],
         body='''<p>Summer tan fades on its own once you protect your skin; a glutathione night cream can help it look lighter sooner. Sun protection does most of the work.</p>
<h2>Daytime: protect</h2><ul><li>Broad-spectrum sunscreen, SPF 30 or higher with a high PA rating (PA+++ or more).</li><li>Use enough: about two finger-lengths for face and neck.</li><li>Reapply every 2 to 3 hours outdoors, and after sweating.</li><li>Cap, sunglasses and shade at midday.</li></ul>
<h2>Night: care</h2><p>Cleanse with %(wash)s, then apply %(cream)s. On sunburnt or peeling skin, pause actives and use a plain moisturiser until it calms.</p>
<h2>How long tan takes to fade</h2><p>Usually a few weeks once you protect your skin consistently; deep tan from months outdoors can take longer.</p>
<h2>Avoid</h2><p>Lemon juice, baking soda, harsh scrubs and bleach creams: they irritate skin and can leave it patchy.</p>''',
         faq=[('How can I remove summer tan fast?', 'Protect your skin daily with SPF 30+ sunscreen and reapply outdoors; a glutathione night cream can help tan look lighter within a few weeks.'), ('Can I use glutathione cream on sunburnt skin?', 'Wait until sunburn has healed; use a plain, soothing moisturiser meanwhile.')]),
    dict(slug='glutathione-in-pregnancy', title='Is glutathione safe in pregnancy?', short='Pregnancy',
         blurb='What is known about glutathione, retinol and skincare during pregnancy and breastfeeding.',
         seo='Is Glutathione Safe in Pregnancy? Creams, Tablets & Injections', desc='Glutathione in pregnancy: what is known about creams, tablets and injections, why retinol should be avoided, safer routine ideas and why to ask your doctor.',
         refs=['ijdvl', 'fda'],
         body='''<p><b>Short answer:</b> the safety of glutathione during pregnancy and breastfeeding has not been well studied, so speak to your doctor before using any glutathione product. Avoid glutathione injections and avoid creams containing retinol.</p>
<h2>Creams</h2><p>Little glutathione is absorbed from a cream, but many glutathione creams also contain other actives. <b>Retinol (vitamin A)</b> is generally avoided in pregnancy. The GlutaNex Night Cream contains retinol and salicylic acid, so do not use it while pregnant or breastfeeding unless your doctor says it is fine.</p>
<h2>Tablets and injections</h2><p>There are no good safety studies of glutathione supplements in pregnancy. Injections carry extra risks and warnings (%(fda)s); avoid them.</p>
<h2>Pregnancy-friendly basics</h2><ul><li>A gentle cleanser and a simple moisturiser.</li><li>Sunscreen every day; pregnancy can make skin more prone to dark patches (melasma).</li><li>Ask your doctor or dermatologist before adding any active ingredient.</li></ul>''',
         faq=[('Can I use glutathione cream during pregnancy?', 'Ask your doctor first. Avoid creams with retinol, such as the GlutaNex Night Cream, while pregnant or breastfeeding.'), ('Are glutathione tablets safe in pregnancy?', 'They have not been studied well in pregnancy. Do not take them without your doctor\'s advice.')]),
]

# ---------------- More Hindi pages ----------------
HI += [
    dict(slug='glutathione-kya-hai', en='/glutathione/',
         title='ग्लूटाथियोन क्या है? त्वचा के लिए पूरी जानकारी', short='ग्लूटाथियोन क्या है',
         seo='Glutathione Kya Hai: ग्लूटाथियोन क्या है, फायदे और उपयोग',
         desc='Glutathione kya hai हिंदी में: ग्लूटाथियोन क्या है, शरीर और त्वचा में क्या करता है, क्रीम, गोली और इंजेक्शन में फर्क, और सुरक्षित उपयोग।',
         body='''<p><b>ग्लूटाथियोन</b> एक एंटीऑक्सीडेंट है जो हमारा शरीर खुद बनाता है, ज्यादातर लिवर में। इसे शरीर का "मास्टर एंटीऑक्सीडेंट" कहा जाता है क्योंकि यह कोशिकाओं को नुकसान से बचाता है और विटामिन C व E को फिर से सक्रिय करता है।</p>
<h2>ग्लूटाथियोन किससे बनता है?</h2><p>यह तीन अमीनो एसिड से बना है: ग्लूटामिक एसिड, सिस्टीन और ग्लाइसिन। उम्र, तनाव, धूम्रपान, शराब और तेज धूप से इसका स्तर कम हो सकता है।</p>
<h2>त्वचा पर ग्लूटाथियोन कैसे काम करता है?</h2><ul><li>मेलानिन बनाने वाले एंजाइम (टायरोसिनेज) को धीमा करता है।</li><li>गहरे मेलानिन को हल्के रूप की ओर ले जाता है।</li><li>धूप और प्रदूषण से होने वाले नुकसान से बचाता है।</li></ul><p>इसलिए यह टैन और असमान रंगत को हल्का दिखाने वाले प्रोडक्ट्स में इस्तेमाल होता है। यह आपका प्राकृतिक रंग नहीं बदलता।</p>
<h2>क्रीम, गोली और इंजेक्शन में फर्क</h2><div class="tbl"><table><thead><tr><th></th><th>क्रीम</th><th>गोली</th><th>इंजेक्शन</th></tr></thead><tbody>
<tr><td>सबूत</td><td>छोटी स्टडी, धीरे-धीरे हल्का असर</td><td>छोटी स्टडी, मिले-जुले नतीजे</td><td>त्वचा गोरी करने के लिए कोई ट्रायल नहीं</td></tr>
<tr><td>सुरक्षा</td><td>आमतौर पर सुरक्षित, पहले पैच टेस्ट</td><td>डॉक्टर से पूछें</td><td>नियामकों की चेतावनी, इनसे बचें</td></tr></tbody></table></div>
<h2>सुरक्षित उपयोग</h2><p>रात में हल्के फेस वॉश के बाद ग्लूटाथियोन क्रीम और सुबह सनस्क्रीन। 8 से 12 हफ्ते नियमित उपयोग करें। गर्भावस्था में डॉक्टर से पूछें।</p>''',
         faq=[('ग्लूटाथियोन क्या है?', 'ग्लूटाथियोन शरीर में बनने वाला एक एंटीऑक्सीडेंट है जो कोशिकाओं को नुकसान से बचाता है। स्किनकेयर में इसका उपयोग त्वचा को चमकदार और एक-समान दिखाने के लिए होता है।'),
              ('क्या ग्लूटाथियोन रंग गोरा करता है?', 'नहीं। यह टैन और असमान रंगत को हल्का दिखाने में मदद कर सकता है, लेकिन प्राकृतिक रंग नहीं बदलता।')]),
    dict(slug='glutathione-goli-ke-fayde-nuksan', en='/glutathione-tablets/',
         title='ग्लूटाथियोन गोली (टैबलेट) के फायदे और नुकसान', short='ग्लूटाथियोन गोली',
         seo='Glutathione Tablet Ke Fayde Aur Nuksan: ग्लूटाथियोन गोली',
         desc='Glutathione tablet ke fayde aur nuksan हिंदी में: गोली क्या करती है, स्टडी में कितनी मात्रा ली गई, साइड इफेक्ट्स, लिवर और किडनी, और क्रीम से तुलना।',
         body='''<p>ग्लूटाथियोन गोलियां शरीर की एंटीऑक्सीडेंट सुरक्षा के लिए और कुछ लोग त्वचा की रंगत के लिए लेते हैं। लेकिन त्वचा पर इनका असर हल्का और मिला-जुला है।</p>
<h2>गोली के संभावित फायदे</h2><p>छोटी स्टडी में रोज 250 से 500 mg, 4 से 12 हफ्ते लेने पर त्वचा के मेलानिन में हल्की कमी दिखी (%(oral)s, %(wesch)s)। यह स्थायी गोरापन नहीं देती।</p>
<h2>संभावित नुकसान</h2><ul><li>पेट में ऐंठन, गैस या दस्त।</li><li>कभी-कभी एलर्जी, जैसे खुजली या रैश।</li><li>एक स्टडी में दो लोगों के लिवर टेस्ट में अस्थायी बदलाव, जो ठीक हो गया।</li></ul>
<h2>किसे डॉक्टर से पूछे बिना नहीं लेनी चाहिए</h2><ul><li>गर्भवती या स्तनपान कराने वाली महिलाएं।</li><li>लिवर या किडनी की बीमारी, अस्थमा, या कीमोथेरेपी वाले लोग।</li><li>बच्चे और किशोर।</li></ul>
<h2>गोली या क्रीम?</h2><p>त्वचा के लिए क्रीम सीधे वहीं लगती है जहां जरूरत है, और जोखिम कम है। %(cream)s में ग्लूटाथियोन, नियासिनामाइड और विटामिन C हैं।</p>''',
         faq=[('क्या ग्लूटाथियोन गोली रोज ले सकते हैं?', 'स्टडी में 4 से 12 हफ्ते रोज लेना आमतौर पर ठीक रहा, लेकिन लंबे समय के असर पर कम जानकारी है। डॉक्टर से सलाह लें।'),
              ('क्या 1000 mg ग्लूटाथियोन गोली ज्यादा असर करती है?', 'इसका कोई सबूत नहीं है। स्टडी में 250 से 500 mg का उपयोग हुआ और असर हल्का था।')]),
    dict(slug='glutathione-cream-price', en='/glutathione-cream-price-in-india/',
         title='ग्लूटाथियोन क्रीम की कीमत: क्या देखें', short='ग्लूटाथियोन क्रीम कीमत',
         seo='Glutathione Cream Price: ग्लूटाथियोन क्रीम की कीमत भारत में',
         desc='Glutathione cream price हिंदी में: भारत में ग्लूटाथियोन क्रीम की कीमत किस पर निर्भर करती है, सस्ती क्रीम के खतरे, और GlutaNex की कीमत।',
         body='''<p>भारत में ग्लूटाथियोन क्रीम कुछ सौ से लेकर कई हजार रुपये तक मिलती है। कीमत सिर्फ "ग्लूटाथियोन" नाम से नहीं, बल्कि पूरे फॉर्मूले, मात्रा और ब्रांड की भरोसेमंदी से तय होती है।</p>
<h2>GlutaNex की कीमत</h2><div class="tbl"><table><thead><tr><th>प्रोडक्ट</th><th>कीमत</th><th>MRP</th></tr></thead><tbody>
<tr><td>Night Cream (30 g)</td><td>%(pcream)s</td><td>%(mcream)s</td></tr><tr><td>Face Wash (100 ml)</td><td>%(pwash)s</td><td>%(mwash)s</td></tr><tr><td>Glow Duo</td><td>%(pduo)s</td><td>%(mduo)s</td></tr></tbody></table></div><p>सभी कीमतों में टैक्स शामिल है, फ्री डिलीवरी और कैश ऑन डिलीवरी।</p>
<h2>कीमत किस पर निर्भर करती है</h2><ul><li>साथ में कौन से तत्व हैं: नियासिनामाइड, विटामिन C, हायलूरोनिक एसिड, सेरामाइड्स।</li><li>मात्रा: हमेशा प्रति ग्राम कीमत देखें।</li><li>पैकिंग, बैच नंबर और एक्सपायरी।</li><li>रिटर्न और ग्राहक सहायता।</li></ul>
<h2>बहुत सस्ती क्रीम से सावधान</h2><p>जिस क्रीम में पूरी सामग्री सूची या कंपनी का पता न हो, या जो कुछ दिनों में गोरा करने का दावा करे, उसमें स्टेरॉयड, हाइड्रोक्विनोन या मरकरी हो सकता है।</p>''',
         faq=[('ग्लूटाथियोन क्रीम की कीमत कितनी है?', 'भारत में कुछ सौ से कई हजार रुपये तक। GlutaNex Night Cream %(pcream)s की है, फ्री डिलीवरी के साथ।'),
              ('क्या महंगी क्रीम ज्यादा अच्छी होती है?', 'जरूरी नहीं। सही फॉर्मूला, साफ लेबल और भरोसेमंद विक्रेता देखें, और रोज सनस्क्रीन के साथ नियमित उपयोग करें।')]),
    dict(slug='glutathione-se-gora-hota-hai-kya', en='/glutathione-for-skin-whitening/',
         title='क्या ग्लूटाथियोन से गोरा होते हैं? सच और भ्रम', short='ग्लूटाथियोन से गोरापन',
         seo='Glutathione Se Gora Hote Hai Kya? सच क्या है',
         desc='क्या ग्लूटाथियोन से गोरा होते हैं? ग्लूटाथियोन टैन और असमान रंगत पर क्या कर सकता है, क्या नहीं, इंजेक्शन के खतरे और सुरक्षित रूटीन।',
         body='''<p>सीधा जवाब: ग्लूटाथियोन <b>टैन और असमान रंगत को हल्का और एक-समान दिखाने</b> में मदद कर सकता है, लेकिन यह आपका प्राकृतिक रंग नहीं बदलता। "पक्का गोरा" करने के दावे सच नहीं हैं।</p>
<h2>ग्लूटाथियोन क्या कर सकता है</h2><ul><li>धूप से हुए टैन को जल्दी हल्का करने में मदद, सनस्क्रीन के साथ।</li><li>मुंहासों के दाग हल्के दिखाना, हफ्तों में।</li><li>बेजान त्वचा को चमकदार दिखाना।</li></ul>
<h2>क्या नहीं कर सकता</h2><ul><li>जन्मजात रंग बदलना।</li><li>सनस्क्रीन के बिना स्थायी असर।</li><li>मेलाज्मा का इलाज; उसके लिए डर्मेटोलॉजिस्ट से मिलें।</li></ul>
<h2>इंजेक्शन से बचें</h2><p>सबसे तेज "गोरापन" के दावे अक्सर इंजेक्शन या ड्रिप से जुड़े होते हैं। इनके समर्थन में कोई क्लिनिकल ट्रायल नहीं है और नियामकों ने चेतावनी दी है (%(fda)s)।</p>
<h2>हर रंग सुंदर है</h2><p>अच्छा लक्ष्य है साफ, एक-समान और सुरक्षित त्वचा, अपने ही रंग में: हल्का फेस वॉश, रात में ग्लूटाथियोन क्रीम, और सुबह सनस्क्रीन।</p>''',
         faq=[('क्या ग्लूटाथियोन से स्थायी गोरापन आता है?', 'नहीं। असर धीरे-धीरे होता है और सनस्क्रीन छोड़ने पर कम हो सकता है। प्राकृतिक रंग नहीं बदलता।'),
              ('ग्लूटाथियोन इंजेक्शन सुरक्षित हैं?', 'त्वचा गोरी करने के लिए इनके समर्थन में कोई ट्रायल नहीं है और नियामकों ने चेतावनी दी है। इनसे बचें।')]),
    dict(slug='glutathione-cream-sawal-jawab', en='/glutathione-cream-questions/',
         title='ग्लूटाथियोन क्रीम: सबसे ज्यादा पूछे जाने वाले सवाल', short='सवाल-जवाब',
         seo='Glutathione Cream Sawal Jawab: ग्लूटाथियोन क्रीम के सवालों के जवाब',
         desc='ग्लूटाथियोन क्रीम के सवालों के आसान जवाब हिंदी में: क्या यह काम करती है, रोज लगा सकते हैं, कितने दिन में असर, कौन सी अच्छी है, और सुरक्षा।',
         body='''<p>ग्लूटाथियोन क्रीम के बारे में सबसे ज्यादा पूछे जाने वाले सवालों के छोटे और सही जवाब।</p>''',
         faq=[('क्या ग्लूटाथियोन क्रीम सुरक्षित है?', 'ज्यादातर वयस्कों के लिए हां। पहले पैच टेस्ट करें और जलन लगातार हो तो बंद करें।')]),
]

HI_QA['glutathione-cream-sawal-jawab'] = [
    ('क्या ग्लूटाथियोन क्रीम सच में काम करती है?', 'हां, धीरे-धीरे और हल्का। 10 हफ्ते की स्टडी में 2%% ग्लूटाथियोन लोशन से मेलानिन प्लेसीबो से ज्यादा कम हुआ। समीक्षाएं इसे उम्मीद भरा मानती हैं, लेकिन स्टडी छोटी हैं। 8 से 12 हफ्ते और रोज सनस्क्रीन जरूरी है।', ''),
    ('क्या ग्लूटाथियोन क्रीम रोज लगा सकते हैं?', 'हां, ज्यादातर लोग रोज रात में लगा सकते हैं, सुबह सनस्क्रीन के साथ। अगर क्रीम में रेटिनॉल या एसिड है, तो पहले 2 हफ्ते, हफ्ते में 2 से 3 रात लगाएं।', ''),
    ('कौन सी ग्लूटाथियोन क्रीम अच्छी है?', 'वह क्रीम जिसमें ग्लूटाथियोन साफ लिखा हो, साथ में नियासिनामाइड या हायलूरोनिक एसिड जैसे तत्व हों, दावे सही हों, और विक्रेता का पता और रिटर्न पॉलिसी हो।', ''),
    ('क्या ग्लूटाथियोन क्रीम ऑयली स्किन के लिए अच्छी है?', 'हां, हल्की और चिपचिपी न होने वाली क्रीम, खासकर नियासिनामाइड या सैलिसिलिक एसिड के साथ। पतली परत लगाएं और दिन में दो बार से ज्यादा चेहरा न धोएं।', ''),
]

# ---------------- Regional language guides (one per language, paired with /glutathione-cream/) ----------------
REG = [
  dict(lang='ta', code='ta-IN', name='தமிழ்', slug='glutathione-cream',
       seo='Glutathione Cream Benefits in Tamil: குளுதாதயோன் கிரீம் நன்மைகள்',
       title='குளுதாதயோன் கிரீம்: நன்மைகள், பயன்படுத்தும் முறை, பாதுகாப்பு',
       desc='Glutathione cream benefits in Tamil: குளுதாதயோன் என்றால் என்ன, சருமத்திற்கு நன்மைகள், பயன்படுத்தும் முறை மற்றும் பாதுகாப்பு குறிப்புகள்.',
       ui=dict(by='GlutaNex குழு · புதுப்பிக்கப்பட்டது: 11 அக்டோபர் 2026', en='ஆங்கிலத்தில் படிக்க', note='இது பொதுவான அழகுசாதன தகவல், மருத்துவ ஆலோசனை அல்ல. முடிவுகள் நபருக்கு நபர் மாறுபடும்.', buy='இப்போது வாங்கு', faq='அடிக்கடி கேட்கப்படும் கேள்விகள்', toc='இந்தப் பக்கத்தில்', guide='தமிழ் வழிகாட்டி'),
       body='''<p><b>குளுதாதயோன்</b> என்பது நம் உடல் தானே உருவாக்கும் ஒரு ஆன்டிஆக்ஸிடன்ட். சரும பராமரிப்பில், சருமம் <b>பளபளப்பாகவும் சீராகவும் தோன்ற</b> இது கிரீம்களில் பயன்படுத்தப்படுகிறது.</p>
<h2>சருமத்திற்கு என்ன நன்மைகள்?</h2><ul><li>டான் மற்றும் சீரற்ற நிறம் வாரங்களில் மங்கலாகத் தோன்ற உதவும்.</li><li>பருக்களுக்குப் பின் வரும் கரும்புள்ளிகள் மெதுவாக மங்க உதவும்.</li><li>வெயில் மற்றும் மாசுபாட்டிலிருந்து ஆன்டிஆக்ஸிடன்ட் பாதுகாப்பு.</li></ul>
<h2>என்ன செய்ய முடியாது?</h2><p>குளுதாதயோன் உங்கள் இயற்கையான நிறத்தை மாற்றாது. ஒரே இரவில் பலன் தராது; 8 முதல் 12 வாரங்கள் தொடர்ந்து பயன்படுத்த வேண்டும்.</p>
<h2>எப்படிப் பயன்படுத்துவது?</h2><ol><li>இரவில் மென்மையான ஃபேஸ் வாஷால் முகம் கழுவி உலர்த்தவும்.</li><li>பட்டாணி அளவு கிரீமை முகம் மற்றும் கழுத்தில் தடவவும்.</li><li>காலையில் SPF 30 அல்லது அதற்கு மேற்பட்ட சன்ஸ்கிரீன் பயன்படுத்தவும்.</li></ol>
<h2>பாதுகாப்பு</h2><ul><li>முதலில் பேட்ச் டெஸ்ட் செய்யவும்.</li><li>சருமத்தை வெண்மையாக்கும் குளுதாதயோன் ஊசிகளைத் தவிர்க்கவும்.</li><li>கர்ப்ப காலம் அல்லது தாய்ப்பால் கொடுக்கும் போது மருத்துவரை அணுகவும். GlutaNex Night Cream-இல் ரெட்டினால் உள்ளது.</li></ul>''',
       faq=[('குளுதாதயோன் கிரீம் சருமத்தை வெண்மையாக்குமா?', 'இல்லை. இது டான் மற்றும் சீரற்ற நிறத்தை மங்கலாகக் காட்ட உதவும், ஆனால் இயற்கையான நிறத்தை மாற்றாது.'),
            ('தினமும் பயன்படுத்தலாமா?', 'ஆம், இரவில் பயன்படுத்தலாம். ரெட்டினால் உள்ள கிரீமை முதல் 2 வாரங்கள் வாரத்திற்கு 2–3 இரவுகள் மட்டும் பயன்படுத்தவும்.')]),
  dict(lang='te', code='te-IN', name='తెలుగు', slug='glutathione-cream',
       seo='Glutathione Cream Benefits in Telugu: గ్లూటాథియోన్ క్రీమ్ ప్రయోజనాలు',
       title='గ్లూటాథియోన్ క్రీమ్: ప్రయోజనాలు, వాడే విధానం, భద్రత',
       desc='Glutathione cream benefits in Telugu: గ్లూటాథియోన్ అంటే ఏమిటి, చర్మానికి ప్రయోజనాలు, ఎలా వాడాలి మరియు భద్రతా సూచనలు.',
       ui=dict(by='GlutaNex బృందం · నవీకరణ: 11 అక్టోబర్ 2026', en='ఇంగ్లీష్‌లో చదవండి', note='ఇది సాధారణ సౌందర్య సమాచారం, వైద్య సలహా కాదు. ఫలితాలు వ్యక్తిని బట్టి మారుతాయి.', buy='ఇప్పుడే కొనండి', faq='తరచుగా అడిగే ప్రశ్నలు', toc='ఈ పేజీలో', guide='తెలుగు గైడ్'),
       body='''<p><b>గ్లూటాథియోన్</b> మన శరీరం స్వయంగా తయారు చేసుకునే ఒక యాంటీఆక్సిడెంట్. చర్మ సంరక్షణలో, చర్మం <b>కాంతివంతంగా మరియు సమానంగా కనిపించడానికి</b> దీన్ని క్రీమ్‌లలో వాడతారు.</p>
<h2>చర్మానికి ప్రయోజనాలు</h2><ul><li>టాన్ మరియు అసమాన రంగు కొన్ని వారాల్లో తేలికగా కనిపించడానికి సహాయపడుతుంది.</li><li>మొటిమల తర్వాత వచ్చే నల్లటి మచ్చలు నెమ్మదిగా తగ్గడానికి సహాయపడుతుంది.</li><li>ఎండ మరియు కాలుష్యం నుండి యాంటీఆక్సిడెంట్ రక్షణ.</li></ul>
<h2>ఏమి చేయలేదు?</h2><p>గ్లూటాథియోన్ మీ సహజ రంగును మార్చదు. ఒక్క రాత్రిలో ఫలితం రాదు; 8 నుండి 12 వారాలు క్రమం తప్పకుండా వాడాలి.</p>
<h2>ఎలా వాడాలి?</h2><ol><li>రాత్రి మృదువైన ఫేస్ వాష్‌తో ముఖం కడిగి ఆరబెట్టండి.</li><li>బఠానీ గింజంత క్రీమ్‌ను ముఖం మరియు మెడపై రాయండి.</li><li>ఉదయం SPF 30 లేదా అంతకంటే ఎక్కువ సన్‌స్క్రీన్ వాడండి.</li></ol>
<h2>భద్రత</h2><ul><li>ముందుగా ప్యాచ్ టెస్ట్ చేయండి.</li><li>చర్మాన్ని తెల్లగా చేసే గ్లూటాథియోన్ ఇంజెక్షన్లకు దూరంగా ఉండండి.</li><li>గర్భధారణ లేదా పాలిచ్చే సమయంలో డాక్టర్‌ను సంప్రదించండి. GlutaNex Night Creamలో రెటినాల్ ఉంది.</li></ul>''',
       faq=[('గ్లూటాథియోన్ క్రీమ్ చర్మాన్ని తెల్లగా చేస్తుందా?', 'లేదు. ఇది టాన్ మరియు అసమాన రంగును తేలికగా కనిపించేలా చేయడంలో సహాయపడుతుంది, కానీ సహజ రంగును మార్చదు.'),
            ('రోజూ వాడవచ్చా?', 'అవును, రాత్రి వాడవచ్చు. రెటినాల్ ఉన్న క్రీమ్‌ను మొదటి 2 వారాలు వారానికి 2–3 రాత్రులు మాత్రమే వాడండి.')]),
  dict(lang='mr', code='mr-IN', name='मराठी', slug='glutathione-cream',
       seo='Glutathione Cream Benefits in Marathi: ग्लुटाथायोन क्रीमचे फायदे',
       title='ग्लुटाथायोन क्रीम: फायदे, वापरण्याची पद्धत आणि सुरक्षितता',
       desc='Glutathione cream benefits in Marathi: ग्लुटाथायोन म्हणजे काय, त्वचेसाठी फायदे, कसे वापरावे आणि सुरक्षिततेच्या सूचना.',
       ui=dict(by='GlutaNex टीम · अद्यतन: 11 ऑक्टोबर 2026', en='इंग्रजीत वाचा', note='ही सामान्य सौंदर्य माहिती आहे, वैद्यकीय सल्ला नाही. परिणाम व्यक्तीनुसार बदलू शकतात.', buy='आता खरेदी करा', faq='वारंवार विचारले जाणारे प्रश्न', toc='या पानावर', guide='मराठी मार्गदर्शक'),
       body='''<p><b>ग्लुटाथायोन</b> हा आपले शरीर स्वतः तयार करणारा एक अँटिऑक्सिडंट आहे. त्वचेच्या काळजीत, त्वचा <b>तेजस्वी आणि एकसमान दिसावी</b> यासाठी तो क्रीममध्ये वापरला जातो.</p>
<h2>त्वचेसाठी फायदे</h2><ul><li>टॅन आणि असमान रंग काही आठवड्यांत फिकट दिसण्यास मदत.</li><li>मुरुमांनंतरचे काळे डाग हळूहळू कमी दिसण्यास मदत.</li><li>ऊन आणि प्रदूषणापासून अँटिऑक्सिडंट संरक्षण.</li></ul>
<h2>काय करू शकत नाही?</h2><p>ग्लुटाथायोन तुमचा नैसर्गिक रंग बदलत नाही. एका रात्रीत परिणाम मिळत नाही; 8 ते 12 आठवडे नियमित वापर आवश्यक आहे.</p>
<h2>कसे वापरावे?</h2><ol><li>रात्री सौम्य फेस वॉशने चेहरा धुवून कोरडा करा.</li><li>वाटाण्याएवढी क्रीम चेहऱ्यावर आणि मानेवर लावा.</li><li>सकाळी SPF 30 किंवा त्यापेक्षा जास्त सनस्क्रीन लावा.</li></ol>
<h2>सुरक्षितता</h2><ul><li>आधी पॅच टेस्ट करा.</li><li>त्वचा गोरी करणारी ग्लुटाथायोन इंजेक्शन्स टाळा.</li><li>गर्भावस्थेत किंवा स्तनपानाच्या काळात डॉक्टरांचा सल्ला घ्या. GlutaNex Night Cream मध्ये रेटिनॉल आहे.</li></ul>''',
       faq=[('ग्लुटाथायोन क्रीमने त्वचा गोरी होते का?', 'नाही. टॅन आणि असमान रंग फिकट दिसण्यास मदत होते, पण नैसर्गिक रंग बदलत नाही.'),
            ('रोज वापरू शकतो का?', 'हो, रात्री वापरू शकता. रेटिनॉल असलेली क्रीम पहिले 2 आठवडे आठवड्यातून 2–3 रात्रीच वापरा.')]),
  dict(lang='bn', code='bn-IN', name='বাংলা', slug='glutathione-cream',
       seo='Glutathione Cream Benefits in Bengali: গ্লুটাথিয়ন ক্রিমের উপকারিতা',
       title='গ্লুটাথিয়ন ক্রিম: উপকারিতা, ব্যবহারের নিয়ম ও নিরাপত্তা',
       desc='Glutathione cream benefits in Bengali: গ্লুটাথিয়ন কী, ত্বকের জন্য উপকারিতা, কীভাবে ব্যবহার করবেন এবং নিরাপত্তার পরামর্শ।',
       ui=dict(by='GlutaNex টিম · আপডেট: 11 অক্টোবর 2026', en='ইংরেজিতে পড়ুন', note='এটি সাধারণ প্রসাধনী তথ্য, চিকিৎসা পরামর্শ নয়। ফলাফল ব্যক্তিভেদে আলাদা হতে পারে।', buy='এখনই কিনুন', faq='প্রায়ই জিজ্ঞাসিত প্রশ্ন', toc='এই পাতায়', guide='বাংলা গাইড'),
       body='''<p><b>গ্লুটাথিয়ন</b> হল একটি অ্যান্টিঅক্সিডেন্ট যা আমাদের শরীর নিজেই তৈরি করে। ত্বকের যত্নে, ত্বককে <b>উজ্জ্বল ও সমান দেখাতে</b> এটি ক্রিমে ব্যবহার করা হয়।</p>
<h2>ত্বকের জন্য উপকারিতা</h2><ul><li>ট্যান ও অসমান রং কয়েক সপ্তাহে হালকা দেখাতে সাহায্য করে।</li><li>ব্রণের পরের কালো দাগ ধীরে ধীরে কম দেখাতে সাহায্য করে।</li><li>রোদ ও দূষণ থেকে অ্যান্টিঅক্সিডেন্ট সুরক্ষা।</li></ul>
<h2>কী করতে পারে না?</h2><p>গ্লুটাথিয়ন আপনার স্বাভাবিক গায়ের রং বদলায় না। এক রাতে ফল পাওয়া যায় না; 8 থেকে 12 সপ্তাহ নিয়মিত ব্যবহার করতে হয়।</p>
<h2>কীভাবে ব্যবহার করবেন?</h2><ol><li>রাতে হালকা ফেস ওয়াশ দিয়ে মুখ ধুয়ে শুকিয়ে নিন।</li><li>মটরদানার মতো পরিমাণ ক্রিম মুখে ও গলায় লাগান।</li><li>সকালে SPF 30 বা তার বেশি সানস্ক্রিন লাগান।</li></ol>
<h2>নিরাপত্তা</h2><ul><li>প্রথমে প্যাচ টেস্ট করুন।</li><li>ত্বক ফর্সা করার গ্লুটাথিয়ন ইনজেকশন এড়িয়ে চলুন।</li><li>গর্ভাবস্থায় বা স্তন্যদানের সময় ডাক্তারের পরামর্শ নিন। GlutaNex Night Cream-এ রেটিনল আছে।</li></ul>''',
       faq=[('গ্লুটাথিয়ন ক্রিম কি ত্বক ফর্সা করে?', 'না। এটি ট্যান ও অসমান রং হালকা দেখাতে সাহায্য করে, কিন্তু স্বাভাবিক রং বদলায় না।'),
            ('রোজ ব্যবহার করা যায়?', 'হ্যাঁ, রাতে ব্যবহার করা যায়। রেটিনল থাকা ক্রিম প্রথম 2 সপ্তাহ সপ্তাহে 2–3 রাত ব্যবহার করুন।')]),
  dict(lang='kn', code='kn-IN', name='ಕನ್ನಡ', slug='glutathione-cream',
       seo='Glutathione Cream Benefits in Kannada: ಗ್ಲುಟಾಥಿಯೋನ್ ಕ್ರೀಮ್ ಪ್ರಯೋಜನಗಳು',
       title='ಗ್ಲುಟಾಥಿಯೋನ್ ಕ್ರೀಮ್: ಪ್ರಯೋಜನಗಳು, ಬಳಸುವ ವಿಧಾನ ಮತ್ತು ಸುರಕ್ಷತೆ',
       desc='Glutathione cream benefits in Kannada: ಗ್ಲುಟಾಥಿಯೋನ್ ಎಂದರೇನು, ಚರ್ಮಕ್ಕೆ ಪ್ರಯೋಜನಗಳು, ಹೇಗೆ ಬಳಸಬೇಕು ಮತ್ತು ಸುರಕ್ಷತಾ ಸಲಹೆಗಳು.',
       ui=dict(by='GlutaNex ತಂಡ · ನವೀಕರಣ: 11 ಅಕ್ಟೋಬರ್ 2026', en='ಇಂಗ್ಲಿಷ್‌ನಲ್ಲಿ ಓದಿ', note='ಇದು ಸಾಮಾನ್ಯ ಸೌಂದರ್ಯ ಮಾಹಿತಿ, ವೈದ್ಯಕೀಯ ಸಲಹೆ ಅಲ್ಲ. ಫಲಿತಾಂಶಗಳು ವ್ಯಕ್ತಿಯಿಂದ ವ್ಯಕ್ತಿಗೆ ಬದಲಾಗಬಹುದು.', buy='ಈಗ ಖರೀದಿಸಿ', faq='ಆಗಾಗ್ಗೆ ಕೇಳುವ ಪ್ರಶ್ನೆಗಳು', toc='ಈ ಪುಟದಲ್ಲಿ', guide='ಕನ್ನಡ ಮಾರ್ಗದರ್ಶಿ'),
       body='''<p><b>ಗ್ಲುಟಾಥಿಯೋನ್</b> ನಮ್ಮ ದೇಹವೇ ತಯಾರಿಸುವ ಒಂದು ಆಂಟಿಆಕ್ಸಿಡೆಂಟ್. ಚರ್ಮದ ಆರೈಕೆಯಲ್ಲಿ, ಚರ್ಮ <b>ಕಾಂತಿಯುತವಾಗಿ ಮತ್ತು ಸಮವಾಗಿ ಕಾಣಲು</b> ಇದನ್ನು ಕ್ರೀಮ್‌ಗಳಲ್ಲಿ ಬಳಸಲಾಗುತ್ತದೆ.</p>
<h2>ಚರ್ಮಕ್ಕೆ ಪ್ರಯೋಜನಗಳು</h2><ul><li>ಟ್ಯಾನ್ ಮತ್ತು ಅಸಮಾನ ಬಣ್ಣ ಕೆಲವು ವಾರಗಳಲ್ಲಿ ತಿಳಿಯಾಗಿ ಕಾಣಲು ಸಹಾಯ ಮಾಡುತ್ತದೆ.</li><li>ಮೊಡವೆಗಳ ನಂತರದ ಕಪ್ಪು ಕಲೆಗಳು ನಿಧಾನವಾಗಿ ಕಡಿಮೆಯಾಗಲು ಸಹಾಯ ಮಾಡುತ್ತದೆ.</li><li>ಬಿಸಿಲು ಮತ್ತು ಮಾಲಿನ್ಯದಿಂದ ಆಂಟಿಆಕ್ಸಿಡೆಂಟ್ ರಕ್ಷಣೆ.</li></ul>
<h2>ಏನು ಮಾಡಲು ಸಾಧ್ಯವಿಲ್ಲ?</h2><p>ಗ್ಲುಟಾಥಿಯೋನ್ ನಿಮ್ಮ ಸಹಜ ಬಣ್ಣವನ್ನು ಬದಲಾಯಿಸುವುದಿಲ್ಲ. ಒಂದೇ ರಾತ್ರಿಯಲ್ಲಿ ಫಲಿತಾಂಶ ಬರುವುದಿಲ್ಲ; 8 ರಿಂದ 12 ವಾರಗಳು ನಿಯಮಿತವಾಗಿ ಬಳಸಬೇಕು.</p>
<h2>ಹೇಗೆ ಬಳಸಬೇಕು?</h2><ol><li>ರಾತ್ರಿ ಮೃದುವಾದ ಫೇಸ್ ವಾಶ್‌ನಿಂದ ಮುಖ ತೊಳೆದು ಒಣಗಿಸಿ.</li><li>ಬಟಾಣಿ ಕಾಳಿನಷ್ಟು ಕ್ರೀಮ್ ಅನ್ನು ಮುಖ ಮತ್ತು ಕುತ್ತಿಗೆಗೆ ಹಚ್ಚಿ.</li><li>ಬೆಳಿಗ್ಗೆ SPF 30 ಅಥವಾ ಹೆಚ್ಚಿನ ಸನ್‌ಸ್ಕ್ರೀನ್ ಬಳಸಿ.</li></ol>
<h2>ಸುರಕ್ಷತೆ</h2><ul><li>ಮೊದಲು ಪ್ಯಾಚ್ ಟೆಸ್ಟ್ ಮಾಡಿ.</li><li>ಚರ್ಮ ಬಿಳಿ ಮಾಡುವ ಗ್ಲುಟಾಥಿಯೋನ್ ಇಂಜೆಕ್ಷನ್‌ಗಳನ್ನು ತಪ್ಪಿಸಿ.</li><li>ಗರ್ಭಾವಸ್ಥೆ ಅಥವಾ ಹಾಲುಣಿಸುವ ಸಮಯದಲ್ಲಿ ವೈದ್ಯರನ್ನು ಸಂಪರ್ಕಿಸಿ. GlutaNex Night Creamನಲ್ಲಿ ರೆಟಿನಾಲ್ ಇದೆ.</li></ul>''',
       faq=[('ಗ್ಲುಟಾಥಿಯೋನ್ ಕ್ರೀಮ್ ಚರ್ಮವನ್ನು ಬಿಳಿ ಮಾಡುತ್ತದೆಯೇ?', 'ಇಲ್ಲ. ಇದು ಟ್ಯಾನ್ ಮತ್ತು ಅಸಮಾನ ಬಣ್ಣವನ್ನು ತಿಳಿಯಾಗಿ ಕಾಣುವಂತೆ ಮಾಡಲು ಸಹಾಯ ಮಾಡುತ್ತದೆ, ಆದರೆ ಸಹಜ ಬಣ್ಣ ಬದಲಾಗುವುದಿಲ್ಲ.'),
            ('ಪ್ರತಿದಿನ ಬಳಸಬಹುದೇ?', 'ಹೌದು, ರಾತ್ರಿ ಬಳಸಬಹುದು. ರೆಟಿನಾಲ್ ಇರುವ ಕ್ರೀಮ್ ಅನ್ನು ಮೊದಲ 2 ವಾರಗಳು ವಾರಕ್ಕೆ 2–3 ರಾತ್ರಿ ಮಾತ್ರ ಬಳಸಿ.')]),
]

# ---------------- Key takeaways (AEO / AI Overviews): 3 quotable bullets per guide ----------------
TLDR = {
 'glutathione': ['Glutathione is an antioxidant your body makes from three amino acids; it protects cells and recycles vitamins C and E.',
                 'In skincare it can help tan and uneven tone look lighter and more even over 8–12 weeks, with daily sunscreen.',
                 'It does not change natural skin colour; creams are low-risk, while injections for skin lightening carry warnings.'],
 'glutathione-cream': ['A glutathione cream is a cosmetic for brighter, more even-looking skin that works gradually.',
                       'Choose one with glutathione clearly listed, partners like niacinamide, honest claims and a contactable seller.',
                       'Use it at night on clean skin and wear sunscreen every morning.'],
 'glutathione-benefits-for-skin': ['Main benefits: antioxidant protection and a brighter, more even-looking tone with regular use.',
                                   'Small studies show modest, gradual drops in skin melanin over 4–12 weeks.',
                                   'Results need daily sunscreen and do not change natural skin colour.'],
 'glutathione-side-effects': ['Creams are generally well tolerated; mild tingling, redness or dryness can happen at first.',
                              'Serious reactions are rare: breathing trouble, swelling or rash need urgent medical help.',
                              'The biggest risks come from injections, which are not recommended for skin lightening.'],
 'is-glutathione-safe-for-skin': ['Glutathione creams and face washes are generally safe for most adults; patch test first.',
                                  'Tablets were well tolerated in short studies but need a doctor\'s advice.',
                                  'Avoid skin-lightening injections, which lack trials and carry regulator warnings.'],
 'how-to-use-glutathione-cream': ['Night: cleanse, pat dry, apply a pea-sized amount to face and neck.',
                                  'Morning: cleanse and use SPF 30 or higher sunscreen.',
                                  'With retinol creams, start 2–3 nights a week and give the routine 8–12 weeks.'],
 'glutathione-for-skin-whitening': ['Glutathione can help tan and uneven tone look lighter, but it does not change natural skin colour.',
                                    'Effects are gradual and fade without sunscreen; "permanent whitening" claims are hype.',
                                    'Avoid injections and creams that lighten within days, which may contain steroids or mercury.'],
 'glutathione-cream-vs-tablets-vs-injections': ['Cream: applied to skin, low risk, modest gradual results.',
                                                'Tablets: mixed evidence, take only with medical advice.',
                                                'Injections: no clinical trial for skin lightening and regulator warnings; avoid.'],
 'glutathione-tablets': ['Studies used 250–500 mg a day for 4–12 weeks and found only modest changes in skin tone.',
                         'Short courses were generally well tolerated; long-term use is not well studied.',
                         'No tablet permanently whitens skin, and 1000 mg is not proven better; ask a doctor first.'],
 'glutathione-cream-price-in-india': ['Glutathione creams in India range from a few hundred to several thousand rupees.',
                                      'Compare price per gram and the full formula, not just the word "glutathione".',
                                      'Very cheap, unlabelled "fairness" creams may contain banned ingredients.'],
 'best-glutathione-cream-in-india': ['No single brand is best for everyone; judge any cream with a clear checklist.',
                                     'Look for a full ingredient list, honest claims, batch and expiry details and a real seller.',
                                     'Use it nightly for 8 weeks with daily sunscreen before judging results.'],
 'glutathione-face-wash': ['A face wash is rinsed off in under a minute, so it mainly cleans and refreshes.',
                           'It is a good first step before a leave-on glutathione cream.',
                           'For visible brightening, pair it with a night cream and daily sunscreen.'],
 'glutathione-vs-kojic-acid': ['Both slow melanin production; glutathione is usually gentler and adds antioxidant protection.',
                               'Kojic acid may help stubborn spots but irritates some skin.',
                               'They can be combined; introduce one product at a time.'],
 'glutathione-rich-foods': ['Spinach, avocado, asparagus and okra contain glutathione directly.',
                            'Garlic, onion, broccoli, eggs, dal and dairy supply its building blocks; vitamin C foods keep it active.',
                            'Diet supports skin health but will not visibly change pigmentation on its own.'],
 'retinol-vs-glutathione': ['Retinol has stronger evidence for texture and fine lines but can irritate.',
                            'Glutathione is a gentler antioxidant for brighter, more even-looking tone.',
                            'They can be used together at night, introduced slowly, with daily sunscreen.'],
 'glutathione-night-cream': ['Night is ideal for glutathione creams, especially those with retinol or acids.',
                             'Look for niacinamide, hyaluronic acid and ceramides alongside glutathione.',
                             'Expect a brighter look in 4–8 weeks and lighter tan in 8–12 weeks with sunscreen.'],
 'glutathione-and-niacinamide': ['Glutathione and niacinamide work on pigment in different ways and combine well.',
                                 'Vitamin C pairs well too, best in the morning under sunscreen.',
                                 'Avoid stacking extra retinol or acids on the same night.'],
 'glutathione-for-dark-spots-and-tan': ['Sunscreen does most of the work; glutathione helps spots and tan look lighter.',
                                        'Tan fades in weeks; dark spots often take 8–12 weeks or longer.',
                                        'Patchy pigmentation on both cheeks may be melasma and needs a dermatologist.'],
 'glutathione-vs-vitamin-c': ['Vitamin C is a well-studied daytime antioxidant; glutathione is a gentle night option.',
                              'Vitamin C helps keep glutathione active, so they work well together.',
                              'Simple split: vitamin C in the morning, glutathione at night.'],
 'glutathione-vs-niacinamide': ['Glutathione acts early in melanin production; niacinamide reduces pigment transfer.',
                                'Niacinamide also helps oil, pores and the skin barrier.',
                                'Both are gentle and are often combined in one cream.'],
 'glutathione-vs-alpha-arbutin': ['Alpha arbutin is often used for targeted dark spots; glutathione suits overall tone.',
                                  'Both are gentle compared with prescription lighteners.',
                                  'They can be used together; patch test first.'],
 'glutathione-vs-hydroquinone': ['Hydroquinone is a strong prescription medicine in India; glutathione is a gentle cosmetic.',
                                 'Use hydroquinone only under a dermatologist, for a limited time.',
                                 'Some unbranded fairness creams hide hydroquinone and steroids; avoid them.'],
 'glutathione-cream-for-men': ['Glutathione cream works the same for men as for women.',
                               'Apply at night, wait after shaving, and use a light sunscreen in the morning.',
                               'Expect a brighter look over 4–8 weeks and lighter tan over 8–12 weeks.'],
 'glutathione-for-acne-marks': ['Flat dark marks after pimples can look lighter in 6–12 weeks with daily sunscreen.',
                                'Creams do not fix dented or raised scars.',
                                'Do not pick pimples; treat active acne first.'],
 'glutathione-for-oily-skin': ['Oily skin suits light glutathione creams, ideally with niacinamide or salicylic acid.',
                               'Apply a thin layer at night and a matte sunscreen in the morning.',
                               'Do not over-wash or scrub, which triggers more oil.'],
 'glutathione-cream-for-summer-tan': ['Daily SPF 30+ sunscreen, reapplied outdoors, does most of the work against tan.',
                                      'A glutathione night cream can help tan look lighter within a few weeks.',
                                      'Avoid lemon, baking soda and bleach creams on tanned skin.'],
 'glutathione-in-pregnancy': ['Glutathione safety in pregnancy and breastfeeding has not been well studied.',
                              'Avoid retinol creams and glutathione injections; ask your doctor before any glutathione product.',
                              'Gentle cleanser, moisturiser and daily sunscreen are safe basics.'],
}

# ---------------- Seasonal pages (winter, wedding season) ----------------
NEW_GUIDES += [
    dict(slug='glutathione-cream-in-winter', title='Glutathione cream in winter: a routine for dry skin', short='Winter routine',
         blurb='How to use a glutathione cream in cold, dry weather without flaking, and why sunscreen still matters.',
         seo='Glutathione Cream in Winter: Dry Skin Routine & Sunscreen Tips', desc='Can you use glutathione cream in winter? Yes: how to adjust for dry skin, layer a moisturiser, use retinol in cold weather, and why winter sunscreen still matters.',
         refs=['study'],
         qa=[('Can I use glutathione cream in winter?', 'Yes. Winter is a good time to start a glutathione cream: the sun is milder, so tan fades more easily. Apply it at night on clean skin, add a moisturiser on top if your skin feels dry, and keep wearing SPF 30+ sunscreen every morning.', ''),
             ('Do I need sunscreen in winter?', 'Yes. UVA rays, which drive tan and dark spots, stay strong through Indian winters and pass through haze, clouds and window glass. Use a broad-spectrum SPF 30 or higher with a good PA rating every morning, even on cool or foggy days.', '')],
         body='''<h2>Why winter is a good season to start</h2><p>Milder sun means less new tan, so the tan you already have can fade with less fighting back. Starting now also means your skin has had 8–12 weeks of steady use by the end of winter, which is how long glutathione creams usually take to show a brighter, more even look.</p>
<h2>Adjust for dry skin</h2><ul><li><b>Cleanse gently.</b> Lukewarm water, not hot. If your skin feels tight, use %(wash)s once a day at night and just rinse with water in the morning.</li><li><b>Apply on dry skin.</b> Wait a minute after washing; actives on damp skin can sting more in cold weather.</li><li><b>Layer a moisturiser.</b> Apply the night cream first, wait a minute, then a plain moisturiser if you need more comfort.</li><li><b>Go slower with retinol.</b> %(cream)s contains retinol and salicylic acid, which can feel stronger in dry air. Use it every other night if you see flaking, and build up again.</li></ul>
<h2>A simple winter routine</h2><div class="tbl"><table><thead><tr><th>When</th><th>Steps</th></tr></thead><tbody><tr><td>Morning</td><td>Rinse or gentle cleanse, moisturiser, SPF 30+ sunscreen</td></tr><tr><td>Night</td><td>Cleanse, pat dry, pea-sized amount of night cream, moisturiser if dry</td></tr><tr><td>Weekly</td><td>Skip scrubs; if skin flakes, take one or two nights off actives</td></tr></tbody></table></div>
<h2>What to avoid in winter</h2><p>Very hot showers on the face, harsh scrubs, alcohol-heavy toners and stacking several new actives at once. They strip the skin barrier, and a damaged barrier makes dullness and uneven tone look worse.</p>''',
         faq=[('Is glutathione cream drying?', 'Glutathione itself is not drying, but creams that also contain retinol or salicylic acid, like the GlutaNex Night Cream, can feel drying in cold weather. Use it every other night and add a moisturiser.'),
              ('Should I apply moisturiser before or after glutathione cream?', 'Apply the glutathione cream first on clean, dry skin, wait about a minute, then apply your moisturiser on top.')]),
    dict(slug='glutathione-before-wedding', title='Glutathione before your wedding: an honest 12-week plan', short='Before the wedding',
         blurb='When to start, a week-by-week plan, and why to skip pre-wedding glutathione injections.',
         seo='Glutathione Before Wedding: 12-Week Bridal & Groom Glow Plan', desc='Glutathione before your wedding: when to start the cream, a 12-week bride and groom plan, what to stop before the day, and why to skip glutathione injections.',
         refs=['study', 'fda'],
         qa=[('Is glutathione good before a wedding?', 'A glutathione cream can help tan and uneven tone look brighter if you start 8–12 weeks before the day and wear sunscreen daily. It will not change your natural skin colour, and glutathione injections, often sold as pre-wedding packages, are not recommended.', ''),
             ('How many weeks before the wedding should I start glutathione cream?', 'Start 10–12 weeks before if you can. That leaves two weeks to build up slowly, about eight weeks for gradual results, and time to stop anything that irritates. Starting a new active cream in the last two weeks is risky.', ''),
             ('Are glutathione injections safe before marriage?', 'There are no proper clinical trials showing glutathione injections are safe or effective for skin lightening, and health regulators have warned about them. Drips given outside a hospital can also carry infection risk. It is best to skip them, especially before a big day.', '<p>Read the warning: %(fda)s.</p>')],
         body='''<h2>A week-by-week plan</h2><div class="tbl"><table><thead><tr><th>Weeks before</th><th>What to do</th></tr></thead><tbody>
<tr><td>12–11</td><td>Patch test for 24 hours. Start the night cream 2–3 nights a week. Sunscreen every morning from now on.</td></tr>
<tr><td>10–9</td><td>If your skin is comfortable, use it every other night.</td></tr>
<tr><td>8–3</td><td>Every night if your skin is happy. Keep up sunscreen, sleep and water; avoid new products.</td></tr>
<tr><td>2–1</td><td>Keep the same routine. No new creams, peels, bleach or threading experiments. Book your last facial at least a week before.</td></tr>
<tr><td>The day</td><td>Your usual gentle routine. Let your makeup artist know which actives you use.</td></tr></tbody></table></div>
<h2>For grooms too</h2><p>The same plan works for men. Shaving can make actives sting, so apply the night cream on shaved areas only once any razor irritation has settled, and use a fragrance-free moisturiser after shaving.</p>
<h2>Only 4 weeks to go (or Diwali is close)?</h2><p>A cream can make skin look fresher and smoother within a few weeks, but tan and spots need longer. Focus on daily sunscreen, a gentle cleanser like %(wash)s, sleep and a steady routine rather than anything strong or new.</p>
<h2>What to avoid before the wedding</h2><ul><li>Glutathione injections and IV "glow drips".</li><li>Bleach creams and unlabelled "fairness" creams, which may contain steroids or mercury.</li><li>A first-ever chemical peel in the final month.</li><li>Lemon, baking soda or toothpaste on the face.</li></ul>''',
         faq=[('Can I use glutathione cream one week before my wedding?', 'If you already use it and your skin is comfortable, keep going. Do not start it for the first time in the final week; a new active can irritate.'),
              ('Is glutathione cream good for grooms?', 'Yes. The same routine works for men; apply it at night and wait until any shaving irritation has settled.')]),
]

HI += [
    dict(slug='shaadi-se-pehle-glutathione', en='/glutathione-before-wedding/',
         title='शादी से पहले ग्लूटाथियोन: 12 हफ्तों का सच्चा प्लान', short='शादी से पहले',
         seo='Shaadi Se Pehle Glutathione: 12 हफ्ते का प्लान',
         desc='शादी से पहले glutathione cream कब शुरू करें, हफ्ते-दर-हफ्ते प्लान, आखिरी दो हफ्तों में क्या न करें, और ग्लूटाथियोन इंजेक्शन से क्यों बचें।',
         body='''<p><b>छोटा जवाब:</b> ग्लूटाथियोन क्रीम शादी से 10–12 हफ्ते पहले शुरू करें और रोज़ सुबह सनस्क्रीन लगाएं। इससे टैन और असमान रंगत धीरे-धीरे हल्की और एक-सी दिख सकती है। यह प्राकृतिक रंग नहीं बदलती, और प्री-वेडिंग ग्लूटाथियोन इंजेक्शन की सलाह नहीं दी जाती।</p>
<h2>हफ्ते-दर-हफ्ते प्लान</h2><div class="tbl"><table><thead><tr><th>शादी से पहले</th><th>क्या करें</th></tr></thead><tbody>
<tr><td>12–11 हफ्ते</td><td>24 घंटे का पैच टेस्ट। हफ्ते में 2–3 रात क्रीम। हर सुबह सनस्क्रीन।</td></tr>
<tr><td>10–9 हफ्ते</td><td>त्वचा ठीक लगे तो एक दिन छोड़कर हर रात।</td></tr>
<tr><td>8–3 हफ्ते</td><td>त्वचा आरामदायक हो तो हर रात। नए प्रोडक्ट न आज़माएं।</td></tr>
<tr><td>आखिरी 2 हफ्ते</td><td>वही रूटीन। कोई नई क्रीम, पील या ब्लीच नहीं। आखिरी फेशियल कम से कम एक हफ्ता पहले।</td></tr></tbody></table></div>
<h2>दूल्हों के लिए भी</h2><p>यही प्लान पुरुषों के लिए भी है। शेविंग के बाद जलन हो तो उसके ठीक होने तक उस जगह क्रीम न लगाएं।</p>
<h2>शादी से पहले किन चीज़ों से बचें</h2><ul><li>ग्लूटाथियोन इंजेक्शन और IV "ग्लो ड्रिप"।</li><li>ब्लीच और बिना लेबल वाली "फेयरनेस" क्रीम, जिनमें स्टेरॉयड या पारा हो सकता है।</li><li>आखिरी महीने में पहली बार केमिकल पील।</li><li>चेहरे पर नींबू, बेकिंग सोडा या टूथपेस्ट।</li></ul>''',
         faq=[('शादी से कितने हफ्ते पहले ग्लूटाथियोन क्रीम शुरू करें?', 'अगर हो सके तो 10–12 हफ्ते पहले। इससे धीरे-धीरे शुरू करने और नतीजे दिखने के लिए पूरा समय मिलता है। आखिरी दो हफ्तों में नई एक्टिव क्रीम शुरू न करें।'),
              ('क्या शादी से पहले ग्लूटाथियोन इंजेक्शन सुरक्षित है?', 'त्वचा गोरी करने के लिए इंजेक्शन के सुरक्षित या असरदार होने का कोई ठीक क्लिनिकल ट्रायल नहीं है, और स्वास्थ्य नियामकों ने इनके बारे में चेतावनी दी है। इनसे बचना बेहतर है।')]),
]

TLDR.update({
    'glutathione-cream-in-winter': ['Winter is a good time to start: milder sun lets existing tan fade more easily.',
                                    'For dry skin, apply on dry skin, add a moisturiser on top and use retinol creams every other night if you flake.',
                                    'Keep SPF 30+ sunscreen every morning; UVA stays strong in Indian winters.'],
    'glutathione-before-wedding': ['Start a glutathione cream 10–12 weeks before the wedding, slowly at first, with daily sunscreen.',
                                   'Do not start new products, peels or bleach in the final two weeks.',
                                   'Skip glutathione injections and IV glow drips; they lack trials and carry warnings.'],
})

# Key takeaways for Hindi pages
TLDR_HI = {
    'glutathione-cream-ke-fayde': ['ग्लूटाथियोन क्रीम एंटीऑक्सीडेंट सुरक्षा देती है और त्वचा को धीरे-धीरे चमकदार व एक-सा दिखाने में मदद करती है।',
                                   'नतीजे 8–12 हफ्तों में दिखते हैं, रोज़ सनस्क्रीन के साथ।',
                                   'यह प्राकृतिक रंग नहीं बदलती।'],
    'glutathione-ke-nuksan': ['क्रीम आमतौर पर सुरक्षित है; शुरुआत में हल्की जलन, लालिमा या रूखापन हो सकता है।',
                              'पहले 24 घंटे पैच टेस्ट करें; सूजन या रैश हो तो इस्तेमाल बंद करें।',
                              'सबसे ज़्यादा जोखिम इंजेक्शन में है; त्वचा गोरी करने के लिए इनसे बचें।'],
    'glutathione-cream-kaise-lagaye': ['रात को चेहरा धोकर सुखाएं, फिर मटर के दाने जितनी क्रीम लगाएं।',
                                       'रेटिनॉल वाली क्रीम पहले दो हफ्ते हफ्ते में 2–3 रात।',
                                       'हर सुबह SPF 30+ सनस्क्रीन; नतीजे 8–12 हफ्तों में।'],
    'glutathione-kya-hai': ['ग्लूटाथियोन शरीर में बनने वाला एंटीऑक्सीडेंट है जो कोशिकाओं को नुकसान से बचाता है।',
                            'स्किनकेयर में यह टैन और असमान रंगत को धीरे-धीरे हल्का दिखाने में मदद कर सकता है।',
                            'यह प्राकृतिक रंग नहीं बदलता; क्रीम कम जोखिम वाली है, इंजेक्शन से बचें।'],
    'glutathione-goli-ke-fayde-nuksan': ['अध्ययनों में 250–500 mg रोज़, 4–12 हफ्तों तक, रंगत में हल्का बदलाव दिखा।',
                                         'कम समय के लिए आमतौर पर ठीक; लंबे इस्तेमाल की जानकारी कम है।',
                                         'गोली लेने से पहले डॉक्टर से पूछें।'],
    'glutathione-cream-price': ['भारत में ग्लूटाथियोन क्रीम कुछ सौ से कई हज़ार रुपये तक मिलती है।',
                                'कीमत प्रति ग्राम, पूरी सामग्री सूची और सच्चे दावे देखें।',
                                'बहुत सस्ती, बिना लेबल वाली "फेयरनेस" क्रीम से बचें।'],
    'glutathione-se-gora-hota-hai-kya': ['नहीं, ग्लूटाथियोन प्राकृतिक त्वचा का रंग नहीं बदलता।',
                                         'यह टैन और दाग-धब्बों को धीरे-धीरे हल्का दिखा सकता है, सनस्क्रीन के साथ।',
                                         '"हमेशा के लिए गोरा" करने वाला कोई इंजेक्शन, गोली या क्रीम साबित नहीं है।'],
    'glutathione-cream-sawal-jawab': ['ग्लूटाथियोन क्रीम रोज़ रात लगाई जा सकती है; रेटिनॉल वाली क्रीम धीरे-धीरे शुरू करें।',
                                      'नतीजे 8–12 हफ्तों में; रोज़ सनस्क्रीन ज़रूरी है।',
                                      'गर्भावस्था में या त्वचा की समस्या हो तो डॉक्टर से पूछें।'],
    'shaadi-se-pehle-glutathione': ['शादी से 10–12 हफ्ते पहले ग्लूटाथियोन क्रीम शुरू करें, रोज़ सनस्क्रीन के साथ।',
                                    'आखिरी दो हफ्तों में कोई नई क्रीम, पील या ब्लीच नहीं।',
                                    'ग्लूटाथियोन इंजेक्शन और IV ड्रिप से बचें।'],
}

# ---------------- GEO pages: a citable fact sheet and three questions people ask AI assistants ----------------
NEW_GUIDES += [
    dict(slug='glutathione-facts', title='Glutathione: key facts and figures, with sources', short='Facts and figures',
         blurb='The essential numbers on glutathione for skin in one place: studies, doses, timelines and safety, each with its source.',
         seo='Glutathione Facts & Figures: Studies, Doses, Safety (Sources)', desc='Key facts on glutathione for skin with sources: what it is, the main clinical studies, doses, how long results take, safety of creams, tablets and injections.',
         refs=['study', 'oral', 'wesch', 'ijdvl', 'review', 'fda'],
         qa=[('What are the key facts about glutathione for skin?', 'Glutathione is an antioxidant the body makes from three amino acids. Small trials found modest, gradual drops in skin melanin: a 2%% lotion over 10 weeks and 250–500 mg tablets over 4–12 weeks. It does not change natural skin colour, and injections for skin lightening lack trials and carry regulator warnings.', '')],
         body='''<h2>The molecule</h2><div class="tbl"><table class="facts"><tbody>
<tr><td>What it is</td><td>A tripeptide antioxidant made of glutamic acid (glutamate), cysteine and glycine; often written GSH</td></tr>
<tr><td>Where it is made</td><td>In the body's own cells, mostly the liver</td></tr>
<tr><td>Main job</td><td>Protects cells from oxidative damage and recycles vitamins C and E</td></tr>
<tr><td>Link to skin tone</td><td>Slows tyrosinase, the enzyme that makes melanin, and may shift production towards lighter pheomelanin (%(ijdvl)s)</td></tr></tbody></table></div>
<h2>The main clinical studies on skin</h2><div class="tbl"><table><thead><tr><th>Study</th><th>What was tested</th><th>Who and how long</th><th>Finding</th></tr></thead><tbody>
<tr><td>%(study)s</td><td>2%% oxidised glutathione lotion, twice daily</td><td>30 healthy women, 10 weeks</td><td>Melanin index fell more on the treated side than placebo</td></tr>
<tr><td>%(oral)s</td><td>500 mg capsules daily</td><td>60 healthy adults, 4 weeks</td><td>Melanin index fell at all six measured sites versus placebo</td></tr>
<tr><td>%(wesch)s</td><td>250 mg a day, reduced or oxidised form</td><td>60 women aged 20–50, 12 weeks</td><td>Trends to lower melanin, mostly not statistically significant</td></tr></tbody></table></div>
<h2>What the reviews conclude</h2><ul><li>A 2025 systematic review of topical glutathione (%(review)s): promising, but studies are few, small and short.</li><li>The Indian dermatology review (%(ijdvl)s): short-term evidence is encouraging for creams and tablets, not strong enough to call glutathione a treatment for melasma, and no trial supports IV glutathione for skin lightening.</li></ul>
<h2>Timelines and numbers to remember</h2><div class="tbl"><table class="facts"><tbody>
<tr><td>Fresher look</td><td>Often 4–8 weeks of nightly use</td></tr>
<tr><td>Lighter-looking tan</td><td>Usually 8–12 weeks, with daily SPF 30+ sunscreen</td></tr>
<tr><td>Doses studied (tablets)</td><td>250–500 mg a day, for 4–12 weeks</td></tr>
<tr><td>Cream tolerance</td><td>In the 10-week lotion study, 1 of 30 women had mild redness that cleared in two days</td></tr>
<tr><td>Injections</td><td>No clinical trial for skin lightening; warned against by regulators (%(fda)s)</td></tr></tbody></table></div>
<h2>What glutathione does not do</h2><p>It does not change natural skin colour, results fade without sun protection, and no cream, tablet or injection is proven to whiten skin permanently.</p>
<h2>How to cite this page</h2><p class="cite">GlutaNex. "Glutathione: key facts and figures, with sources." glutanex.co.in/glutathione-facts/. Please link to the original studies listed below as well.</p>''',
         faq=[('How long does glutathione take to work on skin?', 'In studies, changes appeared after 4 to 12 weeks. With a cream, expect a fresher look in 4 to 8 weeks and lighter-looking tan in 8 to 12 weeks, with daily sunscreen.'),
              ('What dose of glutathione was used in studies?', 'Tablet studies used 250 to 500 mg a day for 4 to 12 weeks. The best-known cream study used a 2%% oxidised glutathione lotion twice daily for 10 weeks.')]),
    dict(slug='glutathione-for-underarms-and-body', title='Glutathione for dark underarms, knees and elbows: what helps', short='Underarms and body',
         blurb='Why underarms, knees and elbows get darker, what glutathione can and cannot do there, and a gentle routine.',
         seo='Glutathione for Dark Underarms, Knees & Elbows: What Helps', desc='Can glutathione lighten dark underarms, knees and elbows? Common causes, a gentle routine, when to see a doctor, and why retinol face creams are not for underarms.',
         refs=['ijdvl', 'review'],
         qa=[('Can glutathione lighten dark underarms?', 'It may help a little where darkness comes from friction or shaving irritation, but evidence is for the face and is modest. Underarm skin is thin and easily irritated, so gentle care matters most. Velvety, thick dark skin can be a sign of insulin resistance and needs a doctor.', ''),
             ('Can I use glutathione face cream on my underarms?', 'Not a cream with retinol or salicylic acid, like the GlutaNex Night Cream: it can sting and irritate thin underarm skin, especially after shaving. On knees and elbows, patch test first and use a thin layer at night.', '')],
         body='''<h2>Why these areas get darker</h2><ul><li><b>Friction:</b> tight clothes and skin rubbing on skin.</li><li><b>Shaving and waxing:</b> repeated irritation leaves dark marks.</li><li><b>Deodorant irritation:</b> some fragrances and alcohol sting.</li><li><b>Dry, thick skin</b> on knees and elbows from pressure.</li><li><b>Acanthosis nigricans:</b> velvety, thick, dark skin in folds, linked to insulin resistance and some hormone conditions. See a doctor if you notice this.</li></ul>
<h2>A gentle routine that helps</h2><ol><li>Wash gently; skip harsh scrubs and lemon.</li><li>Switch to a fragrance-free deodorant if yours stings.</li><li>Trim or use a fresh razor with gel; avoid shaving on irritated skin.</li><li>Moisturise knees and elbows daily.</li><li>Use sunscreen on exposed knees and elbows.</li></ol>
<h2>Where glutathione fits</h2><p>Studies on glutathione creams looked at the face (%(review)s). On knees and elbows a thin layer of a glutathione cream at night is reasonable after a patch test. %(cream)s contains retinol and salicylic acid, so keep it away from underarms and freshly shaved skin.</p>
<h2>Avoid</h2><p>Bleach creams, unlabelled "whitening" creams, and creams that work "in days": they may contain steroids or mercury (%(ijdvl)s).</p>''',
         faq=[('How long does it take for dark underarms to fade?', 'If you remove the cause, such as friction or shaving irritation, marks usually fade over 2 to 3 months. Darkness from acanthosis nigricans needs treatment of the underlying cause.'),
              ('Do glutathione soaps lighten underarms?', 'A soap is rinsed off in seconds, so its glutathione has little time to act. Gentle washing helps; the soap itself is unlikely to change pigmentation.')]),
    dict(slug='glutathione-for-dark-circles', title='Glutathione for dark circles: does it work?', short='Dark circles',
         blurb='The different causes of dark circles, which type glutathione might help, and how to care for the eye area safely.',
         seo='Glutathione for Dark Circles: Does It Work? Causes & Safe Care', desc='Does glutathione help dark circles? The four common causes, which kind may respond, why retinol creams should not go near the eyes, and simple habits that help.',
         refs=['review', 'ijdvl'],
         qa=[('Does glutathione help dark circles?', 'Only a little, and only for the brownish, pigment type. Many dark circles come from thin skin showing blood vessels, hollows, puffiness or genetics, which glutathione cannot change. Never apply retinol or acid creams close to the eyes.', ''),
             ('Can I put glutathione night cream under my eyes?', 'Not one with retinol or salicylic acid, such as the GlutaNex Night Cream. Keep it at least a finger-width away from the eyes and use a gentle, fragrance-free eye cream instead.', '')],
         body='''<h2>Four common causes</h2><div class="tbl"><table><thead><tr><th>Type</th><th>What it looks like</th><th>What helps</th></tr></thead><tbody>
<tr><td>Pigment</td><td>Brownish, common in Indian skin</td><td>Sunscreen, sunglasses, gentle brightening care</td></tr>
<tr><td>Vascular</td><td>Bluish or purple, worse when tired</td><td>Sleep, cool compress, treating allergies</td></tr>
<tr><td>Hollows</td><td>Shadow under the eye</td><td>Mostly structural; a dermatologist can advise</td></tr>
<tr><td>Puffiness</td><td>Bags, worse in the morning</td><td>Less salt at night, sleep, treating allergies</td></tr></tbody></table></div>
<h2>Where glutathione fits</h2><p>Glutathione is studied for overall skin tone, not specifically for dark circles (%(review)s). For the pigment type, sun protection does most of the work.</p>
<h2>Habits that help</h2><ul><li>7 to 8 hours of sleep.</li><li>Do not rub your eyes; treat itchy allergies.</li><li>Sunscreen around the eyes (mineral formulas sting less) and sunglasses.</li><li>A gentle, fragrance-free eye cream at night.</li></ul>
<h2>When to see a doctor</h2><p>Sudden dark circles, one-sided swelling, or circles with tiredness and weight change are worth a check-up.</p>''',
         faq=[('What is the fastest way to reduce dark circles?', 'There is no instant fix. Sleep, a cool compress for puffiness, treating allergies and daily sun protection help most within weeks.'),
              ('Is glutathione safe around the eyes?', 'Glutathione itself is gentle, but many creams also contain retinol or acids that irritate the eye area. Keep those creams away from the eyes.')]),
    dict(slug='glutathione-serum-vs-cream-vs-soap', title='Glutathione serum vs cream vs soap: which works best?', short='Serum vs cream vs soap',
         blurb='How glutathione serums, creams, soaps and face washes differ, and which format makes sense for your skin.',
         seo='Glutathione Serum vs Cream vs Soap: Which Works Best?', desc='Glutathione serum, cream, soap or face wash: how long each stays on skin, which suits oily or dry skin, what the research used, and how to build a simple routine.',
         refs=['study', 'review'],
         qa=[('Which is better, glutathione serum or cream?', 'Both are leave-on, which is what the research used. Serums are lighter and suit oily skin under a moisturiser; creams also moisturise and suit normal to dry skin. The formula, regular use and daily sunscreen matter more than the format.', ''),
             ('Does glutathione soap work?', 'Soaps and face washes are rinsed off within a minute, so they mainly clean. They are a fine first step, but visible change needs a leave-on product and sunscreen.', '')],
         body='''<h2>The formats compared</h2><div class="tbl"><table><thead><tr><th>Format</th><th>Contact time</th><th>Best for</th><th>Role</th></tr></thead><tbody>
<tr><td>Soap / face wash</td><td>Under a minute</td><td>Everyone</td><td>Cleans; prepares skin</td></tr>
<tr><td>Serum</td><td>Leave-on</td><td>Oily or combination skin</td><td>Light active layer under moisturiser</td></tr>
<tr><td>Cream</td><td>Leave-on</td><td>Normal to dry skin</td><td>Active care plus moisture</td></tr>
<tr><td>Body lotion</td><td>Leave-on</td><td>Arms, legs</td><td>Moisture; modest tone care</td></tr></tbody></table></div>
<h2>What the research used</h2><p>The best-known study used a leave-on 2%% glutathione lotion twice daily for 10 weeks (%(study)s). A 2025 review found studies of leave-on glutathione promising but small (%(review)s). There is little evidence for soaps.</p>
<h2>A simple routine</h2><ol><li>Night: cleanse with a gentle face wash such as %(wash)s.</li><li>Apply one leave-on glutathione product (a cream like %(cream)s, or a serum).</li><li>Morning: sunscreen SPF 30 or higher.</li></ol><p>Using several glutathione products at once does not speed results and adds irritation risk.</p>
<h2>Red flags in any format</h2><p>Promises to whiten in days, no ingredient list, or no seller details.</p>''',
         faq=[('Can I use glutathione serum and cream together?', 'You can, but it is rarely needed. One leave-on product used consistently, with sunscreen, is simpler and gentler.'),
              ('Is glutathione face wash enough on its own?', 'It cleans and refreshes, but for a brighter, more even look you need a leave-on product and daily sunscreen.')]),
]
TLDR.update({
    'glutathione-facts': ['Glutathione is a tripeptide antioxidant (glutamate, cysteine, glycine) made mostly in the liver.',
                          'Trials: 2% lotion for 10 weeks (30 women); 500 mg tablets for 4 weeks (60 adults); 250 mg for 12 weeks (60 women): modest effects.',
                          'It does not change natural skin colour; injections for lightening lack trials and carry warnings.'],
    'glutathione-for-underarms-and-body': ['Underarm, knee and elbow darkness usually comes from friction, shaving or dryness.',
                                           'Glutathione evidence is for the face; remove the cause first and care gently.',
                                           'Velvety, thick dark skin can signal insulin resistance: see a doctor.'],
    'glutathione-for-dark-circles': ['Glutathione may help only the brownish, pigment type of dark circles, and only a little.',
                                     'Thin skin, vessels, hollows and puffiness need other care.',
                                     'Keep retinol and acid creams away from the eye area.'],
    'glutathione-serum-vs-cream-vs-soap': ['Soaps and face washes mainly clean; they are rinsed off too fast to change tone.',
                                           'Serums and creams are leave-on, like the products used in research.',
                                           'One leave-on product plus daily sunscreen beats stacking several.'],
})

# ---------------- October 2026: new keyword gaps (melasma, pigmentation, timeline, lips, GSH vs GSSG, liposomal, glossary) ----------------
REFS.update(
    richie='<a href="https://pubmed.ncbi.nlm.nih.gov/24791752/" rel="noopener">Richie et al., 2015</a>',
    lipo='<a href="https://pubmed.ncbi.nlm.nih.gov/28853742/" rel="noopener">Sinha et al., 2018</a>',
    vislight='<a href="https://pubmed.ncbi.nlm.nih.gov/24313385/" rel="noopener">Castanedo-Cázares et al., 2014</a>',
)
SOURCES.update({
    'richie': 'Richie JP Jr, et al. Randomized controlled trial of oral glutathione supplementation on body stores of glutathione. Eur J Nutr. 2015;54(2):251-263.',
    'lipo': 'Sinha R, et al. Oral supplementation with liposomal glutathione elevates body stores of glutathione and markers of immune function. Eur J Clin Nutr. 2018;72(1):105-111.',
    'vislight': 'Castanedo-Cázares JP, et al. Near-visible light and UV photoprotection in the treatment of melasma: a double-blind randomized trial. Photodermatol Photoimmunol Photomed. 2014;30(1):35-42.',
})

GLOSSARY = [
    ('Antioxidant', 'A substance that neutralises free radicals, the unstable molecules made by sunlight, pollution and normal metabolism. Glutathione, vitamin C and vitamin E are antioxidants.', '/glutathione/'),
    ('Broad-spectrum sunscreen', 'A sunscreen that protects against both UVB (burning) and UVA (tanning and ageing) rays.', '/glutathione-cream-for-summer-tan/'),
    ('Ceramides', 'Natural fats in the outer skin layer that hold skin cells together and keep moisture in. Added to creams to support the skin barrier.', ''),
    ('Cysteine', 'One of the three amino acids in glutathione. Its sulphur group is what lets glutathione act as an antioxidant.', '/glutathione-rich-foods/'),
    ('Eumelanin', 'The dark brown-black type of melanin. Glutathione may shift production away from it.', ''),
    ('Free radicals', 'Unstable molecules that damage cells. UV light and pollution increase them in skin.', ''),
    ('GSH (reduced glutathione)', 'The active form of glutathione that neutralises free radicals.', '/reduced-vs-oxidized-glutathione/'),
    ('GSSG (oxidised glutathione)', 'Two glutathione molecules joined after doing their antioxidant job. More stable in lotions; the body can turn it back into GSH.', '/reduced-vs-oxidized-glutathione/'),
    ('Hyaluronic acid', 'A water-holding molecule found naturally in skin. In creams it draws water into the top layer so skin feels hydrated.', ''),
    ('Hyperpigmentation', 'Any area of skin darker than the skin around it: tan, sun spots, acne marks or melasma.', '/glutathione-for-pigmentation/'),
    ('Kojic acid', 'A brightening ingredient made by fungi that slows melanin production. Can irritate some skin.', '/glutathione-vs-kojic-acid/'),
    ('Liposomal', 'Wrapped in tiny fat bubbles (liposomes), usually to help a supplement survive digestion.', '/liposomal-glutathione/'),
    ('Melanin', 'The pigment that gives skin, hair and eyes their colour and helps protect skin from the sun.', '/glutathione/'),
    ('Melanin index', 'A number measured by a skin meter in studies to track how much melanin is in skin.', '/glutathione-facts/'),
    ('Melanocyte', 'The skin cell that makes melanin.', ''),
    ('Melasma', 'Brown or grey-brown patches, usually on both cheeks, forehead or upper lip, linked to sun, hormones and genetics. Needs a dermatologist.', '/glutathione-for-melasma/'),
    ('Niacinamide', 'Vitamin B3. Helps the look of uneven tone and supports the skin barrier. Often paired with glutathione.', '/glutathione-and-niacinamide/'),
    ('PA rating', 'A rating (PA+ to PA++++) used on Asian sunscreens for UVA protection. More plus signs mean more UVA protection.', ''),
    ('Patch test', 'Trying a product on a small area, such as behind the ear, for 24 hours before using it on the face.', '/glutathione-side-effects/'),
    ('Pheomelanin', 'The lighter red-yellow type of melanin.', ''),
    ('PIH (post-inflammatory hyperpigmentation)', 'Dark marks left after a pimple, cut, burn or rash heals. Common in Indian skin.', '/glutathione-for-acne-marks/'),
    ('Retinol', 'A form of vitamin A used at night for smoother-looking skin. Can cause dryness at first and makes skin more sun-sensitive.', '/retinol-vs-glutathione/'),
    ('Salicylic acid (BHA)', 'An oil-soluble acid that exfoliates inside pores. Helpful for oily skin; can sting on broken or shaved skin.', '/glutathione-for-oily-skin/'),
    ('SPF', 'Sun Protection Factor: how well a sunscreen protects against UVB. SPF 30 or higher is recommended for daily use.', ''),
    ('Tripeptide', 'A small chain of three amino acids. Glutathione is a tripeptide of glutamic acid, cysteine and glycine.', '/glutathione/'),
    ('Tyrosinase', 'The enzyme skin uses to make melanin. Glutathione, kojic acid and vitamin C can slow it.', '/glutathione/'),
    ('Visible light', 'The light we can see. On brown skin it can deepen pigmentation such as melasma; tinted sunscreens with iron oxides help block it.', '/glutathione-for-melasma/'),
]
_GL_LBL = {'/glutathione/': 'Glutathione guide', '/glutathione-cream-for-summer-tan/': 'Summer tan guide', '/glutathione-rich-foods/': 'Glutathione-rich foods',
    '/reduced-vs-oxidized-glutathione/': 'GSH vs GSSG', '/glutathione-for-pigmentation/': 'Pigmentation guide', '/glutathione-vs-kojic-acid/': 'Glutathione vs kojic acid',
    '/liposomal-glutathione/': 'Liposomal glutathione', '/glutathione-facts/': 'Facts and figures', '/glutathione-for-melasma/': 'Melasma guide',
    '/glutathione-and-niacinamide/': 'Glutathione and niacinamide', '/glutathione-side-effects/': 'Side effects', '/glutathione-for-acne-marks/': 'Acne marks guide',
    '/retinol-vs-glutathione/': 'Retinol vs glutathione', '/glutathione-for-oily-skin/': 'Oily skin guide'}
_gl_rows = ''.join('<div class="gl-item" id="%s"><dt>%s</dt><dd>%s%s</dd></div>' % (
    re.sub(r'[^a-z0-9]+', '-', t.lower()).strip('-'), t, d.replace('%', '%%'), (' <a href="%s">%s</a>' % (u, _GL_LBL.get(u, 'Read the guide'))) if u else '') for t, d, u in GLOSSARY)

NEW_GUIDES += [
    dict(slug='glutathione-for-melasma', title='Glutathione for melasma: does it help, and what actually works?', short='Melasma',
         blurb='How to tell melasma from tan, what glutathione can and cannot do for it, and the routine dermatologists build around sun protection.',
         seo='Glutathione for Melasma: Does It Work? What Actually Helps', desc='Does glutathione help melasma? How melasma differs from tan, why tinted sunscreen matters, what dermatologists use, and a gentle routine.',
         refs=['ijdvl', 'review', 'vislight'],
         qa=[('Does glutathione help melasma?', 'Not reliably. The Indian dermatology review found the evidence too weak to call glutathione a melasma treatment. A glutathione cream can be part of a gentle routine, but daily sunscreen and a dermatologist\'s plan do most of the work.', ''),
             ('What is the best treatment for melasma?', 'Strict daily sun protection, ideally a tinted sunscreen that also blocks visible light, plus treatment chosen by a dermatologist. Melasma can be controlled but often returns, so long-term care matters.', '')],
         body='''<h2>Is it melasma or tan?</h2><div class="tbl"><table><thead><tr><th></th><th>Tan</th><th>Melasma</th><th>Sun spots</th></tr></thead><tbody>
<tr><td>Looks like</td><td>Even darkening of sun-exposed skin</td><td>Patchy brown or grey-brown areas, often on both cheeks, forehead, nose bridge or upper lip</td><td>Small, flat, round brown spots</td></tr>
<tr><td>Main triggers</td><td>Sun</td><td>Sun and visible light, hormones (pregnancy, pills), genetics, heat</td><td>Years of sun</td></tr>
<tr><td>Fades on its own?</td><td>Yes, over weeks with sun protection</td><td>Rarely; tends to return</td><td>Slowly, if at all</td></tr>
<tr><td>Who to see</td><td>Skincare and sunscreen are enough</td><td>A dermatologist</td><td>A dermatologist if a spot changes</td></tr></tbody></table></div>
<h2>Why sunscreen matters even more for melasma</h2><p>Melasma is darkened not only by UV rays but also by visible light, which ordinary sunscreens do not block well. In a randomised trial, people with melasma who used a sunscreen that also blocked visible light (with iron oxides, which give tinted sunscreens their colour) improved more than those using UV-only sunscreen (%(vislight)s).</p><ul><li>Use a tinted, broad-spectrum SPF 30+ sunscreen every morning, indoors too if you sit near windows.</li><li>Reapply every 2–3 hours outdoors; add a hat and shade.</li><li>Heat can also worsen melasma: avoid steam rooms and very hot kitchens where you can.</li></ul>
<h2>What a dermatologist may suggest</h2><p>Treatment depends on your skin and is a medical decision. Options doctors use include prescription creams (sometimes a short course of a combination cream), azelaic acid, tranexamic acid and gentle peels. Do not use steroid-containing "fairness" creams on your own: misuse of steroid creams on the face is a common cause of thin, red, damaged skin in India (%(ijdvl)s).</p>
<h2>Where glutathione fits</h2><p>Glutathione slows tyrosinase, the enzyme that makes melanin, so it is often tried for pigmentation. But the studies are small and short (%(review)s), and the Indian dermatology review says the evidence is not strong enough to call glutathione a melasma treatment (%(ijdvl)s). If your dermatologist agrees, a glutathione and niacinamide cream such as %(cream)s can sit in a gentle night routine. It contains retinol and salicylic acid, so ask before combining it with prescription creams.</p>
<h2>Melasma in pregnancy</h2><p>Melasma often starts or worsens in pregnancy. Use sunscreen and gentle basics only, and skip retinol creams. Many cases fade after delivery. Read <a href="/glutathione-in-pregnancy/">glutathione in pregnancy</a>.</p>''',
         faq=[('Can melasma be cured permanently?', 'Melasma can be lightened and controlled, but it often returns with sun, heat or hormonal changes. Ongoing sun protection is the key to keeping it away.'),
              ('Are glutathione injections good for melasma?', 'No. There is no clinical trial supporting glutathione injections for melasma or skin lightening, and regulators have warned about their safety.')]),

    dict(slug='glutathione-for-pigmentation', title='Glutathione for pigmentation: types, what helps and what to avoid', short='Pigmentation',
         blurb='The five common kinds of pigmentation on Indian skin, which ones a glutathione cream may help, and when to see a dermatologist.',
         seo='Glutathione for Pigmentation: Types, What Helps, What to Avoid', desc='Can glutathione reduce pigmentation? The common types (tan, sun spots, acne marks, melasma, freckles), what helps each, how long it takes, and warning signs.',
         refs=['study', 'review', 'ijdvl'],
         qa=[('Does glutathione reduce pigmentation?', 'It may help some types look lighter over 8 to 12 weeks, mainly tan and acne marks, when used with daily sunscreen. It works modestly and gradually, and it is not proven for melasma.', ''),
             ('Which glutathione product is best for pigmentation?', 'A leave-on cream or serum, used at night, with SPF 30+ sunscreen every morning. Leave-on products are what the research tested; soaps and face washes rinse off too quickly.', '')],
         body='''<h2>The common types of pigmentation</h2><div class="tbl"><table><thead><tr><th>Type</th><th>What it looks like</th><th>Can a glutathione cream help?</th><th>Read</th></tr></thead><tbody>
<tr><td>Sun tan</td><td>Even darkening of exposed skin</td><td>Yes, gradually, with sunscreen</td><td><a href="/glutathione-cream-for-summer-tan/">Summer tan</a></td></tr>
<tr><td>Acne marks (PIH)</td><td>Flat brown marks where pimples healed</td><td>Can help them fade faster</td><td><a href="/glutathione-for-acne-marks/">Acne marks</a></td></tr>
<tr><td>Sun spots</td><td>Small, round, flat brown spots</td><td>A little; slow</td><td><a href="/glutathione-for-dark-spots-and-tan/">Dark spots and tan</a></td></tr>
<tr><td>Melasma</td><td>Patches on both cheeks, forehead or upper lip</td><td>Not reliably; see a dermatologist</td><td><a href="/glutathione-for-melasma/">Melasma</a></td></tr>
<tr><td>Freckles</td><td>Tiny spots, often since childhood</td><td>Little; sunscreen stops them darkening</td><td></td></tr></tbody></table></div>
<h2>A routine that helps most pigmentation</h2><ol><li><b>Night:</b> gentle face wash such as %(wash)s, then a leave-on glutathione cream such as %(cream)s.</li><li><b>Morning:</b> broad-spectrum SPF 30+ sunscreen, reapplied outdoors.</li><li><b>Hands off:</b> do not pick pimples or scrub hard; irritation makes new marks.</li><li><b>Wait:</b> 8 to 12 weeks before judging. See <a href="/how-long-does-glutathione-take-to-work/">how long glutathione takes to work</a>.</li></ol>
<h2>What the research shows</h2><p>In the best-known study, a 2%% glutathione lotion lowered the melanin index more than placebo over 10 weeks (%(study)s). A 2025 review called topical glutathione promising but noted that studies are few and small (%(review)s).</p>
<h2>What to avoid</h2><ul><li>Steroid or unlabelled "fairness" creams that promise results in days (%(ijdvl)s).</li><li>Lemon, baking soda or toothpaste on the face.</li><li>Starting several strong actives at once.</li></ul>
<h2>When to see a dermatologist</h2><p>Patches on both cheeks, a spot that changes size, shape or colour, bleeding, or no change after 3 months of care.</p>''',
         faq=[('How long does glutathione take to reduce pigmentation?', 'Most people need 8 to 12 weeks of nightly use with daily sunscreen to see tan or acne marks look lighter. Deeper pigmentation takes longer or needs a dermatologist.'),
              ('Can pigmentation come back after stopping glutathione?', 'Yes, if the cause continues. Sun exposure brings tan and spots back, which is why daily sunscreen matters more than any single cream.')]),

    dict(slug='how-long-does-glutathione-take-to-work', title='How long does glutathione cream take to work? A week-by-week timeline', short='How long it takes',
         blurb='What to expect in week 1, month 1 and month 3 of using a glutathione cream, and the common reasons people see no change.',
         seo='How Long Does Glutathione Cream Take to Work? Week-by-Week', desc='Glutathione cream results week by week: what changes in weeks 1–2, 4–8 and 8–12, what studies found, and why some people see no results.',
         refs=['study', 'oral', 'wesch', 'review'],
         qa=[('How long does glutathione cream take to show results?', 'Expect skin to feel smoother within 2 to 4 weeks, a fresher look in 4 to 8 weeks, and lighter-looking tan or marks in 8 to 12 weeks of nightly use with daily sunscreen. Studies on glutathione ran for 4 to 12 weeks.', ''),
             ('Can glutathione show results in 7 days?', 'No honest product can promise visible lightening in 7 days. Skin renews over about a month, and pigment fades slowly. A cream that changes colour in days may contain steroids or bleach.', '')],
         body='''<h2>Week-by-week timeline</h2><div class="tbl"><table><thead><tr><th>When</th><th>What you may notice</th><th>What to do</th></tr></thead><tbody>
<tr><td>Weeks 1–2</td><td>Skin adjusting. With retinol creams, mild tingling or dryness is common.</td><td>Use 2–3 nights a week. Sunscreen every morning.</td></tr>
<tr><td>Weeks 3–4</td><td>Smoother, more hydrated feel.</td><td>Every other night if comfortable.</td></tr>
<tr><td>Weeks 4–8</td><td>A fresher, less dull look.</td><td>Nightly if your skin is happy.</td></tr>
<tr><td>Weeks 8–12</td><td>Tan and acne marks look lighter and more even.</td><td>Keep going; compare photos.</td></tr>
<tr><td>After 12 weeks</td><td>Gains hold only with sun protection.</td><td>Continue the routine to maintain.</td></tr></tbody></table></div>
<h2>What the studies found</h2><ul><li>Topical: a 2%% glutathione lotion showed a lower melanin index after 10 weeks (%(study)s).</li><li>Tablets: changes after 4 weeks at 500 mg a day (%(oral)s), and smaller, mostly non-significant changes over 12 weeks at 250 mg a day (%(wesch)s).</li><li>A 2025 review: effects are modest and studies are short (%(review)s).</li></ul>
<h2>Why some people see no results</h2><ul><li><b>No daily sunscreen</b>, so new tan keeps replacing what fades.</li><li><b>Using it now and then</b> instead of most nights.</li><li><b>Melasma</b>, which needs a dermatologist (see <a href="/glutathione-for-melasma/">glutathione for melasma</a>).</li><li><b>Expecting a colour change:</b> glutathione does not change natural skin colour.</li><li><b>Irritation</b> from too much product or too many actives, which can leave new marks.</li></ul>
<h2>Track progress honestly</h2><p>Take a photo on day 1 in the same spot, same daylight, no filter, then once every 2 weeks. Compare week 1 with week 8, not day to day. If you bought %(cream)s, the free <a href="/routine/">routine tracker</a> counts your nights for you.</p>''',
         faq=[('Is 30 g of glutathione cream enough to see results?', 'Used as a pea-sized amount at night, a 30 g jar usually lasts about 6 to 8 weeks, which is enough to judge the early changes. Tan and marks often need 8 to 12 weeks.'),
              ('Should I use more cream to get faster results?', 'No. More product does not work faster and raises the chance of irritation, especially with retinol creams. A pea-sized amount for the whole face is enough.')]),

    dict(slug='glutathione-for-dark-lips', title='Glutathione for dark lips: causes and safe care', short='Dark lips',
         blurb='Why lips get darker, whether glutathione lip products help, and a gentle routine that works on lips.',
         seo='Glutathione for Dark Lips: Causes, Does It Work, Safe Care', desc='Does glutathione lighten dark lips? Common causes (sun, smoking, lip licking, allergies), why retinol creams should not go on lips, and what helps.',
         refs=['review', 'ijdvl'],
         qa=[('Does glutathione lighten dark lips?', 'There is no good study on glutathione for lips. Dark lips usually improve when the cause is removed: sun protection with an SPF lip balm, no lip licking, no smoking and avoiding products that irritate.', ''),
             ('Can I apply glutathione night cream on my lips?', 'Not one with retinol or salicylic acid, such as the GlutaNex Night Cream; lips are thin and peel easily. Use a plain lip balm with SPF instead.', '')],
         body='''<h2>Why lips get darker</h2><ul><li><b>Sun:</b> lips have very little natural protection.</li><li><b>Smoking:</b> heat and nicotine darken lips over time.</li><li><b>Lip licking and dryness:</b> repeated irritation leaves pigment.</li><li><b>Allergy to a lipstick, balm or toothpaste:</b> look for itching or peeling.</li><li><b>Natural colour:</b> many people have darker lips by genetics; that is normal.</li></ul>
<h2>A gentle lip routine</h2><ol><li>An SPF 15+ lip balm by day, reapplied after eating.</li><li>A plain, fragrance-free balm at night.</li><li>Stop licking or biting lips; drink water.</li><li>If a new lipstick stings or itches, stop it.</li><li>Skip lemon, sugar scrubs and bleach on lips.</li></ol>
<h2>What about glutathione?</h2><p>Glutathione research is on facial skin, not lips (%(review)s). A gentle lip product with glutathione will not harm most people, but sun protection and removing the cause matter far more. Keep retinol and acid creams, including %(cream)s, off the lips.</p>
<h2>When to see a doctor</h2><p>A new dark spot on the lip, a spot that changes or bleeds, or dark patches inside the mouth should be checked by a doctor.</p>''',
         faq=[('How long does it take for dark lips to become lighter?', 'When the cause, such as sun or lip licking, is removed, lips often look better in 4 to 8 weeks. Natural lip colour does not change.'),
              ('Does smoking cause dark lips?', 'Yes, smoking is a common cause. Lips often lighten gradually after quitting.')]),

    dict(slug='reduced-vs-oxidized-glutathione', title='Reduced vs oxidised glutathione (GSH vs GSSG): which is better for skin?', short='Reduced vs oxidised',
         blurb='What reduced and oxidised glutathione are, why creams use one or the other, and what to check on the label.',
         seo='Reduced vs Oxidized Glutathione (GSH vs GSSG) for Skin', desc='Reduced (GSH) vs oxidised (GSSG) glutathione: how they differ, which form skin studies used, stability in creams, and what matters more.',
         refs=['study', 'wesch', 'review'],
         qa=[('What is the difference between reduced and oxidised glutathione?', 'Reduced glutathione (GSH) is the active antioxidant form. After it neutralises a free radical, two molecules join into oxidised glutathione (GSSG). The body turns GSSG back into GSH with an enzyme, so the two forms cycle.', ''),
             ('Is oxidised glutathione better for skin creams?', 'Oxidised glutathione is more stable in water-based formulas, and the best-known cream study used it. There is no head-to-head study showing one form works better in a cream.', '')],
         body='''<h2>The two forms in one table</h2><div class="tbl"><table><thead><tr><th></th><th>Reduced (GSH)</th><th>Oxidised (GSSG)</th></tr></thead><tbody>
<tr><td>What it is</td><td>One glutathione molecule, active</td><td>Two glutathione molecules joined</td></tr>
<tr><td>In the body</td><td>Most of the glutathione in healthy cells</td><td>Formed after antioxidant work, then recycled</td></tr>
<tr><td>Stability in products</td><td>Oxidises with air and water</td><td>More stable</td></tr>
<tr><td>Skin studies</td><td>250 mg tablets, 12 weeks (%(wesch)s)</td><td>2%% lotion, 10 weeks (%(study)s); 250 mg tablets (%(wesch)s)</td></tr></tbody></table></div>
<h2>What the studies used</h2><p>The 10-week lotion study used oxidised glutathione and found a lower melanin index than placebo (%(study)s). A 12-week tablet study compared both forms; both trended towards lower melanin, and the reduced form also showed some wrinkle improvement (%(wesch)s). A 2025 review found no strong reason to prefer one form in creams (%(review)s).</p>
<h2>What matters more than the form</h2><ul><li><b>Packaging:</b> an airtight, opaque jar or tube protects glutathione from air and light. Close the lid after use.</li><li><b>The whole formula:</b> partners like niacinamide and vitamin C do much of the work.</li><li><b>Regular use and sunscreen:</b> they decide results more than GSH vs GSSG.</li><li><b>A faint sulphur smell</b> is normal for glutathione products.</li></ul>
<h2>On labels</h2><p>You may see "glutathione", "reduced glutathione", "L-glutathione" or "oxidised/oxidized glutathione". All are the same molecule family; check the full ingredient list and honest claims.</p>''',
         faq=[('What is L-glutathione?', 'L-glutathione is simply the natural form of glutathione, the one the body makes. Most products labelled glutathione contain the L form.'),
              ('Why does my glutathione cream smell?', 'Glutathione contains sulphur, so a faint smell is normal. A strong change in smell, colour or texture after opening means the product may have gone off.')]),

    dict(slug='liposomal-glutathione', title='Liposomal glutathione: what it is, does it work for skin, and is it safe?', short='Liposomal glutathione',
         blurb='What "liposomal" means, what the studies on liposomal and regular glutathione supplements found, and what is still unknown for skin.',
         seo='Liposomal Glutathione: Benefits, Skin Results, Safety', desc='Liposomal glutathione explained: what liposomes are, what studies found on body glutathione levels, the lack of skin-tone trials, and safety.',
         refs=['richie', 'lipo', 'oral', 'ijdvl'],
         qa=[('What is liposomal glutathione?', 'It is glutathione wrapped in liposomes, tiny fat bubbles, to help it survive digestion when taken by mouth. It is sold as a supplement, usually as a liquid or capsule.', ''),
             ('Does liposomal glutathione lighten skin?', 'We found no published trial of liposomal glutathione for skin tone. Small studies show it can raise glutathione levels in the body, but that is not the same as proven skin lightening.', '')],
         body='''<h2>What the studies found</h2><div class="tbl"><table><thead><tr><th>Study</th><th>Form and dose</th><th>Who and how long</th><th>Finding</th></tr></thead><tbody>
<tr><td>%(richie)s</td><td>Regular oral glutathione, 250 or 1,000 mg a day</td><td>54 adults, 6 months</td><td>Body glutathione stores rose, more with the higher dose</td></tr>
<tr><td>%(lipo)s</td><td>Liposomal glutathione, 500 or 1,000 mg a day</td><td>12 adults, 1 month (pilot)</td><td>Glutathione stores and some immune markers rose</td></tr>
<tr><td>%(oral)s</td><td>Regular capsules, 500 mg a day</td><td>60 adults, 4 weeks</td><td>Melanin index fell slightly at the measured sites</td></tr></tbody></table></div>
<p>So: oral glutathione can raise body levels, and one small trial of regular capsules saw a modest change in melanin. Whether the liposomal form gives better skin results is not known.</p>
<h2>Is it safe?</h2><p>Short-term oral glutathione was generally well tolerated in these studies. Long-term safety at high doses is less clear, and supplements vary in quality. Ask a doctor first if you are pregnant or breastfeeding, take regular medicines, or have a medical condition. Never move from supplements to glutathione injections: they lack trials for skin lightening and carry safety warnings (%(ijdvl)s).</p>
<h2>Supplement or cream?</h2><div class="tbl"><table><thead><tr><th></th><th>Liposomal supplement</th><th>Glutathione cream</th></tr></thead><tbody>
<tr><td>Works on</td><td>Whole body levels</td><td>The skin you apply it to</td></tr>
<tr><td>Skin-tone evidence</td><td>None for the liposomal form</td><td>Small controlled studies</td></tr>
<tr><td>Doctor advice</td><td>Recommended</td><td>Not usually needed; patch test</td></tr></tbody></table></div>
<p>For a simple, low-risk start, a leave-on cream such as %(cream)s with daily sunscreen is the easier route. Compare all forms in <a href="/glutathione-cream-vs-tablets-vs-injections/">cream vs tablets vs injections</a>.</p>''',
         faq=[('Is liposomal glutathione better than regular glutathione tablets?', 'It is designed to be absorbed better, and a small pilot study showed it raised body levels. There is no head-to-head trial showing better skin results than regular tablets.'),
              ('Can I use liposomal glutathione and glutathione cream together?', 'A cream works on the skin surface and does not interact with a supplement. Ask a doctor before starting any supplement.')]),

    dict(slug='glutathione-skincare-glossary', title='Glutathione skincare glossary: 27 terms explained simply', short='Glossary',
         blurb='GSH, GSSG, melanin, tyrosinase, PIH, PA+++ and more: the words you see on glutathione products and guides, in plain English.',
         seo='Glutathione Skincare Glossary: GSH, Melanin, Tyrosinase & More', desc='Plain-English glossary of glutathione and skincare terms: GSH and GSSG, melanin, tyrosinase, melasma, PIH, niacinamide, retinol, SPF and PA ratings.',
         refs=['ijdvl'],
         body='<p>Short, plain definitions of the terms used across our guides and on glutathione product labels. Each term links to the full guide where there is one.</p><dl class="glossary">' + _gl_rows + '</dl>',
         faq=[]),
]
TLDR.update({
    'glutathione-for-melasma': ['Melasma is patchy, hormone- and light-driven pigmentation that needs a dermatologist.',
                                'Glutathione is not proven to treat melasma; at most it supports a gentle routine.',
                                'A tinted sunscreen that blocks visible light helped melasma more than UV-only sunscreen in a trial.'],
    'glutathione-for-pigmentation': ['Tan and acne marks respond best to a glutathione cream used with daily sunscreen.',
                                     'Melasma and changing spots need a dermatologist.',
                                     'Give it 8–12 weeks; avoid steroid "fairness" creams.'],
    'how-long-does-glutathione-take-to-work': ['Smoother skin in 2–4 weeks, fresher look in 4–8 weeks, lighter tan and marks in 8–12 weeks.',
                                               'Studies on glutathione ran for 4 to 12 weeks, with modest effects.',
                                               'No daily sunscreen is the most common reason for no results.'],
    'glutathione-for-dark-lips': ['There is no good study on glutathione for lips.',
                                  'Sun, smoking, lip licking and allergies are the usual causes: remove them first.',
                                  'Keep retinol and acid face creams off the lips; use an SPF lip balm.'],
    'reduced-vs-oxidized-glutathione': ['Reduced glutathione (GSH) is the active form; oxidised (GSSG) is two joined molecules the body recycles.',
                                        'GSSG is more stable in creams and was used in the best-known lotion study.',
                                        'Packaging, the full formula and sunscreen matter more than the form.'],
    'liposomal-glutathione': ['Liposomal glutathione is a supplement wrapped in fat bubbles to aid absorption.',
                              'Small studies show oral glutathione raises body levels; no trial tests liposomal glutathione for skin tone.',
                              'Ask a doctor before supplements; avoid injections.'],
})
RELATED_MORE = {
    'glutathione-for-melasma': ['glutathione-for-pigmentation', 'glutathione-in-pregnancy', 'glutathione-for-dark-spots-and-tan'],
    'glutathione-for-pigmentation': ['glutathione-for-melasma', 'glutathione-for-acne-marks', 'how-long-does-glutathione-take-to-work'],
    'how-long-does-glutathione-take-to-work': ['how-to-use-glutathione-cream', 'glutathione-for-pigmentation', 'glutathione-facts'],
    'glutathione-for-dark-lips': ['glutathione-for-underarms-and-body', 'glutathione-for-pigmentation', 'glutathione-side-effects'],
    'reduced-vs-oxidized-glutathione': ['glutathione', 'liposomal-glutathione', 'glutathione-facts'],
    'liposomal-glutathione': ['glutathione-tablets', 'glutathione-cream-vs-tablets-vs-injections', 'reduced-vs-oxidized-glutathione'],
    'glutathione-skincare-glossary': ['glutathione', 'glutathione-facts', 'reduced-vs-oxidized-glutathione'],
    'glutathione-for-dark-spots-and-tan': ['glutathione-for-pigmentation', 'glutathione-for-melasma', 'how-long-does-glutathione-take-to-work'],
    'glutathione-for-acne-marks': ['glutathione-for-pigmentation', 'how-long-does-glutathione-take-to-work', 'glutathione-for-oily-skin'],
    'glutathione-tablets': ['liposomal-glutathione', 'glutathione-cream-vs-tablets-vs-injections', 'glutathione-side-effects'],
    'glutathione-facts': ['how-long-does-glutathione-take-to-work', 'reduced-vs-oxidized-glutathione', 'glutathione-skincare-glossary'],
}

HI += [
    dict(slug='jhaiyan-aur-glutathione', en='/glutathione-for-melasma/',
         title='चेहरे की झाइयां (मेलास्मा) और ग्लूटाथियोन: क्या सच में मदद करता है?', short='झाइयां',
         seo='Chehre Ki Jhaiyan (Melasma) और Glutathione: सच क्या है',
         desc='झाइयां (मेलास्मा) और टैन में फर्क, ग्लूटाथियोन क्रीम झाइयों में कितनी मदद करती है, रंगीन सनस्क्रीन क्यों ज़रूरी है, और डॉक्टर कब दिखाएं।',
         body='''<p><b>छोटा जवाब:</b> ग्लूटाथियोन झाइयों का साबित इलाज नहीं है। भारतीय त्वचा-विशेषज्ञों की समीक्षा के अनुसार इसके सबूत कमज़ोर हैं। झाइयों में सबसे ज़्यादा मदद रोज़ की सनस्क्रीन और त्वचा-विशेषज्ञ के इलाज से मिलती है।</p>
<h2>झाइयां या टैन?</h2><div class="tbl"><table><thead><tr><th></th><th>टैन</th><th>झाइयां (मेलास्मा)</th></tr></thead><tbody>
<tr><td>कैसी दिखती है</td><td>धूप वाली त्वचा एक-सी गहरी</td><td>दोनों गालों, माथे, नाक या ऊपरी होंठ पर भूरे-स्लेटी धब्बे</td></tr>
<tr><td>कारण</td><td>धूप</td><td>धूप और रोशनी, हार्मोन (गर्भावस्था, गोलियां), आनुवंशिकता, गर्मी</td></tr>
<tr><td>अपने आप जाती है?</td><td>हां, सनस्क्रीन के साथ कुछ हफ्तों में</td><td>कम ही; अक्सर लौट आती है</td></tr></tbody></table></div>
<h2>रंगीन (टिंटेड) सनस्क्रीन क्यों</h2><p>झाइयां सिर्फ UV से नहीं, दिखने वाली रोशनी से भी गहरी होती हैं। एक ट्रायल में आयरन ऑक्साइड वाली (रंगीन) सनस्क्रीन लगाने वालों में झाइयां सामान्य सनस्क्रीन से ज़्यादा कम हुईं। रोज़ सुबह SPF 30+ रंगीन सनस्क्रीन लगाएं और बाहर हर 2–3 घंटे में दोबारा लगाएं।</p>
<h2>किन चीज़ों से बचें</h2><ul><li>स्टेरॉयड वाली या बिना लेबल की "फेयरनेस" क्रीम।</li><li>नींबू, बेकिंग सोडा या ब्लीच।</li><li>ग्लूटाथियोन इंजेक्शन।</li></ul>
<h2>ग्लूटाथियोन क्रीम कहां फिट होती है</h2><p>डॉक्टर सहमत हों तो ग्लूटाथियोन और नियासिनामाइड वाली क्रीम रात के हल्के रूटीन का हिस्सा हो सकती है। GlutaNex नाइट क्रीम में रेटिनॉल है, इसलिए गर्भावस्था में या डॉक्टर की क्रीम के साथ इस्तेमाल से पहले पूछें।</p>''',
         faq=[('क्या झाइयां हमेशा के लिए ठीक हो सकती हैं?', 'झाइयां हल्की और नियंत्रित हो सकती हैं, लेकिन धूप, गर्मी या हार्मोन बदलने पर अक्सर लौट आती हैं। रोज़ की सनस्क्रीन सबसे ज़रूरी है।'),
              ('क्या ग्लूटाथियोन से झाइयां जाती हैं?', 'इसके पक्के सबूत नहीं हैं। यह रूटीन का हिस्सा हो सकती है, लेकिन असली फर्क सनस्क्रीन और त्वचा-विशेषज्ञ के इलाज से आता है।')]),
]
TLDR_HI['jhaiyan-aur-glutathione'] = ['ग्लूटाथियोन झाइयों का साबित इलाज नहीं है।',
                                      'रोज़ SPF 30+ रंगीन सनस्क्रीन झाइयों में सबसे ज़्यादा मदद करती है।',
                                      'झाइयां हों तो त्वचा-विशेषज्ञ को दिखाएं; स्टेरॉयड क्रीम से बचें।']
