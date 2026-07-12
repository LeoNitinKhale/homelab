from django.apps import apps
from django.test import TestCase


class HealthAppTests(TestCase):
    """Smoke test — the app is wired up; models land once the dashboard is specced."""

    def test_app_is_installed(self):
        self.assertTrue(apps.is_installed('health'))
