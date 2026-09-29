/* Publications page behavior (markup: _layouts/bib_entry.html +
   _includes/publications-filter.html).
   1. Toggle the hidden Abstract / BibTeX panels under each entry.
   2. Filter the list by free text, by topic and by person. The three filters
      combine (AND) and are mirrored in the URL hash, e.g.
      /publications/#topic=latam&q=Carisimo */
document.addEventListener('DOMContentLoaded', function () {
  var root = document.querySelector('.publications');
  if (!root) return;

  /* ---- 1. Abs / Bib toggles ------------------------------------------- */
  root.querySelectorAll('.abstract.btn, .bibtex.btn').forEach(function (btn) {
    btn.addEventListener('click', function (e) {
      e.preventDefault();
      var cls = btn.classList.contains('abstract') ? 'abstract' : 'bibtex';
      var row = btn.closest('.row');
      if (!row) return;
      var panel = row.querySelector('.' + cls + '.hidden');
      if (panel) panel.classList.toggle('open');
    });
  });

  /* ---- 2. Filters ------------------------------------------------------- */
  var bar = document.querySelector('.pub-filter');
  if (!bar) return;
  var input = bar.querySelector('.pub-filter__input');
  var clearBtn = bar.querySelector('.pub-filter__clear');
  var count = bar.querySelector('.pub-filter__count');
  var people = bar.querySelector('.pub-filter__people');

  function norm(s) {
    return (s || '').normalize('NFD').replace(/[̀-ͯ]/g, '').toLowerCase().replace(/\s+/g, ' ').trim();
  }

  // One record per entry. jekyll-scholar wraps each entry in an <li>; fall
  // back to the .row itself if the list markup ever changes.
  var items = Array.prototype.map.call(root.querySelectorAll('.row'), function (row) {
    var authorText = (row.querySelector('.author') || {}).textContent || '';
    return {
      el: row.closest('li') || row,
      topics: (row.getAttribute('data-topics') || '').split(/\s+/).filter(Boolean),
      authors: authorText.split(/,\s*|\s+and\s+/).map(function (a) { return a.trim(); }).filter(Boolean),
      hay: norm([
        (row.querySelector('.title') || {}).textContent,
        authorText,
        (row.querySelector('.periodical') || {}).textContent
      ].join(' '))
    };
  });
  var total = items.length;
  var state = { q: '', topic: '' };

  function writeHash() {
    var parts = [];
    if (state.topic) parts.push('topic=' + encodeURIComponent(state.topic));
    if (state.q.trim()) parts.push('q=' + encodeURIComponent(state.q.trim()));
    try { history.replaceState(null, '', parts.length ? '#' + parts.join('&') : location.pathname); } catch (e) {}
  }

  function apply() {
    var q = norm(state.q);
    var shown = 0;
    items.forEach(function (it) {
      var ok = (!q || it.hay.indexOf(q) !== -1) && (!state.topic || it.topics.indexOf(state.topic) !== -1);
      it.el.classList.toggle('is-hidden', !ok);
      if (ok) shown++;
    });
    var filtering = !!(q || state.topic);
    clearBtn.hidden = !filtering;
    count.textContent = filtering ? (shown ? shown + ' ' + bar.dataset.of + ' ' + total : bar.dataset.none) : '';
    document.querySelectorAll('.pub-topic[data-topic]').forEach(function (c) {
      c.classList.toggle('is-active', c.dataset.topic === state.topic);
    });
    people.querySelectorAll('.pub-chip').forEach(function (c) {
      c.classList.toggle('is-active', !!q && norm(c.dataset.q) === q);
    });
    writeHash();
  }

  function setQuery(v) { state.q = v; input.value = v; apply(); }
  function setTopic(id) { state.topic = state.topic === id ? '' : id; apply(); }

  input.addEventListener('input', function () { state.q = input.value; apply(); });
  input.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') { state.topic = ''; setQuery(''); }
  });
  clearBtn.addEventListener('click', function () { state.topic = ''; setQuery(''); input.focus(); });

  // Topic chips: the bar and every entry. Entry chips are real links to
  // /publications/#topic=<id> so they also work from research-area pages; here
  // we filter in place and scroll back to the bar.
  document.addEventListener('click', function (e) {
    var chip = e.target.closest('.pub-topic[data-topic]');
    if (!chip) return;
    e.preventDefault();
    var fromEntry = !bar.contains(chip);
    setTopic(chip.dataset.topic);
    if (fromEntry) bar.scrollIntoView({ behavior: 'smooth', block: 'start' });
  });

  // People chips: surnames of the authors that appear on >= 3 entries, most
  // frequent first. Highlighted (group) authors always come first.
  var freq = {};
  items.forEach(function (it) {
    var seen = {};
    it.authors.forEach(function (a) {
      var parts = a.split(' ');
      var last = parts[parts.length - 1];
      if (!last || seen[last]) return;
      seen[last] = true;
      freq[last] = (freq[last] || 0) + 1;
    });
  });
  var emph = {};
  root.querySelectorAll('.author em').forEach(function (em) {
    var parts = em.textContent.trim().split(' ');
    emph[parts[parts.length - 1]] = true;
  });
  Object.keys(freq)
    .filter(function (k) { return freq[k] >= 3 || emph[k]; })
    .sort(function (a, b) { return (emph[b] ? 1 : 0) - (emph[a] ? 1 : 0) || freq[b] - freq[a] || a.localeCompare(b); })
    .slice(0, 12)
    .forEach(function (last) {
      var b = document.createElement('button');
      b.type = 'button';
      b.className = 'pub-chip' + (emph[last] ? ' pub-chip--group' : '');
      b.dataset.q = last;
      b.textContent = last;
      b.title = freq[last];
      b.addEventListener('click', function () { setQuery(norm(state.q) === norm(last) ? '' : last); });
      people.appendChild(b);
    });

  // Deep links: #topic=latam, #q=Carisimo, #topic=latam&q=Carisimo
  function readHash() {
    var h = location.hash.replace(/^#/, '');
    var m;
    state.topic = (m = /(?:^|&)topic=([^&]+)/.exec(h)) ? decodeURIComponent(m[1]) : '';
    state.q = (m = /(?:^|&)q=([^&]+)/.exec(h)) ? decodeURIComponent(m[1]) : '';
    input.value = state.q;
    apply();
  }
  window.addEventListener('hashchange', readHash);
  if (location.hash) readHash();
});
