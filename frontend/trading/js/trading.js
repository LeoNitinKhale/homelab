// Trading splash — pulls trades from the DRF API, renders a summary + list.
(function () {
  const esc = (s) =>
    String(s ?? '').replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
  const sign = (n) => (n > 0 ? 'pos' : n < 0 ? 'neg' : '');
  const money = (n) => Number(n).toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 });

  fetch('/api/trading/trades/')
    .then((r) => r.json())
    .then((trades) => {
      const open = trades.filter((t) => t.is_open).length;
      const pnl = trades.reduce((sum, t) => sum + (t.pnl != null ? Number(t.pnl) : 0), 0);

      document.getElementById('stat-total').textContent = trades.length;
      document.getElementById('stat-open').textContent = open;
      const pnlEl = document.getElementById('stat-pnl');
      pnlEl.textContent = money(pnl);
      pnlEl.classList.add(sign(pnl));

      const body = document.getElementById('rows');
      if (!trades.length) {
        body.innerHTML = '<tr><td colspan="7" class="empty">No trades yet — add some in the admin.</td></tr>';
        return;
      }
      body.innerHTML = trades
        .map((t) => {
          const pnlCell = t.pnl != null
            ? `<td class="num ${sign(Number(t.pnl))}">${money(t.pnl)}</td>`
            : '<td class="num">—</td>';
          return `<tr>
            <td>${esc(t.symbol)}</td>
            <td>${esc(t.direction)}</td>
            <td class="num">${esc(t.quantity)}</td>
            <td class="num">${esc(t.entry_price)}</td>
            <td class="num">${t.exit_price != null ? esc(t.exit_price) : '—'}</td>
            ${pnlCell}
            <td>${esc(t.opened_on)}</td>
          </tr>`;
        })
        .join('');
    })
    .catch(() => {
      document.getElementById('rows').innerHTML =
        '<tr><td colspan="7" class="empty">Failed to load trades.</td></tr>';
    });
})();
