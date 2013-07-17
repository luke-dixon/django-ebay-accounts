# -*- coding: utf-8 -*-
"""
Ebay Accounts URLs
"""
from __future__ import unicode_literals

from django.conf.urls import patterns, url

from .views import (
    AccountListView,
    AccountBeginCreateView,
    AccountRejectCreateView,
    AccountFinishCreateView,
    AccountCreateView,
    AccountDetailView,
    AccountUpdateView,
    AccountDeleteView,
    PrivacyPolicyView,
)

APP_NAME = 'ebay_accounts'


# pylint: disable=E1120
urlpatterns = patterns(
    'ebay_accounts.views',
    url(
        r'^$',
        AccountListView.as_view(),
        name=APP_NAME + '_account_list',
    ),
    url(
        r'^begin_create$',
        AccountBeginCreateView.as_view(),
        name=APP_NAME + '_account_begin_create',
    ),
    url(
        r'^reject_create$',
        AccountRejectCreateView.as_view(),
        name=APP_NAME + '_account_reject_create',
    ),
    url(
        r'^finish_create$',
        AccountFinishCreateView.as_view(),
        name=APP_NAME + '_account_finish_create',
    ),
    url(
        r'^privacy_policy$',
        PrivacyPolicyView.as_view(),
        name=APP_NAME + '_privacy_policy',
    ),
    url(
        r'^(?P<pk>\d+)/$',
        AccountDetailView.as_view(),
        name=APP_NAME + '_account_detail',
    ),
    url(
        r'^(?P<pk>\d+)/update$',
        AccountUpdateView.as_view(),
        name=APP_NAME + '_account_update',
    ),
    url(
        r'^(?P<pk>\d+)/delete$',
        AccountDeleteView.as_view(),
        name=APP_NAME + '_account_delete',
    ),
)
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4 fileencoding=utf-8
