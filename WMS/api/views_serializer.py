import logging
from rest_framework.views import APIView
from serializers import ProductCategorySerializer,\
StockOperationSerializer, LineItemSerializer,\
StockOperationGetSerializer
from rest_framework.response import Response
from rest_framework import status
from stock.models import StockOperations
from rest_framework import permissions, authentication
from rest_framework.decorators import authentication_classes,\
permission_classes
logger = logging.getLogger(__name__)
class StockoperationsAPIViewSer(APIView):
	def get(self, request):
		data = StockOperations.objects.all()
		ser = StockOperationGetSerializer(data,many=True)
		return Response({"items":ser.data})
	def post(self, request):
		items = []
		for item in request.data.pop("items"):
			lineser = LineItemSerializer(data=item)
			if lineser.is_valid():
				lineser.save()
				items.append(lineser.data.get("id"))
			else:
				errors = lineser._errors
				return Response(
					{"message":"problem in stock operation createion",
					 "errors":errors,
					 "item":{}
					},
					status = status.HTTP_400_BAD_REQUEST
					) 

		data = request.data 
		data["lineitems"]=items
		serializer = StockOperationSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(
			{"message":"stock operation created successfully",
			 "errors":{},
			 "item":{"name":serializer.data.get("name"),
			 "desc":serializer.data.get("desc"),
			 "id":serializer.data.get("id")
			 }
			},
			status = status.HTTP_201_CREATED
			)
		else:
			errors = serializer._errors
			return Response(
				{"message":"problem in stock operation createion",
				 "errors":errors,
				 "item":{}
				},
				status = status.HTTP_400_BAD_REQUEST
				) 

@authentication_classes([])
@permission_classes([])
class ProductCategoryAPIViewSer(APIView):
	#permission_classes = (permissions.IsAuthenticated,)
	#authentication_classes = (authentication.TokenAuthentication,)
	def post(self, request):
		logger.info("product category creation started")
		serializer = ProductCategorySerializer(data=request.data)
		if serializer.is_valid():
			logger.info("validation successful")
			serializer.save()
			logger.info("product category created successful")
			return Response(
			{"message":"product category created successfully",
			 "errors":{},
			 "item":{"name":serializer.data.get("name"),
			 "desc":serializer.data.get("desc")}
			},
			status = status.HTTP_201_CREATED
			)
		else:
			errors = serializer._errors
			logger.error("validation failed errors: %s"%errors)
			return Response(
				{"message":"product category created not created",
				 "errors":errors,
				 "item":{}
				},
				status = status.HTTP_400_BAD_REQUEST
				) 
