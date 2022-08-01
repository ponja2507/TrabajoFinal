from django.db import models

# Create your models here.

class Cliente (models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    mail = models.EmailField(max_length=254)

    def __str__(self) -> str:
        return f'Apellido y Nombre: {self.apellido}, {self.nombre} || E-mail: {self.mail}'

class Producto (models.Model):
    nombre = models.CharField(max_length=50)
    proveedor = models.CharField(max_length=50)
    precio = models.IntegerField()
    
    def __str__(self) -> str:
        return f'Producto: {self.nombre} | Proveedor: {self.proveedor} | Precio: {self.precio}'

class Empleado (models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    puesto = models.CharField(max_length=50)
    def __str__(self) -> str:
        return f'Nombre: {self.nombre} | Apellido: {self.apellido} | Puesto: {self.puesto}'
