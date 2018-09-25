from Project.settings import *  # noqa
import os

DEBUG = False

ALLOWED_HOSTS = ['*']

STATIC_ROOT = os.path.join(BASE_DIR, 'collected_static')  # noqa

DATABASES['default'] = dj_database_url.parse(
    os.getenv('DATABASE_URL'),
    conn_max_age=600
)
