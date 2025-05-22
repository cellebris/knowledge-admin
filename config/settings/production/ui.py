from .base import *  # noqa
from .base import env

# URLS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#root-urlconf
ROOT_URLCONF = "config.ui_urls"

# MIDDLEWARE
# ------------------------------------------------------------------------------
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#middleware
MIDDLEWARE += ["app.global.middleware.user_timezone.TimezoneMiddleware"]  # noqa: F405

# ADMIN
# ------------------------------------------------------------------------------
# Django Admin path regex.
ADMIN_PATH = env("DJANGO_ADMIN_PATH")
