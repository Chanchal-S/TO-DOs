from typing import Any
from django.db import models
from datetime import date,datetime


class Event(models.Model):
    user_name = models.CharField(default='username',max_length=100,primary_key=True)
    event_desc = models.TextField(max_length=200)
    event_date = models.DateField(default=date.today())
    event_time = models.TimeField(default=datetime.time(datetime.now()))

    def __str__(self):
        return self.user_name

class Meta:
        app_label = 'event'

class Maps(models.Model):
    country_name = models.CharField('Country Name',max_length=100)
    country_svg = models.TextField()
    #change file field to textfield to store svg tag

    def __str__(self):
        return self.country_name



    
# Create your models here.
