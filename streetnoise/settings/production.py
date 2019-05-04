import dj_database_url

from .base import *

if os.environ.get('COLLECT_STATIC_OVERRIDE', False):
    SECRET_KEY = 'collect static override'
    DATABASE_URL = 'postgres://none'
    REDIS_URL = 'none'
else:
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

DATABASES = {'default': dj_database_url.parse(DATABASE_URL, conn_max_age=600)}
ALLOWED_HOSTS = ['test.streetnoise.at', 'streetnoise.at']

ADMINS = (
    ('Casey Link', 'me+streetnoiseat@caseylink.com'),
)

MIDDLEWARE.append('whitenoise.middleware.WhiteNoiseMiddleware')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
        },
    },
}

