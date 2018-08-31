# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def warehouses_view(request):
	# do some process
	#return HttpResponse("Hello firfox!!")
	'''
	warehouses = ["ameerpet","SRnagar","bharathnagar"]
	return HttpResponse(warehouses)
	'''
	'''
	resp = """
	<html>
		<h1>WAREHOUSES</h1>
		<ul>
			<li>Ameerpet</li>
			<li>SRnagar</li>
		</ul>
	</html>
	"""
	return HttpResponse(resp)
	'''
	return render(request, "store/warehouses.html")


