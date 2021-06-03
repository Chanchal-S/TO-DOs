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
# Create your models here.
