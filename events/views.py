from django.http.request import host_validation_re
from django.shortcuts import render
from django.http import HttpResponse
from .models import Event

def index(request):
    #return HttpResponse("<h1>Reminder App</h1>")
    return render(request, 
            'events/event.html'
            )

##def all_events(request):
    event_list = Event.objects.all()
    return render(request,
        'events/event_list.html',
        {'event_list':event_list}
        )
###

# Create your views here.
