# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-07 03:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_productcategory_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image1',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]