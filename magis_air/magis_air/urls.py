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
from django.contrib import admin
from django.urls import path, include
from crew_assignments.views import home 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  
    path('crew_assignments/', include('crew_assignments.urls')),
    path('flight_booking/', include('flight_booking.urls')),
    path('flight_routes/', include('flight_routes.urls')),
    path('flight_schedules/', include('flight_schedules.urls')),
]

