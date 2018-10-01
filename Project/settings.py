import os
import logging

from configurations import Configuration, values


class BaseConfiguration(Configuration):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    SECRET_KEY = '!!!!INSECURE SECRET KEY!!!!'
    DEBUG = False
    TEMPLATE_DEBUG = False
    ALLOWED_HOSTS = ['*']
    ROOT_URLCONF = 'Project.urls'
    WSGI_APPLICATION = 'Project.wsgi.application'
    LANGUAGE_CODE = 'ru'
    TIME_ZONE = 'UTC'
    USE_I18N = True
    USE_L10N = True
    USE_TZ = True
    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'static'),
    )
    STATIC_URL = '/static/'
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    SHOP_NAME = 'Simple shop'
    CART_SESSION_ID = 'cart'
    DATABASES = values.DatabaseURLValue()

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
    ]
    THIRD_PARTY_APPS = [
        'sorl.thumbnail',
    ]
    LOCAL_APPS = [
        'apps.base',
        'apps.category',
        'apps.cart'
    ]
    INSTALLED_APPS += THIRD_PARTY_APPS
    INSTALLED_APPS += LOCAL_APPS
    INTERNAL_IPS = ['127.0.0.1']
    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [f'{BASE_DIR}/templates'],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                    'apps.cart.context_processor.cart',
                ],
            },
        },
    ]
    AUTH_PASSWORD_VALIDATORS = [
        {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
        {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
        {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
        {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
    ]


class Develop(BaseConfiguration):
    DEBUG = True
    TEMPLATE_DEBUG = True
    BaseConfiguration.INSTALLED_APPS += ['debug_toolbar']
    BaseConfiguration.MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']
    DATABASES = values.DatabaseURLValue('sqlite:///db.sqlite3')
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


class Testing(BaseConfiguration):
    DEBUG = True
    EMAIL_DEBUG = True
    BaseConfiguration.TEMPLATES[0]['OPTIONS']['debug'] = DEBUG
    MEDIA_ROOT = os.path.join(BaseConfiguration.BASE_DIR, 'test_media')
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    PASSWORD_HASHERS = ('django.contrib.auth.hashers.MD5PasswordHasher',)
    CACHE_DISABLED = True
    LOGGING = {}
    LOCAL_APPS_LOGGERS = {}
    logging.disable(logging.CRITICAL)


class Production(BaseConfiguration):
    SECRET_KEY = 'SECRET_KEY'
    STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'
    STATIC_ROOT = os.path.join(BaseConfiguration.BASE_DIR, 'collected_static')
    DATABASES = values.DatabaseURLValue('postgres://postgres:postgres@db:5432/simpleshop')
