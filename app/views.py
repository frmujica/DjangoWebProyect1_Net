"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from django.conf import settings

from . import servicios

def home(request):
    """Renders the home page."""
    # assert isinstance(request, HttpRequest)

    servicios.temporizadores.start_job1()

    return render(request, 'app/index.html', {"CONTADOR" : settings.CONTADOR} )

def terminosycondiciones(request):

    return render(request, 'app/terminosycondiciones.html')

def soporte(request):

    return render(request, 'app/soporte.html')

def ayuda(request):

    return render(request, 'app/ayuda.html')