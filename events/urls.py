from django import urls
from django.contrib import admin
from django.conf.urls import url
from django.urls import include, path
from django.urls.resolvers import URLPattern
from . import views
from . import addevent  #import the addevent module

urlpatterns = [
    path('admin/', admin.site.urls),
    path('addevent/', addevent.addevent, name='add-events'),
    #path('', views.index, name='index'),
    path('events/', views.all_events, name='show-events'),
    #path('',include('events.urls')),
    ]