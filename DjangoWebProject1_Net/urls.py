"""
Definition of urls for DjangoWebProject1_Net.
"""

from datetime import datetime

from django.urls import path
from django.urls import include

from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView

from app import forms, views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('terminosycondiciones/', views.terminosycondiciones, name='terminosycondiciones'),
    path('soporte/', views.soporte, name='soporte'),
    path('ayuda/', views.ayuda, name='ayuda'),
    path('', include('login.urls')),
]