from django.apps import AppConfig
from plausible.contrib.wagtail.apps import WagtailPlausibleAppConfig
from wagtail.images.apps import WagtailImagesAppConfig


class StreetnoiseConfig(AppConfig):
    name = "streetnoise"

    def ready(self):
        import streetnoise.signals.handlers


class CustomImagesAppConfig(WagtailImagesAppConfig):
    default_attrs = {"decoding": "async", "loading": "lazy"}


class StreetnoisePlausibleAppConfig(WagtailPlausibleAppConfig):
    default_auto_field = "django.db.models.AutoField"
