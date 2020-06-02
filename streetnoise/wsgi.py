"""
WSGI config for streetnoise project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

django_env = os.getenv("DJANGO_ENV", "development")
if django_env == "production":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "streetnoise.settings.production")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "streetnoise.settings.dev")

application = get_wsgi_application()
