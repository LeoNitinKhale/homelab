"""Root URL configuration.

DRF app APIs mount under /api/; the portal SPA shell is served at '/'. Static
frontend assets are served directly in dev (no bundler).
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.decorators.cache import never_cache
from django.views.decorators.http import require_GET
from django.views.generic import TemplateView

from portal.views import health_check


def spa(template):
    # never_cache: SPA shells are edited constantly — don't serve a stale copy.
    return never_cache(TemplateView.as_view(template_name=template))


urlpatterns = [
    path('admin/', admin.site.urls),
    path('health/', require_GET(health_check), name='health'),
    # App APIs (DRF)
    path('api/mnemonics/', include('mnemonics.urls')),
    path('api/trading/', include('trading.urls')),
    # App pages (portal landing + per-area splash pages)
    path('', spa('portal/index.html'), name='home'),
    path('mnemonics/', spa('mnemonics/index.html'), name='mnemonics'),
    path('trading/', spa('trading/index.html'), name='trading'),
] + static('/assets/', document_root=settings.BASE_DIR / 'assets') \
  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# frontend CSS/JS is served under STATIC_URL via STATICFILES_DIRS (see settings).
