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
delete_stockoperation_view, stockoperations_view, login_view
from django.views.generic import TemplateView, ListView,\
CreateView, UpdateView, DeleteView
from stock.models import ProductCategory

urlpatterns = [
    url(r'^api/', include('api.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^login/', login_view),
    url(r'^index/',TemplateView.as_view(template_name="stock/index.html")),
    url(r'^$', home_view),
    url(r'^registration/$', registration_view),
    url(r'^create_stockoperation/$', create_stockoperation_view),
    url(r'^update_stockoperation/([0-9]+)/$', update_stockoperation_view),
    url(r'^delete_stockoperation/([0-9]+)/$', delete_stockoperation_view),
    url(r'^stockoperations/$', stockoperations_view),
    url(r'^productcategories/$', ListView.as_view(
        model=ProductCategory,
        )),
    url(r'^pc_create/$', CreateView.as_view(
        model = ProductCategory,
        success_url = "/productcategories/",
        fields=("unique_name","name","desc"),
        )),
    url(r'^pc_update/(?P<pk>[0-9]+)/$', UpdateView.as_view(
        model = ProductCategory,
        success_url = "/productcategories/",
        fields=("unique_name","name","desc"),
        )),
    url(r'^pc_delete/(?P<pk>[0-9]+)/$', DeleteView.as_view(
        model = ProductCategory,
        success_url = "/productcategories/",
        )),
    
    
]
