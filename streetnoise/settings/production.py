import dj_database_url

from .base import *

def read_env_file(name):
    try:
        return os.environ[name]
    except KeyError:
        with open(os.environ[name+'_FILE']) as f:
            return f.read().strip()

if os.environ.get('COLLECT_STATIC_OVERRIDE', False):
    SECRET_KEY = 'collect static override'
    DATABASE_URL = 'postgres://none'
    REDIS_URL = 'none'
else:
    # Secret key
    # In order to support Docker secrets, which can only be mounted as files, we allow
    # for the secret key to come from the environment or a file specified using an
    # environment variable.

    SECRET_KEY = read_env_file('DJANGO_SECRET_KEY')
    EMAIL_HOST_PASSWORD = read_env_file('EMAIL_HOST_PASSWORD')
    DATABASE_URL = read_env_file('DATABASE_URL')
    STRIPE_PK = read_env_file('STRIPE_PK')
    STRIPE_SK = read_env_file('STRIPE_SK')


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

CONTACT_FORM_RECIPIENTS = ['orchestra@streetnoise.at']
