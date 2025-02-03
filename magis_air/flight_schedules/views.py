from django import forms
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import FlightSchedule, CrewMember

class FlightScheduleListView(ListView):
    model = FlightSchedule
    template_name = 'flight_schedule_list.html'
    context_object_name = 'flight_schedules'  

    def get_queryset(self):
        queryset = FlightSchedule.objects.all()

        schedule_id = self.request.GET.get('schedule_id')
        if schedule_id:
            queryset = queryset.filter(schedule_id__icontains=schedule_id)

        date = self.request.GET.get('date')
        if date:
            queryset = queryset.filter(date=date)

        return queryset

class FlightScheduleCreateView(CreateView):
    model = FlightSchedule
    fields = ['date', 'flight']
    template_name = 'flight_schedule_form.html'
    success_url = reverse_lazy('flight_schedules:flight_schedule_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['crew_members'] = CrewMember.objects.all()  
        return context

    def form_valid(self, form):
        flight_schedule = form.save()

        crew_member_ids = self.request.POST.getlist('crew_members')  
        
        for crew_id in crew_member_ids:
            crew_member = get_object_or_404(CrewMember, crew_id=crew_id)
            flight_schedule.crew_members.add(crew_member)  
            crew_member.flight_schedules.add(flight_schedule)

        return redirect(self.success_url)

class FlightScheduleUpdateView(UpdateView):
    model = FlightSchedule
    fields = ['schedule_id', 'date', 'flight']
    template_name = 'flight_schedule_form.html'
    success_url = reverse_lazy('flight_schedules:flight_schedule_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        flight_schedule = self.get_object()
        context['crew_members'] = CrewMember.objects.all()  
        context['selected_crew_members'] = flight_schedule.crew_members.all()  
        return context
    
    def form_valid(self, form):
        flight_schedule = form.save()

        crew_member_ids = self.request.POST.getlist('crew_members')

        current_crew_members = flight_schedule.crew_members.all()

        for crew_member in current_crew_members:
            if str(crew_member.crew_id) not in crew_member_ids:
                flight_schedule.crew_members.remove(crew_member)
                crew_member.flight_schedules.remove(flight_schedule)

        for crew_id in crew_member_ids:
            crew_member = get_object_or_404(CrewMember, crew_id=crew_id)
            flight_schedule.crew_members.add(crew_member)
            crew_member.flight_schedules.add(flight_schedule)

        return redirect(self.success_url)

class FlightScheduleDeleteView(DeleteView):
    model = FlightSchedule
    template_name = 'flight_schedule_confirm_delete.html'
    success_url = reverse_lazy('flight_schedules:flight_schedule_list')