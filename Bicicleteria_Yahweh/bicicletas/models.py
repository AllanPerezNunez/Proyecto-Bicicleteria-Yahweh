from django.db import models


class TipoUsuario(models.Model):
    descripcion = models.TextField(max_length=20)
    def __str__(self):
        return str(self.descripcion)

class EstadoUsuario(models.Model):
    descripcion = models.TextField(max_length=20)
    def __str__(self):
        return str(self.descripcion)

class TipoTarjeta(models.Model):
    tipo = models.TextField(max_length=20)
    def __str__(self):
        return str(self.tipo)

class TipoProducto(models.Model):
    descripcion = models.TextField(max_length=30)
    def __str__(self):
        return str(self.descripcion)

class EstadoProducto(models.Model):
    descripcion = models.TextField(max_length=20)
    def __str__(self):
        return str(self.descripcion)

class Proveedor(models.Model):
    descripcion = models.TextField(max_length=20)
    def __str__(self):
        return str(self.descripcion)


class Tarjeta(models.Model):
    nroTarjeta = models.BigIntegerField()
    fechaCad = models.DateField()
    cvv = models.IntegerField()
    tipoTarjeta = models.ForeignKey(TipoTarjeta, on_delete=models.CASCADE)
    saldo = models.BigIntegerField()
    def __str__(self):
        return str(self.nroTarjeta + " - " + self.fechaCad + " - " + self.cvv + "-" + self.saldo)

class Usuario(models.Model):
    rut = models.TextField(max_length=13)
    nombre = models.TextField(max_length=20)
    apellido = models.TextField(max_length=20)
    correo = models.TextField(max_length=100)
    contrasena = models.TextField(max_length=100)
    telefono = models.BigIntegerField()
    tipoUsuario = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE)
    estadoUsuario = models.ForeignKey(EstadoUsuario, on_delete=models.CASCADE)
    tarjeta = models.ForeignKey(Tarjeta, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.rut + " - " + self.nombre + " - " + self.apellido + " - " + self.correo + " - " + self.contrasena  + " - " + self.telefono + " - " + self.tipoUsuario + " - " + self.estadoUsuario + " - " + self.tarjeta )

class Producto(models.Model):
    imagen = models.ImageField(upload_to="imagenes_bd/",null=True, blank=True)
    numeroFactura = models.IntegerField(null=True, blank=True)
    nombre = models.TextField(max_length=50)
    descripcion = models.TextField(max_length=30)
    material = models.TextField(max_length=30)
    stock = models.IntegerField() 
    precioCompra = models.IntegerField(null=True, blank=True)
    utilidad = models.FloatField(null=True, blank=True)
    precio = models.IntegerField(null=True, blank=True)
    tipoProducto = models.ForeignKey(TipoProducto, on_delete=models.CASCADE)
    estadoProducto = models.ForeignKey(EstadoProducto, on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return str(self.numeroFactura + " - " + self.nombre + " - " + self.descripcion + " - " + self.material + " - " + self.stock + " - " + self.precioCompra + " - " + self.utilidad + " - " + self.precioVenta + " - " + self.proveedor)

class Region(models.Model):
    nombre = models.CharField(max_length=40)

class Comuna(models.Model): # Necesitas este para 'comuna_entrega'
    nombre = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE) # Si tienes modelo Region
    tiempo_estimado_horas = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    def __str__(self): return self.nombre

class EstadoEnvio(models.Model):
    nombre = models.CharField(max_length=50, unique=True) # Nombre del estado (ej: 'En Ruta')
    porcentaje_visual = models.IntegerField(default=0) # 0, 25, 50, 75, 100
    orden = models.IntegerField(unique=True) # 1, 2, 3, etc.
    descripcion_cliente = models.TextField() # Mensaje para el cliente
    class Meta:
        # Esto es importante para que los estados siempre se ordenen por su número 'orden'
        ordering = ['orden'] 
        verbose_name = "Estado de Envío"
        verbose_name_plural = "Estados de Envío"

    def __str__(self):
        return self.nombre


class Compra(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    tarjeta = models.ForeignKey(Tarjeta, on_delete=models.CASCADE)
    nro_factura = models.TextField(max_length=15, null=True, blank=True)
    estado_seguimiento = models.ForeignKey(EstadoEnvio, on_delete=models.SET_NULL, null=True, blank=True )
    fecha_entrega_estimada = models.DateTimeField(null=True, blank=True)     
    direccion = models.TextField(max_length=100)
    comuna_entrega = comuna_entrega = models.ForeignKey(
        'Comuna', # Asegúrate de que este modelo exista y esté importado
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        help_text="Comuna de destino para el envío a domicilio."
    )
    fecha_compra = models.DateTimeField()
    cantidad = models.IntegerField()
    estado_compra = models.TextField(max_length=50)
    
    def __str__(self):
        return str(self.usuario + " - " + self.producto + " - " + self.tarjeta + " - " + self.direccion + " - " + self.fecha_compra + " - " + self.cantidad + " - " + self.estado_compra)

class Carrito(models.Model):
    comprador = models.ForeignKey(Usuario, on_delete = models.CASCADE)
    articulo = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidadArt = models.IntegerField()
    def __str__(self):
        return str(self.cantidadArt)
    
class EstadoHora(models.Model):
    descripcion = models.TextField(max_length=20)   
    def __str__(self):
        return str(self.descripcion)
    
class HorasDisponibles(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    estado_hora = models.ForeignKey(EstadoHora, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.fecha + " - " + self.hora + " - " + self.estado_hora)
    
class EstadoReparacion(models.Model):
    descripcion = models.TextField(max_length=20)   
    def __str__(self):
        return str(self.descripcion)

class Reparacion(models.Model):
    fecha = models.DateField()
    hora_agendada = models.TimeField()
    observaciones = models.TextField(max_length=200)
    estado_reparacion = models.ForeignKey(EstadoReparacion, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.fecha + " - " + self.hora_agendada + " - " + self.observaciones + " - " + self.estado_reparacion + " - " + self.usuario)

class HistorialAcciones(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    tipoObjeto = models.CharField(max_length=50) 
    objetoAfectado = models.CharField(max_length=200) 
    accion = models.CharField(max_length=50) 
    motivo = models.TextField()
    def __str__(self):
        return f"{self.fecha} - {self.tipoObjeto} - {self.objetoAfectado} - {self.accion} - {self.motivo}"
