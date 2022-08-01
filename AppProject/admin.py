from django.contrib import admin
from AppProject.models import Cliente, Empleado, Producto

from AppProject.models import Cliente, Empleado, Producto

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(Empleado)
