from .base import *

DEBUG = True
ALLOWED_HOSTS = ['alexandereriksson.se', 'www.alexandereriksson.se', '186.66.62.186']

COMPRESS_OFFLINE = True
LIBSASS_OUTPUT_STYLE = 'compressed'
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

# Custom logger
logger = logging.getLogger('django')
