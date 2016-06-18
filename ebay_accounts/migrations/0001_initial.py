# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ebay_accounts.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.CharField(max_length=255)),
                ('expires', models.DateTimeField()),
                ('token', models.TextField()),
                ('production', models.BooleanField(default=False)),
                ('site_id', models.IntegerField(choices=[(0, 'United States'), (2, 'Canada'), (3, 'United Kingdom'), (15, 'Australia'), (16, 'Austria'), (23, 'Belgium (French)'), (71, 'France'), (77, 'Germany'), (100, 'eBay Motors'), (101, 'Italy'), (123, 'Belgium (Dutch)'), (146, 'Netherlands'), (186, 'Spain'), (193, 'Switzerland'), (196, 'Taiwan'), (201, 'Hong Kong'), (203, 'India'), (205, 'Ireland'), (207, 'Malaysia'), (210, 'Canada'), (211, 'Philippines'), (212, 'Poland'), (216, 'Singapore'), (218, 'Sweden'), (223, 'China')])),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'permissions': (('view_account', 'Can view account'),),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('session_id', models.CharField(max_length=40, blank=True)),
                ('uuid', models.CharField(default=ebay_accounts.models.gen_uuid_hex, unique=True, max_length=32)),
                ('production', models.BooleanField(default=False)),
                ('site_id', models.IntegerField(choices=[(0, 'United States'), (2, 'Canada'), (3, 'United Kingdom'), (15, 'Australia'), (16, 'Austria'), (23, 'Belgium (French)'), (71, 'France'), (77, 'Germany'), (100, 'eBay Motors'), (101, 'Italy'), (123, 'Belgium (Dutch)'), (146, 'Netherlands'), (186, 'Spain'), (193, 'Switzerland'), (196, 'Taiwan'), (201, 'Hong Kong'), (203, 'India'), (205, 'Ireland'), (207, 'Malaysia'), (210, 'Canada'), (211, 'Philippines'), (212, 'Poland'), (216, 'Singapore'), (218, 'Sweden'), (223, 'China')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
