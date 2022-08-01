
from django.urls import path

from AppProject.views import inicio, clientes, empleados, productos, crear_producto, editar_producto, eliminar_producto, crear_empleado, editar_empleado, eliminar_empleado



urlpatterns = [
    path('', inicio, name="inicio"),
    path('productos/', productos, name="productos"),
    path('crear_productos/', crear_producto, name="crear_producto"),
    path('editar_producto/<producto_id>', editar_producto, name="editar_producto"),
    path('eliminar_producto/<producto_id>', eliminar_producto, name="eliminar_producto"),
    path('clientes/', clientes, name="clientes"),
    path('empleados/', empleados, name="empleados"),
    path('crear_empleado/', crear_empleado, name="crear_empleado"),
    path('editar_empleado/<empleado_id>', editar_empleado, name="editar_empleado"),
    path('eliminar_empleado/<empleado_id>', eliminar_empleado, name="eliminar_empleado"),
]