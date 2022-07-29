from urllib import request
from django import forms

class crearProducto(forms.Form):

    nombre = forms.CharField(max_length=50)
    proveedor = forms.CharField(max_length=50)
    precio = forms.IntegerField()

