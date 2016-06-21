# -*- coding: utf-8 -*-
"""
Ebay Accounts URLs
"""
from __future__ import unicode_literals

from django.conf.urls import patterns, url

from . import views

APP_NAME = 'ebay_accounts'


# pylint: disable=E1120
urlpatterns = [
    url(
        r'^$',
        views.AccountListView.as_view(),
        name=APP_NAME + '_account_list',
    ),
    url(
        r'^begin_create$',
        views.AccountBeginCreateView.as_view(),
        name=APP_NAME + '_account_begin_create',
    ),
    url(
        r'^reject_create$',
        views.AccountRejectCreateView.as_view(),
        name=APP_NAME + '_account_reject_create',
    ),
    url(
        r'^finish_create$',
        views.AccountFinishCreateView.as_view(),
        name=APP_NAME + '_account_finish_create',
    ),
    url(
        r'^privacy_policy$',
        views.PrivacyPolicyView.as_view(),
        name=APP_NAME + '_privacy_policy',
    ),
    url(
        r'^(?P<pk>\d+)/$',
        views.AccountDetailView.as_view(),
        name=APP_NAME + '_account_detail',
    ),
    url(
        r'^(?P<pk>\d+)/update$',
        views.AccountUpdateView.as_view(),
        name=APP_NAME + '_account_update',
    ),
    url(
        r'^(?P<pk>\d+)/delete$',
        views.AccountDeleteView.as_view(),
        name=APP_NAME + '_account_delete',
    ),
    url(
        r'^(?P<pk>\d+)/revoke_token',
        views.AccountRevokeTokenView.as_view(),
        name=APP_NAME + '_account_revoke_token',
    ),
]
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4 fileencoding=utf-8
