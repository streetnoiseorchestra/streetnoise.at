import dj_database_url

from .base import *

# Secret key
# In order to support Docker secrets, which can only be mounted as files, we allow
# for the secret key to come from the environment or a file specified using an
# environment variable.
try:
    SECRET_KEY = os.environ['DJANGO_SECRET_KEY']
except KeyError:
    with open(os.environ['DJANGO_SECRET_KEY_FILE']) as f:
        SECRET_KEY = f.read().strip()

try:
    EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']
except KeyError:
    with open(os.environ['EMAIL_HOST_PASSWORD_FILE']) as f:
        EMAIL_HOST_PASSWORD = f.read().strip()

try:
    DATABASE_URL = os.environ['DATABASE_URL']
except KeyError:
    with open(os.environ['DATABASE_URL_FILE']) as f:
        DATABASE_URL = f.read().strip()

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = "smtp.sparkpostmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = "SMTP_Injection"
EMAIL_USE_TLS = True

DEBUG = False

try:
    from .local import *
except ImportError:
    pass

DATABASES = {}
DATABASES['default'] = dj_database_url.config(conn_max_age=600)
