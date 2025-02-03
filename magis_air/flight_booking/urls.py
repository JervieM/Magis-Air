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
    path('passengers/', views.PassengerListView.as_view(), name='passenger_list'),
    path('passengers/create/', views.PassengerCreateView.as_view(), name='passenger_create'), 
    path('passenger/<pk>/delete/', views.PassengerDeleteView.as_view(), name='passenger_delete'), 
    path('passenger/update/<pk>/', views.PassengerUpdateView.as_view(), name='passenger_update'),
    path('bookings/', views.BookingListView.as_view(), name='booking_list'),
    path('booking_list/', views.BookingListView.as_view(), name='booking_list'),
    path('bookings/create/', views.BookingCreateView.as_view(), name='booking_create'),
    path('bookings/<str:pk>/update/', views.BookingUpdateView.as_view(), name='booking_update'),
    path('bookings/<str:pk>/delete/', views.BookingDeleteView.as_view(), name='booking_delete'),
]

app_name = 'flight_booking'