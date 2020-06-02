from django.shortcuts import render, redirect
from  django.http import HttpResponse
from TiendaEquipo.forms import FormularioCliente, FormularioProveedor, FormularioProducto, FormularioVenta
from TiendaEquipo.models import Cliente, Proveedor, Producto, Venta
from django.contrib.auth.decorators import login_required
import datetime

#Creación de Vistas

#Decorador que indica que el usuario necesita iniciar sesión para acceder.
@login_required
#Función de Inicio crea instancias de todos los objetos de las clases y las agrega al diccionario.
def home(request):
    cantidades = {
        'clientes': Cliente.objects.all(),
        'proveedores': Proveedor.objects.all(),
        'productos': Producto.objects.all(),
        'ventas': Venta.objects.all(),
        'categorias': 38,
    }
    return render(request, "TiendaEquipo/home.html", cantidades)

#Se utiliza para redirigir al usuario a la vista de inicio de sesión al acceder al localhost.
def redireccion(request):
    return redirect('login')

#Ingresa nuevos clientes a través de FormularioCliente(), este recibe los parámetros request.POST para indicar 
#que el envío del formulario es de tipo POST, request.FILES para indicar que se envían archivos. 
def nuevo_cliente(request):
    #Validacion para recibir datos del formulario o mostrarlo vacío.
    if request.method == "POST":
        #Recibe el formulario con el método POST y recibe archivos.
        form = FormularioCliente(request.POST, files=request.FILES)
        #Se valida si todos los datos del formulario son correctos.
        if form.is_valid():
            #Se guarda el formulario en la BBDD.
            form.save()
            #Al guardar todo en la BBDD se redirige a la url lista_clientes.
            return redirect("lista_clientes")

    else:
        form = FormularioCliente() 
    #Carga de la plantilla nuevo_cliente y un diccionario para el contexto.
    return render(request, "TiendaEquipo/nuevo_cliente.html", {'form': form})

#Muestra la lista de clientes.
def lista_clientes(request):
    #Se instancian todos los objetos de Cliente.
    clientes = Cliente.objects.all()
    #Carga de la plantilla lista_clientes y un diccionario para el contexto.
    return render(request, "TiendaEquipo/lista_clientes.html", {'clientes': clientes})

#Permite realizar la búsqueda de un cliente a través de su nombre.
def busqueda_clientes(request):
    #Validacion para recibir datos del formulario o mostrar mensaje de campo vacío.
    if request.GET["cli"]:
        #Se obtiene la consulta ingresada en el formulario.
        cliente = request.GET["cli"]
        #Si el nombre es demasiado largo se crea un mensaje de error.
        if len(cliente) > 30:
            mensaje = "Nombre Demasiado Largo"
        
        else:
            #Utiliza la consulta para buscar una coincidencia en el nombre.
            clientes = Cliente.objects.filter(nombre__icontains = cliente)
            #Carga de la plantilla resultado_clientes y un diccionario para el contexto.
            return render(request, "TiendaEquipo/resultado_clientes.html", {"clientes": clientes, "query": cliente})
    
    else:
        mensaje = "Por Favor Ingrese Datos al Realizar la Búsqueda"
    #Carga de la plantilla resultado_clientes y un diccionario para el contexto.
    return render(request, "TiendaEquipo/resultado_clientes.html", {"mensaje": mensaje})

#Modifica clientes a través de FormularioCliente(), este recibe los parámetros request.POST para indicar 
#que el envío del formulario es de tipo POST, request.FILES para indicar que se envían archivos. 
def modificar_cliente(request, id):
    #Se instancia Cliente a través del id.
    cliente = Cliente.objects.get(id=id)
    #Se crea el diccionario con el objeto que coincide con el id.
    data = {
        'form': FormularioCliente(instance=cliente)
    }
    #Validacion para recibir datos del formulario.
    if request.method == "POST":
        #Se cargan en el formulario los datos del cliente.
        formulario = FormularioCliente(data=request.POST, instance=cliente, files=request.FILES)
        #Se valida si todos los datos del formulario son correctos.
        if formulario.is_valid():
            #Se guarda el formulario en la BBDD.
            formulario.save()
            #Al guardar todo en la BBDD se redirige a la url lista_clientes.
            return redirect("lista_clientes")

        #Carga de formulario con los nuevos datos guardados.
        data['form'] = FormularioCliente(instance=Cliente.objects.get(id=id))
    #Carga de la plantilla modificar_cliente y un diccionario para el contexto.
    return render(request, 'TiendaEquipo/modificar_cliente.html', data)

#Elimina clientes de la BBDD.
def eliminar_cliente(request, id):
    #Se instancia Cliente a través del id.
    cliente = Cliente.objects.get(id=id)
    #Se elimina ese registro de la BBDD.
    cliente.delete()
    #Redirige a la url lista_clientes.
    return redirect("lista_clientes")

#Ingresa nuevos proveedores a través de FormularioProveedor(), este recibe los parámetros request.POST para
#indicar que el envío del formulario es de tipo POST. Muestra una lista de todos los proveedores registrados.
def proveedores(request):
    #Se instancian todos los objetos de Proveedor.
    proveedores = Proveedor.objects.all()
    #Validacion para recibir datos del formulario o mostrarlo vacío.
    if request.method == "POST":
        #Recibe el formulario con el método POST.
        form = FormularioProveedor(request.POST)
        #Se valida si todos los datos del formulario son correctos.
        if form.is_valid():
            #Se guarda el formulario en la BBDD.
            form.save()
            #Al guardar todo en la BBDD se redirige a la url proveedores.
            return redirect("proveedores")

    else:
        form = FormularioProveedor()
    #Carga de la plantilla proveedores y un diccionario para el contexto.
    return render(request, "TiendaEquipo/proveedores.html", {'form': form, 'proveedores': proveedores})

#Modifica proveedores a través de FormularioProveedor(), este recibe los parámetros
#request.POST para indicar que el envío del formulario es de tipo POST. 
def modificar_proveedor(request, id):
    #Se instancia Proveedor a través del id.
    proveedor = Proveedor.objects.get(id=id)
    #Se crea el diccionario con el objeto que coincide con el id.
    data = {
        'form': FormularioProveedor(instance=proveedor)
    }
    #Validacion para recibir datos del formulario.
    if request.method == "POST":
        #Se cargan en el formulario los datos del proveedor.
        formulario = FormularioProveedor(data=request.POST, instance=proveedor, files=request.FILES)
        #Se valida si todos los datos del formulario son correctos.
        if formulario.is_valid():
            #Se guarda el formulario en la BBDD.
            formulario.save()
            #Al guardar todo en la BBDD se redirige a la url proveedores.
            return redirect("proveedores")
        #Carga de formulario con los nuevos datos guardados.
        data['form'] = FormularioProveedor(instance=Proveedor.objects.get(id=id))
    #Carga de la plantilla modificar_proveedor y un diccionario para el contexto.
    return render(request, 'TiendaEquipo/modificar_proveedor.html', data)

#Ingresa nuevos productos a través de FormularioProducto(), este recibe los parámetros request.POST para
#indicar que el envío del formulario es de tipo POST, request.FILES para indicar que se envían archivos. 
def nuevo_producto(request):
    #Validacion para recibir datos del formulario o mostrarlo vacío.
    if request.method == "POST":
        #Recibe el formulario con el método POST y recibe archivos.
        form = FormularioProducto(request.POST, files=request.FILES)
        #Se valida si todos los datos del formulario son correctos.
        if form.is_valid():
            #Se obtienen los datos del formulario pero aún no se guardan en la BBDD.
            formulario = form.save(commit=False)
            #Se ingresa la fecha actual en el campo fecha_ingreso del formulario.
            formulario.fecha_ingreso = datetime.date.today()
            #Se obtiene el precio y las unidades ingresadas.
            nuevas_unidades = form.cleaned_data['unidades']
            precio = form.cleaned_data['precio_compra']
            #Se obtiene el nombre del producto.
            nuevo_producto = form.cleaned_data['nombre_producto']
            #Se calcula el total.
            formulario.precio_total_compra = nuevas_unidades * precio
            #Se buscan productos existentes con el mismo nombre ingresado.
            prod = Producto.objects.filter(nombre_producto=nuevo_producto)
            #Se valida si ya existe el producto
            if prod:
                #Si el producto ya existe únicamente se suman las unidades ingresadas.
                producto = Producto.objects.get(nombre_producto=nuevo_producto)
                unidades = producto.unidades
                total_unidades = unidades + nuevas_unidades
                producto.unidades = total_unidades
                #Se guarda el formulario con las nuevas unidades en la BBDD.
                producto.save()
                #Al guardar todo en la BBDD se redirige a la url inventario.
                return redirect("inventario")

            else:
                #Si no existe se guarda el formulario con todos los datos en la BBDD.
                formulario.save()
                #Al guardar todo en la BBDD se redirige a la url inventario.
                return redirect("inventario")

    else:
        form = FormularioProducto()
    #Carga de la plantilla nuevo_producto y un diccionario para el contexto.
    return render(request, "TiendaEquipo/nuevo_producto.html", {'form': form})

#Muestra la lista de productos.
def inventario(request):
    #Se instancian todos los objetos de Producto.
    productos = Producto.objects.all()
    #Carga de la plantilla inventario y un diccionario para el contexto.
    return render(request, "TiendaEquipo/inventario.html", {'productos': productos})

#Muestra los productos existentes.
def productos(request):
    #Se instancian todos los objetos de Producto.
    productos = Producto.objects.all()
    #Carga de la plantilla productos y un diccionario para el contexto.
    return render(request, "TiendaEquipo/productos.html", {'productos': productos})

#Agrega nuevas unidades a los productos existentes.
def anadir_unidades(request, id):
    #Validacion para recibir datos del formulario o mostrar mensaje de campo vacío.
    if request.GET["cant"]:
        #Se obtiene la cantidad ingresada en el formulario.
        get = request.GET["cant"]
        #Se convierte la cantidad ingresada a tipo entero.
        nuevas_unidades = int(get)
        #Se instancia Producto a través del id.
        producto = Producto.objects.get(id=id)
        #Se obtienen las unidades existentes del producto.
        unidades = producto.unidades
        #Se suman las nuevas unidades y las existentes y se guardan.
        total_unidades = unidades + nuevas_unidades
        producto.unidades = total_unidades
        producto.save()

    else:
        #Si no se ingresa nada se toman nuevas unidades como 0 y se repite el procedimiento.
        nuevas_unidades = 0
        producto = Producto.objects.get(id=id)
        unidades = producto.unidades
        total_unidades = unidades + nuevas_unidades
        producto.unidades = total_unidades
        producto.save()
    #Redirige a la url productos.
    return redirect("productos")

#Modifica productos a través de FormularioProducto(), este recibe los parámetros request.POST para indicar 
#que el envío del formulario es de tipo POST, request.FILES para indicar que se envían archivos. 
def modificar_producto(request, id):
    #Se instancia Producto a través del id.
    producto = Producto.objects.get(id=id)
    #Se crea el diccionario con el objeto que coincide con el id.
    data = {
        'form': FormularioProducto(instance=producto)
    }
    #Validacion para recibir datos del formulario.
    if request.method == "POST":
        #Se cargan en el formulario los datos del producto.
        formulario = FormularioProducto(data=request.POST, instance=producto, files=request.FILES)
        #Se valida si todos los datos del formulario son correctos.
        if formulario.is_valid():
            #Se guarda el formulario en la BBDD.
            formulario.save()
            #Al guardar todo en la BBDD se redirige a la url inventario.
            return redirect("inventario")
        #Carga de formulario con los nuevos datos guardados.
        data['form'] = FormularioProducto(instance=Producto.objects.get(id=id))
    #Carga de la plantilla modificar_producto y un diccionario para el contexto.
    return render(request, 'TiendaEquipo/modificar_producto.html', data)

#Permite realizar la búsqueda de un producto a través de su nombre.
def busqueda_productos(request):
    #Validacion para recibir datos del formulario o mostrar mensaje de campo vacío.
    if request.GET["prod"]:
        #Se obtiene la consulta ingresada en el formulario.
        producto = request.GET["prod"]
        #Si el nombre es demasiado largo se crea un mensaje de error.
        if len(producto) > 50:
            mensaje = "Nombre de Producto Demasiado Largo"

        else:
            #Utiliza la consulta para buscar una coincidencia en el nombre.
            productos = Producto.objects.filter(nombre_producto__icontains = producto)
            #Carga de la plantilla resultado_productos y un diccionario para el contexto.
            return render(request, "TiendaEquipo/resultado_productos.html", {"productos": productos, "query": producto})
    
    else:
        mensaje = "Por Favor Ingrese Datos al Realizar la Búsqueda"
    #Carga de la plantilla resultado_productos y un diccionario para el contexto.
    return render(request, "TiendaEquipo/resultado_productos.html", {"mensaje": mensaje})

#Elimina productos de la BBDD.
def eliminar_producto(request, id):
    #Se instancia Producto a través del id.
    producto = Producto.objects.get(id=id)
    #Se elimina ese registro de la BBDD.
    producto.delete()
    #Redirige a la url inventario.
    return redirect("inventario")

#Ingresa nuevas ventas a través de FormularioVenta(), este recibe los parámetros request.POST para
#indicar que el envío del formulario es de tipo POST. Muestra una lista de todas las ventas registradas.
def ventas(request):
    mensaje = ''
    #Se instancian todos los objetos de Venta.
    ventas = Venta.objects.all()
    #Validacion para recibir datos del formulario o mostrarlo vacío.
    if request.method == "POST":
        #Recibe el formulario con el método POST.
        form = FormularioVenta(request.POST)
        #Se valida si todos los datos del formulario son correctos.
        if form.is_valid():
            #Se obtienen los datos del formulario pero aún no se guardan en la BBDD.
            venta = form.save(commit=False)
            #Se ingresa la fecha actual en el campo fecha_ingreso del formulario.
            venta.fecha = datetime.date.today()
            #Se obtiene el producto y las unidades ingresadas.
            cantidad = form.cleaned_data['cantidad']
            nombre = form.cleaned_data['producto']
            #Se busca el producto existente con el mismo nombre ingresado.
            producto = Producto.objects.get(nombre_producto=nombre)
            #Se obtienen las unidades existentes del producto.
            unidades = producto.unidades
            #Se valida que la existen suficientes unidades para la cantidad ingresada.
            if cantidad > unidades:
                mensaje = f'No existen suficientes unidades, por favor ingrese una cantidad menor o igual a {unidades}'

            else:
                #Se calcula el total de la venta.
                venta.total = cantidad * producto.precio_venta
                #Se guarda el formulario en la BBDD.
                venta.save()
                #Se resta de las unidades existentes del producto la cantidad de la venta.
                total_unidades = unidades - cantidad
                #Se guardan las nuevas unidades en la BBDD.
                producto.unidades = total_unidades
                producto.save()
                #Al guardar todo en la BBDD se redirige a la url ventas.
                return redirect("ventas")

    else:
        form = FormularioVenta()
    #Carga de la plantilla ventas y un diccionario para el contexto.
    return render(request, "TiendaEquipo/ventas.html", {'form': form, 'ventas': ventas, 'mensaje': mensaje})

#Elimina ventas de la BBDD.
def eliminar_venta(request, id):
    #Se instancia Venta a través del id.
    venta = Venta.objects.get(id=id)
    #Se obtiene el nombre del producto asociado a la venta.
    nombre = venta.producto
    #Se instancia Producto a través del nombre.
    producto = Producto.objects.get(nombre_producto=nombre)
    #Se obtienen las unidades existentes del producto.
    unidades = producto.unidades
    #Se obtiene la cantidad de unidades de la venta.
    cantidad = venta.cantidad
    #Se agregan la cantidad de unidades de la venta a las unidades existentes del producto.
    nuevas_unidades = unidades + cantidad
    #Se guardan las nuevas unidades en la BBDD.
    producto.unidades = nuevas_unidades
    producto.save()
    #Se elimina ese registro de la BBDD.
    venta.delete()
    #Redirige a la url ventas.
    return redirect("ventas")

#Muestra la factura.
def factura(request, id):
    #Se instancia Venta a través del id.
    ventas = Venta.objects.get(id=id)
    #Se obtiene el nombre del producto asociado a la venta.
    producto_busqueda = ventas.producto
    #Se instancia Producto a través del nombre.
    producto = Producto.objects.get(nombre_producto=producto_busqueda)
    #Se obtiene el precio de venta del producto.
    precio = producto.precio_venta
    #Se obtiene el id del cliente asociado a la venta.
    id_busqueda = ventas.cliente.id
    #Se instancia Cliente a través del id.
    cliente = Cliente.objects.get(id=id_busqueda)
    #Se obtiene la dirección del cliente.
    direccion = cliente.direccion
    #Se obtiene el nit del cliente.
    nit = cliente.nit
    #Se obtiene el número de venta.
    numero = ventas.numeroVenta
    #Se genera el número de factura.
    numero_factura = numero + 1100
    #Diccionario con los valores obtenidos.
    data = {
        'ventas':ventas ,
        'precio': precio,
        'nit': nit,
        'direccion': direccion,
        'numero': numero_factura
    }
    #Carga de la plantilla factura y un diccionario para el contexto.
    return render(request, 'TiendaEquipo/factura.html', data)