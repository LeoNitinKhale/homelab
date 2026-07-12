"""
Django settings for the Homelab project.

Personal, single-user site. Two PostgreSQL databases split by criticality:
  - core  — durable data (mnemonics, trading, health)          -> 'default'
  - ops   — ephemeral operational data (tasks, review state)   -> 'ops'
The OpsRouter (config/db_router.py) routes the `ops` app to the ops DB and
everything else to core. See CLAUDE.md and docs/ARCHITECTURE.md.
"""

import os
import sys
from pathlib import Path

import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

# Load .env at the project root if present (real secrets live here, gitignored).
try:
    from dotenv import load_dotenv
    load_dotenv(BASE_DIR / '.env')
except ImportError:
    pass

# Blank falls back to an insecure dev default — fine for a local checkout, set a
# real SECRET_KEY in .env for the Hetzner deployment.
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-dev-key-change-in-production')

# DEBUG on unless explicitly disabled (DEBUG=0 in prod .env).
DEBUG = os.environ.get('DEBUG', '1').lower() in ('1', 'true', 'yes')

# Comma-separated in .env, e.g. ALLOWED_HOSTS=homelab.khale.net. '*' in dev.
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '*').split(',')

_TESTING = 'test' in sys.argv

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    # Local apps
    'common',       # abstract base models only — no tables
    'mnemonics',
    'trading',
    'health',
    'ops',
    'portal',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'frontend'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# ── Databases ────────────────────────────────────────────────────────────────
# PostgreSQL everywhere (no SQLite fallback — dev/prod parity). Local dev defaults
# to the local `homelab` role + homelab_core/homelab_ops databases; the Hetzner
# deployment overrides both URLs in .env.
DATABASES = {
    'default': dj_database_url.config(
        default='postgres://homelab:homelab@localhost:5432/homelab_core',
        conn_max_age=600,
    ),
    'ops': dj_database_url.config(
        env='OPS_DATABASE_URL',
        default='postgres://homelab:homelab@localhost:5432/homelab_ops',
        conn_max_age=600,
    ),
}

DATABASE_ROUTERS = ['config.db_router.OpsRouter']

# Django auto-creates/drops throwaway test databases; names them explicitly so
# core and ops stay distinct. The `homelab` role has CREATEDB for this.
if _TESTING:
    DATABASES['default'].setdefault('TEST', {})['NAME'] = 'test_homelab_core'
    DATABASES['ops'].setdefault('TEST', {})['NAME'] = 'test_homelab_ops'

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': ['rest_framework.renderers.JSONRenderer'],
    'DEFAULT_PAGINATION_CLASS': None,
}

# UK site: store UTC but interpret local wall-clock for admin display + any cron.
LANGUAGE_CODE = 'en-gb'
TIME_ZONE = 'Europe/London'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
# Serve the SPA's CSS/JS straight from frontend/ (no bundler). A request for
# /static/shared/css/app.css resolves to frontend/shared/css/app.css, etc.
STATICFILES_DIRS = [BASE_DIR / 'frontend']

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
