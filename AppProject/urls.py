
from django.urls import path

from AppProject.views import inicio, clientes, empleados, productos, crear_producto, editar_producto, eliminar_producto
from AppProject.views import clienteFormulario


urlpatterns = [
    path('', inicio, name="inicio"),
    path('productos/', productos, name="productos"),
    path('crear_productos/', crear_producto, name="crear_producto"),
    path('editar_producto/<producto_id>', editar_producto, name="editar_producto"),
    path('eliminar_producto/<producto_id>', eliminar_producto, name="eliminar_producto"),
    path('clientes/', clientes, name="clientes"),
    path('empleados/', empleados, name="empleados"),
    path('cliente-formulario', clienteFormulario, name = "ClienteFormulario"  )
]