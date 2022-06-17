from django.contrib import admin
from .models import Imagenes, Pedido, Producto, Estado, Empleado, Cliente

# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    list_display=("nombre_cliente","rut_cliente","email_cliente")
    search_fields= ("nombre_cliente","rut_cliente")

    
admin.site.register(Cliente, ClienteAdmin)

class ImagenesAdmin(admin.ModelAdmin):
    list_display=("title","sub_title")


admin.site.register(Imagenes, ImagenesAdmin)


class ProductoAdmin(admin.ModelAdmin):
    list_display=("nombre_producto","cantidad", "idProducto")
    
admin.site.register(Producto, ProductoAdmin)


admin.site.register(Pedido)

admin.site.register(Estado)
admin.site.register(Empleado)
