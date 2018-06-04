from django.contrib import admin
from sign.models import Event, Guest

# Register your models here.


class EventAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'status', 'address', 'start_time']


class GuestAdmin(admin.ModelAdmin):
    list_display = ['real_name', 'phone', 'email', 'sign', 'create_time', 'event']

admin.site.register(Event, EventAdmin)
admin.site.register(Guest, GuestAdmin)
