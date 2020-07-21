# -*- coding: utf-8 -*-
"""
Ebay Accounts Views
"""
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect
from django.views.generic import (
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
    ListView,
    View,
    TemplateView,
)
from django.views.generic.detail import SingleObjectMixin

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from .models import Account, Session
from .forms import BeginAccountCreationForm


APP_NAME = 'ebay_accounts'


class AccountBeginCreateView(
        LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """
    View for beginning the account creation process

    Gets a session_id from Ebay and redirects to the sign-in URL
    """
    form_class = BeginAccountCreationForm
    permission_required = APP_NAME + '.add_account'
    template_name = APP_NAME + '/account_begin_create_form.html'

    def get_success_url(self):
        self.object.set_session_id()
        return self.object.get_sign_in_url()


class AccountRejectCreateView(
        LoginRequiredMixin, PermissionRequiredMixin, SingleObjectMixin, View):
    """
    View for rejecting the account creation process

    Ebay redirects to this view when the user rejects the authorization
    process.
    """
    model = Session
    permission_required = APP_NAME + '.add_account'

    def get_object(self, uuid):
        return self.get_queryset().get(uuid=uuid)

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(uuid=request.GET['UUID'])
        self.object.reject()
        return redirect(reverse(APP_NAME + '_account_list'))


class AccountFinishCreateView(
        LoginRequiredMixin, PermissionRequiredMixin, SingleObjectMixin, View):
    """
    View for finishing the account creation process

    Ebay redirects to this view when the user accepts the authorization
    process.
    """
    model = Session
    permission_required = APP_NAME + '.add_account'

    def get_object(self, uuid):
        return self.get_queryset().get(uuid=uuid)

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(uuid=request.GET['UUID'])
        account = self.object.create_account()
        return redirect(account.get_absolute_url())


class AccountDetailView(
        LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    """
    View for viewing a ``Account`` object
    """
    model = Account
    permission_required = APP_NAME + '.view_account'


class AccountUpdateView(
        LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """
    View for updating a ``Account`` object
    """
    model = Account
    permission_required = APP_NAME + '.change_account'


class AccountDeleteView(
        LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """
    View for deleting a ``Account`` object
    """
    model = Account
    permission_required = APP_NAME + '.delete_account'
    success_url = reverse_lazy(APP_NAME + '_account_list')


class AccountListView(
        LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Account
    permission_required = APP_NAME + '.view_account'


class PrivacyPolicyView(
        LoginRequiredMixin, PermissionRequiredMixin, TemplateView):
    permission_required = APP_NAME + '.view_account'
    template_name = 'ebay_accounts/privacy_policy.html'

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4 fileencoding=utf-8
