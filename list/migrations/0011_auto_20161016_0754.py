# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-16 07:54
from __future__ import unicode_literals

from django.db import migrations, models
import list.models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0010_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(default='default.svg', upload_to=list.models.item_image_path),
        ),
    ]
