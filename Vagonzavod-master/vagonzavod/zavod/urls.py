from django.urls import path

from . import views

app_name = 'app_zavod'
urlpatterns = [
    # path('', views.all_products, name ='all_products'),
    path('', views.Home, name='home'),
    path('productos/', views.Productos, name='productos'),
    path('detalle_producto/<pk>/', views.DetalleProducto.as_view(), name='detalle_producto'),

    path('objetos-admin/', views.ListObj.as_view(), name='obj_adm'),
    path('add-prd/', views.CreateProduct.as_view(), name='add_prd'),
    path('update-prd/<pk>', views.UpdateObj.as_view(), name='update_prd'),
    path('delete-prd/<pk>', views.DeleteObj.as_view(), name='delete_prd'),
    path("validar-compra", views.ValidarCompra, name="validar_compra")
]