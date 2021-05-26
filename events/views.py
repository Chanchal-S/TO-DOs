from django.http.request import host_validation_re
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Reminder App</h1>")

# Create your views here.
