from .base import *  # noqa
from .base import env

# URLS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#root-urlconf
ROOT_URLCONF = "config.ui_urls"

# WhiteNoise
# ------------------------------------------------------------------------------
# http://whitenoise.evans.io/en/latest/django.html#using-whitenoise-in-development
INSTALLED_APPS = ["whitenoise.runserver_nostatic"] + INSTALLED_APPS  # noqa: F405,E501

if env("RUN_TESTS", default="") == "":
    # django-debug-toolbar
    # ------------------------------------------------------------------------------
    # https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#prerequisites
    INSTALLED_APPS += ["debug_toolbar"]  # noqa: F405
    # https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#middleware
    MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]  # noqa: F405
    # https://django-debug-toolbar.readthedocs.io/en/latest/configuration.html#debug-toolbar-config
    DEBUG_TOOLBAR_CONFIG = {
        # "DISABLE_PANELS": ["debug_toolbar.panels.redirects.RedirectsPanel"],
        "SHOW_TEMPLATE_CONTEXT": True,
        "SHOW_TOOLBAR_CALLBACK": lambda r: True,
    }
    # https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#internal-ips
    INTERNAL_IPS = ["127.0.0.1", "10.0.2.2"]
    if env("USE_DOCKER", default="") == "true":
        import socket

        hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
        INTERNAL_IPS += [".".join(ip.split(".")[:-1] + ["1"]) for ip in ips]
        try:
            _, _, ips = socket.gethostbyname_ex("node")
            INTERNAL_IPS.extend(ips)
        except socket.gaierror:
            # The node container isn't started (yet?)
            pass


# MIDDLEWARE
# ------------------------------------------------------------------------------
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#middleware
MIDDLEWARE += ["app.global.middleware.user_timezone.TimezoneMiddleware"]

# SECURITY
# ------------------------------------------------------------------------------
# django-cors-headers - https://github.com/adamchainz/django-cors-headers#setup
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_ALL_ORIGINS = True
