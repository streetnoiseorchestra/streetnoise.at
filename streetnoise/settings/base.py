"""
Django settings for streetnoise project.
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

from django.utils.translation import gettext_lazy as _

WAGTAIL_ENABLE_UPDATE_CHECK = True
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/


# Application definition

INSTALLED_APPS = [
    "wagtail_modeltranslation",
    "wagtail_modeltranslation.makemigrations",
    "wagtail_modeltranslation.migrate",
    "wagtail.contrib.modeladmin",
    "wagtail.contrib.forms",
    "wagtail.contrib.redirects",
    "wagtail.embeds",
    "wagtail.sites",
    "wagtail.users",
    "wagtail.snippets",
    "wagtail.documents",
    "wagtail.images",
    "wagtail.search",
    "wagtail.admin",
    "wagtail.core",
    "modelcluster",
    "taggit",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.keycloak",
    "home",
    "blog",
    "gigs",
    "festival2023",
    "streetnoise",
    "wagtailmenus",
    "plausible",
    "mjml",
    "newsletter",
    "birdsong",
]

MIGRATION_MODULES = {
    "wagtailmenus": "streetnoise.contrib.wagtailmenus.migrations",
}

SITE_ID = 1

MIDDLEWARE = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    # LocaleMiddleware should be after SessionMiddleware and before CommonMiddleware
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "wagtail.contrib.redirects.middleware.RedirectMiddleware",
]

ROOT_URLCONF = "streetnoise.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(PROJECT_DIR, "templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.request",
                "wagtailmenus.context_processors.wagtailmenus",
            ],
            "libraries": {
                "app_tags": "streetnoise.templatetags.app_tags",
            },
        },
    },
]

WSGI_APPLICATION = "streetnoise.wsgi.application"

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
)

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = "de"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGES = (
    ("de", _("German")),  # this is the default
    ("en", _("English")),
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, "static"),
]

# ManifestStaticFilesStorage is recommended in production, to prevent outdated
# Javascript / CSS assets being served from cache (e.g. after a Wagtail upgrade).
# See https://docs.djangoproject.com/en/2.2/ref/contrib/staticfiles/#manifeststaticfilesstorage
STATICFILES_STORAGE = "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"

STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = "/static/"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

# Wagtail settings

WAGTAIL_SITE_NAME = "streetnoise"

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
BASE_URL = "https://streetnoise.at"
WAGTAILADMIN_BASE_URL = "https://streetnoise.at"

COMPRESS_PRECOMPILERS = (("text/x-scss", "django_libsass.SassCompiler"),)

COMPRESS_CACHEABLE_PRECOMPILERS = (("text/x-scss", "django_libsass.SassCompiler"),)

WAGTAILADMIN_NOTIFICATION_FROM_EMAIL = (
    "StreetNoise Orchestra <website@notifications.streetnoise.at>"
)
DEFAULT_FROM_EMAIL = WAGTAILADMIN_NOTIFICATION_FROM_EMAIL

LOGIN_URL = "/login/"
LOGIN_REDIRECT_URL = "/admin/"
ACCOUNT_AUTHENTICATION_METHOD = "username_email"
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "optional"
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_LOGIN_ON_PASSWORD_RESET = True
ACCOUNT_LOGOUT_REDIRECT_URL = "/login/"
ACCOUNT_PRESERVE_USERNAME_CASING = False
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False
ACCOUNT_USERNAME_BLACKLIST = ["admin", "god"]
ACCOUNT_USERNAME_MIN_LENGTH = 2
ACCOUNT_ADAPTER = "streetnoise.auth_adapter.SNOAccountAdapter"
SOCIALACCOUNT_ADAPTER = "streetnoise.auth_adapter.SNOSocialAccountAdapter"
SOCIALACCOUNT_AUTO_SIGNUP = True
SOCIALACCOUNT_PROVIDERS = {
    # "nextcloud": {
    # "SERVER": "https://data.streetnoise.at",
    # },
    "keycloak": {
        "KEYCLOAK_URL": "https://id.streetnoise.at/",
        "KEYCLOAK_REALM": "sno",
        "VERIFIED_EMAIL": True,
    },
}

# Extra Wagtail config to disable password usage (SSO should be the only way in)
# https://docs.wagtail.io/en/v2.6.3/advanced_topics/settings.html#password-management
# Don't let users change or reset their password
WAGTAIL_PASSWORD_MANAGEMENT_ENABLED = False
WAGTAIL_PASSWORD_RESET_ENABLED = False

# Don't require a password when creating a user,
# and blank password means cannot log in unless SSO
WAGTAILUSERS_PASSWORD_ENABLED = False


# If True (which should only be done in settings.local), then show username and
# password fields. You'll also need to enable the model backend in local settings
USE_CONVENTIONAL_AUTH = False

LOCALE_PATHS = ["locale"]

WAGTAILEMBEDS_FINDERS = [
    {
        "class": "streetnoise.embeds.finders.AudioFinder",
        "extensions": ["mp3"],
        "mimetype": "audio/mpeg",
    },
    {
        "class": "streetnoise.embeds.finders.AudioFinder",
        "extensions": ["ogg", "oga"],
        "mimetype": "audio/ogg",
    },
    {
        "class": "streetnoise.embeds.finders.AudioFinder",
        "extensions": ["wav"],
        "mimetype": "audio/wav",
    },
    {
        "class": "streetnoise.embeds.finders.AudioFinder",
        "extensions": ["m4a"],
        "mimetype": "audio/mp4",
    },
    # Handles all other oEmbed providers the default way
    {
        "class": "wagtail.embeds.finders.oembed",
    },
]


MAILGUN_NEWSLETTER_LIST = "news@mg.streetnoise.at"

MAILGUN_NEWSLETTER_FROM = "StreetNoise Orchestra <news@mg.streetnoise.at>"

PLAUSIBLE_DOMAIN = "stats.streetnoise.at"
PLAUSIBLE_SCRIPT_NAME = "app2.js"

MJML_EXEC_CMD = "./node_modules/.bin/mjml"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

BIRDSONG_REPLY_TO = "orchestra@streetnoise.at"

WAGTAILIMAGES_FORMAT_CONVERSIONS = {
    "bmp": "jpeg",
    "webp": "webp",
}
