from .models import Event
from django.forms import ModelForm

class EventForm(ModelForm):
    class Meta:
        model : Event
        fields = ('user_name','event_desc','event_date','event_time',)