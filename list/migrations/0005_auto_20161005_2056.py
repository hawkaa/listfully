# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-05 20:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('list', '0004_auto_20161003_2343'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='list',
            name='user_id',
        ),
        migrations.AddField(
            model_name='list',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
