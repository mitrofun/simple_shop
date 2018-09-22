from Project.settings import *  # noqa
import os

DEBUG = False

ALLOWED_HOSTS = ['*']

STATIC_ROOT = os.path.join(BASE_DIR, 'collected_static')  # noqa
