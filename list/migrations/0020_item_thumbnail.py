# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-11 21:49
from __future__ import unicode_literals

from django.db import migrations, models
import list.models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0019_auto_20161109_2351'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to=list.models.item_image_path),
        ),
    ]
