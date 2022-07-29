from django.shortcuts import redirect, render
from django.db.models import Q

from AppProject.models import Producto
from AppProject.forms import crearProducto

# Create your views here.

def inicio(request):

    return render (request, 'inicio.html')

#PRODUCTOS

def productos(request):

    if request.method == "POST":
        
        search = request.POST["search"]

        if search != "":

            productos = Producto.objects.filter( Q(nombre__icontains=search) | Q(proveedor__icontains=search) | Q(precio__icontains=search) ).values()

            return render(request,"productos.html",{"productos":productos, "search":True, "busqueda":search})

    productos = Producto.objects.all()

    return render (request, 'productos.html', {'productos':productos})

def crear_producto(request):
    
        if request.method == "POST":
        
            formulario = crearProducto(request.POST)

            if formulario.is_valid():
            
                dato = formulario.cleaned_data

                producto = Producto(nombre=dato["nombre"], proveedor=dato["proveedor"],precio=dato["precio"])
                producto.save()

                return redirect("productos")

            return render(request,"producto_form.html",{"form":formulario})

        formulario = crearProducto()

        return render(request,"producto_form.html",{"form":formulario})

def editar_producto(request,producto_id):

    producto = Producto.objects.get(id=producto_id)

    if request.method == "POST":

        formulario = crearProducto(request.POST)

        if formulario.is_valid():
            
            dato_producto = formulario.cleaned_data
            
            producto.nombre = dato_producto["nombre"]
            producto.apellido = dato_producto["apellido"]
            producto.email = dato_producto["email"]
            producto.save()

            return redirect("productos")

    
    formulario = crearProducto(initial={"nombre":producto.nombre, "apellido":producto.apellido, "email": producto.email})
    
    return render(request,"producto_form.html",{"form":formulario})


def eliminar_producto(request,producto_id):

    producto = Producto.objects.get(id=producto_id)
    producto.delete()

    return redirect("productos")





#CLIENTES
def clientes(request):
    
    return render (request, 'clientes.html')

def empleados(request):
    
    return render (request, 'empleados.html')
