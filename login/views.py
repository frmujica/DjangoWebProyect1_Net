from datetime import datetime

from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpRequest
from django.conf import settings
from django.db import connections

from django.core import serializers
import json

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
            
                if request.POST.get('terminos') != 'on':
                    return render(request, 'login/acceso.html', {'entrada_estado': settings.STAUS_LOGIN, 'POST':'True', 'error':'1', 'msg':'Debe aceptar los terminos y condiciones'})

                if ( validarUsuario(request.POST.get('usuario'), request.POST.get('clave')) ) == True:
                    settings.STAUS_LOGIN = True
                else:
                    settings.STAUS_LOGIN = False
            else:
                msg = 'No ha indicado usuario/clave'
                error = '1'
                settings.STAUS_LOGIN = False

            if error == '0':
                return render(request, 'login/acceso.html', {'entrada_estado': settings.STAUS_LOGIN, 'POST':'True', 'error':error, 'msg':msg})
            else:
                return redirect('/ordenes/nuevos/')

        else:
            return render(request, 'login/acceso.html', {'entrada_estado': '', 'POST':'False', 'error':'', 'msg':''})

    except Exception as e:

        msg = str(e)
        error = '1'
        settings.STAUS_LOGIN = False
        return render(request, 'login/acceso.html', {'entrada_estado': settings.STAUS_LOGIN, 'error':error, 'msg':msg})

def listaUsuarios(request):

    usuarios, usuariosjs = fun_listaUsuarios()

    return render(request, 'login/listaUsuarios.html', {'usuarios': usuarios, 'usuariosjs': usuariosjs, 'error':error, 'msg':msg} )

def editarusuario(request, id):

    usuario, usuariojs = fun_buscarusuariosporId(id)

    return render(request, 'login/editarusuario.html', {'usuario': usuario, 'usuariojs': usuariojs, 'error':error, 'msg':msg} )

def actualizarusuario(request):

    global msg
    global error

    try:
       
        if request.method == 'POST':

            if request.POST.get('usuario') != '' and request.POST.get('clave') != '' and request.POST.get('correo') != '':
            
                if request.POST.get('guardar') == 'guardar':

                    miusuario = models.usuarios()
                    miusuario.id = request.POST.get('id')
                    miusuario.usuario = request.POST.get('usuario')
                    miusuario.clave = request.POST.get('clave')
                    miusuario.correo = request.POST.get('correo')
                    #miusuario.fecha_ultima_entrada = request.POST.get('fecha_ultima_entrada')
                    #miusuario.hora_ultima_entrada = request.POST.get('hora_ultima_entrada')
                    miusuario.intentos = request.POST.get('intentos')
                    miusuario.activo = request.POST.get('activo')
                
                    fun_actualizarusuario(miusuario)

                if request.POST.get('eliminar') == 'eliminar':
                    fun_eliminarusuario(request.POST.get('id'))


                if  error == '0' or error == '':
                    usuarios, usuariosjs = fun_listaUsuarios()
                    return render(request, 'login/listaUsuarios.html', {'usuarios': usuarios, 'usuariosjs': usuariosjs, 'error':error, 'msg':msg} )
                else:
                    usuario, usuariojs = fun_buscarusuariosporId(request.POST.get('id'))
                    return render(request, 'login/editarusuario.html', {'usuario': usuario, 'usuariojs': usuariojs, 'error':error, 'msg':msg} )
            else:
                msg = 'cumplimente todos los campos'
                error = 1
                usuario, usuariojs = fun_buscarusuariosporId(request.POST.get('id'))
                return render(request, 'login/editarusuario.html', {'usuario': usuario, 'usuariojs': usuariojs, 'error':error, 'msg':msg} )

    except Exception as e:

        msg = str(e)
        error = '1'
        usuario, usuariojs = fun_buscarusuariosporId(id)
        return render(request, 'login/editarusuario.html', {'usuario': usuario, 'usuariojs': usuariojs, 'error':error, 'msg':msg} )
 
def nuevousuario(request):

    global msg
    global error

    try:
       
        if request.method == 'POST':

            if request.POST.get('usuario') != '' and request.POST.get('clave') != '' and request.POST.get('correo') != '':
            
                miusuario = models.usuarios()
                miusuario.usuario = request.POST.get('usuario')
                miusuario.clave = request.POST.get('clave')
                miusuario.correo = request.POST.get('correo')
                miusuario.activo = request.POST.get('activo')
                
                fun_guardarnuevousuario(miusuario)

                if  error == '0' or error == '':
                    usuarios, usuariosjs = fun_listaUsuarios()
                    return render(request, 'login/listaUsuarios.html', {'usuarios': usuarios, 'usuariosjs': usuariosjs, 'error':error, 'msg':msg} )
                else:
                    return render(request, 'login/nuevousuario.html', {'error':error, 'msg':msg} )
            else:
                msg = 'cumplimente todos los campos'
                error = 1
                return render(request, 'login/nuevousuario.html', {'error':error, 'msg':msg} )
        else:

            return render(request, 'login/nuevousuario.html', {'error':error, 'msg':msg} )

    except Exception as e:

        msg = str(e)
        error = '1'
        usuario, usuariojs = fun_buscarusuariosporId(id)
        return render(request, 'login/nuevousuario.html', {'error':error, 'msg':msg} )




# Funciones locales a la vista
# ============================


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

def fun_listaUsuarios(ordenado = 'usuario', filtro = ''):
    global msg
    global error

    try:

        sql = 'SELECT id, usuario, clave, correo, fecha_ultimo_acceso, hora_ultimo_acceso, intentos, activo '
        
        if filtro != '':
            sql += 'WHERE usuario like "%' + filtro + '%" OR correo like "%' + filtro + '%" '

        sql += 'FROM usuarios '

        sql += 'ORDER BY ' + ordenado
        
        usuarios = models.usuarios.objects.using('usuarios').raw(sql)

        usuariosjs = serializers.serialize('json', usuarios, fields=('id', 'usuario', 'clave', 'correo', 'fecha_ultimo_acceso', 'hora_ultimo_acceso', 'intentos', 'activo'))

        return usuarios, usuariosjs

    except Exception as e:

        msg = str(e)
        error = '1'
        return False, False

def fun_buscarusuariosporId(id):
    global msg
    global error

    try:

        sql = 'SELECT id, usuario, clave, correo, fecha_ultimo_acceso, hora_ultimo_acceso, intentos, activo '
        
        sql += 'FROM usuarios '

        sql += 'WHERE id = ' + id 
        
        usuario = models.usuarios.objects.using('usuarios').raw(sql)

        usuariojs = serializers.serialize('json', usuario, fields=('id', 'usuario', 'clave', 'correo', 'fecha_ultimo_acceso', 'hora_ultimo_acceso', 'intentos', 'activo'))

        return usuario, usuariojs

    except Exception as e:

        msg = str(e)
        error = '1'
        return False, False

def fun_actualizarusuario(usuario):

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
                usuario = "%s",
                clave = "%s",
                correo = "%s",
                intentos = %s,
                activo = "%s"
            WHERE 
                id = "%s"
             ''' % (usuario.usuario, usuario.clave, usuario.correo, usuario.intentos, usuario.activo, usuario.id)


        cursor = connections['usuarios'].cursor()
        cursor.execute(sql)
   
    except Exception as e:
        msg = str(e)
        error = 1
        pass

def fun_eliminarusuario(id):

    global msg
    global error

    try:
        sql = '''
            DELETE FROM usuarios 
            WHERE id = "%s"
             ''' % (id)

        cursor = connections['usuarios'].cursor()
        cursor.execute(sql)
   
    except Exception as e:
        msg = str(e)
        error = 1
        pass

def fun_guardarnuevousuario(usuario):
    
    global msg
    global error

    try:

        sql = '''
            INSERT INTO usuarios (usuario, clave, correo, intentos, activo) VALUES ("%s", "%s", "%s", 0, "%s") 
             ''' % (usuario.usuario, usuario.clave, usuario.correo, usuario.activo)

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


    






