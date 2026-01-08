
from django.contrib import admin
from django.urls import path
from bicicletas import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    #INDEX: PÁGINA PRINCIPAL
    path('', views.mostrarIndex, name='mostrarIndex'),
    path('filtrarcategoria', views.funcionFiltrarCategoria, name="funcionfiltrarcategoria"),
    path('buscador', views.funcionBuscador, name="funcionBuscador"),
    path('botones', views.funcionBotones, name="funcionBotones"),
    #INICIO SESIÓN
    path('Inicio de Sesion', views.mostrarInicioSesion, name='mostrarInicioSesion'),
    path('iniciar Sesion', views.funcionInicioSesion, name='funcionInicioSesion'),
    path('registro_usuario', views.mostrarRegistroUsuario),
    path('registrar_usuario',views.RegistrarUsuario),
    path('cerrar Sesion', views.funcionCerrarSesion, name='cerrar Sesion'),
#**************************PERFIL DE USUARIO***********************************
    path('pagar', views.funcionBotonPagar, name='funcionBotonPagar'),
    #CARRITO DE COMPRAS
    path('Carrito de Compras', views.mostrarCarritoDeCompras, name='mostrarCarritoDeCompras'),
    #HISTORIAL DE COMPRAS
    path('Historial de Compras', views.mostrarHistorialDeCompras, name='mostrarHistorialDeCompras'),
    #PERFIL DE USUARIO
    path('perfil_usuario', views.mostrarPerfilUsuario, name='mostrarPerfilUsuario'),
    path('actualizar_perfil', views.actualizarUsuario, name='actualizar_usuario'),
    path('cambiar_contrasena', views.cambiarContrasena, name='cambiar_contrasena'),
#--------------AGENDAMIENTOS---------------------------------
    path('Agendamientos', views.mostrarAgendamientos, name='mostrarAgendamientos'), 
    path('procesar_agendamiento', views.procesarAgendamientos, name='procesarAgendamientos'),
    path('seguimiento_pedido_cli', views.visualizarSeguimientoCliente, name='seguimiento_pedido_cli'),
#--------------SEGUIMIENTO_DEL_PEDIDO----------------------------------------------------
    path('seguimiento_cliente', views.mostrarSeguimientoCliente, name='mostrarSeguimientoCliente'),
    #link AYAX para que acepte las comunas acorde a la región de manera DINAMICA
    path('get_comunas_por_region/<int:region_id>/', views.get_comunas_por_region, name='get_comunas_por_region'),


#*********************PERFIL ADMINISTRADOR**************************************
#V. AGREGAR REGISTROS
    path('registrarproducto', views.mostraragregarproducto),
    path('insertarproducto', views.agregarproducto),
    path('agregarcategorias',views.mostraragregarcategorias),
    path('insertarcategoria',views.agregarcategoria),
    path("agregarhoras", views.mostraragregarhoras),
    path('insertarhoras',views.agregarhoras),
#V. LISTAS  
    path('dashboard',views.mostrardashboard, name='mostrardashboard'),
    path('listarproductos',views.mostrarlistapro, name='mostrarlistapro'),
    path('listarusuarios',views.mostrarlistausu),
    path('listarcategorias',views.mostrarlistacat),
    path('lista_agendas', views.mostrarlistaagendas),
    path('listar_historial', views.mostrarhistorialAcciones),
#V. MODIFICAR REGISTROS 
    path('modificarproducto/<int:id>',views.mostrarmodificarproducto),
    path('modificarcategoria/<int:id>',views.mostrarmodificarcategoria),
    path('actualizarcategoria/<int:id>',views.actualizarcategoria),
    path('actualizarproducto/<int:id>',views.actualizarproducto),
    path('actualizar_estado/<int:reparacion_id>/', views.actualizar_estado),
#V. DILIT REGISTROS
    path('eliminarproducto/<int:id>',views.eliminarproducto),
    path('eliminarcategoria/<int:id>',views.eliminarcategoria),
    path('eliminarusuario/<int:id>',views.eliminarusuario),
#A. SEGUIMIENTO
    path('seguimiento_admin', views.mostrarSeguimientoAdmin, name='seguimiento_admin'),
    path('seguimiento_pedido_admin', views.visualizarSeguimientoAdmin, name = 'seguimiento_pedido_admin'),
    path('actualizacion_pedido_admin', views.actualizar_estado_envio_admin, name='actualizar_estado_envio_admin'),
#A. ADMIN-COMPRA_PRESENCIAL
    path('presencial_admin', views.mostrarSeguimientoAdminPresencial, name='presencialAdmin'),
    path('presencial_admin_comprado', views.confirmarCompra, name = 'confirmarCompra')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

