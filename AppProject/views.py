from django.shortcuts import redirect, render
from django.db.models import Q

from AppProject.models import Producto, Empleado, Cliente
from AppProject.forms import crearProducto, crearEmpleado, crearProducto

# Create your views here.

def inicio(request):

    return render (request, 'inicio.html')

# <---------- PRODUCTOS ---------->

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
            producto.proveedor = dato_producto["proveedor"]
            producto.precio = dato_producto["precio"]
            producto.save()

            return redirect("productos")

    
    formulario = crearProducto(initial={"nombre":producto.nombre, "proveedor":producto.proveedor, "precio": producto.precio})
    
    return render(request,"producto_form.html",{"form":formulario})

def eliminar_producto(request,producto_id):

    producto = Producto.objects.get(id=producto_id)
    producto.delete()

    return redirect("productos")

# <---------- CLIENTES ---------->
def clientes(request):
    return render (request, 'clientes.html')

def clienteFormulario(request):
    if request.method == 'POST':

        cliente = Cliente(nombre=request.POST['nombre'], apellido=request.POST['apellido'], mail=request.POST['mail'])
        cliente.save()

        return render(request,"clientes.html")

    return render (request,"clienteFormulario.html")

def vistaClientes(self):
    listaClientes = Cliente.objects.all()
    return render(self, "clientes.html", {"vistaClientes": listaClientes})

# <---------- EMPLEADOS ---------->
def empleados(request):

    if request.method == "POST":
        
        search = request.POST["search"]

        if search != "":

            empleados = Empleado.objects.filter( Q(nombre__icontains=search) | Q(apellido__icontains=search) | Q(puesto__icontains=search) ).values()

            return render(request,"empleados.html",{"empleados":empleados, "search":True, "busqueda":search})

    empleados = Empleado.objects.all()

    return render (request, 'empleados.html', {'empleados':empleados})

def crear_empleado(request):
    
        if request.method == "POST":
        
            formulario = crearEmpleado(request.POST)

            if formulario.is_valid():
            
                dato = formulario.cleaned_data

                empleado = Empleado(nombre=dato["nombre"], apellido=dato["apellido"],puesto=dato["puesto"])
                empleado.save()

                return redirect("empleados")

            return render(request,"empleado_form.html",{"form":formulario})

        formulario = crearEmpleado()

        return render(request,"empleado_form.html",{"form":formulario})

def editar_empleado(request,empleado_id):

    empleado = Empleado.objects.get(id=empleado_id)

    if request.method == "POST":

        formulario = crearEmpleado(request.POST)

        if formulario.is_valid():
            
            dato_empleado = formulario.cleaned_data
            
            empleado.nombre = dato_empleado["nombre"]
            empleado.apellido = dato_empleado["apellido"]
            empleado.puesto = dato_empleado["puesto"]
            empleado.save()

            return redirect("empleados")

    
    formulario = crearEmpleado(initial={"nombre":empleado.nombre, "apellido":empleado.apellido, "puesto": empleado.puesto})
    
    return render(request,"empleado_form.html",{"form":formulario})


def eliminar_empleado(request,empleado_id):

    empleado = Empleado.objects.get(id=empleado_id)
    empleado.delete()

    return redirect("empleados")

