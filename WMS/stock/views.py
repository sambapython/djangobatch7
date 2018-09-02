# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def home_view(request):
	return render(request,"stock/home.html") 

def registration_view(request):
	print "*"*20
	# print "method=",request.method
	# print "get=",request.GET
	# print "post=",request.POST
	data = request.POST
	print data.get("user")
	print data.get("password")
	print "*"*20
	return render(request,"stock/reg.html")

