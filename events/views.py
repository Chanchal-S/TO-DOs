from django import http
from django.views import generic
from django.shortcuts import render
from .models import Event
from .models import Maps
from django.http import HttpResponse, request


#function to view home page
def index(request):
    different_base =  "base.html"
    return render(request, 'events/event.html', {'different_base': different_base})

#function to view list of saved events
def all_events(request):
    different_base =  "base.html"
    event_list = Event.objects.all()
    return render(request, 'events/event_list.html',{'event_list':event_list}, {'different_base': different_base})

def jigsaw_func(request):
    different_base =  "base.html"
    print("jigsaw_func")
    return render(request, 'jigsaw/jigsaw.html', {'different_base': different_base})
    
svgelement=None
def all_svg(request):
    different_base =  "b2.html"
    print("all_svg")
    selected_map=request.POST.get('puzzle', False)
    map_from_db=Maps.objects.get(country_name=selected_map)
    svgelement = map_from_db.country_svg
    #return render(request, 'events/loadmap.html',{'aditi':svgelement})
    return render(request, 'loadmap/loadmap.html',{'aditi':svgelement}, {'different_base': different_base})


  # https://stackoverflow.com/questions/5895588/django-multivaluedictkeyerror-error-how-do-i-deal-with-it  