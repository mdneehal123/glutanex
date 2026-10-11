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
    desc='Glutathione explained: what it is, how it works in the body and skin, benefits, cream vs tablets vs injections, side effects, foods, and what the research really shows.',
    refs=['study', 'oral', 'wesch', 'ijdvl', 'review', 'fda'],
    body='''<p><b>Glutathione</b> is a small antioxidant molecule that your body makes every day, mostly in the liver. It is often called the body's "master antioxidant" because it helps protect cells from damage and recycles other antioxidants such as vitamin C and vitamin E. In skincare, glutathione is used in creams, serums and face washes made for <b>brighter-looking, more even skin</b>.</p>
<p>This guide covers everything in one place: what glutathione is, how it affects skin, the different forms you can buy, what the research shows, and how to use it safely.</p>

<h2>What is glutathione?</h2>
<p>Glutathione (often written GSH) is a <b>tripeptide</b>, a chain of three amino acids:</p>
<ul><li><b>Glutamic acid</b> (glutamate)</li><li><b>Cysteine</b>, which carries the sulphur group that makes glutathione such an effective antioxidant</li><li><b>Glycine</b></li></ul>
<p>It exists in two forms. <b>Reduced glutathione (GSH)</b> is the active form that neutralises free radicals. When it does that job it becomes <b>oxidised glutathione (GSSG)</b>, which the body then converts back. Skincare products may use either form.</p>
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
<p>A 2025 systematic review of topical glutathione (%(review)s) concluded that it "shows promise", but that studies are few, small and short, and that more and larger trials are needed. The Indian review (%(ijdvl)s) reached a similar view: the evidence is encouraging for creams and tablets in the short term, but not strong enough to call glutathione a treatment for pigmentation disorders such as melasma.</p>
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
<ul><li>Pregnant or breastfeeding women, especially with products that also contain retinol.</li><li>People with eczema, rosacea or very sensitive skin.</li><li>Anyone with patchy pigmentation that may be melasma, or spots that change shape or colour: see a dermatologist first.</li></ul>''',
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
         desc='Glutathione cream price in India explained: what drives the price, how to compare value per gram, red flags with very cheap creams, and GlutaNex prices with free shipping.',
         refs=['ijdvl', 'review'],
         body='''<p>Glutathione creams in India range from a few hundred rupees to several thousand. The price depends less on the word "glutathione" on the label and more on <b>what else is in the formula, how much you get, and who stands behind it</b>.</p>
<h2>GlutaNex prices</h2>
<div class="tbl"><table><thead><tr><th>Product</th><th>Price</th><th>MRP</th><th>Shipping</th></tr></thead><tbody>
<tr><td>%(cream)s</td><td>%(pcream)s</td><td>%(mcream)s</td><td>Free</td></tr>
<tr><td>%(wash)s</td><td>%(pwash)s</td><td>%(mwash)s</td><td>Free</td></tr>
<tr><td><a href="%(uduo)s">Glow Duo (cream + face wash)</a></td><td>%(pduo)s</td><td>%(mduo)s</td><td>Free</td></tr>
</tbody></table></div>
<p>Prices include taxes. Cash on Delivery is available with a small refundable advance.</p>
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
    seo='Glutathione Cream Questions Answered: Does It Work, Daily Use, Best One',
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
