from django import forms
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import Flight, generate_flight_id


class FlightSearchForm(forms.Form):
    origin = forms.ChoiceField(
        choices=[('', '---------')] + [('Manila, Philippines', 'Manila, Philippines'), ('Tokyo, Japan', 'Tokyo, Japan'), ('London, UK', 'London, UK'), ('New York, USA', 'New York, USA')],
        required=False,
        label="Select Origin"
    )
    destination = forms.ChoiceField(
        choices=[('', '---------')] + [('Manila, Philippines', 'Manila, Philippines'), ('Tokyo, Japan', 'Tokyo, Japan'), ('London, UK', 'London, UK'), ('New York, USA', 'New York, USA')],
        required=False,
        label="Select Destination"
    )

class FlightListView(ListView):
    model = Flight
    template_name = 'flight_list.html'
    context_object_name = 'data'

    def get_queryset(self):
        origin_filter = self.request.GET.get('origin')
        destination_filter = self.request.GET.get('destination')

        queryset = Flight.objects.all()

        if origin_filter:
            queryset = queryset.filter(origin=origin_filter)

        if destination_filter:
            queryset = queryset.filter(destination=destination_filter)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = FlightSearchForm(self.request.GET)
        return context

class FlightCreateView(CreateView):
    model = Flight
    fields = ['flight_id', 'origin', 'destination', 'travel_duration_hours', 'travel_duration_minutes', 'departure_time']
    template_name = 'flight_form.html'
    success_url = reverse_lazy('flight_routes:flight_list')

    def get_initial(self):
        """Override the get_initial method to add flight_id to the form."""
        initial = super().get_initial()
        initial['flight_id'] = generate_flight_id()  
        return initial

    def form_valid(self, form):
        flight = form.save(commit=False)
        flight.flight_id = form.cleaned_data['flight_id']
        flight.save()
        return super().form_valid(form)

class FlightUpdateView(UpdateView):
    model = Flight
    fields = ['flight_id', 'origin', 'destination', 'travel_duration_hours', 'travel_duration_minutes', 'departure_time']
    template_name = 'flight_form.html'
    success_url = reverse_lazy('flight_routes:flight_list')

class FlightDeleteView(DeleteView):
    model = Flight
    template_name = 'flight_confirm_delete.html'
    success_url = reverse_lazy('flight_routes:flight_list')

class FlightDetailView(DetailView):
    model = Flight
    template_name = 'flight_detail.html'
    context_object_name = 'flight'  
