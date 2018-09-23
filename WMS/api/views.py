# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.views import APIView
from stock.models import ProductCategory
from rest_framework import status

class ProductCategoryAPIView(APIView):
	def post(self, request):
		data = request.data
		#pc = ProductCategory(**data)
		name= data.get("name")
		if not name.isalnum():
			return Response(
				{"message":"product category created not created",
				 "errors":{'name': "expecting only alpha numeric"},
				 "item":{}
				},
				status = status.HTTP_400_BAD_REQUEST
				)
		pc = ProductCategory(name=data.get("name"),
			desc=data.get("desc"))
		pc.save()
		#import pdb; pdb.set_trace()
		return Response(
			{"message":"product category created successfully",
			 "errors":{},
			 "item":{"name":pc.name,"desc":pc.desc}
			},
			status = status.HTTP_201_CREATED
			)
	def put(self, request,pk):
		data = request.data
		pc = ProductCategory.objects.get(pk=pk)
		if "name" in data:
			pc.name=data.get("name")
		if "desc" in data:
			pc.desc=data.get("desc")
		pc.save()
		return Response(
			{"message":"product category updated successfully",
			 "errors":{},
			 "item":{"name":pc.name,"desc":pc.desc}
			},
			status = status.HTTP_201_CREATED
			)
	def delete(self, request,pk):
		try:
			try:
				pc = ProductCategory.objects.get(pk=pk)
			except:
				return Response({"error":"Product category not found"},
					status=status.HTTP_404_NOT_FOUND)
			pc.delete()
			return Response(
				status = status.HTTP_204_NO_CONTENT
				)
		except Exception as err:
			return Response({"erros":"%s"%err},
				status=status.HTTP_400_BAD_REQUEST)
	def get(self, request,pk=None):
		if pk:
			try:
				pc= ProductCategory.objects.get(pk=pk)
			except Exception as err:
				return Response({"error":"Product category not found"},
					status=status.HTTP_404_NOT_FOUND)
			else:
				return Response({"message":"product categories get successfully",
				 "errors":{},
				 "item":{"name":pc.name,"desc":pc.desc,"id":x.id}
				})
		else:
			data = ProductCategory.objects.all()
			return Response({"message":"product categories get successfully",
				 "errors":{},
				 "items":map(lambda x:{"name":x.name,"desc":x.desc,"id":x.id},
				 	data)
				})









# Create your views here.
'''
@csrf_exempt
def api_product_view(request):
	import pdb; pdb.set_trace()
	# check for user session
	if request.method=="POST":
		# take the data and insert the record
	elif request.method=="PUT":
		# take the data and update the record
	elif request.method=="DELETE":
		# take the id and delete the record
	return HttpResponse(json.dumps("HELLO FIREFOX"))
'''
