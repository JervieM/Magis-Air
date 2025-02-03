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
    path('', views.CrewMemberListView.as_view(), name='crew_list'),
    path('create/', views.CrewMemberCreateView.as_view(), name='crew_create'),
    path('<str:pk>/update/', views.CrewMemberUpdateView.as_view(), name='crew_update'),
    path('<str:pk>/delete/', views.CrewMemberDeleteView.as_view(), name='crew_delete'),
]

app_name = 'crew_assignments'