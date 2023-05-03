from django.apps import AppConfig
from wagtail.images.apps import WagtailImagesAppConfig


class StreetnoiseConfig(AppConfig):
    name = "streetnoise"

    def ready(self):
        import streetnoise.signals.handlers


class CustomImagesAppConfig(WagtailImagesAppConfig):
    default_attrs = {"decoding": "async", "loading": "lazy"}
