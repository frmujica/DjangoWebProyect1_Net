from django.db import models

# Create your models here.

class usuarios(models.Model):

    id = models.IntegerField(primary_key=True)
    usuario = models.CharField((""), max_length=50)
    clave = models.CharField((""), max_length=50)
    correo = models.CharField((""), max_length=50)
    fecha_ultimo_acceso = models.DateField((""), auto_now=True)
    hora_ultimo_acceso = models.DateTimeField((""), auto_now=True)
    intentos = models.IntegerField((""))
    activo = models.BooleanField((""))

    class Meta:
        verbose_name = "usuarios"

class usuarios_logs(models.Model):

    id = models.IntegerField(primary_key=True)
    id_usuario = models.IntegerField()
    usuario = models.CharField((""), max_length=50)
    fecha = models.DateField()
    hora = models.DateTimeField()
    accion = models.CharField((""), max_length=50)

    class Meta:
        verbose_name = "usuarios_logs"



