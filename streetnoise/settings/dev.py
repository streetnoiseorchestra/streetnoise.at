import dj_database_url

from .base import *

DATABASE_URL = os.environ.get("DATABASE_URL", "postgres://streetnoise_cms:dev@localhost/streetnoise_cms")


MAILGUN_KEY = os.environ.get("MAILGUN_KEY")
SNORGA_SHARED_TOKEN = os.environ.get("SNORGA_SHARED_TOKEN")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "rsrmy+d$6h&c@3!qs5y=9gw!clsdazzu6f1p#$&ah20=j1zym2"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


INSTALLED_APPS = INSTALLED_APPS + [
    "wagtail.contrib.styleguide",
    # 'debug_toolbar',
]
# MIDDLEWARE = MIDDLEWARE + ['debug_toolbar.middleware.DebugToolbarMiddleware']

INTERNAL_IPS = "127.0.0.1"


DATABASES = {"default": dj_database_url.parse(DATABASE_URL, conn_max_age=600)}

CONTACT_FORM_RECIPIENTS = ["me@caseylink.com"]

try:
    from .local import *
except ImportError:
    pass
