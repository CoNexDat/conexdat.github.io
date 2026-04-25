// Toggle .abstract.hidden / .bibtex.hidden panels under each publication entry.
// Markup is emitted by _layouts/bib_entry.html.
document.addEventListener('DOMContentLoaded', function () {
  document.querySelectorAll('.publications .abstract.btn, .publications .bibtex.btn').forEach(function (btn) {
    btn.addEventListener('click', function (e) {
      e.preventDefault();
      var cls = btn.classList.contains('abstract') ? 'abstract' : 'bibtex';
      var row = btn.closest('.row');
      if (!row) return;
      var panel = row.querySelector('.' + cls + '.hidden');
      if (panel) panel.classList.toggle('open');
    });
  });
});
