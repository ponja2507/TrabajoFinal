from django.db import models

# Create your models here.

class Cliente (models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    mail = models.EmailField(max_length=254)

class Producto (models.Model):
    nombre = models.CharField(max_length=50)
    proveedor = models.CharField(max_length=50)
    precio = models.IntegerField()

class Empleado (models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    puesto = models.CharField(max_length=50)

