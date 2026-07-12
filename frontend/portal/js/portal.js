// Minimal portal shell script — pings the health endpoint and reflects the
// backend/database status in the top bar. Grows into the SPA as areas land.
(function () {
  const el = document.getElementById('health');
  fetch('/health/')
    .then((r) => r.json())
    .then((d) => {
      const ok = d.status === 'ok';
      el.textContent = ok ? 'online' : 'degraded';
      el.classList.add(ok ? 'ok' : 'bad');
    })
    .catch(() => {
      el.textContent = 'offline';
      el.classList.add('bad');
    });
})();
