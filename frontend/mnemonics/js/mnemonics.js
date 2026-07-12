// Mnemonics splash — pulls pegs from the DRF API and renders a summary + list.
(function () {
  const esc = (s) =>
    String(s ?? '').replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));

  fetch('/api/mnemonics/pegs/')
    .then((r) => r.json())
    .then((pegs) => {
      document.getElementById('stat-count').textContent = pegs.length;
      const body = document.getElementById('rows');
      if (!pegs.length) {
        body.innerHTML = '<tr><td colspan="3" class="empty">No pegs yet — add some in the admin.</td></tr>';
        return;
      }
      body.innerHTML = pegs
        .map((p) => `<tr><td class="num">${p.number}</td><td>${esc(p.word)}</td><td>${esc(p.notes)}</td></tr>`)
        .join('');
    })
    .catch(() => {
      document.getElementById('rows').innerHTML =
        '<tr><td colspan="3" class="empty">Failed to load pegs.</td></tr>';
    });
})();
