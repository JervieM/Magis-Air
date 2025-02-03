from django import forms
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Passenger, Booking

# Passengers

class PassengerIDSearchForm(forms.Form):
    passenger_id = forms.CharField(
        min_length=17,
        max_length=17,
        required=False,
        label="Type Passenger ID"
    )
    
class PassengerNameSearchForm(forms.Form):
    name = forms.CharField(
        min_length=1,
        max_length=160,
        required=False,
        label="Type Passenger Name"
    )
    
class PassengerGenderSearchForm(forms.Form):
    gender = forms.ChoiceField(
        choices= [('', '---------')] + [('M', 'Male'), ('F', 'Female'), ('O', 'Others')],
        required=False,
        label="Select Gender"
    )

class PassengerListView(ListView):
    model = Passenger
    template_name = 'passenger_list.html'
    
    def get_queryset(self):
        passenger_id_filter = self.request.GET.get('passenger_id')
        name_filter = self.request.GET.get('name')
        gender_filter = self.request.GET.get('gender')

        queryset = Passenger.objects.all()

        if passenger_id_filter:
            queryset = queryset.filter(passenger_id=passenger_id_filter)

        if name_filter:
            queryset = queryset.filter(name__icontains=name_filter)
        
        if gender_filter:
            queryset = queryset.filter(gender=gender_filter)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['passenger_id_form'] = PassengerIDSearchForm(self.request.GET)
        context['name_form'] = PassengerNameSearchForm(self.request.GET)
        context['gender_form'] = PassengerGenderSearchForm(self.request.GET)
        return context
    
class PassengerCreateView(CreateView):
    model = Passenger
    fields = ['first_name', 'middle_name', 'last_name', 'birth_date', 'gender'] 
    template_name = 'passenger_form.html'
    success_url = reverse_lazy('flight_booking:passenger_list') 
    
# Booking

class BookingIDSearchForm(forms.Form):
    booking_id = forms.CharField(
        min_length=13,
        max_length=13,
        required=False,
        label="Type Booking ID"
    )

class Booking_PassengerSearchForm(forms.Form):
    passenger = forms.CharField(
        min_length=1,
        max_length=160,
        required=False,
        label="Type Passenger Name"
    )

class BookingListView(ListView):
    model = Booking
    template_name = 'booking_list.html'
  
    def get_queryset(self):
        booking_id_filter = self.request.GET.get('booking_id')
        passenger_filter = self.request.GET.get('passenger')

        queryset = Booking.objects.all()

        if booking_id_filter:
            queryset = queryset.filter(booking_id=booking_id_filter)

        if passenger_filter:
            queryset = queryset.filter(passenger__name__icontains=passenger_filter)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['booking_id_form'] = BookingIDSearchForm(self.request.GET)
        context['passenger_id_form'] = Booking_PassengerSearchForm(self.request.GET)
        return context

class BookingCreateView(CreateView):
    model = Booking
    fields = ['total_cost', 'passenger', 'flight', 'additional_items']  
    template_name = 'booking_form.html'

    def get_success_url(self):
        return reverse_lazy('flight_booking:booking_list')

class BookingUpdateView(UpdateView):
    model = Booking
    fields = ['total_cost', 'additional_items']
    template_name = 'booking_form.html'
    success_url = reverse_lazy('flight_booking:booking_list')

class BookingDeleteView(DeleteView):
    model = Booking
    template_name = 'booking_confirm_delete.html'
    success_url = reverse_lazy('flight_booking:booking_list')  

class PassengerDeleteView(DeleteView):
    model = Passenger
    template_name = 'passenger_confirm_delete.html'
    success_url = reverse_lazy('flight_booking:passenger_list')

class PassengerUpdateView(UpdateView):
    model = Passenger
    fields = ['first_name', 'middle_name', 'last_name', 'birth_date', 'gender']
    template_name = 'passenger_form.html'
    success_url = reverse_lazy('flight_booking:passenger_list')
