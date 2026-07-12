from rest_framework import viewsets

from .models import Trade
from .serializers import TradeSerializer


class TradeViewSet(viewsets.ReadOnlyModelViewSet):
    """Read-only for now — the splash page consumes this; editing stays in the
    admin until in-app authoring (with CSRF/auth) is built."""
    queryset = Trade.objects.all()
    serializer_class = TradeSerializer
