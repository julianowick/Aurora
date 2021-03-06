"""
Django settings for Aurora project.

Generated by 'django-admin startproject' using Django 1.8.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ''

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Social Authentication app
    'social_django',
    # Widget Tweaks
    'widget_tweaks',
    # Aurora main application
    'cloud',
)

MIDDLEWARE_CLASSES = (
    # Django defaults
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'Aurora.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # Social Auth
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'Aurora.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'aurora',
        'USER': 'aurora',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
        'OPTIONS': {
               "init_command": "SET default_storage_engine=INNODB",
        }
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_URL = '/Aurora/static/'

MEDIA_ROOT = '/var/www/Aurora/cloud/'

AUTHENTICATION_BACKENDS = (
    #'social_core.backends.open_id.OpenIdAuth',
    #'social_core.backends.google.GoogleOpenId',
    'social_core.backends.google.GoogleOAuth2',
    #'social_core.backends.google.GoogleOAuth',
    #'social_core.backends.twitter.TwitterOAuth',
    #'social_core.backends.yahoo.YahooOpenId',

    'django.contrib.auth.backends.ModelBackend',
)

# URL to redirect user to login
LOGIN_URL = '/Aurora/accounts/login/'
LOGIN_REDIRECT_URL = '/Aurora/'
LOGIN_ERROR_URL = '/Aurora/accounts/login-error/'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': '/var/www/Aurora/logs/main.log',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
        'cloud': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d ' +
                '%(thread)d: %(message)s'
        },
        'simple': {
            'format': '%(levelname)s: %(message)s'
        },
    },
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'aurora_cache',
        #'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        #'LOCATION': 'unix:/tmp/memcached.sock',
        #'LOCATION': '127.0.0.1:11211',
    }
}

# SDN Controller IP address
# Network reachable IP address (usually not 127.0.0.1) so other switches can connect remotelly to your controller
# Currently works with floodlight 0.90
SDN_CONTROLLER = {
    'type': 'floodlight',
    'transport': 'tcp',
    'ip': '127.0.0.1',
    'port': 6633,
}

# Path to store images in remote hosts
REMOTE_IMAGE_PATH = '/'

# Override default settings locally
try:
    from local_settings import *
except ImportError as e:
    pass

