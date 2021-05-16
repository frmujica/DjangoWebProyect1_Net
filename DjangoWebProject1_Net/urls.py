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
    path('', include('login.urls')),
]
