# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.
from rest_framework.test import APITestCase, APIClient
class ProductCategoryTestCases(APITestCase):
	@classmethod
	def setUpClass(cls):
		cls.client = APIClient()
		cls.client.force_authenticate(user=None)
	def test_pc_create(self):
		resp = self.client.post("/api/productcategory/",
			data={"name":"pc1","unique_name":"pc1"})
		print resp.content
		self.assertEqual(resp.status_code, 201)
		resp = self.client.get("/api/productcategory/")


	@classmethod
	def tearDownClass(cls):
		cls.client.logout()
