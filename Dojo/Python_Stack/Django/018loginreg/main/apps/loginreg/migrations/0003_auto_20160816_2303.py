# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-17 06:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginreg', '0002_auto_20160816_2256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlog',
            name='birthday',
            field=models.DateField(null=True),
        ),
    ]
