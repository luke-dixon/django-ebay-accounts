# -*- coding: utf-8 -*-
"""
Ebay Accounts Tests Views
"""
import os
from datetime import datetime, timedelta
from unittest.mock import patch, Mock
from urllib.parse import urlparse, parse_qs

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.urls import reverse
from django.utils import timezone
from django.utils.timezone import now, utc
from django.test import TestCase

from ..forms import BeginAccountCreationForm
from ..models import Account, Session
from .. import app_settings as settings


APP_NAME = 'ebay_accounts'


class LoginTestMixin(object):
    user = None
    user_permissions = None
    username = 'testuser'
    email = 'testuser@example.com'
    password = 'testpw'

    def add_permissions_to_user(self, permissions):
        for permission in permissions:
            app_label, codename = permission.split('.')
            permission = Permission.objects.get(
                codename=codename, content_type__app_label=app_label)
            self.user.user_permissions.add(permission)

    def create_user(self):
        User = get_user_model()
        self.user = User.objects.create_user(
            self.username, self.email, self.password)
        self.user.is_active = True
        self.user.save()
        if self.user_permissions:
            self.add_permissions_to_user(self.user_permissions)

    def login(self):
        if not self.user:
            self.create_user()
        login_successful = self.client.login(
            username=self.username, password=self.password)
        self.assertTrue(self.user.is_active)
        self.assertTrue(login_successful)


class AccountListView(LoginTestMixin, TestCase):
    """
    Tests for the ``AccountListView`` view
    """
    user_permissions = (APP_NAME + '.view_account', )

    def test_get_none(self):
        self.login()
        response = self.client.get(reverse(APP_NAME + '_account_list'))
        self.assertEqual(response.status_code, 200)

        # Check that the context has no ``Account`` objects
        self.assertEqual(len(response.context['object_list']), 0)
        self.assertEqual(len(response.context['account_list']), 0)

    def test_get(self):
        account = Account.objects.create(
            user_id='test_user',
            expires=now(),
            token='12345',
            site_id=0,
        )

        self.login()
        response = self.client.get(reverse(APP_NAME + '_account_list'))
        self.assertEqual(response.status_code, 200)

        # Check that the context has the ``account`` object
        self.assertIn(account, response.context['object_list'])
        self.assertIn(account, response.context['account_list'])


class AccountBeginCreateViewTest(LoginTestMixin, TestCase):
    """
    Tests for the ``AccountBeginCreateView`` view
    """
    user_permissions = (APP_NAME + '.add_account', )

    def test_get(self):
        self.login()
        response = self.client.get(reverse(APP_NAME + '_account_begin_create'))
        self.assertEqual(response.status_code, 200)

        # Check we get the right form
        self.assertIsInstance(
            response.context['form'], BeginAccountCreationForm)

    def test_post(self):
        self.login()

        # Setup mock for the GetSessionID call
        folder = os.path.join(os.path.dirname(__file__), 'xml')
        side_effect = []

        filename = os.path.join(folder, 'GetSessionID1.xml')
        with open(filename) as f:
            side_effect.append(Mock(content=f.read()))

        with patch(APP_NAME + '.trading_api.requests') as m:
            m.post.side_effect = side_effect

            kw = {
                'site_id': 0,
            }
            response = self.client.post(
                reverse(APP_NAME + '_account_begin_create'), kw)

            m.post.assert_called_once_with(
                settings.EBAY_SANDBOX_TRADING_API_ENDPOINT,
                data="""\
<?xml version="1.0" encoding="utf-8"?>
<GetSessionIDRequest xmlns="urn:ebay:apis:eBLBaseComponents"><RuName>{ru_name}</RuName></GetSessionIDRequest>""".format(
                    ru_name=settings.EBAY_SANDBOX_RU_NAME,
                ),
                headers={
                    'X-EBAY-API-COMPATIBILITY-LEVEL': '{0}'.format(
                        settings.EBAY_TRADING_API_VERSION
                    ),
                    'X-EBAY-API-DEV-NAME': settings.EBAY_SANDBOX_DEVID,
                    'X-EBAY-API-APP-NAME': settings.EBAY_SANDBOX_APPID,
                    'X-EBAY-API-CERT-NAME': settings.EBAY_SANDBOX_CERTID,
                    'X-EBAY-API-SITEID': '0',
                    'X-EBAY-API-CALL-NAME': 'GetSessionID',
                }
            )

        # Get the created session
        session = Session.objects.all()[0]

        # Check that we generated a UUID for this account
        uuid = session.uuid
        self.assertEqual(len(uuid), 32)

        # Check that we got a session id
        session_id = session.session_id
        self.assertEqual(len(session_id), 40)
        # We actually know what the session id is because we used mock
        self.assertEqual(
            session_id, 'a11AAA**a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1')

        # Check that we would get redirected to the ebay sign-in URL
        self.assertEqual(response.status_code, 302)
        url = urlparse(response['Location'])
        self.assertEqual(url.scheme, 'https')
        self.assertEqual(url.netloc, 'signin.sandbox.ebay.com')
        self.assertEqual(url.path, '/ws/eBayISAPI.dll')
        query = parse_qs(url.query)
        self.assertListEqual(query['RuName'], [settings.EBAY_SANDBOX_RU_NAME])
        self.assertListEqual(query['SessID'], [session_id])
        self.assertListEqual(query['ruparams'], ['UUID={0}'.format(uuid)])


class AccountRejectCreateViewTest(LoginTestMixin, TestCase):
    """
    Tests for the ``AccountRejectCreateView`` view
    """
    user_permissions = (
        APP_NAME + '.add_account',
        APP_NAME + '.view_account',
    )

    def test_get(self):
        session = Session.objects.create(
            session_id='test-session-id', site_id=0)

        self.login()
        response = self.client.get(
            reverse(APP_NAME + '_account_reject_create'),
            data={'UUID': session.uuid},
            follow=True)

        # Check that we get redirected to the list view
        self.assertRedirects(response, reverse(APP_NAME + '_account_list'))

        # Check that the session got deleted
        self.assertRaises(
            Session.DoesNotExist, Session.objects.get, pk=session.pk)


class AccountFinishCreateViewTest(LoginTestMixin, TestCase):
    """
    Tests for the ``AccountFinishCreateView`` view
    """
    user_permissions = (
        APP_NAME + '.add_account',
        APP_NAME + '.view_account',
    )

    def test_get(self):
        # The session that we are going to finish and turn into an account
        session = Session.objects.create(
            session_id='test-session-id', site_id=0)

        self.login()

        # We don't want to actually contact Ebay as we don't have an actual
        # session id to use so we'll mock the call that is made
        folder = os.path.join(os.path.dirname(__file__), 'xml')
        side_effect = []

        filename = os.path.join(folder, 'FetchToken1.xml')
        with open(filename) as f:
            side_effect.append(Mock(content=f.read()))

        filename = os.path.join(folder, 'GetUser1.xml')
        with open(filename) as f:
            side_effect.append(Mock(content=f.read()))

        with patch(APP_NAME + '.trading_api.requests') as m:
            m.post.side_effect = side_effect
            response = self.client.get(
                reverse(APP_NAME + '_account_finish_create'),
                data={'UUID': session.uuid},
                follow=True)

        account = Account.objects.first()

        # Check that we get redirected to newly created account detail view
        self.assertRedirects(response, account.get_absolute_url())

        # Check the expiry date for the token
        self.assertEqual(
            account.expires,
            datetime(2014, 7, 12, 21, 21, 36, tzinfo=utc)
        )

        self.assertFalse(account.production)

        # active will be false as the expires timestamp is in the past
        self.assertFalse(account.is_active())

        account.expires = timezone.now() + timedelta(days=3)
        self.assertTrue(account.is_active())

        account.active = False
        self.assertFalse(account.is_active())

        account.active = True
        account.token = ''
        self.assertFalse(account.is_active())


class AccountUpdateViewTest(LoginTestMixin, TestCase):
    """
    Tests for the ``AccountUpdateView`` view
    """
    user_permissions = (
        APP_NAME + '.view_account',
        APP_NAME + '.change_account',
    )

    def test_get(self):
        account = Account.objects.create(
            user_id='test_user',
            expires=now(),
            token='12345',
            site_id=0,
        )

        self.login()

        response = self.client.get(
            reverse(APP_NAME + '_account_update', kwargs={'pk': account.pk})
        )

        # Check we get a successful status code from the response
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        account = Account.objects.create(
            user_id='test_user',
            expires=now(),
            token='12345',
            site_id=0,
        )

        self.assertTrue(account.active)

        self.login()

        response = self.client.post(
            reverse(APP_NAME + '_account_update', kwargs={'pk': account.pk}),
            data={'status': False},
            follow=True,
        )

        # Check we get a successful status code from the response
        self.assertEqual(response.status_code, 200)

        # Check that the account instance was updated
        account.refresh_from_db()
        self.assertFalse(account.active)


class AccountDeleteViewTest(LoginTestMixin, TestCase):
    """
    Tests for the ``AccountDeleteView`` view
    """
    user_permissions = (
        APP_NAME + '.view_account',
        APP_NAME + '.delete_account',
    )

    def test_get(self):
        account = Account.objects.create(
            user_id='test_user',
            expires=now(),
            token='12345',
            site_id=0,
        )

        self.login()

        response = self.client.get(
            reverse(APP_NAME + '_account_delete', kwargs={'pk': account.pk})
        )

        # Check we get a successful status code from the response
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        account = Account.objects.create(
            user_id='test_user',
            expires=now(),
            token='12345',
            site_id=0,
        )

        self.assertTrue(account.active)

        self.login()

        response = self.client.post(
            reverse(APP_NAME + '_account_delete', kwargs={'pk': account.pk}),
            follow=True,
        )

        # Check we get a successful status code from the response
        self.assertEqual(response.status_code, 200)

        # Check that the account instance was
        with self.assertRaises(Account.DoesNotExist):
            account.refresh_from_db()


class PrivacyPolicyViewTest(LoginTestMixin, TestCase):
    """
    Tests for the ``PrivacyPolicyView`` view
    """
    user_permissions = (
        APP_NAME + '.view_account',
    )

    def test_get(self):
        self.login()

        response = self.client.get(reverse(APP_NAME + '_privacy_policy'))

        # Check we get a successful status code from the response
        self.assertEqual(response.status_code, 200)

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4 fileencoding=utf-8
