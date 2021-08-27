from django import http
from django.views import generic
from django.shortcuts import render
from .models import Event
from .models import Maps
from django.http import HttpResponse, request


#function to view home page
def index(request):
    return render(request, 'events/event.html')

#function to view list of saved events
def all_events(request):
    event_list = Event.objects.all()
    return render(request, 'events/event_list.html',{'event_list':event_list})

def jigsaw_func(request):
    print("jigsaw_func")
    return render(request, 'jigsaw/jigsaw.html')
    
svgelement=None
def all_svg(request):
    print("all_svg")
    abc=request.POST.get('country', False)
    country=Maps.objects.get(country_name=abc)
    svgelement = country.country_svg
    #return render(request, 'events/loadmap.html',{'aditi':svgelement})
    return render(request, 'loadmap/loadmap.html',{'aditi':svgelement})


  # https://stackoverflow.com/questions/5895588/django-multivaluedictkeyerror-error-how-do-i-deal-with-it  