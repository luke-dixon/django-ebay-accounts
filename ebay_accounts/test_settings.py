# -*- coding: utf-8 -*-
"""
Test Settings
"""
from __future__ import unicode_literals
import os


APP_NAME = 'ebay_accounts'

TEST_RUNNER = 'discover_runner.DiscoverRunner'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'discover_runner',
    'ebay_accounts',
    'south',
)
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
EBAY_SANDBOX_DEVID = os.environ['EBAY_SANDBOX_DEVID']
EBAY_SANDBOX_APPID = os.environ['EBAY_SANDBOX_APPID']
EBAY_SANDBOX_CERTID = os.environ['EBAY_SANDBOX_CERTID']
EBAY_PRODUCTION_DEVID = ''
EBAY_PRODUCTION_APPID = ''
EBAY_PRODUCTION_CERTID = ''
EBAY_SANDBOX_RU_NAME = os.environ['EBAY_SANDBOX_RU_NAME']
EBAY_PRODUCTION_RU_NAME = ''

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4 fileencoding=utf-8
