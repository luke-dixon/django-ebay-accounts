# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Account'
        db.create_table(u'ebay_accounts_account', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_id', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('expires', self.gf('django.db.models.fields.DateTimeField')()),
            ('token', self.gf('django.db.models.fields.TextField')()),
            ('production', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('site_id', self.gf('django.db.models.fields.IntegerField')()),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'ebay_accounts', ['Account'])

        # Adding model 'Session'
        db.create_table(u'ebay_accounts_session', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('session_id', self.gf('django.db.models.fields.CharField')(max_length=40, blank=True)),
            ('uuid', self.gf('django.db.models.fields.CharField')(default='6bf2635f5b4a4b5282a3f314959b2e2e', unique=True, max_length=32)),
            ('production', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('site_id', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'ebay_accounts', ['Session'])


    def backwards(self, orm):
        # Deleting model 'Account'
        db.delete_table(u'ebay_accounts_account')

        # Deleting model 'Session'
        db.delete_table(u'ebay_accounts_session')


    models = {
        u'ebay_accounts.account': {
            'Meta': {'object_name': 'Account'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'expires': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'production': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'site_id': ('django.db.models.fields.IntegerField', [], {}),
            'token': ('django.db.models.fields.TextField', [], {}),
            'user_id': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'ebay_accounts.session': {
            'Meta': {'object_name': 'Session'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'production': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'session_id': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'site_id': ('django.db.models.fields.IntegerField', [], {}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'6d20268e11564342bb0fd10fc12f0773'", 'unique': 'True', 'max_length': '32'})
        }
    }

    complete_apps = ['ebay_accounts']