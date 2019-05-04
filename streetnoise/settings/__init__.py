import os

django_env = os.getenv('DJANGO_ENV', 'development')

if django_env == 'production':
    from .production import *
else:
    from .dev import *
