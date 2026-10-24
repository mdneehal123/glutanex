/* Launch waitlist: shows the form only when the shop's database is connected, posts with consent, shows the personal 10% code. */
(function () {
  var forms = document.querySelectorAll('[data-waitlist]');
  if (!forms.length) { return; }
  fetch('/api/config').then(function (r) { return r.json(); }).then(function (c) {
    if (c && c.leads) { forms.forEach(function (f) { f.hidden = false; }); }
  }).catch(function () {});
  forms.forEach(function (f) {
    var msg = f.querySelector('.wl-msg'), btn = f.querySelector('button[type=submit]');
    function say(t, cls) { msg.textContent = ''; msg.className = 'wl-msg ' + (cls || ''); msg.hidden = !t; if (t) { msg.appendChild(document.createTextNode(t)); } }
    f.addEventListener('submit', function (e) {
      e.preventDefault();
      var phone = f.elements.phone.value.replace(/\D/g, '');
      if (phone.length === 12 && phone.indexOf('91') === 0) { phone = phone.slice(2); }
      if (!/^[6-9]\d{9}$/.test(phone)) { say('Please enter a valid 10-digit mobile number.', 'bad'); return; }
      if (!f.elements.consent.checked) { say('Please tick the box so we can message you on WhatsApp.', 'bad'); return; }
      btn.disabled = true; say('Adding you…', '');
      fetch('/api/waitlist', { method: 'POST', headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ phone: phone, name: f.elements.name ? f.elements.name.value : '', product: f.getAttribute('data-product') || 'all', consent: true }) })
        .then(function (r) { return r.json().then(function (j) { return { ok: r.ok, j: j }; }); })
        .then(function (x) {
          btn.disabled = false;
          if (x.ok && x.j && x.j.ok) {
            f.classList.add('done');
            say("You're on the list ✓ " + (x.j.code ? 'Your code: ' + x.j.code + '. ' : '') + x.j.pct + '% off for ' + x.j.days + ' days from launch day. We will message you on WhatsApp when it opens.', 'ok');
          } else { say(x.j && x.j.error === 'busy' ? 'Too many tries. Please wait a little and try again.' : 'Could not add you right now. Please try again, or tap Notify me on WhatsApp.', 'bad'); }
        }).catch(function () { btn.disabled = false; say('Could not add you right now. Please try again, or tap Notify me on WhatsApp.', 'bad'); });
    });
  });
})();
