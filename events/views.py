from django.views import generic
from django.shortcuts import render
from .models import Event


"""def FormView(request):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Your event has been saved')
    
    else:
        form = Form()
        context = {
            'form':form,
        }
    return render(request,)"""

def all_events(request):
    event_list = Event.objects.all()
    return render(request, 'events/event_list.html',{'event_list':event_list})
