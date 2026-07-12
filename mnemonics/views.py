from rest_framework import viewsets

from .models import Peg
from .serializers import PegSerializer


class PegViewSet(viewsets.ReadOnlyModelViewSet):
    """Read-only for now — the splash page consumes this; editing stays in the
    admin until in-app authoring (with CSRF/auth) is built."""
    queryset = Peg.objects.all()
    serializer_class = PegSerializer
