import logging
from .settings import *  # noqa

DEBUG = True
EMAIL_DEBUG = True
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG  # noqa

MEDIA_ROOT = os.path.join(BASE_DIR, 'test_media')  # noqa

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
PASSWORD_HASHERS = ('django.contrib.auth.hashers.MD5PasswordHasher', )

# Disable cache during testing
CACHE_DISABLED = True

LOGGING = {}
LOCAL_APPS_LOGGERS = {}
# Disable all logging calls with levels less severe than or equal to CRITICAL
logging.disable(logging.CRITICAL)
