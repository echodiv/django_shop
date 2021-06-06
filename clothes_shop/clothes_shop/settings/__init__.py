import os

if 'DJANGO_ENV' in os.environ.keys() and os.environ['DJANGO_ENV'] == 'TEST':
    from .settings_test import *
elif 'DJANGO_ENV' in os.environ.keys() and os.environ['DJANGO_ENV'] == 'DEV':
    from .settings_dev import *
else:
    from .settings import *
