# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Tracker(models.Model):
	hostname = models.CharField(max_length=250)
	request_url = models.CharField(max_length=1000)
	response_statu_code=models.IntegerField()
	user = models.ForeignKey(User, blank=True)


class BaseAbstractModel(models.Model):
	name=models.CharField(max_length=250)
	desc=models.TextField(blank=True)
	status = models.BooleanField(default=True)
	create_date = models.DateTimeField(auto_now_add=True)
	update_date = models.DateTimeField(blank=True, null=True)
	delete_date = models.DateTimeField(blank=True, null=True)
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

	def __str__(self):
		return self.user.username



# Create your models here.
# create table productcategory(id int primarykey, name varchar(250))
class ProductCategory(BaseAbstractModel):
	#pk_id=models.IntegerField(primary_key=True)
	unique_name = models.CharField(max_length=250, unique=True)
	create_user = models.ForeignKey(UserProfile, 
		related_name ="pc_cr",blank=True, null=True, on_delete = models.PROTECT)
	update_user = models.ForeignKey(UserProfile, related_name ="pc_up",
		blank=True, null=True, on_delete = models.PROTECT)
	delete_user = models.ForeignKey(UserProfile, related_name ="pc_de",
		blank=True, null=True, on_delete = models.PROTECT)
	image = models.FileField(blank=True)
	class Meta:
		db_table="productcategory"
		
	def __str__(self):
		return self.name

class Product(BaseAbstractModel):
	category = models.ForeignKey(ProductCategory, 
		on_delete = models.PROTECT)
	charge_day = models.IntegerField()
	create_user = models.ForeignKey(UserProfile, related_name ="p_cr",
		blank=True, null=True, on_delete = models.PROTECT)
	update_user = models.ForeignKey(UserProfile, related_name ="p_up",
		blank=True, null=True, on_delete = models.PROTECT)
	delete_user = models.ForeignKey(UserProfile, related_name ="p_de",
		blank=True, null=True,on_delete = models.PROTECT)
	class Meta:
		db_table="product"
	image1 = models.FileField(blank=True)
	image2 = models.ImageField(blank=True)
	def __str__(self):
		return "%s--%s--%s"%(self.name,self.charge_day,self.category)

# class UserProfile(User):
# 	roles = [('v','vendor'),('m',"manager")]
# 	address = models.TextField()
# 	phone = models.CharField(max_length=15)
# 	role = models.CharField(choices=roles, max_length=2)

class LineItem(BaseAbstractModel):
	product = models.ForeignKey(Product, on_delete = models.PROTECT)
	count = models.IntegerField()


class StockOperations(BaseAbstractModel):
	#products = models.ManyToManyField(Product)
	types = [("i","in"),("o","out")]
	vendor = models.ForeignKey(UserProfile, on_delete = models.PROTECT)
	create_user = models.ForeignKey(UserProfile, related_name ="so_cr",
		blank=True, null=True, on_delete = models.PROTECT)
	update_user = models.ForeignKey(UserProfile, related_name ="so_up",
		blank=True, null=True, on_delete = models.PROTECT)
	delete_user = models.ForeignKey(UserProfile, related_name ="so_del",
		blank=True, null=True, on_delete = models.PROTECT)
	lineitems = models.ManyToManyField(LineItem)
	operation_type = models.CharField(max_length=3,choices=types)
	class Meta:
		db_table="stockoperation"






