# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-12 02:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orm', '0002_auto_20160811_1928'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comments',
            new_name='comment',
        ),
    ]