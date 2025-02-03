from django.contrib import admin
from .models import Passenger, Booking, AdditionalItem

@admin.register(Passenger)
class PassengerAdmin(admin.ModelAdmin):
    list_display = ('passenger_id', 'name', 'birth_date', 'gender')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('booking_id', 'passenger', 'flight', 'total_cost', 'booking_date')

@admin.register(AdditionalItem)
class AdditionalItemAdmin(admin.ModelAdmin):
    list_display = ('item_id', 'description')
