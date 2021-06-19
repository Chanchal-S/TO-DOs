from datetime import datetime
from django import forms
from .models import Event
from django.forms import ModelForm, fields
from django.shortcuts import render
from django.http import HttpResponseRedirect

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['user_name', 'event_desc', 'event_date', 'event_time']

def addevent(request):
    submitted = False
    if request.method == 'POST':
        a=Event.objects.get(pk='user1')
        form = EventForm(request.POST, instance=a)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/addevent/?submitted=True')
    else:
        form = EventForm()
        if 'submitted' in request.GET:
            submitted = True
        
    return render(request,
        'addevent/addevent.html',
        {'form':form, 'submitted':submitted}
        )       