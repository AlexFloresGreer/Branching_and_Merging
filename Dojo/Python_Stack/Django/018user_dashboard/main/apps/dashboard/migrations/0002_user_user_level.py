# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-17 23:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_level',
            field=models.CharField(default=0, max_length=2),
        ),
    ]
