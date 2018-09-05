# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class WareHouse(models.Model):
	name=models.CharField(max_length=250)
	class Meta:
		db_table="warehouse1"
class Product(models.Model):
	name=models.CharField(max_length=250)
	class Meta:
		db_table="product"
