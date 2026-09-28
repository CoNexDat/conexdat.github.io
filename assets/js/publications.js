/* Publications page behaviour (markup: _layouts/bib_entry.html +
   _includes/publications-filter.html).
   1. Toggle the hidden Abstract / BibTeX panels under each entry.
   2. Free-text filter over author / title / venue / year.
   3. "By person" chips, built from the authors that appear most often. */
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

  /* ---- 2 + 3. Filter ---------------------------------------------------- */
  var bar = document.querySelector('.pub-filter');
  if (!bar) return;
  var input = bar.querySelector('.pub-filter__input');
  var clearBtn = bar.querySelector('.pub-filter__clear');
  var count = bar.querySelector('.pub-filter__count');
  var chips = bar.querySelector('.pub-filter__chips');

  function norm(s) {
    return (s || '').normalize('NFD').replace(/[̀-ͯ]/g, '').toLowerCase().replace(/\s+/g, ' ').trim();
  }

  // One searchable record per entry. jekyll-scholar wraps each entry in an
  // <li>; fall back to the .row itself if the list markup ever changes.
  var items = Array.prototype.map.call(root.querySelectorAll('.row'), function (row) {
    var el = row.closest('li') || row;
    var authorText = (row.querySelector('.author') || {}).textContent || '';
    var authors = authorText.split(/,\s*|\s+and\s+/).map(function (a) { return a.trim(); }).filter(Boolean);
    var hay = norm([
      (row.querySelector('.title') || {}).textContent,
      authorText,
      (row.querySelector('.periodical') || {}).textContent
    ].join(' '));
    return { el: el, hay: hay, authors: authors };
  });
  var total = items.length;

  var active = '';
  function apply() {
    var q = norm(active);
    var shown = 0;
    items.forEach(function (it) {
      var ok = !q || it.hay.indexOf(q) !== -1;
      it.el.classList.toggle('is-hidden', !ok);
      if (ok) shown++;
    });
    clearBtn.hidden = !q;
    count.textContent = q ? (shown ? shown + ' ' + bar.dataset.of + ' ' + total : bar.dataset.none) : '';
    chips.querySelectorAll('.pub-chip').forEach(function (c) {
      c.classList.toggle('is-active', !!q && norm(c.dataset.q) === q);
    });
    try { history.replaceState(null, '', q ? '#q=' + encodeURIComponent(active.trim()) : location.pathname); } catch (e) {}
  }
  function set(v) { active = v; input.value = v; apply(); }

  input.addEventListener('input', function () { active = input.value; apply(); });
  input.addEventListener('keydown', function (e) { if (e.key === 'Escape') set(''); });
  clearBtn.addEventListener('click', function () { set(''); input.focus(); });

  // Chips: surnames of the authors that appear on >= 3 entries, most frequent
  // first. Highlighted (group) authors always come first.
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
      b.addEventListener('click', function () { set(norm(active) === norm(last) ? '' : last); });
      chips.appendChild(b);
    });

  // Deep link: /publications/#q=Carisimo
  var m = /[#&]q=([^&]+)/.exec(location.hash);
  if (m) set(decodeURIComponent(m[1]));
});
