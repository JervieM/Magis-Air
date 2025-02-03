
from django import forms
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import CrewMember
from datetime import date

def home(request):
    return render(request, 'home.html') 

class CrewIDSearchForm(forms.Form):
    crew_ID = forms.CharField(
        min_length=6,
        max_length=6,
        required=False,
        label="Type Crew ID"
    )

class CrewRoleSearchForm(forms.Form):
    role = forms.ChoiceField(
        choices= [('', '---------')] + [('Captain', 'Captain'), ('First Officer', 'First Officer'), ('Flight Attendant', 'Flight Attendant'), ('Flight Engineer', 'Flight Engineer')],
        required=False,
        label="Select Role"
    )

class CrewMemberListView(ListView):
    model = CrewMember
    fields = ['crew_id', 'role', 'flight_schedules']
    template_name = 'crew_list.html'

    def get_queryset(self):
        crew_ID_filter = self.request.GET.get('crew_ID')
        crew_role_filter = self.request.GET.get('role')

        queryset = CrewMember.objects.all()

        if crew_ID_filter:
            queryset = queryset.filter(crew_id=crew_ID_filter)

        if crew_role_filter:
            queryset = queryset.filter(role=crew_role_filter)

        return queryset


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['crew_id_form'] = CrewIDSearchForm(self.request.GET)
        context['crew_role_form'] = CrewRoleSearchForm(self.request.GET)
        context['current_date'] = date.today()
        return context
    

class CrewMemberCreateView(CreateView):
    model = CrewMember
    fields = ['first_name', 'middle_name', 'last_name', 'role']
    template_name = 'crew_form.html'
    success_url = reverse_lazy('crew_assignments:crew_list')

class CrewMemberUpdateView(UpdateView):
    model = CrewMember
    fields = ['first_name', 'middle_name', 'last_name', 'role']
    template_name = 'crew_form.html'
    success_url = reverse_lazy('crew_assignments:crew_list')

class CrewMemberDeleteView(DeleteView):
    model = CrewMember
    template_name = 'crew_confirm_delete.html'
    success_url = reverse_lazy('crew_assignments:crew_list')
