from urllib import request
from django import forms

class crearProducto(forms.Form):

    nombre = forms.CharField(max_length=50)
    proveedor = forms.CharField(max_length=50)
    precio = forms.IntegerField()

class crearCliente(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    mail = forms.EmailField(max_length=254)