# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# create table productcategory(id int primarykey, name varchar(250))
class ProductCategory(models.Model):
	#pk_id=models.IntegerField(primary_key=True)
	name=models.CharField(max_length=250)

	class Meta:
		db_table="productcategory"

class UserProfile(User):
	roles = [('v','vendor'),('m',"manager")]
	address = models.TextField()
	phone = models.CharField(max_length=15)
	role = models.CharField(choices=roles, max_length=2)

class UserProfile1(models.Model):
	roles = [('v','vendor'),('m',"manager")]
	address = models.TextField()
	phone = models.CharField(max_length=15)
	role = models.CharField(choices=roles, max_length=2)
	user = models.OneToOneField(User)



