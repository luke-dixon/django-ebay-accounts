# -*- coding: utf-8 -*-
"""
Test Settings
"""
import django


APP_NAME = 'ebay_accounts'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'ebay_accounts',
)

MIDDLEWARE = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

if django.VERSION[:2] >= (1, 8):
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [
            ],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
    },
}
SECRET_KEY = '^&*TESTING123^&*'
ROOT_URLCONF = APP_NAME + '.urls'
USE_TZ = True
LOGGING = {
    'version': 1,
    'formatters': {
        'simple': {
            'format': '%(levelname)s %(module)s: %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        }
    },
    'loggers': {
        'ebay_accounts': {
            'handlers': ['console'],
            'level': 'DEBUG',
        }
    }
}
EBAY_SANDBOX_DEVID = ''
EBAY_SANDBOX_APPID = ''
EBAY_SANDBOX_CERTID = ''
EBAY_SANDBOX_RU_NAME = 'TEST_SANDBOX_RU_NAME'
EBAY_PRODUCTION_DEVID = ''
EBAY_PRODUCTION_APPID = ''
EBAY_PRODUCTION_CERTID = ''
EBAY_PRODUCTION_RU_NAME = 'TEST_PRODUCTION_RU_NAME'

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4 fileencoding=utf-8
