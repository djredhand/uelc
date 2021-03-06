# flake8: noqa
from settings_shared import *

TEMPLATE_DIRS = (
    "/var/www/uelc/uelc/uelc/templates",
)

MEDIA_ROOT = '/var/www/uelc/uploads/'
# put any static media here to override app served static media
STATICMEDIA_MOUNTS = (
    ('/sitemedia', '/var/www/uelc/uelc/sitemedia'),
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'uelc',
        'HOST': '',
        'PORT': 6432,
        'USER': '',
        'PASSWORD': '',
    }
}

COMPRESS_ROOT = "/var/www/uelc/uelc/media/"
DEBUG = False
TEMPLATE_DEBUG = DEBUG

if 'migrate' not in sys.argv:
    INSTALLED_APPS.append('raven.contrib.django.raven_compat')				

try:
    from local_settings import *
except ImportError:
    pass
