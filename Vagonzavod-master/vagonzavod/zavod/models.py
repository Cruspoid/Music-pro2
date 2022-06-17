from pyexpat import model
from django.db import models

# Create your models here.

class Pedido(models.Model):
    idpedido = models.AutoField(primary_key = True,verbose_name = 'Id de pedido')
    estado_pedido = models.CharField(max_length = 20, verbose_name = 'EstadoP' )
    def __str__(self):
        return self.Pedido

class Producto(models.Model):
    
    Tipo_motor = (
        ('DIESEL', 'DIESEL'),
        ('PETROL', 'PETROL'),
        ('GAS', 'GAS'),
    )
    
    
    idProducto = models.AutoField(primary_key = True,verbose_name = 'Id de producto')
    nombre_producto = models.CharField(max_length = 100, verbose_name = 'Nombre de producto')
    image = models.ImageField(upload_to='images', verbose_name='Imagen')
    valor = models.IntegerField(verbose_name="valor")
    cantidad = models.IntegerField(verbose_name="cantidad")
    descripcion = models.CharField(verbose_name='descripcion', max_length=200)
    tipo_motor = models.CharField('Tipo de motor', max_length=10, choices=Tipo_motor)
    caballos_fuerza = models.IntegerField()
    peso = models.CharField(max_length=10)
    
    class Meta:   
        verbose_name = 'Productos'
        verbose_name_plural = 'Todos los Productos'

class Estado(models.Model):
    idEstado = models.AutoField(primary_key = True,verbose_name = 'Id de Estado')
    estado = models.CharField(max_length = 20, verbose_name = 'Estado' )
    def __str__(self):
        return self.Estado

class Empleado(models.Model):
    rut_empleado = models.CharField(max_length=12,verbose_name="RUT")
    nombre = models.CharField(max_length=100, verbose_name = "empleado" )
    appaterno = models.CharField(max_length=50, verbose_name= "apellido paterno" )
    apmaterno = models.CharField(max_length=50, verbose_name= "apellido materno" )
    def __str__  (self):
        return self.Empleado

class Cliente(models.Model):
    rut_cliente = models.CharField(max_length=10)
    nombre_cliente = models.CharField(max_length=50)
    apellido_cliente = models.CharField(max_length=50)
    celular_cliente = models.CharField(max_length=12)
    email_cliente = models.EmailField(max_length=50)
    contrasena_cliente = models.CharField(max_length=50)
    confirmar_contrasena_cliente = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Todos los Clientes'
        unique_together = ('rut_cliente','celular_cliente','email_cliente')
    
class Imagenes(models.Model):
    image = models.ImageField(upload_to='images')
    title = models.CharField(max_length=50)
    sub_title = models.CharField(max_length=200)
    
    class Meta:   
        verbose_name = 'Imagenes'
        verbose_name_plural = 'Todas las Imagenes'
    