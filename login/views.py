from datetime import datetime

from django.shortcuts import render, HttpResponse
from django.http import HttpRequest
from django.conf import settings
from django.db import connections

from . import models

# Create your views here.

msg = ''
error = ''

def acceso(request):
    
    global msg
    global error

    try:

        if request.method == 'POST':

            if request.POST.get('usuario') != '' and request.POST.get('clave') != '':
            
                if ( validarUsuario(request.POST.get('usuario'), request.POST.get('clave')) ) == True:
                    settings.STAUS_LOGIN = True
                else:
                    settings.STAUS_LOGIN = False
            else:
                msg = 'No ha indicado usuario/clave'
                error = '1'
                settings.STAUS_LOGIN = False

            return render(request, 'login/acceso.html', {'entrada_estado': settings.STAUS_LOGIN, 'POST':'True', 'error':error, 'msg':msg})

        else:
            return render(request, 'login/acceso.html', {'entrada_estado': '', 'POST':'False', 'error':'', 'msg':''})

    except Exception as e:

        msg = str(e)
        error = '1'
        settings.STAUS_LOGIN = False
        return render(request, 'login/acceso.html', {'entrada_estado': settings.STAUS_LOGIN, 'error':error, 'msg':msg})



def validarUsuario(usuario, clave):

    global msg
    global error

    try:

        first_person = models.usuarios.objects.using('usuarios').raw('''
            SELECT 
                id, 
                usuario, 
                clave,  
                correo, 
                fecha_ultimo_acceso, 
                hora_ultimo_acceso, 
                intentos, activo
            FROM 
                usuarios 
            WHERE 
                usuario = "%s"
                AND 
                clave = "%s"
        ''' %  (usuario, clave))

        if len(first_person) == 1:
            if first_person[0].activo == 'True':
                guardarUltimaEntrada(first_person[0].usuario)
                settings.USUARIO = { 'id': first_person[0].id,  'usuario': first_person[0].usuario }
                return True
            else:
                msg = 'usuario desactivado'
                error = '1'
                return False
        else:
            guardarIntentoFallido(usuario)
            msg = 'usuario o clave incorrecta'
            error = '1'
            return False

    except Exception as e:

        msg = str(e)
        error = '1'
        return False

def guardarIntentoFallido(usuario):
    
    global msg
    global error

    try:

        usuario_fallido_select = models.usuarios.objects.using('usuarios').raw('''
            SELECT 
                id, 
                usuario, 
                clave,  
                correo, 
                fecha_ultimo_acceso, 
                hora_ultimo_acceso, 
                intentos, activo
            FROM 
                usuarios 
            WHERE 
                usuario = "%s"
        ''' %  (usuario))

        if len(usuario_fallido_select) >= 1:

            activo = 'True' if str(usuario_fallido_select[0].activo) == '' else usuario_fallido_select[0].activo
            intentos  = int(usuario_fallido_select[0].intentos) if str(usuario_fallido_select[0].intentos).isnumeric() else 0
            intentos += 1

            sql = ''
            if intentos < 4:
                sql = 'UPDATE usuarios SET intentos = %s WHERE usuario = "%s"' % (intentos, usuario)
            elif(intentos >= 3 and activo == 'True'):
                sql = 'UPDATE usuarios SET intentos = %s, activo = "False" WHERE usuario = "%s"' % (intentos, usuario)
            else:
                pass

            if sql != '':
                cursor = connections['usuarios'].cursor()
                cursor.execute(sql)
   

        else:
            # Usuario no encontrado
               pass

    except Exception as e:
        msg = str(e)
        error = '1'

def guardarUltimaEntrada(usuario):
    
    global msg
    global error

    try:

        today = datetime.now()
        date = today.strftime("%Y-%m-%d")
        time = today.strftime("%H:%M:%S")

        sql = '''
            UPDATE 
                usuarios 
            SET 
                fecha_ultimo_acceso = "%s", 
                hora_ultimo_acceso = "%s" 
            WHERE 
                usuario = "%s"
             ''' % (date, time, usuario)


        cursor = connections['usuarios'].cursor()
        cursor.execute(sql)
   
    except Exception as e:
        msg = str(e)
        error = 1
        pass



    #rows = []

    #with connections['usuarios'].cursor() as cursor:
    #    cursor.execute('''
    #        SELECT 
    #            id, 
    #            usuario, 
    #            clave,  
    #            correo, 
    #            fecha_ultimo_acceso, 
    #            hora_ultimo_acceso, 
    #            intentos, activo
    #        FROM 
    #            usuarios 
    #        WHERE 
    #            usuario = "%s"
    #            AND 
    #            clave = "%s"
    #            AND
    #            activo = 'True'
    #    ''' %  (usuario, clave) )
    #    rows = cursor.fetchall()

    #if len(rows) == 0:
    #    return False
    #else:
    #    return True


    






