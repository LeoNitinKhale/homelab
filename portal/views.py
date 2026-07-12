from django.db import connections
from django.http import JsonResponse


def health_check(request):
    """Liveness + both-databases check for uptime monitoring on Hetzner."""
    db_ok = {}
    for alias in ('default', 'ops'):
        try:
            connections[alias].cursor().execute('SELECT 1')
            db_ok[alias] = True
        except Exception:
            db_ok[alias] = False
    healthy = all(db_ok.values())
    return JsonResponse(
        {'status': 'ok' if healthy else 'degraded', 'databases': db_ok},
        status=200 if healthy else 503,
    )
