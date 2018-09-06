# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class BaseAbstractModel(models.Model):
	name=models.CharField(max_length=250)
	desc=models.TextField(blank=True)
	status = models.BooleanField(default=True)
	create_date = models.DateTimeField(auto_now_add=True)
	update_date = models.DateTimeField(blank=True)
	delete_date = models.DateTimeField(blank=True)
	class Meta:
		abstract=True

class UserProfile(models.Model):
	roles = [('v','vendor'),('m',"manager")]
	address = models.TextField()
	phone = models.CharField(max_length=15)
	role = models.CharField(choices=roles, max_length=2, default='v')
	user = models.OneToOneField(User)
	class Meta:
		db_table="userprofile"


# Create your models here.
# create table productcategory(id int primarykey, name varchar(250))
class ProductCategory(BaseAbstractModel):
	#pk_id=models.IntegerField(primary_key=True)
	create_user = models.ForeignKey(UserProfile, related_name ="pc_cr")
	update_user = models.ForeignKey(UserProfile, related_name ="pc_up")
	delete_user = models.ForeignKey(UserProfile, related_name ="pc_de")



	class Meta:
		db_table="productcategory"

class Product(BaseAbstractModel):
	category = models.ForeignKey(ProductCategory)
	charge_day = models.IntegerField()
	create_user = models.ForeignKey(UserProfile, related_name ="p_cr")
	update_user = models.ForeignKey(UserProfile, related_name ="p_up")
	delete_user = models.ForeignKey(UserProfile, related_name ="p_de")
	class Meta:
		db_table="product"

# class UserProfile(User):
# 	roles = [('v','vendor'),('m',"manager")]
# 	address = models.TextField()
# 	phone = models.CharField(max_length=15)
# 	role = models.CharField(choices=roles, max_length=2)


class StockOperations(BaseAbstractModel):
	products = models.ManyToManyField(Product)
	vendor = models.ForeignKey(UserProfile)
	create_user = models.ForeignKey(UserProfile, related_name ="so_cr")
	update_user = models.ForeignKey(UserProfile, related_name ="so_up")
	delete_user = models.ForeignKey(UserProfile, related_name ="so_del")
	class Meta:
		db_table="stockoperation"




