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

    nombre_origen = models.CharField((""), max_length=50)
    compania_origen = models.CharField((""), max_length=50)
    telefono_origen = models.CharField((""), max_length=50)
    correo_origen = models.CharField((""), max_length=50)
    direccion_origen = models.CharField((""), max_length=130)
    suburbio_origen = models.CharField((""), max_length=130)
    ciudad_origen = models.CharField((""), max_length=50)
    codigo_postal_origen = models.CharField((""), max_length=50)
    estado_origen = models.CharField((""), max_length=50)
    pais_origen = models.CharField((""), max_length=50)
    pais_origen_iso = models.CharField((""), max_length=50)
    

    class Meta:
        verbose_name = "ordenes_origen"



class ordenes_destino(models.Model):

    id = models.IntegerField(primary_key=True)
    referencia = models.CharField((""), max_length=50)
    orden = models.CharField((""), max_length=50)

    nombre_destino = models.CharField((""), max_length=50)
    compania_destino = models.CharField((""), max_length=50)
    telefono_destino = models.CharField((""), max_length=50)
    correo_destino = models.CharField((""), max_length=50)
    direccion_destino = models.CharField((""), max_length=130)
    suburbio_destino = models.CharField((""), max_length=130)
    ciudad_destino = models.CharField((""), max_length=50)
    codigo_postal_destino = models.CharField((""), max_length=50)
    estado_destino = models.CharField((""), max_length=50)
    pais_destino = models.CharField((""), max_length=50)
    pais_destino_iso = models.CharField((""), max_length=50)
    

    class Meta:
        verbose_name = "ordenes_destino"



class ordenes_item(models.Model):

    id = models.IntegerField(primary_key=True)
    referencia = models.CharField((""), max_length=50)
    orden = models.CharField((""), max_length=50)

    item_nombre = models.CharField((""), max_length=50)
    item_peso = models.CharField((""), max_length=50)
    item_precio = models.CharField((""), max_length=50)
    item_sku = models.CharField((""), max_length=50)
    item_pais_manofacturacion = models.CharField((""), max_length=130)
    item_hscode_exportacion = models.CharField((""), max_length=130)
    item_hscode_importacion = models.CharField((""), max_length=50)
    item_size = models.CharField((""), max_length=50)
    item_color = models.CharField((""), max_length=50)

    class Meta:
        verbose_name = "ordenes_item"



class ordenes_caja(models.Model):

    id = models.IntegerField(primary_key=True)
    referencia = models.CharField((""), max_length=50)
    orden = models.CharField((""), max_length=50)

    caja_numero = models.CharField((""), max_length=130)
    caja_nombre = models.CharField((""), max_length=130)
    caja_alto = models.CharField((""), max_length=50)
    caja_ancho = models.CharField((""), max_length=50)
    caja_largo = models.CharField((""), max_length=50)
    caja_peso = models.CharField((""), max_length=50)
  
    class Meta:
        verbose_name = "ordenes_caja"

