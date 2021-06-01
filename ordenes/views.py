from datetime import datetime

from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpRequest
from django.conf import settings
from django.db import connections

from . import models

# Create your views here.

def nuevos(request):
    
    if chequeo_login() == False: return redirect('/acceso/')

    return render(request, 'ordenes/nuevos.html')
 
def archivados(request):
    if chequeo_login() == False: return redirect('/acceso/')

    return render(request, 'ordenes/archivados.html')

def manifestados(request):
    if chequeo_login() == False: return redirect('/acceso/')

    return render(request, 'ordenes/manifestados.html')

def seguimiento(request):
    if chequeo_login() == False: return redirect('/acceso/')

    return render(request, 'ordenes/seguimiento.html')


def chequeo_login():

    if settings.STAUS_LOGIN == True:
        return True
    else:
        return False