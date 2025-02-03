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
    path('', views.FlightListView.as_view(), name='flight_list'),
    path('create/', views.FlightCreateView.as_view(), name='flight_create'),
    path('<str:pk>/update/', views.FlightUpdateView.as_view(), name='flight_update'),
    path('<str:pk>/delete/', views.FlightDeleteView.as_view(), name='flight_delete'),
    path('<str:pk>/', views.FlightDetailView.as_view(), name='flight_detail'),  # Add this line
]

app_name = 'flight_routes'
