# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-23 04:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('caralibroapp', '0003_auto_20160822_2114'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='last_name',
            new_name='alias',
        ),
    ]
