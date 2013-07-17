# -*- coding: utf-8 -*-
"""
Ebay Account Settings
"""
from __future__ import unicode_literals

from django.conf import settings

from django.utils.translation import ugettext as _


#: Ebay Sandbox DevID
EBAY_SANDBOX_DEVID = settings.EBAY_SANDBOX_DEVID
#: Ebay Sandbox AppID
EBAY_SANDBOX_APPID = settings.EBAY_SANDBOX_APPID
#: Ebay Sandbox CertID
EBAY_SANDBOX_CERTID = settings.EBAY_SANDBOX_CERTID

#: Ebay Production DevID
EBAY_PRODUCTION_DEVID = settings.EBAY_PRODUCTION_DEVID
#: Ebay Production AppID
EBAY_PRODUCTION_APPID = settings.EBAY_PRODUCTION_APPID
#: Ebay Production CertID
EBAY_PRODUCTION_CERTID = settings.EBAY_PRODUCTION_CERTID

#: The version of the Ebay Trading API to use
EBAY_TRADING_API_VERSION = getattr(settings, 'EBAY_TRADING_API_VERSION', 829)

#: The Ebay SiteID to use (defaults to 0 (US))
EBAY_SITEID = getattr(settings, 'EBAY_SITEID', '0')

#: Your RuName for the Ebay Sandbox
EBAY_SANDBOX_RU_NAME = settings.EBAY_SANDBOX_RU_NAME
#: Your RuName for Ebay
EBAY_PRODUCTION_RU_NAME = settings.EBAY_PRODUCTION_RU_NAME

#: The template to use for generating the sign-in URL for the Ebay Sandbox
EBAY_SANDBOX_TOKEN_SIGNIN_URL_TEMPLATE = getattr(
    settings,
    'EBAY_SANDBOX_TOKEN_SIGNIN_URL_TEMPLATE',
    'https://signin.sandbox.ebay.com/ws/eBayISAPI.dll?'
    'SignIn&{params}'
)
#: The template to use for generating the sign-in URL for Ebay
EBAY_PRODUCTION_TOKEN_SIGNIN_URL_TEMPLATE = getattr(
    settings,
    'EBAY_PRODUCTION_TOKEN_SIGNIN_URL_TEMPLATE',
    'https://signin.ebay.com/ws/eBayISAPI.dll?'
    'SignIn&{params}'
)

#: Ebay Sandbox Trading API Endpoint
EBAY_SANDBOX_TRADING_API_ENDPOINT = getattr(
    settings,
    'EBAY_SANDBOX_TRADING_API_ENDPOINT',
    'https://api.sandbox.ebay.com/ws/api.dll')
#: Ebay Production Trading API Endpoint
EBAY_PRODUCTION_TRADING_API_ENDPOINT = getattr(
    settings,
    'EBAY_PRODUCTION_TRADING_API_ENDPOINT',
    'https://api.sandbox.ebay.com/ws/api.dll')

#: Ebay Site Choices
EBAY_SITE_CHOICES = (
    (0, _('United States')),
    (2, _('Canada')),
    (3, _('United Kingdom')),
    (15, _('Australia')),
    (16, _('Austria')),
    (23, _('Belgium (French)')),
    (71, _('France')),
    (77, _('Germany')),
    (100, _('eBay Motors')),
    (101, _('Italy')),
    (123, _('Belgium (Dutch)')),
    (146, _('Netherlands')),
    (186, _('Spain')),
    (193, _('Switzerland')),
    (196, _('Taiwan')),
    (201, _('Hong Kong')),
    (203, _('India')),
    (205, _('Ireland')),
    (207, _('Malaysia')),
    (210, _('Canada')),
    (211, _('Philippines')),
    (212, _('Poland')),
    (216, _('Singapore')),
    (218, _('Sweden')),
    (223, _('China')),
)

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4 fileencoding=utf-8
