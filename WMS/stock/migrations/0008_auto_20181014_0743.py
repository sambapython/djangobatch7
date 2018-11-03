# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-14 02:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0007_tracker_hostname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracker',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]