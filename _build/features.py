# Feature pages: skin quiz, wholesale, unboxing reward, routine streak. Read by build.py with exec().
SVG_CHECK = ''

# ---------------- Skin quiz ----------------
page('/skin-quiz/', 'Glutathione Skin Quiz: Find Your Routine in 30 Seconds | GlutaNex',
     'Answer 5 quick questions about your skin and get an honest glutathione routine: which product, how often, and what to avoid. Free, no sign-up.',
     top('Skin quiz', 'Find your routine in <span class="gold">30 seconds</span>', 'Five taps. An honest answer, even if that answer is "not for you right now".') +
     '<section style="padding-top:18px"><div class="wrap"><div id="quiz" class="quiz"><noscript>Please turn on JavaScript to use the quiz.</noscript></div>'
     '<p class="muted" style="font-size:.84rem;margin-top:16px;max-width:60ch">This quiz gives general cosmetic skincare guidance, not medical advice. Your answers stay on your phone. '
     'For a skin condition, see a dermatologist.</p></div></section>',
     js='store.js,quiz.js', crumbs=[('Skin quiz', '/skin-quiz/')])

# ---------------- Wholesale / resellers ----------------
_WS_FAQ = [('Do you sell glutathione cream wholesale?', 'Yes. Beauty parlours, salons, cosmetic shops and online sellers can order GlutaNex Glutathione Night Cream and Gluta Boost Face Wash in bulk. Send the form and we reply with wholesale prices on WhatsApp.'),
           ('What is the minimum wholesale order?', 'The minimum order is 6 jars or bottles in total. You can mix the Night Cream and the Face Wash.'),
           ('Do you ship wholesale orders across India?', 'Yes. Orders ship from Bhatkal, Karnataka, to most pincodes in India. Delivery time depends on your location.'),
           ('Is the stock genuine and sealed?', 'Yes. Every pack ships sealed, directly from GlutaNex.')]
page('/wholesale/', 'Glutathione Cream Wholesale for Parlours & Resellers | GlutaNex',
     'Buy GlutaNex glutathione cream and face wash wholesale for your beauty parlour, salon or shop. Minimum 6 pieces. Prices on WhatsApp, delivery across India.',
     top('Wholesale', 'GlutaNex for <span class="gold">parlours and resellers</span>', 'Glutathione Night Cream and Face Wash in bulk for beauty parlours, salons and shops. Minimum 6 pieces.') +
     '''<section style="padding-top:20px"><div class="wrap ws">
<div class="prose"><p class="answer">Beauty parlours, salons, cosmetic shops and online sellers can order GlutaNex glutathione skincare in bulk. The minimum order is 6 pieces, mixed as you like. Send the form below and we reply on WhatsApp with wholesale prices within one working day.</p>
<ul><li><b>Products:</b> GlutaNex Glutathione Night Cream (30 g) and Gluta Boost Face Wash (100 ml)</li><li><b>Minimum order:</b> 6 pieces in total</li><li><b>Genuine stock:</b> sealed packs, shipped directly from us in Bhatkal, Karnataka</li><li><b>Support:</b> product information and honest usage guidance you can share with your clients</li></ul></div>
<form class="panel wsform" id="wsform" novalidate>
  <h2>Wholesale enquiry</h2>
  <div class="f"><label for="ws-biz">Business name</label><input id="ws-biz" required maxlength="80" autocomplete="organization"></div>
  <div class="f"><label for="ws-type">Type of business</label><select id="ws-type"><option>Beauty parlour / salon</option><option>Cosmetic or general shop</option><option>Pharmacy</option><option>Online seller</option><option>Other</option></select></div>
  <div class="two"><div class="f"><label for="ws-name">Your name</label><input id="ws-name" required maxlength="60" autocomplete="name"></div><div class="f"><label for="ws-phone">Mobile number</label><input id="ws-phone" type="tel" inputmode="numeric" maxlength="14" required autocomplete="tel"></div></div>
  <div class="two"><div class="f"><label for="ws-city">City</label><input id="ws-city" required maxlength="60" autocomplete="address-level2"></div><div class="f"><label for="ws-pin">Pincode</label><input id="ws-pin" inputmode="numeric" maxlength="6" autocomplete="postal-code"></div></div>
  <div class="two"><div class="f"><label for="ws-cream">Night Cream (pieces)</label><input id="ws-cream" type="number" min="0" max="999" inputmode="numeric" value="6"></div><div class="f"><label for="ws-wash">Face Wash (pieces)</label><input id="ws-wash" type="number" min="0" max="999" inputmode="numeric" value="0"></div></div>
  <div class="f"><label for="ws-note">Anything else? (optional)</label><textarea id="ws-note" rows="2" maxlength="300"></textarea></div>
  <p class="oerr" id="ws-err" hidden></p>
  <button class="btn wa block" type="submit">Send enquiry on WhatsApp</button>
  <p class="muted" style="font-size:.8rem;margin:0">Opens WhatsApp with your details filled in. Nothing is sent until you press send there.</p>
</form></div></section>
<section style="padding-top:0"><div class="wrap">''' + faq_block(_WS_FAQ) + '</div></section>',
     schema=[faq_ld(_WS_FAQ)], js='store.js,features.js', crumbs=[('Wholesale', '/wholesale/')])

# ---------------- Routine streak (for buyers; not for search) ----------------
page('/routine/', 'Your 56-night routine | GlutaNex', 'Track your GlutaNex Night Cream nights. 56 nights unlock ₹200 off your next order.',
     top('Routine tracker', 'Your <span class="gold">56-night</span> routine', 'Tap "Done tonight" after your Night Cream. 56 nights unlock ₹200 off your next order.') +
     '<section style="padding-top:18px"><div class="wrap"><div id="rt" class="rt"><div class="panel rt-card"><p class="muted">Loading your tracker…</p></div></div>'
     '<p class="muted" style="font-size:.82rem;margin-top:14px;max-width:60ch">One tap counts per day. Results vary from person to person; the tracker is here to help you stay consistent, which is what makes a routine work.</p></div></section>',
     index=False, js='store.js,routine.js', crumbs=[('Routine tracker', '/routine/')])

# ---------------- Unboxing reel reward ----------------
page('/unboxing-reward/', 'Unboxing Reel Reward: ₹150 Off Your Next Order | GlutaNex',
     'Post an Instagram Reel of your GlutaNex unboxing, tag @glutanexofficial and get ₹150 off your next order.',
     top('Unboxing reward', 'Post your unboxing, get <span class="gold">₹150 off</span>', 'Film yourself opening your GlutaNex parcel, post it as a Reel, and we send you ₹150 off your next order.') +
     '''<section style="padding-top:20px"><div class="wrap ws">
<div class="prose">
<h2>How it works</h2><ol>
<li><b>Film the unboxing:</b> open your GlutaNex parcel on camera so the box and product are clearly visible.</li>
<li><b>Post it as an Instagram Reel</b> (public), tag <a href="''' + INSTAGRAM + '''" target="_blank" rel="noopener">@glutanexofficial</a> and add <b>#GlutaNexReward</b> to the caption.</li>
<li><b>Send us the link</b> with the form. We check it within 2 working days and send your ₹150 code on WhatsApp.</li></ol>
<h2>The rules</h2><ul>
<li>One reward per order, for a real GlutaNex parcel.</li>
<li><b>Be honest.</b> You do not have to say anything nice, and please do not claim results you have not had.</li>
<li>Because you get a reward, keep <b>#GlutaNexReward</b> in the caption: Indian advertising rules ask for this.</li>
<li>Keep the Reel public for at least 30 days. We may reshare it on our page with credit, and we will ask you first.</li>
<li>The code gives ₹150 off your next order of ₹399 or more, is valid for 60 days and works with the mobile number on your order.</li></ul>
</div>
<form class="panel wsform" id="ubform" novalidate>
  <h2>Send your Reel</h2>
  <div class="f"><label for="ub-order">Order number (starts with pay_)</label><input id="ub-order" required maxlength="40" autocomplete="off" spellcheck="false"></div>
  <div class="f"><label for="ub-phone">Mobile number on the order</label><input id="ub-phone" type="tel" inputmode="numeric" maxlength="14" required autocomplete="tel"></div>
  <div class="f"><label for="ub-link">Instagram Reel link</label><input id="ub-link" type="url" required placeholder="https://www.instagram.com/reel/..." autocomplete="off"></div>
  <p class="oerr" id="ub-err" hidden></p>
  <button class="btn wa block" type="submit">Send on WhatsApp</button>
  <p class="muted" style="font-size:.8rem;margin:0">Opens WhatsApp with your details filled in.</p>
</form></div></section>''', index=False, js='store.js,features.js', crumbs=[('Unboxing reward', '/unboxing-reward/')])
