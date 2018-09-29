"""WMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from stock.views import home_view, registration_view,\
create_stockoperation_view, update_stockoperation_view,\
delete_stockoperation_view, stockoperations_view, login_view,\
index_view
from api.views import ProductCategoryAPIView, StockoperationsAPIView
from api.views_serializer import ProductCategoryAPIViewSer,\
StockoperationsAPIViewSer


urlpatterns = [
    #url(r'^products/$', api_product_view),
    url(r'^productcategory/$', ProductCategoryAPIView.as_view()),
    url(r'^productcategory/([0-9]+)/$', ProductCategoryAPIView.as_view()),
    url(r'^stockoperations/$', StockoperationsAPIView.as_view()),
    url(r'^stockoperations/([0-9]+)/$', StockoperationsAPIView.as_view()),
    url(r'^productcategoryser/$', ProductCategoryAPIViewSer.as_view()),
    url(r'^productcategoryser/([0-9]+)/$', ProductCategoryAPIViewSer.as_view()),
    url(r'^stockoperationsser/$', StockoperationsAPIViewSer.as_view()),
    url(r'^stockoperationsser/([0-9]+)/$', StockoperationsAPIViewSer.as_view()),


]
