from rest_framework import serializers
from stock.models import ProductCategory, StockOperations, LineItem
import re

class StockOperationSerializer(serializers.ModelSerializer):
	class Meta:
		model = StockOperations
		fields = "__all__"

	def validate_vendor(self, vendor_inst):
		print vendor_inst,"*"*60
		return vendor_inst

class StockOperationGetSerializer(serializers.ModelSerializer):
	class Meta:
		model = StockOperations
		fields = ("name","lineitems")
class LineItemSerializer(serializers.ModelSerializer):
	class Meta:
		model = LineItem
		fields = "__all__"

class ProductCategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = ProductCategory
		fields  = "__all__"
	# def validate(self, data):
	# 	if not data.get("name").isalnum():
	# 		raise serializers.ValidationError("Invalid name passed")
	# 	if re.search("[0-9]+",data.get("desc")):
	# 		raise serializers.ValidationError("Invalid description")
	# 	return data


	def validate_name(self, value):
		if value.isalnum():
			return value
		else:
			raise serializers.ValidationError("Invalid name passed")
	def validate_desc(self, value):
		if re.search("[0-9]+",value):
			raise serializers.ValidationError("Invalid description")
		return value