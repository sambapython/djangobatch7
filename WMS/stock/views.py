# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os

from django.shortcuts import render, redirect
from stock.forms import UserProfileForm, UserProfileFormAll,\
StockOperationForm, ProductForm
from django.contrib.auth.models import User
from stock.models import StockOperations, ProductCategory,\
Product
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.paginator import Paginator
import time
from django.conf import settings
media_path = settings.MEDIA_ROOT

records_per_page=settings.RECORDS_PER_PAGE

def product_create_view(request):
	
	form = ProductForm()
	if request.method=="POST":
		# model form view code
		p = ProductForm(data=request.POST,
		 files=request.FILES)
		p.save()
		return  redirect("/products/")
		#BASIC VIEW CODE
		# data=request.POST
		# f1 = request.FILES.get("image1")
		# image_name = str(time.time())+f1.name
		# f=open(os.path.join(media_path,image_name),"wb")
		# for chunk in f1.chunks():
		# 	f.write(chunk)
		# f.close()
		# category=ProductCategory.objects.get(pk=data.get("category"))
		# p = Product(name=data.get("name"),
		# 	desc=data.get("desc"),
		# 	charge_day=data.get("charge_day"),
		# 	category=category,
		# 	image1=image_name)
		# p.save()
	return render(request, "stock/product_form.html",
		{"form":form})

def products_view(request):
	msg=""
	products = Product.objects.all()
	p = Paginator(products, records_per_page)
	page_num = request.GET.get("page", 1)
	try:
		required_page=p.page(page_num)
	except Exception as err:
		page_num=1
		msg=err.message
		required_page=p.page(page_num)
	msg = msg+ " Showing page:%s records"%page_num
	return render(request, "stock/product_list.html",
		{"object_list": required_page.object_list,
		"msg":msg,"page_num":page_num})
def checklogin(view_fun):
	def inner(request,*args, **kwargs):
		user_id = request.session.get('_auth_user_id')
		if not user_id:
			return redirect("/")
		else:
			return view_fun(request,*args, **kwargs)
	return inner


# Create your views here.
# def productcategories_view(request):
# 	data = ProductCategory.objects.all()
# 	return render(request, "stock/productcategories.html",
# 		"data":data)
# def index_view(request):
# 	return render(request,"stock/index.html")
def logout_view(request):
	#request.session=None
	logout(request)
	return redirect("/")

def login_view(request):
	next_url = request.GET.get("next","")
	message = ""
	if request.method=="POST":
		username = request.POST.get("username")
		password = request.POST.get("password")
		user = authenticate(username=username,
			password=password)
		if user:
			#request.session
			# request.session["user"]=user.username
			login(request, user)
			message="successfully logedin"
			if next_url:
				return redirect(next_url)
			return redirect("/index/")
		else:
			message = "wrong credentials"
	return render(request,"stock/login.html",{"message":message})
def home_view(request):
	return render(request,"stock/base.html") 

# def registration_view(request):
# 	print "*"*20
# 	# print "method=",request.method
# 	# print "get=",request.GET
# 	# print "post=",request.POST
# 	data = request.POST
# 	print data.get("user")
# 	print data.get("password")
# 	print "*"*20
# 	return render(request,"stock/reg.html"
@login_required
def stockoperations_view(request):
	user_id = request.session.get('_auth_user_id')
	if not user_id:
		return redirect("/")
	else:
		data = StockOperations.objects.all()
		return render(request,"stock/stockoperations.html",{"data":data})

@login_required
def delete_stockoperation_view(request,pk):
	message=""
	if request.method=="POST":
		so = StockOperations.objects.get(id=pk)
		so.delete()
		message="Record deleted successfully"
		return redirect('/stockoperations/')
	return render(request, "stock/so_del.html",{"message":message})

@login_required
def update_stockoperation_view(request, pk):
	data = StockOperations.objects.get(id=pk)
	message=""
	form = StockOperationForm(instance=data)
	if request.method=="POST":
		form = StockOperationForm(request.POST, instance=data)
		if form.is_valid():
			form.save()
			message="Record updated successfully"
			return redirect('/stockoperations/')
		else:
			message=form.errors

	return render(request,"stock/so.html",
		{"form":form,"message": message})
@login_required
def create_stockoperation_view(request):
	form = StockOperationForm()
	message=""
	try:
		if request.method=="POST":
			soform = StockOperationForm(request.POST)
			if soform.is_valid():
		
				soform.save()
				message="stock operation created successfully"
				return redirect('/stockoperations/')
			else:
				message=soform.errors
	except Exception as err:
		message=err.message
		form=soform
	return render(request,"stock/so.html",{"form":form,
		"message":message})

def registration_view(request):
	form = UserProfileForm()
	message = ""
	if request.method=="POST":
		data = request.POST 
		username = data.get("username")
		password = data.get("password")
		#user = User(username=username, password=password)
		try:
			#user.save()
			user= User.objects.create_user(username=username,
				password=password)
		except Exception as err:
			# if there is an exception this part will execute
			message=err.message
		else:
			# if there is no exception this part will execute
			upf = UserProfileFormAll({"address":data.get("address"),
							"phone":data.get("phone"),
							"role":data.get("role"),
							"user":user.id})
			if upf.is_valid():
				upf.save()
				message="Registration successful"
			else:
				message = upf.errors
	return render(request,"stock/reg.html",
		{"regform":form,"message":message})

