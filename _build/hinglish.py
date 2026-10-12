# Hinglish pages: Hindi written in English letters, the way most Indians actually type their searches
# ("glutathione cream ke fayde", "glutathione kaise lagaye"). Read by content.py with exec().
# Each page maps to an English page ('en') so hreflang can join en-IN, hi-IN (Devanagari) and hi-Latn (Hinglish).
# Bodies are formatted with P, so a literal percent sign must be written as two percent signs.
HL = [
    dict(slug='glutathione-kya-hai', en='/glutathione/', short='Glutathione kya hai',
         title='Glutathione kya hai? Skin ke liye poori jaankari',
         seo='Glutathione Kya Hai? Fayde, Kaam Aur Sahi Use (Hinglish Guide)',
         desc='Glutathione kya hai, body aur skin mein kya karta hai, cream, tablet aur injection mein kya farak hai, aur safe tarike se kaise use karein. Aasan Hinglish mein.',
         qa=[('Glutathione kya hai?', 'Glutathione ek antioxidant hai jo hamara body khud banata hai, zyada tar liver mein. Yeh teen amino acids se banta hai aur cells ko damage se bachata hai. Skincare mein iska use skin ko brighter aur even-looking dikhane ke liye hota hai.', ''),
             ('Glutathione skin par kaise kaam karta hai?', 'Glutathione melanin banane wale enzyme (tyrosinase) ko dheema karta hai aur dark melanin ki jagah halka melanin banne mein madad karta hai. Isliye regular use aur daily sunscreen ke saath tan aur uneven tone 8 se 12 hafte mein halka dikh sakta hai.', '')],
         body='''<h2>Glutathione kis cheez se banta hai?</h2><p>Teen amino acids se: glutamic acid, cysteine aur glycine. Umar, stress, smoking, sharab aur tez dhoop se body mein iska level kam ho sakta hai.</p>
<h2>Cream, tablet aur injection mein farak</h2><div class="tbl"><table><thead><tr><th></th><th>Cream</th><th>Tablet</th><th>Injection</th></tr></thead><tbody>
<tr><td>Kaise</td><td>Skin par lagate hain</td><td>Muh se lete hain</td><td>Nas mein</td></tr>
<tr><td>Asar</td><td>Dheere, halka</td><td>Mixed evidence</td><td>Skin ke liye trial nahi</td></tr>
<tr><td>Safety</td><td>Aam taur par safe, pehle patch test</td><td>Doctor se poochein</td><td>Regulators ki warning, avoid karein</td></tr></tbody></table></div>
<h2>Kya glutathione se rang badalta hai?</h2><p>Nahi. Yeh tan aur dark patches ko halka dikhane mein madad kar sakta hai, lekin aapka natural skin colour nahi badalta. "Permanent gora" jaise claims sach nahi hain.</p>
<h2>Safe use ka tarika</h2><p>Raat ko halke face wash ke baad glutathione cream, aur subah SPF 30+ sunscreen. Kam se kam 8 se 12 hafte regular use karein. Pregnancy mein doctor se poochein.</p>''',
         faq=[('Glutathione ko Hindi mein kya kehte hain?', 'Iska koi alag Hindi naam nahi hai; Hindi mein bhi ise glutathione (ग्लूटाथियोन) hi kehte hain. Yeh body ka ek natural antioxidant hai.'),
              ('Glutathione kis cheez mein milta hai?', 'Palak, avocado, bhindi aur asparagus mein thoda glutathione hota hai. Lahsun, pyaaz, broccoli, ande aur dal iske building blocks dete hain.')]),
    dict(slug='glutathione-cream-ke-fayde', en='/glutathione-benefits-for-skin/', short='Glutathione cream ke fayde',
         title='Glutathione cream ke fayde: sach kya hai?',
         seo='Glutathione Cream Ke Fayde: Skin Ke Liye Asli Benefits (Hinglish)',
         desc='Glutathione cream ke fayde aasan Hinglish mein: tan, dark spots aur dull skin par kya asar hota hai, kitne din mein result dikhta hai aur kya nahi hota.',
         qa=[('Glutathione cream ke kya fayde hain?', 'Glutathione cream skin ko antioxidant protection deti hai aur regular use se tan, dull skin aur uneven tone ko halka aur even dikhane mein madad karti hai. Best result daily sunscreen ke saath 8 se 12 hafte mein dikhta hai. Yeh natural rang nahi badalti.', ''),
             ('Glutathione cream kitne din mein asar karti hai?', 'Zyada tar logon ko 4 se 8 hafte mein skin thodi fresh aur bright dikhti hai, aur tan 8 se 12 hafte mein halka hota hai. Iske liye roz raat ko use aur subah sunscreen zaroori hai. Results har insaan mein alag hote hain.', '')],
         body='''<h2>Kin problems mein madad milti hai?</h2><ul><li><b>Sun tan:</b> dhoop se hua tan dheere dheere halka dikh sakta hai.</li><li><b>Dull skin:</b> skin zyada fresh aur glowing dikhti hai.</li><li><b>Uneven tone aur dark patches:</b> rang zyada ek jaisa dikh sakta hai.</li><li><b>Antioxidant protection:</b> dhoop aur pollution se hone wale damage se bachav.</li></ul>
<h2>Studies kya kehti hain?</h2><p>Chhoti studies mein 4 se 12 hafte mein skin melanin mein thodi, dheere dheere kami dekhi gayi. Matlab asar hota hai, lekin modest aur gradual.</p>
<h2>Saath mein kaunse ingredients achhe hain?</h2><p>Niacinamide, vitamin C aur hyaluronic acid glutathione ke saath achha kaam karte hain. %(cream)s mein yeh sab hain, saath mein retinol, ceramides aur peptides bhi.</p>
<h2>Kya nahi hota?</h2><p>Glutathione cream aapka natural skin colour nahi badalti, aur sunscreen ke bina result tik nahi paata. 7 din mein gora karne wale claims se bachein.</p>''',
         faq=[('Kya glutathione cream roz laga sakte hain?', 'Haan, zyada tar log roz raat ko laga sakte hain. Retinol wali cream ho to pehle 2 hafte, hafte mein 2 se 3 raat se shuru karein.'),
              ('Kya glutathione cream oily skin par chalegi?', 'Haan, halki aur non-greasy cream patli layer mein lagayein. Niacinamide ya salicylic acid wali cream oily skin ke liye achhi rehti hai.')]),
    dict(slug='glutathione-ke-nuksan', en='/glutathione-side-effects/', short='Glutathione ke nuksan',
         title='Glutathione ke nuksan aur side effects: kya normal hai?',
         seo='Glutathione Ke Nuksan: Side Effects Aur Safety (Hinglish Guide)',
         desc='Glutathione ke nuksan aur side effects Hinglish mein: cream, tablet aur injection ke risk, kaun si problem normal hai aur kab doctor ko dikhana chahiye.',
         qa=[('Glutathione ke kya nuksan hain?', 'Glutathione cream aam taur par safe hai; shuru mein halki chubhan, redness ya dryness ho sakti hai. Tablets se kabhi kabhi pet mein gas ya ulti jaisa lag sakta hai. Sabse zyada risk injections mein hai, jinke liye skin lightening mein koi proper trial nahi hai.', ''),
             ('Kya glutathione cream safe hai?', 'Zyada tar adults ke liye haan. Pehle 24 ghante kaan ke peeche ya andar ki baanh par patch test karein. Retinol wali cream pregnancy aur breastfeeding mein na lagayein, aur jalan ya sujan ho to use band karein.', '')],
         body='''<h2>Cream ke side effects</h2><ul><li>Shuru mein halki chubhan ya garmi lagna</li><li>Thodi redness ya dryness, khaaskar retinol wali cream se</li><li>Bahut kam case mein allergy: khujli, rash</li></ul><p>Halki problem ho to cream ek din chhod kar lagayein aur moisturiser use karein.</p>
<h2>Tablets ke side effects</h2><p>Short studies mein tablets zyada tar theek rahe, kuch logon ko pet mein gas ya bloating hui. Lambe time ka use achhe se study nahi hua, isliye doctor se poochkar hi lein.</p>
<h2>Injections: sabse zyada risk</h2><p>Skin gori karne ke liye glutathione injections ka koi proper clinical trial nahi hai, aur regulators ne warning di hai (%(fda)s). Bina license wali jagah drip se infection ka bhi risk hai. Inse bachein.</p>
<h2>Kab turant doctor ke paas jaayein?</h2><p>Saans lene mein dikkat, chehre ya hothon par sujan, ya tezi se failta rash ho to turant medical madad lein.</p>''',
         faq=[('Kya glutathione se kidney kharab hoti hai?', 'Cream se aisa koi saboot nahi hai. Injections ke saath kuch serious reports aaye hain, isliye injections avoid karein aur tablets doctor ki salah se hi lein.'),
              ('Glutathione cream se pimples ho sakte hain?', 'Bhaari formula se kuch logon ko ho sakte hain. Halki, non-greasy cream patli layer mein lagayein; salicylic acid pores saaf rakhne mein madad karta hai.')]),
    dict(slug='glutathione-cream-kaise-lagaye', en='/how-to-use-glutathione-cream/', short='Glutathione cream kaise lagaye',
         title='Glutathione cream kaise lagaye: sahi tarika step by step',
         seo='Glutathione Cream Kaise Lagaye: Raat Ka Sahi Tarika (Hinglish)',
         desc='Glutathione cream kaise lagaye, kitni lagayein, din mein ya raat mein, aur kitne din mein result dikhega: step-by-step Hinglish guide.',
         qa=[('Glutathione cream kaise lagaye?', 'Raat ko chehra halke face wash se dhoyein aur pochh kar sukha lein. Phir matar ke daane jitni cream maathe, gaalon, thodi aur gardan par lagakar halke haathon se upar ki taraf failayein. Subah SPF 30+ sunscreen zaroor lagayein.', ''),
             ('Glutathione cream din mein lagayein ya raat mein?', 'Raat mein lagana best hai, khaaskar agar cream mein retinol ya salicylic acid ho, kyunki yeh dhoop mein skin ko sensitive kar sakte hain. Din mein sirf sunscreen aur moisturiser rakhein.', '')],
         body='''<h2>Step by step</h2><ol><li><b>Saaf karein:</b> %(wash)s jaise halke face wash se chehra dhoyein.</li><li><b>Sukha lein:</b> towel se halke se pochhein, ek minute rukein.</li><li><b>Matar ke daane jitni cream:</b> chehre aur gardan ke liye kaafi hai.</li><li><b>Patli layer:</b> upar ki taraf halke haath se failayein; aankhon aur hothon ke paas na lagayein.</li><li><b>Subah sunscreen:</b> SPF 30 ya zyada, dhoop mein ho to 2 se 3 ghante mein dobara.</li></ol>
<h2>Shuruat dheere karein</h2><p>Retinol wali cream ho to pehle 2 hafte, hafte mein 2 se 3 raat. Skin theek lage to ek din chhod kar, aur phir roz raat.</p>
<h2>Kitne din mein result?</h2><p>Fresh look 4 se 8 hafte mein, aur tan halka hone mein 8 se 12 hafte. Beech mein band na karein.</p>
<h2>Kya na karein</h2><p>Ek saath kai nayi strong creams na lagayein, scrub zyada na karein, aur nimbu ya baking soda chehre par na lagayein.</p>''',
         faq=[('Glutathione cream kitni lagani chahiye?', 'Poore chehre aur gardan ke liye matar ke daane jitni cream kaafi hai. Zyada lagane se jaldi result nahi aata.'),
              ('Kya glutathione cream ke baad moisturiser laga sakte hain?', 'Haan. Pehle glutathione cream, ek minute rukein, phir moisturiser. Sardi mein ya dry skin par yeh madad karta hai.')]),
    dict(slug='glutathione-tablet-ke-fayde-aur-nuksan', en='/glutathione-tablets/', short='Glutathione tablet',
         title='Glutathione tablet ke fayde aur nuksan: kya kaam karti hai?',
         seo='Glutathione Tablet Ke Fayde Aur Nuksan: Dose, Safety (Hinglish)',
         desc='Glutathione tablet ke fayde aur nuksan Hinglish mein: studies mein kitni dose li gayi, skin par kitna asar hua, side effects, aur kise nahi leni chahiye.',
         qa=[('Glutathione tablet ke kya fayde hain?', 'Studies mein 250 se 500 mg roz, 4 se 12 hafte tak lene par skin tone mein thoda, modest badlaav dekha gaya. Koi bhi tablet skin ko permanently gora nahi karti, aur 1000 mg zyada asardaar hone ka saboot nahi hai. Lene se pehle doctor se poochein.', ''),
             ('Glutathione tablet ke nuksan kya hain?', 'Short studies mein tablets zyada tar theek rahe; kuch logon ko gas, bloating ya pet mein dikkat hui. Lambe samay ka use achhe se study nahi hua. Pregnancy, breastfeeding, asthma ya koi dawa chal rahi ho to doctor ki salah zaroori hai.', '')],
         body='''<h2>Tablet ya cream?</h2><p>Tablet poore body mein jaati hai aur iske saboot mixed hain. Cream seedhe skin par kaam karti hai aur kam risk wali hai. Bahut se log pehle cream aur sunscreen se shuru karte hain.</p>
<h2>Kise tablet nahi leni chahiye?</h2><ul><li>Pregnant ya breastfeeding mahilayein</li><li>Asthma ke mareez (doctor se poochein)</li><li>Jo log pehle se koi dawa le rahe hain</li></ul>
<h2>Fake products se bachein</h2><p>Bina label ya bahut sasti "whitening" tablets mein kya hai, pata nahi hota. Sirf bharosemand brand aur doctor ki salah se lein.</p>''',
         faq=[('Glutathione tablet kitne din leni chahiye?', 'Studies mein 4 se 12 hafte tak li gayi. Isse lamba use doctor ki salah se hi karein.'),
              ('Kya glutathione tablet aur cream saath le sakte hain?', 'Cream ke saath tablet lena zaroori nahi hai. Tablet lena ho to pehle doctor se baat karein.')]),
    dict(slug='kya-glutathione-se-gora-hota-hai', en='/glutathione-for-skin-whitening/', short='Kya glutathione se gora hota hai',
         title='Kya glutathione se gora hota hai? Seedha jawab',
         seo='Kya Glutathione Se Gora Hota Hai? Sach Aur Myths (Hinglish)',
         desc='Kya glutathione se gora hota hai? Seedha aur sach jawab: tan aur dark spots par kya asar hota hai, natural rang par kya nahi, aur kin claims se bachein.',
         qa=[('Kya glutathione se gora hota hai?', 'Nahi, glutathione aapka natural skin colour nahi badalta. Yeh dhoop ke tan, dark patches aur uneven tone ko dheere dheere halka aur ek jaisa dikhane mein madad kar sakta hai, woh bhi daily sunscreen ke saath 8 se 12 hafte mein.', ''),
             ('Kya glutathione injection se permanent gora ho sakte hain?', 'Nahi. Permanent gora karne wala koi bhi injection, tablet ya cream proven nahi hai. Glutathione injections ka skin lightening ke liye koi proper trial nahi hai aur regulators ne inke baare mein warning di hai.', '')],
         body='''<h2>Phir tan halka kaise hota hai?</h2><p>Tan dhoop se bana extra melanin hai. Glutathione naye melanin ko dheema kar sakta hai, aur sunscreen naya tan banne se rokti hai. Dono saath mein tan ko dheere dheere halka dikhate hain.</p>
<h2>In claims se savdhaan</h2><ul><li>"7 din mein gora": aisi creams mein steroid ya mercury ho sakta hai.</li><li>"Permanent whitening": sunscreen chhodte hi tan wapas aata hai.</li><li>Bina label ki "fairness" cream: skin ko lambe samay tak nuksan ho sakta hai.</li></ul>
<h2>Sahi umeed kya rakhein?</h2><p>Fresh, even aur healthy dikhne wali skin. Har skin tone sundar hai; glutathione ka kaam rang badalna nahi, skin ko behtar dikhana hai.</p>''',
         faq=[('Gora hone ke liye sabse safe tarika kya hai?', 'Natural rang badalna safe ya zaroori nahi hai. Tan aur dark spots ke liye daily sunscreen, halki glutathione ya niacinamide cream aur dheeraj sabse safe tarika hai.'),
              ('Kya glutathione cream black skin ko white kar sakti hai?', 'Nahi. Yeh natural rang nahi badalti; sirf tan aur uneven tone ko halka dikhane mein madad kar sakti hai.')]),
    dict(slug='glutathione-injection-safe-hai-kya', en='/glutathione-cream-vs-tablets-vs-injections/', short='Glutathione injection',
         title='Glutathione injection safe hai kya? Cream, tablet aur injection ka farak',
         seo='Glutathione Injection Safe Hai Kya? Risk Aur Behtar Option',
         desc='Glutathione injection safe hai kya? Skin lightening ke liye injections ke risk, regulators ki warning, aur cream ya tablet se kya farak hai: Hinglish mein.',
         qa=[('Glutathione injection safe hai kya?', 'Skin gori karne ke liye glutathione injections ko safe ya asardaar saabit karne wala koi proper clinical trial nahi hai, aur health regulators ne inke baare mein warning di hai. Bina license wali jagah drip se infection ka risk bhi hai. Inse bachna behtar hai.', ''),
             ('Glutathione cream, tablet aur injection mein kya behtar hai?', 'Zyada tar logon ke liye raat ko glutathione cream aur subah sunscreen sabse kam risk wala option hai. Tablets doctor ki salah se hi lein. Skin lightening ke liye injections ki salah nahi di jaati.', '')],
         body='''<h2>Injections ke risk</h2><ul><li>Skin lightening ke liye koi proper trial nahi</li><li>Allergic reaction aur serious side effects ki reports</li><li>Ganda needle ya bina license wala clinic: infection ka risk</li><li>Bottle par kya likha hai aur andar kya hai, pata nahi hota</li></ul><p>Warning padhein: %(fda)s.</p>
<h2>Teeno ka farak</h2><div class="tbl"><table><thead><tr><th></th><th>Cream</th><th>Tablet</th><th>Injection</th></tr></thead><tbody>
<tr><td>Risk</td><td>Kam</td><td>Medium, doctor se poochein</td><td>Zyada</td></tr>
<tr><td>Result</td><td>Dheere, modest</td><td>Modest, mixed</td><td>Skin ke liye proven nahi</td></tr>
<tr><td>Kharcha</td><td>Kam</td><td>Medium</td><td>Bahut zyada</td></tr></tbody></table></div>
<h2>Shaadi se pehle injection?</h2><p>Shaadi se pehle "glow drip" packages bahut bechte hain. Behtar hai 10 se 12 hafte pehle cream aur sunscreen se shuru karein.</p>''',
         faq=[('Glutathione injection ka asar kitne din rehta hai?', 'Koi proven asar nahi hai, aur jo bhi farak dikhe woh dhoop mein wapas aa jaata hai. Isliye injections ki salah nahi di jaati.'),
              ('Kya doctor glutathione injection dete hain?', 'Kuch clinics dete hain, lekin skin lightening ke liye iska koi approved use nahi hai. Kisi bhi injection se pehle dermatologist se risk samjhein.')]),
    dict(slug='glutathione-cream-price-aur-best-kaise-chune', en='/glutathione-cream-price-in-india/', short='Glutathione cream price',
         title='Glutathione cream price India mein, aur best cream kaise chunein',
         seo='Glutathione Cream Price Aur Best Cream Kaise Chunein',
         desc='Glutathione cream ka price India mein kitna hai, sasti aur mehngi cream mein kya farak hai, aur best glutathione cream kaise chunein: aasan checklist Hinglish mein.',
         qa=[('Glutathione cream ka price kitna hai?', 'India mein glutathione creams kuch sau se lekar kai hazaar rupaye tak milti hain. Sirf price na dekhein: price per gram aur poora ingredient list dekhein. %(cream)s 30 g ki hai, aur iska price %(pcream)s hai, free shipping aur COD ke saath.', ''),
             ('Best glutathione cream kaise chunein?', 'Aisi cream chunein jismein glutathione saaf likha ho, saath mein niacinamide ya vitamin C jaise ingredients hon, poora ingredient list, batch aur expiry ho, claims sach hon aur seller se contact ho sake. "7 din mein gora" jaise claims wali cream se bachein.', '')],
         body='''<h2>Checklist</h2><ul><li>Glutathione ingredient list mein saaf likha ho</li><li>Partner ingredients: niacinamide, vitamin C, hyaluronic acid</li><li>Batch number, expiry aur manufacturer ka naam</li><li>Sach claims: "dheere dheere", "sunscreen ke saath"</li><li>Seller ka phone ya WhatsApp</li></ul>
<h2>Bahut sasti cream se savdhaan</h2><p>Bina label ya bahut sasti "fairness" creams mein steroid, hydroquinone ya mercury ho sakta hai, jo skin ko patla aur damaged kar sakte hain.</p>
<h2>Ek jar kitne din chalta hai?</h2><p>Roz raat matar ke daane jitni lagane par 30 g jar lagbhag 6 se 8 hafte chalta hai.</p>''',
         faq=[('Glutathione cream kahan se khareedein?', 'Brand ki official website ya official marketplace listing se. GlutaNex %(cream)s glutanex.co.in par free shipping aur Cash on Delivery ke saath milti hai.'),
              ('Kya mehngi glutathione cream zyada achhi hoti hai?', 'Zaroori nahi. Ingredient list, sach claims aur seller ka bharosa price se zyada important hain.')]),
]

HL_UI = dict(hub='Hinglish guides', toc='Is page par', faq='Aksar pooche jaane wale sawal', src='Sources', buy='Abhi kharidein', more='Aur padhein',
             note='Yeh general cosmetic skincare jaankari hai, medical salah nahi. Koi skin problem ho to dermatologist se milein.',
             by='GlutaNex team · Updated: 12 Oct 2026')
EN2HL = {h['en']: '/hinglish/%s/' % h['slug'] for h in HL}

# Key takeaways for Hinglish pages (shown at the top, also read aloud by voice assistants via speakable)
TLDR_HL = {
    'glutathione-kya-hai': ['Glutathione ek antioxidant hai jo body khud banati hai; yeh cells ko damage se bachata hai.',
                            'Skincare mein yeh tan aur uneven tone ko 8–12 hafte mein halka aur even dikhane mein madad kar sakta hai.',
                            'Yeh natural rang nahi badalta; cream kam risk wali hai, injections se bachein.'],
    'glutathione-cream-ke-fayde': ['Fayde: antioxidant protection aur dheere dheere brighter, even-looking skin.',
                                   'Fresh look 4–8 hafte mein, tan halka hone mein 8–12 hafte, roz sunscreen ke saath.',
                                   'Natural rang nahi badalta; "7 din mein gora" claims sach nahi hain.'],
    'glutathione-ke-nuksan': ['Cream aam taur par safe hai; shuru mein halki chubhan, redness ya dryness ho sakti hai.',
                              'Pehle 24 ghante patch test karein; sujan ya rash ho to turant band karein.',
                              'Sabse zyada risk injections mein hai; skin lightening ke liye inse bachein.'],
    'glutathione-cream-kaise-lagaye': ['Raat ko chehra dhoyein, sukhayein, phir matar ke daane jitni cream lagayein.',
                                       'Retinol wali cream: pehle 2 hafte, hafte mein 2–3 raat.',
                                       'Subah SPF 30+ sunscreen zaroor; result 8–12 hafte mein.'],
    'glutathione-tablet-ke-fayde-aur-nuksan': ['Studies mein 250–500 mg roz, 4–12 hafte se thoda, modest badlaav dikha.',
                                               'Short-term mein zyada tar theek; lambe use ki jaankari kam hai.',
                                               'Tablet lene se pehle doctor se poochein; 1000 mg behtar hone ka saboot nahi.'],
    'kya-glutathione-se-gora-hota-hai': ['Nahi, glutathione natural skin colour nahi badalta.',
                                         'Yeh tan aur dark patches ko dheere dheere halka dikha sakta hai, sunscreen ke saath.',
                                         'Permanent gora karne wala koi injection, tablet ya cream proven nahi hai.'],
    'glutathione-injection-safe-hai-kya': ['Skin lightening ke liye glutathione injection ka koi proper trial nahi hai.',
                                           'Regulators ne warning di hai; bina license wali drip se infection ka risk bhi hai.',
                                           'Raat ko cream aur subah sunscreen sabse kam risk wala option hai.'],
    'glutathione-cream-price-aur-best-kaise-chune': ['India mein glutathione cream kuch sau se kai hazaar rupaye tak milti hai.',
                                                     'Price per gram, poora ingredient list aur sach claims dekhein.',
                                                     'Bahut sasti, bina label wali "fairness" cream se bachein.'],
}
