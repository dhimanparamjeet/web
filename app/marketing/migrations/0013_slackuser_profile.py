# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-02 04:35
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0012_slackuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='slackuser',
            name='profile',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={}),
        ),
    ]