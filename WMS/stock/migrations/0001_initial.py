# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-30 02:07
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LineItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('desc', models.TextField(blank=True)),
                ('status', models.BooleanField(default=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
                ('delete_date', models.DateTimeField(blank=True, null=True)),
                ('count', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('desc', models.TextField(blank=True)),
                ('status', models.BooleanField(default=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
                ('delete_date', models.DateTimeField(blank=True, null=True)),
                ('charge_day', models.IntegerField()),
            ],
            options={
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('desc', models.TextField(blank=True)),
                ('status', models.BooleanField(default=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
                ('delete_date', models.DateTimeField(blank=True, null=True)),
                ('unique_name', models.CharField(max_length=250, unique=True)),
            ],
            options={
                'db_table': 'productcategory',
            },
        ),
        migrations.CreateModel(
            name='StockOperations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('desc', models.TextField(blank=True)),
                ('status', models.BooleanField(default=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
                ('delete_date', models.DateTimeField(blank=True, null=True)),
                ('operation_type', models.CharField(choices=[('i', 'in'), ('o', 'out')], max_length=3)),
            ],
            options={
                'db_table': 'stockoperation',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('phone', models.CharField(max_length=15)),
                ('role', models.CharField(choices=[('v', 'vendor'), ('m', 'manager')], default='v', max_length=2)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'userprofile',
            },
        ),
        migrations.AddField(
            model_name='stockoperations',
            name='create_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='so_cr', to='stock.UserProfile'),
        ),
        migrations.AddField(
            model_name='stockoperations',
            name='delete_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='so_del', to='stock.UserProfile'),
        ),
        migrations.AddField(
            model_name='stockoperations',
            name='lineitems',
            field=models.ManyToManyField(to='stock.LineItem'),
        ),
        migrations.AddField(
            model_name='stockoperations',
            name='update_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='so_up', to='stock.UserProfile'),
        ),
        migrations.AddField(
            model_name='stockoperations',
            name='vendor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='stock.UserProfile'),
        ),
        migrations.AddField(
            model_name='productcategory',
            name='create_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='pc_cr', to='stock.UserProfile'),
        ),
        migrations.AddField(
            model_name='productcategory',
            name='delete_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='pc_de', to='stock.UserProfile'),
        ),
        migrations.AddField(
            model_name='productcategory',
            name='update_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='pc_up', to='stock.UserProfile'),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='stock.ProductCategory'),
        ),
        migrations.AddField(
            model_name='product',
            name='create_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='p_cr', to='stock.UserProfile'),
        ),
        migrations.AddField(
            model_name='product',
            name='delete_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='p_de', to='stock.UserProfile'),
        ),
        migrations.AddField(
            model_name='product',
            name='update_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='p_up', to='stock.UserProfile'),
        ),
        migrations.AddField(
            model_name='lineitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='stock.Product'),
        ),
    ]
