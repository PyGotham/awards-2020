from awards.settings.base import *  # NOQA

SECRET_KEY = "__5^!hevku!ls@mi#8*t_spy3k#my%24jpscvu^v8h5o(_$2o@"

DEBUG = True

INSTALLED_APPS += ["debug_toolbar"]

MIDDLEWARE = ["debug_toolbar.middleware.DebugToolbarMiddleware"] + MIDDLEWARE

INTERNAL_IPS = ["127.0.0.1"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
