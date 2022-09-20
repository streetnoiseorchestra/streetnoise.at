#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    django_env = os.getenv("DJANGO_ENV", "development")
    if django_env == "production":
        os.environ.setdefault(
            "DJANGO_SETTINGS_MODULE", "streetnoise.settings.production"
        )
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "streetnoise.settings.dev")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
