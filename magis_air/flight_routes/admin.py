from django.contrib import admin
from .models import Flight

@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = ('flight_id', 'origin', 'destination', 'travel_duration_hours', 'travel_duration_minutes', 'departure_time')
    search_fields = ('flight_id',)