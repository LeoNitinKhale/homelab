from rest_framework.routers import DefaultRouter

from .views import PegViewSet

router = DefaultRouter()
router.register(r'pegs', PegViewSet, basename='peg')

urlpatterns = router.urls
