from django.contrib import admin
from .models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ('user_name','event_desc','event_date','event_time')
    ordering = ('user_name',)
    search_fields = ('user_name',)

admin.site.register(Event, EventAdmin)

# Register your models here.
