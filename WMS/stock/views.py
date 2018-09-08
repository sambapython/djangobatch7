# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from stock.forms import UserProfileForm, UserProfileFormAll,\
StockOperationForm
from django.contrib.auth.models import User

# Create your views here.
def home_view(request):
	return render(request,"stock/home.html") 

# def registration_view(request):
# 	print "*"*20
# 	# print "method=",request.method
# 	# print "get=",request.GET
# 	# print "post=",request.POST
# 	data = request.POST
# 	print data.get("user")
# 	print data.get("password")
# 	print "*"*20
# 	return render(request,"stock/reg.html")
def create_stockoperation_view(request):
	form = StockOperationForm()
	message=""
	try:
		if request.method=="POST":
			soform = StockOperationForm(request.POST)
			if soform.is_valid():
				print 1/0
				soform.save()
				message="stock operation created successfully"
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
		user = User(username=username, password=password)
		try:
			user.save()
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

