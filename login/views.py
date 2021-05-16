from datetime import datetime

from django.db import connection

from django.shortcuts import render, HttpResponse
from django.http import HttpRequest
from django.conf import settings


# Create your views here.

def acceso(request):

    if request.method == 'POST':

        if request.POST.get('usuario') != '' and request.POST.get('clave') != '':
            
            if ( entradaValida(request.POST.get('usuario'), request.POST.get('clave')) ) == True:
                settings.STAUS_LOGIN = True
            else:
                settings.STAUS_LOGIN = True
        else:
            settings.STAUS_LOGIN = False

        return render(request, 'login/acceso.html', {'entrada_estado': settings.STAUS_LOGIN})

    else:

        return render(request, 'login/acceso.html', {'entrada_estado': ''})


def entradaValida(usuario, clave):
    
    rows = []

    with connection.cursor() as cursor:
        cursor.execute('''
            SELECT 
                usuario, clave 
            FROM 
                usuarios 
            WHERE 
                usuario = "%s"
                AND 
                clave = "%s"
                AND
                activo = 'True'
        ''' %  (usuario, clave) )
        rows = cursor.fetchall()

    if len(rows) == 0:
        return False
    else:
        return True


    






