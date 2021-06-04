import os

if 'DJANGO_TEST' in os.environ.keys() and os.environ['DJANGO_TEST']:
    from .settings_test import *
elif 'DJANGO_DEV' in os.environ.keys() and os.environ['DJANGO_DEV']:
    from .settings_dev import *
else:
    from .settings import *
