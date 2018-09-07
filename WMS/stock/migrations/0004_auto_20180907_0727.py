# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-07 01:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0003_auto_20180907_0726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='create_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p_cr', to='stock.UserProfile'),
        ),
        migrations.AlterField(
            model_name='product',
            name='delete_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p_de', to='stock.UserProfile'),
        ),
        migrations.AlterField(
            model_name='product',
            name='update_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p_up', to='stock.UserProfile'),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='create_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pc_cr', to='stock.UserProfile'),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='delete_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pc_de', to='stock.UserProfile'),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='update_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pc_up', to='stock.UserProfile'),
        ),
        migrations.AlterField(
            model_name='stockoperations',
            name='create_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='so_cr', to='stock.UserProfile'),
        ),
        migrations.AlterField(
            model_name='stockoperations',
            name='delete_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='so_del', to='stock.UserProfile'),
        ),
        migrations.AlterField(
            model_name='stockoperations',
            name='update_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='so_up', to='stock.UserProfile'),
        ),
    ]
