from django.contrib import admin
from .models import Event
from .models import Maps

class EventAdmin(admin.ModelAdmin):
    list_display = ('user_name','event_desc','event_date','event_time')
    ordering = ('user_name',)
    search_fields = ('user_name',)

class MapsAdmin(admin.ModelAdmin):
    list_display = ('country_name','country_svg')
    ordering = ('country_name',)
    search_fields = ('country_name',)

admin.site.register(Event, EventAdmin)
admin.site.register(Maps, MapsAdmin)

# Register your models here.
