from django import urls
from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', views.index, name='index'),
    ]