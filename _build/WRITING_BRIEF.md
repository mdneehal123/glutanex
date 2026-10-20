# Writing brief: GlutaNex (glutanex.co.in) guides

Used by people and by the daily SEO agent. Keep it up to date when products or prices change.

Static site built by `python3 _build/build.py` from the repository root. Existing pages: every <loc> in sitemap.xml (link only to those, or to pages you add in the same build).

## Read first (to match voice, format and facts exactly)
- _build/content_more.py: NEW_GUIDES entries (e.g. glutathione-for-dark-lips, glutathione-cream-in-winter, glutathione-before-wedding) and the REFS / SOURCES dicts at the top.
- _build/build.py lines 20–45 (PRODUCTS), 300–330 (HOME_FAQ, INGREDIENTS), 471–475 (CREAM_FAQ, PDP_FAQ).
- _build/content.py lines 85–118 (how guides are processed: placeholders P, 'qa' list → H2 + short answer + FAQ schema, 'faq' list, 'refs').
- For Hindi/Hinglish: the HI list in content_more.py and HL in _build/hinglish.py.

## Product facts (only these)
- GlutaNex Glutathione Night Cream, 30 g jar, ₹2,499 (MRP ₹3,000). Ingredients: glutathione, niacinamide (vitamin B3), hyaluronic acid, vitamin C, retinol (vitamin A), ceramides, salicylic acid (BHA), peptides, aloe vera, turmeric (haldi) and neem extracts. NIGHT USE ONLY (retinol + salicylic acid): start 2–3 nights a week, sunscreen every morning, not in pregnancy/breastfeeding unless a doctor says it is fine, not on lips or broken/freshly waxed skin. Percentages are NOT published: never state them.
- GlutaNex Gluta Boost Face Wash, 100 ml pump, ₹399 (MRP ₹599): gentle daily face wash. Do not invent its ingredients beyond "glutathione face wash".
- Glow Duo (Night Cream + Face Wash) ₹2,699 (MRP ₹3,599), ₹199 less than buying both.
- Free shipping, Cash on Delivery (no COD fee), pay online with Razorpay, or order on WhatsApp. Also sold on Amazon and Flipkart (links in MARKET_LINKS in build.py). Brand: Indian, Bhatkal, Karnataka.
- Placeholders available in bodies: %(cream)s (Night Cream link), %(wash)s (Face Wash link), %(uduo)s (Duo URL), %(pcream)s %(mcream)s %(pwash)s %(mwash)s %(pduo)s %(mduo)s (prices), refs %(study)s %(oral)s %(wesch)s %(ijdvl)s %(review)s %(fda)s. A literal percent sign MUST be written %%.

## Honesty rules (strict)
- Cosmetic wording only: brighter-looking, more even-looking, helps tan/dark marks look lighter over weeks.
- NEVER promise or imply: whitening, fairness, gora, permanent, cure/treat, guaranteed, results in X days, "No. 1", clinically proven, dermatologist recommended. You may discuss those search phrases only to correct them (as existing pages do).
- Never change natural skin colour claims. No invented studies, numbers, reviews, customers, before/after photos or doctors. Only cite the REFS that exist, and only for what they actually say (read SOURCES and existing pages' wording).
- Medical topics (melasma, PCOS/acanthosis, pregnancy, injections, tablets dosing): send to a dermatologist/doctor; no dosing advice.
- No competitor brand names.
- Mention GlutaNex products 1–3 times where they truly fit, not salesy. Always respect that the Night Cream is night-only and has retinol + salicylic acid.

## Format of each English guide (Python dict, same keys as NEW_GUIDES)
dict(slug=..., title=..., short=..., blurb=..., seo='≤ 60 chars, no brand suffix', desc='140–158 chars meta description with the keyword',
     refs=[...only those used...],
     qa=[('Exact Google question?', 'Direct 1–3 sentence answer (40–60 words) that can stand alone.', ''), ... 2–4 items],
     body='''HTML: 5–8 <h2> sections with real substance, at least one <div class="tbl"><table>…</table></div> or <ol> steps, 4+ internal links to existing pages (exact paths), 900–1,300 words''',
     faq=[('Question?', 'Answer.'), ... 3–5 items])
Quality bar: answer the searcher's real question immediately, specific and practical for Indian skin, weather and budgets; no filler intros; no repetition of existing pages (link to them instead). Write in the same calm, honest, evidence-aware voice as existing GlutaNex guides.

## Output
New English guides go in a new file _build/new_<YYYYMMDD>.py defining one UPPERCASE list of guide dicts; add the file name to the list in the `for _f in [...]` loop in _build/content.py and add the list to the `NEW_GUIDES +=` line (Hindi dicts: `HI +=`, Hinglish: `HL +=`). Write valid Python. Validate it with:
python3 -c "
import sys; sys.path.insert(0,'_build')
ns={}; exec(open('<yourfile>').read(), ns)
P={k:'X' for k in ['cream','wash','uduo','pcream','mcream','pwash','mwash','pduo','mduo','study','oral','wesch','ijdvl','review','fda','owner','name','lipo','richie','vislight']}
L=[v for k,v in ns.items() if k.isupper() and isinstance(v,list)][0]
for g in L:
  (g['body'] % P); [a % P for q,a,*r in g.get('qa',[])]
  print(g['slug'], len(g['seo']), len(g['desc']), len(g['body'].split()))
"
Then grep your file for: whiten|fair|gora|permanent|cure|treat|guarantee|No\. 1|clinically|dermatologist recommended — every hit must be a correction/negation, not a promise. Reply with only the list of slugs written.
