# -*- coding: utf-8 -*-
"""
Ebay Accounts Forms
"""
from __future__ import unicode_literals

from django import forms

from .models import Session

class BeginAccountCreationForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = ('production', 'site_id')

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4 fileencoding=utf-8
