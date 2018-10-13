# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class StockConfig(AppConfig):
    name = 'stock'
    def ready(self):
    	print "ready method called"
    	from stock.signals import update_model

