# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-30 21:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0015_auto_20161030_2033'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='bought',
            field=models.BooleanField(default=False),
        ),
    ]
