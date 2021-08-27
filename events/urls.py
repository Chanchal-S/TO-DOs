from django import urls
from django.contrib import admin
from django.urls import include, path
from django.urls.resolvers import URLPattern

#importing all views from current package
from . import views 
#import the addevent module
from . import addevent
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('addevent/', addevent.addevent, name='add-events'),
    path('events/', views.all_events, name='show-events'),
    path('jigsaw/', views.jigsaw_func, name='play-jigsaw'),
    path('jigsaw/loadmap/',views.all_svg, name='loadmap'),
    ]