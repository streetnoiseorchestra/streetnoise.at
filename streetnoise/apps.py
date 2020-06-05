from django.apps import AppConfig


class StreetnoiseConfig(AppConfig):
    name = "streetnoise"

    def ready(self):
        import streetnoise.signals.handlers
