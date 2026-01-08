#DÍA 1 A: IMPORTACIÓN DE MODELOS
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Region, Comuna, EstadoEnvio, EstadoHora, HorasDisponibles, TipoUsuario, EstadoUsuario, TipoTarjeta, TipoProducto, EstadoProducto, Usuario, Tarjeta, Producto, Compra, Carrito, EstadoReparacion, Reparacion, Proveedor, HistorialAcciones
from datetime import datetime,  timedelta
from django.urls import reverse
from django.db.models import Q, Max, Sum
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from .models import Usuario
from django.shortcuts import render
from django.utils import timezone
from . import views
from datetime import date, datetime
import random 
from collections import defaultdict
import json
from functools import wraps
from django.http import JsonResponse
from django.db import transaction
from django.db.models import Count, Sum
from django.db.models.functions import TruncMonth
from django.utils.timezone import now
from django.contrib.auth.hashers import check_password, make_password # <--- Estas son las funciones correctas
from django.utils import translation
import logging
#DÍA 1 A: VIEWS DE INDEX


#######################################################################################
##                              INDEX (PÁGINA PRINCIPAL)
#######################################################################################


#A. VIEWS CREADAS PARA MOSTRAR EL INDEX, INICIO SESION Y EL REGISTRO DEL USUARIO NUEVO
def mostrarIndex(request):
    if "estadoSesion" in request.session: #Si estadoSesion(True) existe en request.session (sesion de django)
        productos = Producto.objects.all().values()#Que muestre todos los productos
        tipoProductos = TipoProducto.objects.all().values()#Que muestre todos los tipos productos
        estadoSesion = request.session.get("estadoSesion")#Que reciba el estadoSesion
        usuario = request.session.get("usuario")#reciba los datos del usuario
        datos = {
            'usuario' : usuario, #Para referirnos al usuario en el sitio web
            'estadoSesion': estadoSesion, #Para referirnos al estadoSesion en el sitio web
            'productos' : productos, #Para referirnos a los productos en el sitio web
            'tipoProductos': tipoProductos #Para referirnos a los tiposProductos en el sitio web
        }
        return render(request, "index.html", datos)
    else: #En caso contrario de que no exista estadoSesion
        usuario = Usuario.objects.all().values()#Reciba los datos del usuario, pero no el estadoSesion
        productos = Producto.objects.all().values()#Que muestre todos los productos
        tipoProductos = TipoProducto.objects.all().values()#Que muestre todos los tipos de productos
        datos = {
            'usuario': usuario, #Para referirnos al usuario en el sitio web
            'productos' : productos, #Para referirnos a productos en el sitio web
            'tipoProductos': tipoProductos #Para referirnos a los tipos de productos en el sitio web
            
        }
        return render(request, "index.html", datos)
    
def funcionFiltrarCategoria(request):
    estadoSesion = request.session.get("estadoSesion")
    tipoProductos = TipoProducto.objects.all().values()
    productos = Producto.objects.all().values()  # Productos por defecto
    error_message = None  # Inicializa el mensaje de error

    if request.method == 'POST':
        tipo_producto_id = request.POST.get('tipo_producto_id')
        if tipo_producto_id:
            productos_filtrados = Producto.objects.filter(tipoProducto_id=tipo_producto_id).values()
            if productos_filtrados:
                productos = productos_filtrados
                usuario = request.session.get("usuario")
                datos = {
                    'estadoSesion': estadoSesion,
                    'tipoProductos': tipoProductos,
                    'productos': productos,
                    'usuario' : usuario
                }
                return render(request, "index.html", datos)
            else:
                error_message = 'No hay ningún producto con esa categoría.'
                usuario = request.session.get("usuario")
                datos = {
                    'estadoSesion': estadoSesion,
                    'tipoProductos': tipoProductos,
                    'productos': productos,
                    'error': error_message,
                    'usuario' : usuario
                }
                return render(request, "index.html", datos)
    
def funcionBuscador(request):
    estadoSesion = request.session.get("estadoSesion")
    usuario = request.session.get("usuario")
    tipoProductos = TipoProducto.objects.all().values()
    productos_base = Producto.objects.all().values()  # Productos base para el caso de no búsqueda
    productos = productos_base
    error_message = None  # Inicializa el mensaje de error
    datos = {
        'estadoSesion': estadoSesion,
        'tipoProductos': tipoProductos,
        'productos': productos,
        'usuario': usuario,
        'error': error_message, 
    }
    if request.method == 'POST':
        productos_encontrado = request.POST.get('barraBuscador')
        if productos_encontrado:
            productos_filtrados = Producto.objects.filter(nombre__icontains=productos_encontrado).values()
            if productos_filtrados:
                datos['productos'] = productos_filtrados
            else:
                datos['error'] = 'No hay ningún producto con ese nombre.'
    return render(request, "index.html", datos)

    
def funcionBotones(request):
    estadoSesion = request.session.get("estadoSesion")
    if estadoSesion == True and request.method == 'POST':    
        if 'btn_comprar' in request.POST: #Primer IF para poder comprar 1 producto desde el catálogo (index.html)
            estadoSesion = request.session.get("estadoSesion")#Que reciba el estadoSesion
            usuario = request.session.get("usuario")#reciba los datos del usuario
            productos = Producto.objects.all().values()#Que muestre todos los productos (esto también ayuda a que, al pasar al siguiente enlace, envíe los datos de los productos en cada url)
            tipoProductos = TipoProducto.objects.all().values() # Para mostrar todos los tipo Productos
            producto_id = request.POST.get('producto_id') #Importante para recibir solo el producto que se seleccionó
            tipoTarjeta = TipoTarjeta.objects.all().values()
            tarjeta = Tarjeta.objects.all().values()
            region = Region.objects.all()
            print(region)
            producto = Producto.objects.get(id = producto_id)
            cantidad = float(request.POST.get('uniPro')) #Permite obtener la cantidad seleccionada
            preciotot = cantidad * producto.precio
            print(preciotot)
            datos = {
                'estadoSesion' : estadoSesion,
                'usuario' : usuario,
                'productos' : productos,
                'producto_id' : producto_id,
                'tipoProductos' : tipoProductos,
                'tipoTarjeta' : tipoTarjeta,
                'tarjeta' : tarjeta,
                'cantidad': cantidad,
                'precio' : preciotot,
                'nombreProducto' : producto.nombre,
                'region' : region
            }   
            return render(request, "Pagar.html", datos)
        
        elif 'btn_carrito' in request.POST:
            estadoSesion = request.session.get("estadoSesion")#Que reciba el estadoSesion
            usuario_data = request.session.get("usuario")#reciba los datos del usuario
            usuario_id_sesion = usuario_data[0]['id'] if usuario_data and isinstance(usuario_data, list) and usuario_data[0].get('id') else None
            productos = Producto.objects.all().values()#Que muestre todos los productos (esto también ayuda a que, al pasar al siguiente enlace, envíe los datos de los productos en cada url)
            tipoProductos = TipoProducto.objects.all().values() # Para mostrar todos los tipo Productos
            producto_id_str = request.POST.get('producto_id') #Importante para recibir solo el producto que se seleccionó
            tipoTarjeta = TipoTarjeta.objects.all().values()
            tarjeta = Tarjeta.objects.all().values()
            cantidad = float(request.POST.get('uniPro')) #Permite obtener la cantidad seleccionada
            usuario_obj = Usuario.objects.get(id = usuario_id_sesion)
            producto = Producto.objects.get(id=producto_id_str)
            lista_carrito = Carrito.objects.filter(comprador=usuario_obj, articulo=producto)
            
            if lista_carrito.exists():
                carrito = lista_carrito.first()
                cantidad_total = carrito.cantidadArt + cantidad
                if cantidad_total > producto.stock:
                    carrito.cantidadArt = producto.stock
                else:
                    carrito.cantidadArt = cantidad_total
                carrito.save()
            else:
                if cantidad <= producto.stock:
                    carrito = Carrito.objects.create(comprador=usuario_obj, articulo=producto, cantidadArt=cantidad)    
                else:
                    print("Producto fuera de stock, imposible añadir al carrito")
            datos = {
                'estadoSesion' : estadoSesion,
                'id_usuario' : usuario_id_sesion,
                'usuario' : usuario_data,
                'productos' : productos,
                'producto_id' : producto_id_str,
                'tipoProductos' : tipoProductos,
                'tipoTarjeta' : tipoTarjeta,
                'tarjeta' : tarjeta,
                'cantidad': cantidad,
                'msg': 'Tiene un nuevo Producto añadido en el Carrito'
            }   
            return render(request, "index.html", datos)
        
        elif 'btn_descartar' in request.POST:
            carrito_id_str = request.POST.get('carrito_id')
            carrito_descartar = Carrito.objects.get(id = carrito_id_str)
            carrito_descartar.delete()
            print('bien')
            return redirect("mostrarCarritoDeCompras")
        
        elif 'btn_vaciar' in request.POST:
            usuario_dict = request.session.get('usuario')
            usuario_id = usuario_dict[0].get('id') if usuario_dict and isinstance(usuario_dict, list) and usuario_dict[0].get('id') else None
            usuario = Usuario.objects.get(id=usuario_id)
            carrito_vaciar = Carrito.objects.filter(comprador=usuario).all()
            carrito_vaciar.delete()
            return redirect("mostrarCarritoDeCompras")
        
        elif 'btn_comprar2' in request.POST: #Primer IF para poder comprar 1 producto desde el catálogo (index.html)
            tipoTarjeta = TipoTarjeta.objects.all().values()
            estadoSesion = request.session.get("estadoSesion")#Que reciba el estadoSesion
            usuario_dict = request.session.get("usuario")#reciba los datos del usuario
            usuario_id = usuario_dict[0].get('id') if usuario_dict and isinstance(usuario_dict, list) and usuario_dict[0].get('id') else None
            usuario = Usuario.objects.get(id=usuario_id)
            region = Region.objects.all()
            print(region)
            productos = Producto.objects.all().values()#Que muestre todos los productos (esto también ayuda a que, al pasar al siguiente enlace, envíe los datos de los productos en cada url)
            tipoProductos = TipoProducto.objects.all().values() # Para mostrar todos los tipo Productos
            tarjeta = Tarjeta.objects.all().values()
            Toproducto = Carrito.objects.filter(comprador=usuario).select_related('articulo').order_by("id")
            #actualizar la cantidad de productos que se quieren comprar
            tabla = []
            for carrito in Toproducto:
                tabla.append({
                    'carrito_id': carrito.id,
                    'IdProducto': carrito.articulo_id,
                    'imagenProducto': carrito.articulo.imagen.url if carrito.articulo.imagen else '',  
                    'nombreProducto': carrito.articulo.nombre,
                    'precioProducto': carrito.articulo.precio,
                    'UnidadesProducto': carrito.cantidadArt,
                })
            producto = [carrito.articulo_id for carrito in Toproducto]
            producto_nombre = [carrito.articulo.nombre for carrito in Toproducto]
            cantidad = [carrito.cantidadArt for carrito in Toproducto]
            preciopro = [carrito.articulo.precio for carrito in Toproducto]
            precio = [cantidad_producto * precio_producto for cantidad_producto, precio_producto in zip(cantidad, preciopro)]
            sumpreciotot = sum(precio)
            #Ver el cómo actualizar 'cantidadArt' al type number que el usuario desee
            
            datos = {
                'estadoSesion' : request.session.get("estadoSesion"),
                'usuario' : request.session.get('usuario'),
                'productos' : productos,
                'producto_id' : producto,
                'tipoProductos' : tipoProductos,
                'tipoTarjeta' : tipoTarjeta,
                'tarjeta' : tarjeta,
                'cantidad': cantidad,
                'nombreProducto' : producto_nombre,
                'precio' : sumpreciotot,
                'region' : region
            }  
            return render(request, "Pagar.html", datos)
        elif 'btn_nav_agendar' in request.POST: #Primer IF para poder comprar 1 producto desde el catálogo (index.html)
            estadoSesion = request.session.get("estadoSesion")#Que reciba el estadoSesion
            usuario = request.session.get("usuario")#reciba los datos del usuario
            productos = Producto.objects.all().values()#Que muestre todos los productos (esto también ayuda a que, al pasar al siguiente enlace, envíe los datos de los productos en cada url)
            tipoProductos = TipoProducto.objects.all().values() # Para mostrar todos los tipo Productos
            tipoTarjeta = TipoTarjeta.objects.all().values()
            tarjeta = Tarjeta.objects.all().values()
            datos = {
                'estadoSesion' : estadoSesion,
                'usuario' : usuario,
                'productos' : productos,
                'tipoProductos' : tipoProductos,
                'tipoTarjeta' : tipoTarjeta,
                'tarjeta' : tarjeta
            }   
            return render(request, "Agendamientos.html", datos)

    else:
        return render(request, "InicioSesion.html")
    
                            
    
#######################################################################################
##                     INICIO SESION, REGISTRO USUARIO, CIERRE SESION Y ACTUALIZAR PERFIL
#######################################################################################
def mostrarRegistroUsuario(request):
    return render(request, "RegistroUsuario.html")

# --- Vista para procesar el Registro de Usuario ---
def RegistrarUsuario(request):
    if request.method == "POST":
        rut = request.POST['rutcli2']
        nom = request.POST['nomcli2']
        ape = request.POST['apecli2']
        ema = request.POST['emacli2']
        con_plano = request.POST['pascli2'] # Contraseña en texto plano
        fon = request.POST['foncli2']

        # 1. Comprobar si el RUT ya existe
        if Usuario.objects.filter(rut=rut).exists():
            messages.error(request, 'Ya hay un Usuario con ese Rut, intente con otro.')
            return render(request, "RegistroUsuario.html") # No es necesario pasar 'usu'

        # 2. Comprobar si el Email ya existe
        if Usuario.objects.filter(correo=ema).exists():
            messages.error(request, 'Ya hay un Usuario con ese Correo, intente con otro.')
            return render(request, "RegistroUsuario.html") # No es necesario pasar 'usu'
            
        # 3. Eliminar la comprobación de contraseña existente (¡muy importante!)
        # No debes comprobar si una contraseña ya existe, ya que las contraseñas se hashean
        # y no son identificadores únicos. Dos usuarios pueden tener la misma contraseña de texto
        # plano, pero sus hashes serán diferentes si se generan con "salts" aleatorios (como make_password hace).
        # if Usuario.objects.filter(contrasena=con).exists(): # <-- ¡ELIMINAR ESTO!

        # Si todo está bien, proceder con el registro
        try:
            # Generación de datos para Tarjeta (tal como lo tenías)
            tar_nro = random.randint(1111111111111111, 9999999999999999)
            fec_cad = date(2030, 2, 2)
            cvv = random.randint(100, 999)
            tip_tar = random.randint(1, 2)
            
            # Crear y guardar la Tarjeta
            nuevatarjeta = Tarjeta.objects.create(nroTarjeta=tar_nro, fechaCad=fec_cad, cvv=cvv, tipoTarjeta_id=tip_tar, saldo=100000000000)
            # nuevatarjeta.save() # .create() ya guarda el objeto

            # Obtener TipoUsuario y EstadoUsuario (asegúrate de que existan en tu DB)
            tipusu = TipoUsuario.objects.get(descripcion='CLIENTE')
            estusu = EstadoUsuario.objects.get(descripcion='Habilitado') # O 'ACTIVO' o el estado inicial que desees

            # ¡IMPORTANTE!: Hashear la contraseña antes de guardarla
            contrasena_hasheada = make_password(con_plano)

            # Crear y guardar el Usuario
            usu = Usuario(
                rut=rut,
                nombre=nom,
                apellido=ape,
                correo=ema,
                contrasena=contrasena_hasheada, # Guardamos el hash, no el texto plano
                telefono=fon,
                tipoUsuario=tipusu,
                estadoUsuario=estusu,
                tarjeta=nuevatarjeta # Asumiendo que 'tarjeta' es un ForeignKey
            )
            usu.save()
            
            messages.success(request, '¡Usuario registrado correctamente! Ya puedes iniciar sesión.')
            return redirect('mostrarInicioSesion') # Redirigimos a la página de inicio de sesión
        except TipoUsuario.DoesNotExist:
            messages.error(request, 'Error: Tipo de usuario "CLIENTE" no encontrado. Verifique su base de datos.')
            return render(request, "RegistroUsuario.html")
        except EstadoUsuario.DoesNotExist:
            messages.error(request, 'Error: Estado de usuario "Habilitado" no encontrado. Verifique su base de datos.')
            return render(request, "RegistroUsuario.html")
        except Exception as e:
            messages.error(request, f'Ocurrió un error inesperado al registrar el usuario: {e}')
            return render(request, "RegistroUsuario.html")
            
    else: # Si la solicitud no es POST (ej. alguien intenta acceder directamente a /registrar_usuario)
        messages.info(request, 'Por favor, complete el formulario de registro para crear una cuenta.')
        return redirect('mostrarRegistroUsuario') # Redirigir a la vista que muestra el formulario

# --- Vista para mostrar el HTML de Inicio de Sesión ---
def mostrarInicioSesion(request):
    # La lógica de try/except pass es innecesaria aquí, a menos que tengas algo específico que manejar.
    return render(request, "InicioSesion.html")

# --- Vista para procesar el Inicio de Sesión ---
def funcionInicioSesion(request):
    if request.method == "POST":
        correo = request.POST["correocliente"]
        contrasena_ingresada = request.POST["passwordcliente"] # Contraseña en texto plano ingresada por el usuario

        try:
            # 1. Intentar obtener el usuario por correo
            usuario = Usuario.objects.get(correo=correo)

            # 2. Verificar la contraseña ingresada contra el hash almacenado
            if check_password(contrasena_ingresada, usuario.contrasena):
                # Login exitoso

                # Actualizar estado del usuario en la base de datos
                usuario.estadoUsuario_id = 1 # 'Habilitado' o el ID que corresponda
                usuario.save(update_fields=['estadoUsuario']) # Solo guardar el campo que cambió

                # Actualizar información en la sesión
                request.session["usuario"] = [{ # Manteniendo tu formato de lista de diccionarios
                    'id': usuario.id,
                    'rut': usuario.rut,
                    'nombre': usuario.nombre,
                    'apellido': usuario.apellido,
                    'correo': usuario.correo,
                    'telefono': usuario.telefono,
                    'tipoUsuario_id': usuario.tipoUsuario_id,
                    'estadoUsuario_id': usuario.estadoUsuario_id,
                    'tarjeta_id': usuario.tarjeta_id if hasattr(usuario, 'tarjeta_id') else None # Si el usuario puede no tener tarjeta
                }]
                request.session["estadoSesion"] = True
                
                print(f"Usuario logueado y estado actualizado: {usuario.correo}, Estado: {usuario.estadoUsuario_id}")

                # Redirigir según el tipo de usuario
                if usuario.tipoUsuario_id == 2: # Asumiendo que 2 es un tipo de usuario específico
                    productos = Producto.objects.all().values()
                    tipoProductos = TipoProducto.objects.all().values()
                    datos = {
                        'usuario': request.session["usuario"],
                        'estadoSesion': request.session["estadoSesion"],
                        'productos': productos,
                        'tipoProductos': tipoProductos
                    }
                    return render(request, "index.html", datos)
                elif usuario.tipoUsuario_id == 1: # Asumiendo que 1 es otro tipo de usuario específico
                    # No necesitas volver a cargar productos/tipoProductos si solo rediriges.
                    return redirect('mostrardashboard') # Asegúrate que esta URL existe
                else:
                    messages.info(request, 'Tipo de usuario desconocido. Redirigido a la página principal.')
                    return redirect('/') # O a una página por defecto

            else:
                # Contraseña incorrecta
                messages.error(request, 'Email o contraseña erróneos, por favor, inténtelo de nuevo.')
                # No pases la contraseña de vuelta al template por seguridad
                return render(request, "InicioSesion.html", {'correo': correo}) 

        except Usuario.DoesNotExist:
            # Usuario no encontrado por el correo
            messages.error(request, 'Email o contraseña erróneos, por favor, inténtelo de nuevo.')
            return render(request, "InicioSesion.html", {'correo': correo})
        except Exception as e:
            # Capturar cualquier otro error inesperado
            messages.error(request, f'Ocurrió un error inesperado al iniciar sesión: {e}')
            return render(request, "InicioSesion.html", {'correo': correo})

    else: # Si la solicitud no es POST
        return render(request, "InicioSesion.html")
    
def funcionCerrarSesion(request):
    try:
        usu_id_from_session = request.session.get("usuario")
        if usu_id_from_session: # Asegúrate de que haya un usuario en sesión antes de intentar actualizar
            usuario_id = usu_id_from_session[0]['id']
            usuario_a_actualizar = Usuario.objects.get(id=usuario_id)
            usuario_a_actualizar.estadoUsuario_id = 2 # Marcar como desconectado en DB
            usuario_a_actualizar.save()

        # Borrar específicamente la información del usuario de la sesión
        if "usuario" in request.session:
            del request.session["usuario"]
        if "estadoSesion" in request.session: # Borra también estadoSesion si existe
            del request.session["estadoSesion"]
        
        # Redirige a la página principal. No es necesario cargar todos los datos aquí,
        # ya que la vista 'mostrarIndex' se encargará de eso.
        messages.success(request, "Sesión cerrada correctamente.")
        return redirect('mostrarIndex') # Asegúrate que 'mostrarIndex' es la URL para tu index.html

    except KeyError:
        # Esto ocurre si "usuario" o "estadoSesion" ya no están en la sesión
        messages.info(request, "No había sesión activa para cerrar.")
        return redirect('mostrarIndex')
    except Usuario.DoesNotExist:
        messages.error(request, "Error: Usuario no encontrado en la base de datos.")
        return redirect('mostrarIndex') # O a una página de error
    except Exception as e:
        messages.error(request, f"Ocurrió un error al cerrar la sesión: {e}")
        return redirect('mostrarIndex')




#######################################################################################
##                            CARRITO DE COMPRAS
#######################################################################################

def mostrarCarritoDeCompras(request):
    estadoSesion = request.session.get("estadoSesion")
    if estadoSesion is True:
        usuario = request.session.get("usuario")
        tipoProductos = TipoProducto.objects.all().values()
        productos = Producto.objects.all().values()
        if usuario:
            usuario_id = usuario[0]['id'] if usuario and isinstance(usuario, list) and usuario[0].get('id') else None
            carrito = Carrito.objects.filter(comprador = usuario_id).select_related('articulo', 'comprador').order_by("id")
            if carrito.exists():
                datos = []
                for carrito in carrito:
                    datos.append({
                        'carrito_id': carrito.id,
                        'imagenProducto': carrito.articulo.imagen.url if carrito.articulo.imagen else '',  # Aquí obtienes la URL de la imagen si existe
                        'nombreProducto': carrito.articulo.nombre,
                        'precioProducto': carrito.articulo.precio,
                        'UnidadesProducto': carrito.cantidadArt,
                        'UnidadesMaxima' : carrito.articulo.stock,
                        'producto_id' : carrito.articulo_id
                    })
                tabla = {
                    'datos' : datos,
                    'id_usuario' : usuario_id,
                    'usuario' : usuario,
                    'producto' : productos,
                    'tipoProductos': tipoProductos,
                    'estadoSesion' : estadoSesion,
                    
                }
                return render(request, "CarritodeCompras.html", tabla)
            else:
                estadoSesion = request.session.get("estadoSesion")
                usuario = request.session.get("usuario")
                tipoProductos = TipoProducto.objects.all().values()
                productos = Producto.objects.all().values()
                usuario_id = usuario[0]['id'] if usuario and isinstance(usuario, list) and usuario[0].get('id') else None 
                carrito = Carrito.objects.filter(comprador=usuario_id).select_related('articulo', 'comprador').order_by("id")
                datos = []
                for carrito in carrito:
                    datos.append({
                        'carrito_id': carrito.id,
                        'imagenProducto': carrito.articulo.imagen.url if carrito.articulo.imagen else '',  # Aquí obtienes la URL de la imagen si existe
                        'nombreProducto': carrito.articulo.nombre,
                        'precioProducto': carrito.articulo.precio,
                        'UnidadesProducto': carrito.cantidadArt,
                        'UnidadesMaxima' : carrito.articulo.stock,
                        'producto_id' : carrito.articulo_id
                    })
                tabla = {
                    'datos' : datos,
                    'id_usuario' : usuario_id,
                    'usuario' : usuario,
                    'producto' : productos,
                    'tipoProductos': tipoProductos

                }
                mensaje = "Usted no tiene Productos añadidos en su carrito de compras"
                return render(request, "CarritodeCompras.html", {'mensaje': mensaje, 'datos': datos, 'id_usuario': usuario_id, 'usuario' : usuario ,'producto' : productos,'tipoProductos' : tipoProductos , 'estadoSesion': estadoSesion})
    else:
        usuario = Usuario.objects.all().values()
        productos = Producto.objects.all().values()
        tipoProductos = TipoProducto.objects.all().values()
        datos = {
            'usuario': usuario,
            'productos': productos,
            'tipoProductos': tipoProductos
        }
        return render(request, "InicioSesion.html", datos)

        
        

#######################################################################################
##                              PAGAR
#######################################################################################
# tu_app/views.py
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import (
    Producto, TipoProducto, Region, Comuna, Usuario, Tarjeta, Compra, Carrito,
    EstadoEnvio # Usamos tu modelo correcto
)
from datetime import datetime, timedelta
from django.db.models import Max
from django.contrib import messages # Para mostrar mensajes al usuario
from django.utils import timezone # Importante para datetime en Django, especialmente si usas USE_TZ=True in settings

def funcionBotonPagar(request):
    productos = Producto.objects.all().values()
    tipoProductos = TipoProducto.objects.all().values()
    region_all = Region.objects.all()
    comuna_all = Comuna.objects.all()

    estadoSesion = request.session.get("estadoSesion")
    usuario_dict = request.session.get('usuario')
    usuario_id = None
    if usuario_dict and isinstance(usuario_dict, list) and usuario_dict:
        usuario_id = usuario_dict[0].get('id')
    
    if not usuario_id:
        messages.error(request, 'Debes iniciar sesión para realizar una compra.')
        return redirect('mostrarInicioSesion')

    usuario = Usuario.objects.get(id=usuario_id)
    saldo = usuario.tarjeta.saldo
    print(f"Saldo actual del usuario {usuario.nombre}: {saldo}")

    if request.method == 'POST':
        tipo_compra = request.POST.get('tipo_compra')
        cantidad_str = request.POST.get("cantidad")
        precio_total_form = float(request.POST.get("precio"))
        quiere_instalacion = request.POST.get('quiere_instalacion')
        producto_ide = request.POST.get("producto_id") # Can be a single ID or a string like "[id1, id2]"

        # Flag to indicate if the purchase originated from the cart (multiple items)
        # or if it's a single item purchase (direct or potentially from cart)
        is_multi_item_cart_purchase = False 
        purchased_product_obj = None # To store the product object if single purchase

        try:
            estado_seguimiento_inicial = EstadoEnvio.objects.get(nombre='Pedido Recibido')
        except EstadoEnvio.DoesNotExist:
            estado_seguimiento_inicial = EstadoEnvio.objects.create(
                nombre='Pedido Recibido',
                porcentaje_visual=0,
                orden=1,
                descripcion_cliente='Tu pedido ha sido recibido y está pendiente de procesamiento.'
            )
            print("Estado de Envío 'Pedido Recibido' creado automáticamente.")

        hoy = timezone.now()
        fecha_formato_boleta = hoy.strftime('%d%m%Y')
        
        last_boleta = Compra.objects.filter(
            nro_factura__startswith=f'B{fecha_formato_boleta}-'
        ).order_by('-id').values_list('nro_factura', flat=True).first()

        secuencia_actual = 0
        if last_boleta:
            try:
                secuencia_str = last_boleta.split('-')[-1]
                secuencia_actual = int(secuencia_str)
            except (IndexError, ValueError):
                print(f"Advertencia: Formato de nro_factura '{last_boleta}' no esperado, reiniciando secuencia.")
                secuencia_actual = 0
        
        proximo_numero_boleta = secuencia_actual + 1
        nro_factura_generado = f'B{fecha_formato_boleta}-{proximo_numero_boleta:05d}'
        
        items_a_comprar = [] # Lista para almacenar los items a procesar
        sumpreciotot = 0 # Initialize sumpreciotot

        # --- Lógica para determinar items_a_comprar ---
        # If product_id is a JSON string (meaning it came from the cart with multiple items)
        if isinstance(producto_ide, str) and producto_ide.startswith('[') and producto_ide.endswith(']'):
            print("Procesando carrito para compra online/presencial (múltiples ítems).")
            is_multi_item_cart_purchase = True # Set the flag for multi-item cart purchase
            carrito_items = Carrito.objects.filter(comprador=usuario).select_related('articulo').order_by("id")
            
            sumpreciotot = sum(item.articulo.precio * item.cantidadArt for item in carrito_items)
            
            if sumpreciotot == 0:
                messages.error(request, 'El carrito está vacío o los precios son cero.')
                return redirect(request.META.get('HTTP_REFERER', '/'))

            for item_carrito in carrito_items:
                items_a_comprar.append({
                    'producto': item_carrito.articulo,
                    'cantidad': item_carrito.cantidadArt,
                    'precio_unitario': item_carrito.articulo.precio
                })
        
        # If product_id is a single digit (meaning a direct single product purchase)
        elif isinstance(producto_ide, str) and producto_ide.isdigit():
            print("Procesando producto individual para compra online/presencial.")
            try:
                producto_obj = Producto.objects.get(id=int(producto_ide))
                purchased_product_obj = producto_obj # Store the product object for later cart removal
                cantidad_entera = int(float(cantidad_str))
                if cantidad_entera <= 0:
                    messages.error(request, 'La cantidad del producto debe ser un número positivo.')
                    return redirect(request.META.get('HTTP_REFERER', '/'))

                items_a_comprar.append({
                    'producto': producto_obj,
                    'cantidad': cantidad_entera,
                    'precio_unitario': producto_obj.precio
                })
                sumpreciotot = precio_total_form # This comes from the form for a single product
            except Producto.DoesNotExist:
                messages.error(request, 'El producto seleccionado no es válido.')
                return redirect(request.META.get('HTTP_REFERER', '/'))
            except ValueError:
                messages.error(request, 'La cantidad ingresada no es válida.')
                return redirect(request.META.get('HTTP_REFERER', '/'))
        else:
            messages.error(request, 'Tipo de producto o ID no válido para la compra.')
            return redirect(request.META.get('HTTP_REFERER', '/'))

        # --- Check if items_a_comprar is empty after parsing ---
        if not items_a_comprar:
            messages.error(request, 'No hay productos válidos para procesar la compra.')
            return redirect(request.META.get('HTTP_REFERER', '/'))


        # --- Lógica específica para compra ONLINE ---
        if tipo_compra == 'online':
            direccion_usuario = request.POST.get('direccion_envio')
            comuna_id = request.POST.get('selcomuna')
            
            if not direccion_usuario or not comuna_id:
                messages.error(request, 'Por favor, complete la dirección de envío y seleccione una comuna.')
                return redirect(request.META.get('HTTP_REFERER', '/'))
            
            try:
                comuna_obj = Comuna.objects.get(id=comuna_id)
            except Comuna.DoesNotExist:
                messages.error(request, 'La comuna seleccionada no es válida.')
                return redirect(request.META.get('HTTP_REFERER', '/'))

            horas_estimadas = float(comuna_obj.tiempo_estimado_horas)
            fecha_entrega_estimada = hoy + timedelta(hours=horas_estimadas)
            
            if saldo >= sumpreciotot:
                try:
                    with transaction.atomic():
                        tar_usu = usuario.tarjeta
                        tar_usu.saldo -= sumpreciotot
                        tar_usu.save()
                        
                        for item in items_a_comprar:
                            producto_actual = item['producto']
                            cantidad_actual = item['cantidad']

                            if producto_actual.stock < cantidad_actual:
                                raise ValueError(f"Stock insuficiente para {producto_actual.nombre}. Stock: {producto_actual.stock}, Intentado comprar: {cantidad_actual}")

                            Compra.objects.create(
                                direccion=direccion_usuario,
                                comuna_entrega=comuna_obj,
                                fecha_entrega_estimada=fecha_entrega_estimada,
                                nro_factura=nro_factura_generado,
                                estado_seguimiento=estado_seguimiento_inicial,
                                fecha_compra=hoy,
                                cantidad=cantidad_actual,
                                producto=producto_actual,
                                usuario=usuario,
                                tarjeta=tar_usu,
                                estado_compra="PENDIENTE"
                            )
                            
                            producto_actual.stock -= cantidad_actual
                            producto_actual.save()

                        # Logic to clear cart based on purchase type
                        if is_multi_item_cart_purchase:
                            # Clear entire cart if multiple items were purchased from it
                            Carrito.objects.filter(comprador=usuario).delete()
                        elif purchased_product_obj: # If a single product was purchased directly
                            # Remove only that specific product from the cart
                            Carrito.objects.filter(comprador=usuario, articulo=purchased_product_obj).delete()


                        messages.success(request, f'¡Compra online realizada con éxito! Factura {nro_factura_generado}. Revisa tu historial de compras.')
                        return redirect('mostrarHistorialDeCompras')

                except ValueError as ve:
                    messages.error(request, f"Error en la compra: {ve}")
                    return redirect(request.META.get('HTTP_REFERER', '/'))
                except Exception as e:
                    messages.error(request, f"Error inesperado al procesar la compra: {e}")
                    return redirect(request.META.get('HTTP_REFERER', '/'))
            else:
                messages.error(request, "Saldo insuficiente para completar la compra.")
                return redirect(request.META.get('HTTP_REFERER', '/'))


        # --- Lógica específica para compra PRESENCIAL ---
        elif tipo_compra == 'presencial':
            direccion_presencial = 'PRESENCIAL'

            if saldo >= sumpreciotot:
                try:
                    with transaction.atomic():
                        nuevo_saldo = saldo - sumpreciotot
                        tar_usu = usuario.tarjeta
                        tar_usu.saldo = nuevo_saldo
                        tar_usu.save()
                        
                        for item in items_a_comprar:
                            producto_actual = item['producto']
                            cantidad_actual = item['cantidad']

                            if producto_actual.stock < cantidad_actual:
                                raise ValueError(f"Stock insuficiente para {producto_actual.nombre}. Stock: {producto_actual.stock}, Intentado comprar: {cantidad_actual}")

                            Compra.objects.create(
                                direccion=direccion_presencial,
                                fecha_compra=hoy,
                                cantidad=cantidad_actual,
                                producto=producto_actual,
                                usuario=usuario,
                                tarjeta=tar_usu,
                                nro_factura=nro_factura_generado,
                                estado_compra="PENDIENTE"
                            )
                            
                            producto_actual.stock -= cantidad_actual
                            producto_actual.save()
                        
                        # Logic to clear cart based on purchase type
                        if is_multi_item_cart_purchase:
                            # Clear entire cart if multiple items were purchased from it
                            Carrito.objects.filter(comprador=usuario).delete()
                        elif purchased_product_obj: # If a single product was purchased directly
                            # Remove only that specific product from the cart
                            Carrito.objects.filter(comprador=usuario, articulo=purchased_product_obj).delete()

                        messages.success(request, f'¡Compra presencial registrada con éxito! Factura {nro_factura_generado}. Revisa tu historial. Dirijase a "Juan Enrique - Rosales 775, 2830767" Para despachar su pedido')
                        return redirect('mostrarHistorialDeCompras')
                
                except ValueError as ve:
                    messages.error(request, f"Error en la compra: {ve}")
                    return redirect(request.META.get('HTTP_REFERER', '/'))
                except Exception as e:
                    messages.error(request, f"Error inesperado al procesar la compra presencial: {e}")
                    return redirect(request.META.get('HTTP_REFERER', '/'))
            else:
                messages.error(request, "Saldo insuficiente para completar la compra.")
                return redirect(request.META.get('HTTP_REFERER', '/'))
        
        else:
            messages.error(request, 'Tipo de compra no válido.')
            return redirect(request.META.get('HTTP_REFERER', '/'))

    else:
        messages.info(request, 'Acceso inválido a la función de pago.')
        return redirect("index")
#######################################################################################
##                           SEGUIMIENTO
#######################################################################################

def get_comunas_por_region(request, region_id):
    """
    Vista que devuelve las comunas de una región específica en formato JSON.
    """
    # Filtra las comunas donde el id_region (campo 'region' en tu modelo Comuna)
    # sea igual al region_id que se pasó en la URL.
    comunas = Comuna.objects.filter(region_id=region_id).order_by('nombre')
    
    # Convierte los objetos de comuna en una lista de diccionarios.
    # JsonResponse necesita que los datos sean serializables.
    data = [{'id': comuna.id, 'nombre': comuna.nombre} for comuna in comunas]
    
    return JsonResponse(data, safe=False) # safe=False permite enviar una lista directamente

def mostrarSeguimientoCliente(request):
    if "estadoSesion" in request.session:
        productos = Producto.objects.all().values()
        tipoProductos = TipoProducto.objects.all().values()
        estadoSesion = request.session.get("estadoSesion")
        usuario_data = request.session.get("usuario")#usuario_data lo que permite es acceder y obtener los datos del usuario en una LISTA
        usuario_id = usuario_data[0]['id'] if usuario_data and isinstance(usuario_data, list) and usuario_data[0].get('id') else None #Al obtener los datos del Usuario en un lista, básicamente toma solamente el ID del usuario de esa lista
        compras_usuario = []

        if usuario_id:
            usuario_obj = Usuario.objects.get(id=usuario_id) # Obtener el objeto Usuario
            compras_usuario = Compra.objects.filter(usuario_id=int(usuario_id)).exclude(direccion = 'PRESENCIAL').select_related('producto', 'tarjeta').order_by("-fecha_compra").values(
                'id',
                'direccion',
                'fecha_compra',
                'cantidad',
                'nro_factura',
                'producto__imagen',
                'producto__nombre',
                'producto__precio',
                'estado_compra',
                'tarjeta__tipoTarjeta__tipo',
                'usuario__rut',
                'estado_compra',
                'fecha_entrega_estimada',
                'comuna_entrega_id',
                'estado_seguimiento_id',  
            )

            datos = {
                'usuario': usuario_data, # Mantener la estructura de la sesión
                'estadoSesion': estadoSesion,
                'productos': productos,
                'tipoProductos': tipoProductos,
                'compras': compras_usuario,
            }
            return render(request, "seguimiento_cliente.html", datos)
        else:
            # Manejar el caso en que no se encuentra el ID del usuario en la sesión
            datos = {
                'estadoSesion': estadoSesion,
                'tipoProductos': tipoProductos,
                'productos': productos,
                'compras': []
            }
            return render(request, "seguimiento_cliente.html", datos)
    else:
        usuario = Usuario.objects.all().values()
        productos = Producto.objects.all().values()
        tipoProductos = TipoProducto.objects.all().values()
        datos = {
            'usuario': usuario,
            'productos': productos,
            'tipoProductos': tipoProductos
        }
        return render(request, "InicioSesion.html", datos)

def visualizarSeguimientoCliente(request):
    productos = Producto.objects.all().values()
    tipoProductos = TipoProducto.objects.all().values()
    estadoSesion = request.session.get("estadoSesion")
    usuario_data = request.session.get("usuario")#usuario_data lo que permite es acceder y obtener los datos del usuario en una LISTA
    usuario_id = usuario_data[0]['id'] if usuario_data and isinstance(usuario_data, list) and usuario_data[0].get('id') else None #Al obtener los datos del Usuario en un lista, básicamente toma solamente el ID del usuario de esa lista

    usuario_dict = request.session.get('usuario')
    if usuario_dict and isinstance(usuario_dict, list) and usuario_dict:
        usuario_id = usuario_dict[0].get('id')
    
    if not usuario_id:
        messages.error(request, 'Debes iniciar sesión para ver el seguimiento de pedidos.')
        return redirect('mostrarInicioSesion')

    usuario = get_object_or_404(Usuario, id=usuario_id)
    
    compra_id = request.POST.get('compra_vis_id') # Viene del botón 'btn_seguir'
    # nro_factura = request.GET.get('nro_factura') # Podrías usarlo si pasas por GET, pero no es el caso aquí

    compra_a_mostrar = None
    if request.method == 'POST' and compra_id:
        # Acceso desde el botón 'SEGUIR' en el historial de compras
        try:
            # Aseguramos que la compra pertenezca al usuario logueado
            compra_a_mostrar = Compra.objects.get(id=compra_id, usuario=usuario)
            messages.info(request, f'Mostrando seguimiento para factura: {compra_a_mostrar.nro_factura}')
        except Compra.DoesNotExist:
            messages.error(request, 'La compra solicitada no existe o no te pertenece.')
            return redirect('mostrarHistorialDeCompras') # Redirige al historial si no encuentra la compra
    elif request.method == 'GET':
        # Este caso es un fallback si la URL de seguimiento se accede directamente
        # o si funcionBotonPagar redirigiera con un parámetro GET (que no lo hace ahora)
        # Por simplicidad, si no es POST con compra_id, redirigimos al historial.
        messages.warning(request, 'Acceso inválido al seguimiento directo. Por favor, selecciona una compra de tu historial.')
        return redirect('mostrarHistorialDeCompras')
    else:
        # Esto captura POSTs sin compra_id u otros métodos inesperados
        messages.error(request, 'Solicitud inválida para el seguimiento de la compra.')
        return redirect('mostrarHistorialDeCompras')

    if compra_a_mostrar:
        # Cargar todos los estados de envío para la barra de progreso
        estados_envio = EstadoEnvio.objects.all().order_by('orden')
        
        context = {
            'compra': compra_a_mostrar,
            'estados_envio': estados_envio,
            'tipo_acceso': 'btn_seguir', # Para que el template sepa de dónde viene
            'usuario': usuario_data,
            'estadoSesion': request.session.get("estadoSesion"),
            'tipoProductos' : tipoProductos,
            
        }
        return render(request, "Seguimiento.html", context)
    else:
        # Esto solo debería ocurrir si no se encontró la compra, y ya se manejó con un redirect.
        # Pero como una última medida, podemos devolver a una página segura.
        messages.error(request, 'No se pudo cargar la información de seguimiento.')
        return redirect('mostrarHistorialDeCompras')

def mostrarSeguimientoAdmin(request):
    if "estadoSesion" in request.session:
        productos = Producto.objects.all().values()
        tipoProductos = TipoProducto.objects.all().values()
        estadoSesion = request.session.get("estadoSesion")
        usuario_data = request.session.get("usuario")#usuario_data lo que permite es acceder y obtener los datos del usuario en una LISTA
        usuario_id = usuario_data[0]['id'] if usuario_data and isinstance(usuario_data, list) and usuario_data[0].get('id') else None #Al obtener los datos del Usuario en un lista, básicamente toma solamente el ID del usuario de esa lista
        compras_usuario = []

        if usuario_id:
            usuario_obj = Usuario.objects.get(id=usuario_id) # Obtener el objeto Usuario
            compras_usuario = Compra.objects.all().exclude(direccion = 'PRESENCIAL').select_related('producto', 'tarjeta').order_by("-fecha_compra").values(
                'id',
                'direccion',
                'fecha_compra',
                'cantidad',
                'nro_factura',
                'producto__imagen',
                'producto__nombre',
                'producto__precio',
                'estado_compra',
                'tarjeta__tipoTarjeta__tipo',
                'usuario__rut',
                'estado_compra',
                'fecha_entrega_estimada',
                'comuna_entrega_id',
                'estado_seguimiento_id',  
            )

            datos = {
                'usuario': usuario_data, # Mantener la estructura de la sesión
                'estadoSesion': estadoSesion,
                'productos': productos,
                'tipoProductos': tipoProductos,
                'compras': compras_usuario,
            }
            return render(request, "seguimiento_admin.html", datos)
        else:
            # Manejar el caso en que no se encuentra el ID del usuario en la sesión
            datos = {
                'estadoSesion': estadoSesion,
                'tipoProductos': tipoProductos,
                'productos': productos,
                'compras': []
            }
            return render(request, "seguimiento_admin.html", datos)
    else:
        usuario = Usuario.objects.all().values()
        productos = Producto.objects.all().values()
        tipoProductos = TipoProducto.objects.all().values()
        datos = {
            'usuario': usuario,
            'productos': productos,
            'tipoProductos': tipoProductos
        }
        return render(request, "InicioSesion.html", datos)

def visualizarSeguimientoAdmin(request, nro_factura = None):
    productos = Producto.objects.all().values()
    tipoProductos = TipoProducto.objects.all().values()
    
    compra_id = request.POST.get('nro_factura_admin') # Viene del botón 'btn_seguir'
    # nro_factura = request.GET.get('nro_factura') # Podrías usarlo si pasas por GET, pero no es el caso aquí

    compra_a_mostrar = None
    if request.method == 'POST' and compra_id:
        # Acceso desde el botón 'SEGUIR' en el historial de compras
        try:
            # Aseguramos que la compra pertenezca al usuario logueado
            compra_a_mostrar = Compra.objects.get(id=compra_id)
            messages.info(request, f'Mostrando seguimiento para factura: {compra_a_mostrar.nro_factura}')
        except Compra.DoesNotExist:
            messages.error(request, 'La compra solicitada no existe o no te pertenece.')
            print('La compra solicitada no existe o no te pertenece')
            return redirect('mostrarlistapro') # Redirige al historial si no encuentra la compra
    elif request.method == 'GET':
        # Este caso es un fallback si la URL de seguimiento se accede directamente
        # o si funcionBotonPagar redirigiera con un parámetro GET (que no lo hace ahora)
        # Por simplicidad, si no es POST con compra_id, redirigimos al historial.
        messages.warning(request, 'Acceso inválido al seguimiento directo. Por favor, selecciona una compra de tu historial.')
        print('Acceso inválido al seguimiento directo. Por favor, selecciona una compra de tu historial.')
        return redirect('mostrarlistapro')
    else:
        # Esto captura POSTs sin compra_id u otros métodos inesperados
        messages.error(request, 'Solicitud inválida para el seguimiento de la compra.')
        print('Solicitud inválida para el seguimiento de la compra.')
        return redirect('mostrarlistapro')

    if compra_a_mostrar:
        # Cargar todos los estados de envío para la barra de progreso
        estados_envio = EstadoEnvio.objects.all().order_by('orden')
        
        context = {
            'compra': compra_a_mostrar,
            'estados_envio': estados_envio,
            'tipo_acceso': 'btn_seguir', # Para que el template sepa de dónde viene
            'estadoSesion': request.session.get("estadoSesion"),
            'tipoProductos' : tipoProductos,
            
        }
        return render(request, "SeguimientoAdmin.html", context)
    else:
        # Esto solo debería ocurrir si no se encontró la compra, y ya se manejó con un redirect.
        # Pero como una última medida, podemos devolver a una página segura.
        messages.error(request, 'No se pudo cargar la información de seguimiento.')
        return redirect('mostrarHistorialDeCompras')

def actualizar_estado_envio_admin(request):
    if request.method == 'POST':
        tipoProductos = TipoProducto.objects.all().values()
        compra_id = request.POST.get('nro_factura_admin')
        nro_factura = request.POST.get('nro_factura')
        nuevo_estado_id = int(request.POST.get('btn_porcentaje')) # From the percentage buttons
        accion_extra = request.POST.get('accion_extra')     # From 'RECHAZADO'/'COMPRADO' buttons
        compra_a_mostrar = Compra.objects.get(id=compra_id)
        estados_envio = EstadoEnvio.objects.all().order_by('orden')
        print(nro_factura)
        print(nuevo_estado_id)
        # if not nro_factura or (not nuevo_estado_id and not accion_extra):
        #     messages.error(request, 'Datos incompletos para actualizar el estado.')
        #     return redirect('nombre_de_tu_vista_admin_principal') # Redirect to admin dashboard/list

        try:
            with transaction.atomic(): # Ensure atomicity for multiple Compra objects
                compras_a_actualizar = Compra.objects.filter(nro_factura=nro_factura)

                if not compras_a_actualizar.exists():
                    messages.error(request, f'No se encontraron compras con el número de factura {nro_factura}.')
                    print('No se encontraron compras con el número de factura.')
                    return redirect('seguimiento_admin')

                # Handle percentage update buttons
                if nuevo_estado_id:
                    nuevo_estado_envio = get_object_or_404(EstadoEnvio, id=nuevo_estado_id)
                    compras_a_actualizar.update(estado_seguimiento=nuevo_estado_envio)
                    messages.success(request, f'Estado de envío actualizado a "{nuevo_estado_envio.nombre}" ({nuevo_estado_envio.porcentaje_visual}%) para la factura {nro_factura}.')
                # Handle 'RECHAZADO'/'COMPRADO' actions
                if accion_extra == 'RECHAZADO':
                    descripcion_rechazo = request.POST.get('descripcion_rechazo', 'Sin descripción.')
                    compras_a_actualizar.update(
                        estado_compra='RECHAZADO',
                        estado_seguimiento=None, # Clear tracking if rejected, or set to a 'Cancelado' state
                        # If you add a 'motivo_rechazo' field to Compra model:
                        # motivo_rechazo=descripcion_rechazo 
                    )
                    messages.success(request, f'Factura {nro_factura} marcada como RECHAZADA. Motivo: {descripcion_rechazo}')
                elif nuevo_estado_id == 5:
                    # This might be redundant if 'COMPRADO' is set at payment, but included for completeness
                    compras_a_actualizar.update(estado_compra='COMPRADO')
                    messages.success(request, f'Factura {nro_factura} marcada como COMPRADA.')

        except Exception as e:
            messages.error(request, f'Error al actualizar el estado: {e}')
            import logging
            logging.error(f"Error updating purchase status for admin: {e}", exc_info=True)

    # Redirect back to the detailed admin tracking page for this invoice after update
    return render(request, 'SeguimientoAdmin.html', {'compra': compra_a_mostrar,
            'estados_envio': estados_envio,
            'tipo_acceso': 'btn_seguir', # Para que el template sepa de dónde viene
            'estadoSesion': request.session.get("estadoSesion"),
            'tipoProductos' : tipoProductos})

def mostrarSeguimientoAdminPresencial(request):
    if "estadoSesion" in request.session:
        productos = Producto.objects.all().values()
        tipoProductos = TipoProducto.objects.all().values()
        estadoSesion = request.session.get("estadoSesion")
        usuario_data = request.session.get("usuario")#usuario_data lo que permite es acceder y obtener los datos del usuario en una LISTA
        usuario_id = usuario_data[0]['id'] if usuario_data and isinstance(usuario_data, list) and usuario_data[0].get('id') else None #Al obtener los datos del Usuario en un lista, básicamente toma solamente el ID del usuario de esa lista
        compras_usuario = []

        if usuario_id:
            usuario_obj = Usuario.objects.get(id=usuario_id) # Obtener el objeto Usuario
            compras_usuario = Compra.objects.filter(direccion = 'PRESENCIAL').select_related('producto', 'tarjeta').order_by("-fecha_compra").values(
                'id',
                'direccion',
                'fecha_compra',
                'cantidad',
                'nro_factura',
                'producto__imagen',
                'producto__nombre',
                'producto__precio',
                'estado_compra',
                'tarjeta__tipoTarjeta__tipo',
                'usuario__rut',
                'estado_compra',
                'fecha_entrega_estimada',
                'comuna_entrega_id',
                'estado_seguimiento_id',  
            )

            datos = {
                'usuario': usuario_data, # Mantener la estructura de la sesión
                'estadoSesion': estadoSesion,
                'productos': productos,
                'tipoProductos': tipoProductos,
                'compras': compras_usuario,
            }
            return render(request, "presencial_admin.html", datos)
        else:
            # Manejar el caso en que no se encuentra el ID del usuario en la sesión
            datos = {
                'estadoSesion': estadoSesion,
                'tipoProductos': tipoProductos,
                'productos': productos,
                'compras': []
            }
            return render(request, "presencial_admin.html", datos)
    else:
        usuario = Usuario.objects.all().values()
        productos = Producto.objects.all().values()
        tipoProductos = TipoProducto.objects.all().values()
        datos = {
            'usuario': usuario,
            'productos': productos,
            'tipoProductos': tipoProductos
        }
        return render(request, "InicioSesion.html", datos)

def confirmarCompra(request):
    if request.method == 'POST':
        # No necesitas tipoProductos y estados_envio aquí a menos que los uses después
        # tipoProductos = TipoProducto.objects.all().values()
        # estados_envio = EstadoEnvio.objects.all().order_by('orden')

        compra_id = request.POST.get('id_compra_pres')
        nro_factura = request.POST.get('nro_factura_pres')
        accion_extra = request.POST.get('accion_extra') # From 'RECHAZADO'/'COMPRADO' buttons

        # El print es solo para depuración, puedes quitarlo en producción
        print(f"DEBUG: nro_factura={nro_factura}, accion_extra={accion_extra}, compra_id={compra_id}")

        try:
            with transaction.atomic(): # Ensure atomicity for multiple Compra objects
                compras_a_actualizar = Compra.objects.filter(nro_factura=nro_factura)

                if not compras_a_actualizar.exists():
                    messages.error(request, f'No se encontraron compras con el número de factura {nro_factura}.')
                    logging.warning(f"No se encontraron compras con el número de factura: {nro_factura}")
                    return redirect('presencialAdmin') # O 'seguimiento_admin' si es tu vista principal

                # Handle 'RECHAZADO' action
                if accion_extra == 'RECHAZADO':
                    descripcion_rechazo = request.POST.get('descripcion_rechazo', 'Sin descripción proporcionada.')
                    
                    # VALIDACIÓN: Asegurarse de que el motivo no esté vacío si es RECHAZADO
                    if not descripcion_rechazo.strip():
                        messages.error(request, 'La descripción del motivo de rechazo no puede estar vacía.')
                        return redirect('presencialAdmin') # Vuelve a la página actual para que el usuario intente de nuevo
                        
                    compras_a_actualizar.update(
                        estado_compra='RECHAZADO',
                        estado_seguimiento=None, # Limpia el seguimiento si se rechaza
                        # Si tienes un campo en tu modelo Compra para almacenar el motivo de rechazo:
                        # motivo_rechazo=descripcion_rechazo 
                    )
                    messages.success(request, f'Factura {nro_factura} marcada como RECHAZADA. Motivo: {descripcion_rechazo}')
                
                # Handle 'COMPRADO' action
                elif accion_extra == 'COMPRADO':
                    compras_a_actualizar.update(estado_compra='COMPRADO')
                    messages.success(request, f'Factura {nro_factura} marcada como COMPRADA.')

                else:
                    messages.error(request, 'Acción no reconocida.')

        except Exception as e:
            messages.error(request, f'Error al actualizar el estado: {e}')
            logging.error(f"Error updating purchase status for admin: {e}", exc_info=True)

    # Redirige de vuelta a la página de administración de compras presenciales después de la actualización
    return redirect('presencialAdmin')


#######################################################################################
##                            HISTORIAL DE COMPRA
#######################################################################################

def mostrarHistorialDeCompras(request):
    if "estadoSesion" in request.session:
        productos = Producto.objects.all().values()
        tipoProductos = TipoProducto.objects.all().values()
        estadoSesion = request.session.get("estadoSesion")
        usuario_data = request.session.get("usuario")#usuario_data lo que permite es acceder y obtener los datos del usuario en una LISTA
        usuario_id = usuario_data[0]['id'] if usuario_data and isinstance(usuario_data, list) and usuario_data[0].get('id') else None #Al obtener los datos del Usuario en un lista, básicamente toma solamente el ID del usuario de esa lista
        compras_usuario = []

        if usuario_id:
            usuario_obj = Usuario.objects.get(id=usuario_id) # Obtener el objeto Usuario
            compras_usuario = Compra.objects.filter(usuario_id=int(usuario_id)).select_related('producto', 'tarjeta').order_by("-fecha_compra").values(
                'id',
                'producto__nombre',
                'producto__precio',
                'cantidad',
                'fecha_compra',
                'estado_compra',
                'tarjeta__tipoTarjeta__tipo',
                'usuario__rut',
                'direccion'
            )

            datos = {
                'usuario': usuario_data, # Mantener la estructura de la sesión
                'estadoSesion': estadoSesion,
                'productos': productos,
                'tipoProductos': tipoProductos,
                'compras': compras_usuario
            }
            return render(request, "HistorialDeCompras.html", datos)
        else:
            # Manejar el caso en que no se encuentra el ID del usuario en la sesión
            datos = {
                'estadoSesion': estadoSesion,
                'tipoProductos': tipoProductos,
                'productos': productos,
                'compras': []
            }
            return render(request, "HistorialDeCompras.html", datos)
    else:
        usuario = Usuario.objects.all().values()
        productos = Producto.objects.all().values()
        tipoProductos = TipoProducto.objects.all().values()
        datos = {
            'usuario': usuario,
            'productos': productos,
            'tipoProductos': tipoProductos
        }
        return render(request, "InicioSesion.html", datos)

#######################################################################################
##                            AGENDAMIENTOS
#######################################################################################    
def mostrarAgendamientos(request):
    if "estadoSesion" in request.session:
        usuario_data = request.session.get("usuario")
        estadoSesion = request.session.get("estadoSesion")

        # Obtener todas las horas disponibles ordenadas por fecha y hora
        horas_disponibles = HorasDisponibles.objects.filter(estado_hora=1).order_by('fecha', 'hora')

        # Agrupar las horas por fecha
        horas_por_fecha = defaultdict(list)
        for hora in horas_disponibles:
            fecha_str = hora.fecha.strftime('%Y-%m-%d')
            hora_str = hora.hora.strftime('%H:%M')
            horas_por_fecha[fecha_str].append(hora_str)

        # Convertir defaultdict a dict para serializar a JSON
        horas_por_fecha = dict(horas_por_fecha)

        datos = {
            'usuario': usuario_data,
            'estadoSesion': estadoSesion,
            'horas_por_fecha': json.dumps(horas_por_fecha),  # Serializar a JSON
            'fechas_disponibles': list(horas_por_fecha.keys()),  # Lista de fechas disponibles
        }
        return render(request, 'agendamientos.html', datos)
    else:
        return render(request, "InicioSesion.html", {})

def procesarAgendamientos(request):
    if "estadoSesion" in request.session:
        productos = Producto.objects.all().values()
        tipoProductos = TipoProducto.objects.all().values()
        estadoSesion = request.session.get("estadoSesion")
        usuario_data = request.session.get("usuario")#usuario_data lo que permite es acceder y obtener los datos del usuario en una LISTA
        usuario_id = usuario_data[0]['id'] if usuario_data and isinstance(usuario_data, list) and usuario_data[0].get('id') else None 
        if request.method == "POST":
            fecha_agendamiento = request.POST.get("fecha_agendamiento")
            hora_agendamiento = request.POST.get("hora_agendamiento")
            descripcion_consulta = request.POST.get("descripcion_consulta")
            try:
                # Corrección: formato esperado es "YYYY-MM-DD"
                fecha_agendada = datetime.strptime(fecha_agendamiento, "%Y-%m-%d").date()
                
                # Corrección: formato esperado es "HH:MM"
                hora_agendada = datetime.strptime(hora_agendamiento, "%H:%M").time()

            except ValueError:
                print("Fecha recibida:", request.POST.get("fecha_agendamiento"))
                print("Hora recibida:", request.POST.get("hora_agendamiento"))
                return HttpResponse("Formato de fecha u hora inválido", status=400)

            rep = Reparacion(fecha = fecha_agendada, hora_agendada = hora_agendada, observaciones = descripcion_consulta, estado_reparacion_id = 1, usuario_id = usuario_id)
            rep.save()
            datos = {
                'usuario': usuario_data, # Mantener la estructura de la sesión
                'estadoSesion': estadoSesion,
                'productos': productos,
                'tipoProductos': tipoProductos,
                'r':'Agendamiento registrado correctamente'
            }

            hora_disponible = HorasDisponibles.objects.filter(fecha=fecha_agendada, hora=hora_agendada).first()
            if hora_disponible:
                hora_disponible.estado_hora_id = 2  
                hora_disponible.save()

            return render(request,'index.html',datos)
        
    else:
        usuario = Usuario.objects.all().values()
        productos = Producto.objects.all().values()
        tipoProductos = TipoProducto.objects.all().values()
        datos = {
            'usuario': usuario,
            'productos': productos,
            'tipoProductos': tipoProductos
        }
        return render(request, "InicioSesion.html", datos)

#######################################################################################
##                            PERFIL DE USUARIO
#######################################################################################

# views.py


# --- Vista para mostrar el Perfil ---
def mostrarPerfilUsuario(request):
    estadoSesion = request.session.get("estadoSesion")
    usu_id = request.session.get("usuario")
    usuario_id = usu_id[0]['id'] if usu_id and isinstance(usu_id, list) else None

    if not estadoSesion or not usuario_id:
        messages.error(request, 'Debes iniciar sesión para ver tu perfil.')
        return redirect('mostrarInicioSesion')

    try:
        usuario = Usuario.objects.get(id=usuario_id)
    except Usuario.DoesNotExist:
        messages.error(request, 'Usuario no encontrado.')
        return redirect('mostrarInicioSesion')

    productos = Producto.objects.all().values()
    tpro = TipoProducto.objects.all().values()

    datos = {
        'pro': productos,
        'tpro': tpro,
        'usuario': [{
            'id': usuario.id,
            'rut': usuario.rut,
            'nombre': usuario.nombre,
            'apellido': usuario.apellido,
            'correo': usuario.correo,
            # ¡IMPORTANTE! NO PASAR LA CONTRASEÑA (NI HASH) AL TEMPLATE HTML POR SEGURIDAD.
            # 'contrasena': usuario.contrasena, # ESTA LÍNEA DEBE PERMANECER COMENTADA O ELIMINADA.
            'telefono': usuario.telefono,
            'tipoUsuario_id': usuario.tipoUsuario_id,
            'estadoUsuario_id': usuario.estadoUsuario_id
        }],
        'estadoSesion': estadoSesion
    }

    return render(request, 'PerfilUsuario.html', datos)


# --- Vista para actualizar el Perfil (Nombre, Apellido, Email, Teléfono) ---
def actualizarUsuario(request):
    estadoSesion = request.session.get("estadoSesion")
    usu_id = request.session.get("usuario")
    usuario_id = usu_id[0]['id'] if usu_id and isinstance(usu_id, list) else None

    if not estadoSesion or not usuario_id:
        messages.error(request, 'Debes iniciar sesión para actualizar tu perfil.')
        return redirect('mostrarInicioSesion')

    try:
        usuario = Usuario.objects.get(id=usuario_id)
    except Usuario.DoesNotExist:
        messages.error(request, 'Usuario no encontrado.')
        return redirect('mostrarInicioSesion')

    if request.method == 'POST':
        nuevo_nombre = request.POST.get('nomcli2')
        nuevo_apellido = request.POST.get('apecli2')
        nuevo_correo = request.POST.get('emacli2')
        nuevo_telefono = request.POST.get('foncli2')
        current_password = request.POST.get('current_password')

        email_cambio = (usuario.correo != nuevo_correo)
        telefono_cambio = (usuario.telefono != nuevo_telefono)

        if email_cambio or telefono_cambio:
            if not current_password:
                messages.error(request, 'Para cambiar el Email o Teléfono, debe ingresar su contraseña actual.')
                return redirect('mostrarPerfilUsuario')

            # --- VERIFICACIÓN DE CONTRASEÑA ACTUAL HASHEADA ---
            # Compara la contraseña ingresada (texto plano) con el hash almacenado en usuario.contrasena
            if not check_password(current_password, usuario.contrasena):
                messages.error(request, 'Contraseña actual incorrecta para actualizar Email o Teléfono.')
                return redirect('mostrarPerfilUsuario')

        usuario.nombre = nuevo_nombre
        usuario.apellido = nuevo_apellido
        usuario.correo = nuevo_correo
        usuario.telefono = nuevo_telefono
        
        try:
            usuario.save()
            messages.success(request, '¡Perfil actualizado con éxito!')
        except Exception as e:
            messages.error(request, f'Error al actualizar el perfil: {e}')

        return redirect('mostrarPerfilUsuario')

    return redirect('mostrarPerfilUsuario')


# --- Nueva Vista para Cambiar Contraseña ---
def cambiarContrasena(request):
    estadoSesion = request.session.get("estadoSesion")
    usu_id = request.session.get("usuario")
    usuario_id = usu_id[0]['id'] if usu_id and isinstance(usu_id, list) else None

    if not estadoSesion or not usuario_id:
        messages.error(request, 'Debes iniciar sesión para cambiar tu contraseña.')
        return redirect('mostrarInicioSesion')

    try:
        usuario = Usuario.objects.get(id=usuario_id)
    except Usuario.DoesNotExist:
        messages.error(request, 'Usuario no encontrado.')
        return redirect('mostrarInicioSesion')

    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        new_password1 = request.POST.get('new_password1')
        new_password2 = request.POST.get('new_password2')

        # 1. Verificar que la contraseña actual sea correcta (comparando texto plano con hash)
        if not check_password(old_password, usuario.contrasena):
            messages.error(request, 'Contraseña actual incorrecta.')
            return redirect('mostrarPerfilUsuario')

        # 2. Verificar que las nuevas contraseñas coincidan
        if new_password1 != new_password2:
            messages.error(request, 'Las nuevas contraseñas no coinciden.')
            return redirect('mostrarPerfilUsuario')
        
        # Opcional: Añadir validación de complejidad de la contraseña (ej. longitud mínima)
        if len(new_password1) < 8:
            messages.error(request, 'La nueva contraseña debe tener al menos 8 caracteres.')
            return redirect('mostrarPerfilUsuario')

        # 3. Guardar la nueva contraseña (hasheando el texto plano de la nueva contraseña)
        try:
            usuario.contrasena = make_password(new_password1) # <--- Aquí hasheamos la nueva contraseña
            usuario.save()

            messages.success(request, '¡Contraseña cambiada con éxito!')
        except Exception as e:
            messages.error(request, f'Error al cambiar la contraseña: {e}')

        return redirect('mostrarPerfilUsuario')

    messages.info(request, 'Acceso inválido para cambiar contraseña.')
    return redirect('mostrarPerfilUsuario')



#######################################################################################
##                            INTERFAZ ADMINISTRADOR
#######################################################################################

#===================AUTENTICAR ADMIN=============================================
def admin_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        estadoSesion = request.session.get("estadoSesion")
        usuario_sesion = request.session.get("usuario")

        # Verifica que haya sesión activa y usuario con tipoUsuario_id == 1 (admin)
        if estadoSesion and usuario_sesion and isinstance(usuario_sesion, list):
            usuario_data = usuario_sesion[0]
            if usuario_data.get("tipoUsuario_id") == 1:
                return view_func(request, *args, **kwargs)

        return HttpResponse("No tienes permisos para acceder a esta página.", status=403)

    return wrapper
#===================================================================================

@admin_required
def mostraragregarproducto(request): 
    tippro = TipoProducto.objects.all().values()
    prov = Proveedor.objects.all().values()

    materiales = [
        "Sintetico", "Metal", "Acero", "Caucho",
        "Aluminio", "Plastico", "Acero Inoxidable", "Fibra de Carbono"
    ]

    datos = { 'tippro': tippro, 'prov':prov,'materiales':materiales}
    return render(request, "agregar_productos.html",datos)

@admin_required
def mostrardashboard(request):
    # Filtros GET
    mes = request.GET.get('mes')
    anio = request.GET.get('anio')

    # Valores por defecto: mes y año actual
    hoy = now()
    mes = int(mes) if mes else hoy.month
    anio = int(anio) if anio else hoy.year

    # Ventas mensuales (para gráfico general)
    ventas_mensuales = Compra.objects.annotate(
        mes=TruncMonth('fecha_compra')
    ).values('mes').annotate(total=Sum('cantidad')).order_by('mes')

    meses = [v['mes'].strftime('%B') for v in ventas_mensuales]
    cantidades = [v['total'] for v in ventas_mensuales]

    # Clientes recurrentes
    clientes_recurrentes = Compra.objects.values('usuario').annotate(
        compras=Count('id')
    ).filter(compras__gte=2).count()

    # Agendamientos mensuales
    agendamientos = Reparacion.objects.annotate(
        mes=TruncMonth('fecha')
    ).values('mes').annotate(total=Count('id')).order_by('mes')

    meses_ag = [a['mes'].strftime('%B') for a in agendamientos]
    totales_ag = [a['total'] for a in agendamientos]

    # Productos más vendidos
    top_productos = Compra.objects.values('producto__nombre').annotate(
        total=Sum('cantidad')
    ).order_by('-total')[:5]

    nombres_prod = [p['producto__nombre'] for p in top_productos]
    ventas_prod = [p['total'] for p in top_productos]

    # Compras del mes filtrado
    compras_mes = Compra.objects.filter(
        fecha_compra__month=mes,
        fecha_compra__year=anio
    )
    total_ventas_mes = compras_mes.count()
    dinero_total_mes = compras_mes.aggregate(total=Sum('producto__precio'))['total'] or 0

    productos_bajo_stock = Producto.objects.filter(stock__lte=10).exclude(estadoProducto=4)

    # Lista de meses para el select
    meses_lista = [
    (1, "Enero"), (2, "Febrero"), (3, "Marzo"), (4, "Abril"),
    (5, "Mayo"), (6, "Junio"), (7, "Julio"), (8, "Agosto"),
    (9, "Septiembre"), (10, "Octubre"), (11, "Noviembre"), (12, "Diciembre"),
    ]

    context = {
        'meses': meses,
        'cantidades': cantidades,
        'clientes_recurrentes': clientes_recurrentes,
        'meses_ag': meses_ag,
        'totales_ag': totales_ag,
        'nombres_prod': nombres_prod,
        'ventas_prod': ventas_prod,
        'total_ventas_mes': total_ventas_mes,
        'dinero_total_mes': dinero_total_mes,
        'productos_bajo_stock': productos_bajo_stock,
        'meses_lista': meses_lista,
        'mes_seleccionado': mes,
        'anio_seleccionado': anio,
    }

    return render(request, 'dashboard.html', context)

#===========================================================================0

@admin_required
def mostrarhistorialAcciones(request):
    his = HistorialAcciones.objects.select_related('usuario').all()

    for h in his:
        h.usuario_nombre_completo = f"{h.usuario.nombre} {h.usuario.apellido}"

    datos = {'his': his}
    return render(request, "listar_historial.html", datos)

@admin_required
def mostrarlistapro(request):
    pro = Producto.objects.exclude(estadoProducto=4)

    cero = pro.count()<1 == True
    
    if cero == True: 
        tip = TipoProducto.objects.get(descripcion = 'Bicicleta')
        est = EstadoProducto.objects.get(descripcion = 'Disponible')
        uno = Producto(imagen="imagenes_bd/noborrar1.jpg", nombre="Bicicleta Mountain Bike Galia",descripcion="Aro 26', Color Calipso",material="Acero",stock=2,precio=299990,tipoProducto=tip, estadoProducto=est)
        uno.save()
        
        tip2 = TipoProducto.objects.get(descripcion = 'Bicicleta')
        est2 = EstadoProducto.objects.get(descripcion = 'Disponible')
        dos = Producto(imagen="imagenes_bd/noborrar2.jpg",nombre="Bicicleta Toimsa Hello Kitty", descripcion="Bicicleta con diseño de Hello Kitty, Aro 14'",material="Fibra de Carbono",stock=8,precio=90000,tipoProducto=tip2, estadoProducto=est2)
        dos.save()
        
        tip3 = TipoProducto.objects.get(descripcion = 'Luz')
        est3 = EstadoProducto.objects.get(descripcion = 'Disponible')
        tres = Producto(imagen="imagenes_bd/noborrar3.jpg",nombre= "Luz LED Rueda de bicicleta", descripcion="Luces para iluminar las ruedas de la bicicleta",material="Sintetico",stock=20,precio=15000,tipoProducto=tip3, estadoProducto=est3)
        tres.save()

        tip4 = TipoProducto.objects.get(descripcion = "Casco")
        est4 = EstadoProducto.objects.get(descripcion = "Disponible")
        cuatro = Producto(imagen="imagenes_bd/noborrar4.jpg", nombre="Casco infantil Hello Kitty", descripcion="Casco para niños con diseño de Hello Kitty, 46/53CM", material="Plástico", stock=3, precio=17000,tipoProducto=tip4,estadoProducto=est4)
        cuatro.save()

        tip5 = TipoProducto.objects.get(descripcion = "Accesorio")
        est5 = EstadoProducto.objects.get(descripcion = "Disponible")
        cinco = Producto(imagen="imagenes_bd/noborrar5.jpg", nombre="Juego de accesorios de bicicleta de 7 piezas", descripcion="Soporte de teléfono de silicona, Bocina, soporte de botella, 2 luces USB recargables, 2 espejos retrovisores convexos", material="Sintético", stock=5, precio=25000,tipoProducto=tip5,estadoProducto=est5)
        cinco.save()

        tip6 = TipoProducto.objects.get(descripcion = "Repuesto")
        est6 = EstadoProducto.objects.get(descripcion = "Disponible")
        seis = Producto(imagen="imagenes_bd/noborrar6.jpg", nombre="Rueda de bicicleta", descripcion="Rueda trasera para bicicleta, plateada, aro 20'", material="Caucho", stock=10, precio=23000,tipoProducto=tip6,estadoProducto=est6)
        seis.save()

    datos = {'pro': pro}
    return render(request,"listar_productos.html",datos)


#==========================================================

@admin_required
def mostrarlistausu(request): 
    usu = Usuario.objects.filter(tipoUsuario_id=2)

    datos = {'usu': usu}
    return render(request, "listar_usuarios.html", datos)

#==========================================================

@admin_required
def mostraragregarhoras(request):    
    return render(request,"agregar_horas.html")


@admin_required
def agregarhoras(request): 
    fec = request.POST['txtfec']
    hor = request.POST['txthor']
    est = EstadoHora.objects.get(descripcion = 'Disponible')

    # Verificamos si ya existe una hora igual en esa fecha
    existe = HorasDisponibles.objects.filter(fecha=fec, hora=hor).exists()

    if existe:
        datos = {'r':'Ya existe una hora registrada en ese horario'}
        return render(request,'agregar_horas.html',datos)
    else:
        nueva_hora = HorasDisponibles(fecha=fec, hora=hor, estado_hora=est)
        nueva_hora.save()
        datos = {'r':'Hora registrada correctamente'}
        
        return render(request,'agregar_horas.html',datos)

#=========================================================

@admin_required
def mostrarlistacat(request):    
    cat = TipoProducto.objects.all()
    datos = {'cat': cat}
    return render(request,"listar_categorias.html",datos)


@admin_required
def mostrarlistaagendas(request):    
    translation.activate('es')  # Fuerza español

    rep = Reparacion.objects.select_related('estado_reparacion').order_by(
        'estado_reparacion__descripcion', 'fecha', 'hora_agendada'
    )
    return render(request, 'listar_agendamientos.html', {'rep': rep})

#=====================================================

@admin_required
def mostraragregarcategorias(request): 
    return render(request,"agregar_categorias.html")


@admin_required
def agregarproducto(request): 
    fac = request.POST['txtfac']
    nom = request.POST['txtnom']
    des = request.POST['txtdes']
    mat = request.POST['cbomat']
    sto = request.POST['txtsto']          
    cos = request.POST['txtcos']            
    uti_str = request.POST['cbouti']        
    ven = request.POST['txtpre']
    tip = request.POST['cbotip']
    prov = request.POST['cboprov']

    if uti_str is None or uti_str == "":
        datos = {'r': 'Debe seleccionar una utilidad válida'}
        return render(request, 'agregar_productos.html', datos)

    uti = float(uti_str)

    tipo = TipoProducto.objects.get(descripcion = tip)
    est = EstadoProducto.objects.get(descripcion = 'Disponible')
    prove = Proveedor.objects.get(descripcion = prov)

    try: 
        ima = request.FILES['txtima']
    except: 
        ima = "imagenes_bd/noimagen.jpg"
    
    pro = Producto(imagen=ima,numeroFactura=fac,nombre=nom,descripcion=des,material=mat,stock=sto, precioCompra=cos,utilidad=uti,precio=ven,tipoProducto=tipo,proveedor=prove,estadoProducto=est)
    pro.save()
    datos = {'r':'Producto registrado correctamente'}
    
    return render(request,'agregar_productos.html',datos)


@admin_required
def agregarcategoria(request):
    des = request.POST['txtnom']
    tpro = TipoProducto(descripcion=des)
    tpro.save()
    datos = {'r':'Categoria registrada correctamente'}

    return render(request,"agregar_categorias.html",datos)

#================================================================
#                     MODIFICAR REGISTROS   
#================================================================

@admin_required
def mostrarmodificarproducto (request,id): 
    tippro = TipoProducto.objects.all()
    estpro = EstadoProducto.objects.all()
    prov = Proveedor.objects.all().values()
    pro = Producto.objects.get(id=id)
    prod = Producto.objects.all()

    materiales = [
        "Sintetico", "Metal", "Acero", "Caucho",
        "Aluminio", "Plastico", "Acero Inoxidable", "Fibra de Carbono"
    ]

    datos ={'pro':pro,'tippro': tippro,'estpro':estpro,'prod':prod, 'prov':prov, 'materiales': materiales}
    return render(request,"modificarproducto.html",datos)


@admin_required
def mostrarmodificarcategoria (request,id): 
    cat = TipoProducto.objects.get(id=id)
    datos={'cat':cat}
    return render(request,"modificarcategoria.html",datos)


@admin_required
def actualizarcategoria(request,id): 
    usuario_sesion = request.session.get("usuario")
    usuario_id = usuario_sesion[0]['id'] if usuario_sesion else None
    usuario = Usuario.objects.get(id=usuario_id)
    motivo = request.POST.get('motivo', 'Sin motivo proporcionado')
    try:
        nom = request.POST['txtnom']
    

        cat = TipoProducto.objects.get(id=id)
        cat.descripcion= nom 

        his = HistorialAcciones()
        his.fecha = timezone.now()
        his.tipoObjeto = "Categoria"
        his.objetoAfectado = nom
        his.accion = "Actualizacion"
        his.motivo = motivo
        his.usuario = usuario
        his.save()
        
        cat.save()
        cat = TipoProducto.objects.all().values()
        datos = { 'cat':cat, 'r':'El registro '+str(id)+' se ha actualizado correctamente'}
        return render(request,"listar_categorias.html",datos)
    
    except: 
        cat = TipoProducto.objects.all().values()
        datos = { 'cat':cat, 'r2':'No se ha podido actualizar el registro '+str(id)}
        return render(request,"listar_categorias.html",datos)
    

@admin_required
def actualizarproducto(request, id):
    usuario_sesion = request.session.get("usuario")
    usuario_id = usuario_sesion[0]['id'] if usuario_sesion else None
    usuario = Usuario.objects.get(id=usuario_id)
    motivo = request.POST.get('motivo', 'Sin motivo proporcionado')

    try:
        if request.method == 'POST':
            fac = request.POST.get('txtfac')
            nom = request.POST.get('txtnom')
            des = request.POST.get('txtdes')
            mat = request.POST.get('cbomat')
            sto = request.POST.get('txtsto')
            cos = request.POST.get('txtcos')
            uti_str = request.POST.get('cbouti')
            ven = request.POST.get('txtpre')
            prov_desc = request.POST.get('cboprov')
            tip_desc = request.POST.get('cbotip')
            est_desc = request.POST.get('cboest')
            ima = request.FILES.get('txtima')

            if uti_str is None or uti_str == "":
                datos = {'r': 'Debe seleccionar una utilidad válida'}
                return render(request, 'agregar_productos.html', datos)

            uti = float(uti_str)

            pro = Producto.objects.get(id=id)

            tipo = TipoProducto.objects.get(descripcion=tip_desc)
            estado = EstadoProducto.objects.get(descripcion=est_desc)
            proveedor = Proveedor.objects.get(descripcion=prov_desc)

            pro.numeroFactura = fac
            pro.nombre = nom
            pro.descripcion = des
            pro.material = mat
            pro.stock = sto
            pro.precioCompra = cos
            pro.utilidad = uti
            pro.precio = ven
            pro.tipoProducto = tipo
            pro.estadoProducto = estado
            pro.proveedor = proveedor

            if ima:
                pro.imagen = ima

            pro.save()

            his = HistorialAcciones()
            his.fecha = timezone.now()
            his.tipoObjeto = "Producto"
            his.objetoAfectado = nom
            his.accion = "Actualizacion"
            his.motivo = motivo
            his.usuario = usuario
            his.save()

            prods = Producto.objects.all()
            datos = {'pro': prods, 'r': f'El registro {id} se ha actualizado correctamente'}
            return render(request, "listar_productos.html", datos)
        
            

    except Exception as e:
        prods = Producto.objects.all()
        datos = {'pro': prods, 'r2': f'Error al actualizar: {str(e)}'}
        return render(request, "listar_productos.html", datos)


@admin_required    
def actualizar_estado(request, reparacion_id): 
    if request.method == 'POST':
        data = json.loads(request.body)
        nuevo_estado_nombre = data.get('estado')

        try:
            nuevo_estado = EstadoReparacion.objects.get(descripcion=nuevo_estado_nombre)
        except EstadoReparacion.DoesNotExist:
            return JsonResponse({'error': 'Estado no válido'}, status=400)

        reparacion = Reparacion.objects.get(id=reparacion_id)
        reparacion.estado_reparacion = nuevo_estado
        reparacion.save()

        return JsonResponse({'success': True})
    
    return JsonResponse({'error': 'Método no permitido'}, status=405)

#----------------------------------------------------------------
#                      DILIT REGISTROS
#================================================================

@admin_required
def eliminarproducto (request,id):
    usuario_sesion = request.session.get("usuario")
    usuario_id = usuario_sesion[0]['id'] if usuario_sesion else None
    usuario = Usuario.objects.get(id=usuario_id)
    motivo = request.GET.get('motivo', 'Sin motivo proporcionado').strip()

    try:
        pro = Producto.objects.get(id=id)

        # Registrar en historial
        HistorialAcciones.objects.create(
            fecha=timezone.now(),
            tipoObjeto="Producto",
            objetoAfectado=pro.descripcion,
            accion="Marcado como Eliminado",
            motivo=motivo,
            usuario=usuario
        )

        # Obtener estado "Eliminado"
        estado_eliminado = EstadoProducto.objects.get(descripcion="Deshabilitado")
        pro.estadoProducto = estado_eliminado
        pro.save()

        # Mostrar solo productos activos
        productos = Producto.objects.exclude(estadoProducto__descripcion="Eliminado")
        datos = {'pro': productos, 'r': f'El registro {id} se ha marcado como eliminado correctamente'}
        return render(request, "listar_productos.html", datos)

    except Producto.DoesNotExist:
        productos = Producto.objects.exclude(estadoProducto__descripcion="Eliminado")
        datos = {'pro': productos, 'r2': f'No se ha podido encontrar el registro {id}'}
        return render(request, "listar_productos.html", datos)
    

@admin_required
def eliminarcategoria (request,id): 
    usuario_sesion = request.session.get("usuario")
    usuario_id = usuario_sesion[0]['id'] if usuario_sesion else None
    usuario = Usuario.objects.get(id=usuario_id)
    motivo = request.GET.get('motivo', 'Sin motivo proporcionado').strip()

    try:
        cat = TipoProducto.objects.get(id=id)

        his = HistorialAcciones()
        his.fecha = timezone.now()
        his.tipoObjeto = "Categoria"
        his.objetoAfectado = cat.descripcion
        his.accion = "Eliminación"
        his.motivo = motivo
        his.usuario = usuario
        his.save()

        cat.delete()
        cat = TipoProducto.objects.all()
        datos={'cat':cat, 'r':'El registro '+str(id)+' se ha eliminado correctamente'}
        return render(request,"listar_categorias.html",datos)
    except: 
        cat = TipoProducto.objects.all()
        datos = { 'cat':cat, 'r2':'No se ha podido eliminar el registro '+str(id)}
        return render(request,"listar_categorias.html",datos) 
    

@admin_required
def eliminarusuario(request, id):
    usuario_sesion = request.session.get("usuario")
    usuario_id = usuario_sesion[0]['id'] if usuario_sesion else None

    # No permitir eliminarse a sí mismo
    if str(usuario_id) == str(id):
        usu = Usuario.objects.filter()
        datos = {
            'usu': usu,
            'r2': 'No puedes eliminar tu propia cuenta desde la sesión actual.'
        }
        return render(request, "listar_usuarios.html", datos)

    motivo = request.GET.get('motivo', 'Sin motivo proporcionado').strip()

    try:
        usuario = Usuario.objects.get(id=usuario_id)
        usuario_a_eliminar = Usuario.objects.get(id=id)

        # Registrar en historial
        HistorialAcciones.objects.create(
            fecha=timezone.now(),
            tipoObjeto="Usuario",
            objetoAfectado=f"{usuario_a_eliminar.nombre} {usuario_a_eliminar.apellido}",
            accion="Marcado como Deshabilitado",
            motivo=motivo,
            usuario=usuario
        )

        # Eliminar lógicamente
        estado_eliminado = EstadoUsuario.objects.get(descripcion="Deshabilitado")
        usuario_a_eliminar.estadoUsuario = estado_eliminado
        usuario_a_eliminar.save()

        usu = Usuario.objects.filter(activo=True)
        datos = {'usu': usu, 'r': f'El usuario {id} se ha marcado como inactivo correctamente'}
        return render(request, "listar_usuarios.html", datos)

    except Exception as e:
        usu = Usuario.objects.filter(activo=True)
        datos = {'usu': usu, 'r2': f'No se ha podido eliminar el usuario {id}: {e}'}
        return render(request, "listar_usuarios.html", datos)



