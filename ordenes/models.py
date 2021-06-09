from django.db import models

# Create your models here.

class ordenes(models.Model):

    id = models.IntegerField(primary_key=True)
    referencia = models.CharField((""), max_length=50)
    orden = models.CharField((""), max_length=50)
    fecha = models.CharField((""), max_length=50)
    estado = models.CharField((""), max_length=50)
    eliminado = models.BooleanField((""))

    class Meta:
        verbose_name = "ordenes"



class ordenes_origen(models.Model):

    id = models.IntegerField(primary_key=True)
    referencia = models.CharField((""), max_length=50)
    orden = models.CharField((""), max_length=50)

    nombre = models.CharField((""), max_length=50)
    compania = models.CharField((""), max_length=50)
    telefono = models.CharField((""), max_length=50)
    correo = models.CharField((""), max_length=50)
    direccion = models.CharField((""), max_length=130)
    suburbio = models.CharField((""), max_length=130)
    ciudad = models.CharField((""), max_length=50)
    codigo_postal = models.CharField((""), max_length=50)
    estado = models.CharField((""), max_length=50)
    pais = models.CharField((""), max_length=50)
    pais_iso = models.CharField((""), max_length=50)
    

    class Meta:
        verbose_name = "ordenes_origen"



class ordenes_destino(models.Model):

    id = models.IntegerField(primary_key=True)
    referencia = models.CharField((""), max_length=50)
    orden = models.CharField((""), max_length=50)

    nombre = models.CharField((""), max_length=50)
    compania = models.CharField((""), max_length=50)
    telefono = models.CharField((""), max_length=50)
    correo = models.CharField((""), max_length=50)
    direccion = models.CharField((""), max_length=130)
    suburbio = models.CharField((""), max_length=130)
    ciudad = models.CharField((""), max_length=50)
    codigo_postal = models.CharField((""), max_length=50)
    estado = models.CharField((""), max_length=50)
    pais = models.CharField((""), max_length=50)
    pais_iso = models.CharField((""), max_length=50)
    

    class Meta:
        verbose_name = "ordenes_destino"



class ordenes_item(models.Model):

    id = models.IntegerField(primary_key=True)
    referencia = models.CharField((""), max_length=50)
    orden = models.CharField((""), max_length=50)

    nombre = models.CharField((""), max_length=50)
    peso = models.FloatField(null=True, blank=True, default=0.0)
    precio = models.FloatField(null=True, blank=True, default=0.0)
    sku = models.CharField((""), max_length=50)
    pais_manofacturacion = models.CharField((""), max_length=130)
    hscode_exportacion = models.CharField((""), max_length=130)
    hscode_importacion = models.CharField((""), max_length=50)
    size = models.CharField((""), max_length=50)
    color = models.CharField((""), max_length=50)
    otros = models.CharField((""), max_length=100)

    class Meta:
        verbose_name = "ordenes_item"



class ordenes_caja(models.Model):

    id = models.IntegerField(primary_key=True)
    referencia = models.CharField((""), max_length=50)
    orden = models.CharField((""), max_length=50)

    numero = models.IntegerField(null=True, blank=True)
    nombre = models.CharField((""), max_length=130)
    alto = models.FloatField(null=True, blank=True, default=0.0)
    ancho = models.FloatField(null=True, blank=True, default=0.0)
    largo = models.FloatField(null=True, blank=True, default=0.0)
    peso = models.FloatField(null=True, blank=True, default=0.0)
  
    class Meta:
        verbose_name = "ordenes_caja"

