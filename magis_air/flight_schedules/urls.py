"""
URL configuration for magis_air project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.FlightScheduleListView.as_view(), name='flight_schedule_list'),
    path('create/', views.FlightScheduleCreateView.as_view(), name='flight_schedule_create'),
    path('<str:pk>/update/', views.FlightScheduleUpdateView.as_view(), name='flight_schedule_update'),
    path('<str:pk>/delete/', views.FlightScheduleDeleteView.as_view(), name='flight_schedule_delete'),
]

app_name = 'flight_schedules'

