# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-19 06:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caralibroapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poke',
            name='pokee',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='poke',
            name='poker',
            field=models.IntegerField(),
        ),
    ]