# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from stock.forms import UserProfileForm, UserProfileFormAll,\
StockOperationForm
from django.contrib.auth.models import User
from stock.models import StockOperations, ProductCategory
from django.contrib.auth import authenticate

# Create your views here.
# def productcategories_view(request):
# 	data = ProductCategory.objects.all()
# 	return render(request, "stock/productcategories.html",
# 		"data":data)
# def index_view(request):
# 	return render(request,"stock/index.html")
def login_view(request):
	message = ""
	if request.method=="POST":
		username = request.POST.get("username")
		password = request.POST.get("password")
		user = authenticate(username=username,
			password=password)
		if user:
			message="successfully logedin"
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
def stockoperations_view(request):
	data = StockOperations.objects.all()
	return render(request,"stock/stockoperations.html",{"data":data})
def delete_stockoperation_view(request,pk):
	message=""
	if request.method=="POST":
		so = StockOperations.objects.get(id=pk)
		so.delete()
		message="Record deleted successfully"
		return redirect('/stockoperations/')
	return render(request, "stock/so_del.html",{"message":message})
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

