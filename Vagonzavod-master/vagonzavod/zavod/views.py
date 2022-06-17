from turtle import update
from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView, FormView, UpdateView, DeleteView
from .models import Cliente, Producto, Imagenes
from django.urls import reverse_lazy
from .forms import ProductRegisterForm, UserRegisterForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.


def Home(request):
    home = Imagenes.objects.all()
    context = {'home':home}
    return render(request, 'home.html', context)

def Productos(request):
    producto = Producto.objects.all()
    context = {'producto':producto}
    return render(request, 'productos.html', context)

def ValidarCompra(request):
    return render(request, "validar_compra.html")


# class CreateUser(CreateView):
#     model = Cliente
#     template_name = "registro.html"
#     form_class = UserRegisterForm
   
#     success_url = reverse_lazy('app_zavod:home')
    
#     def form_valid(self, form):
#         #logica del proceso
#         cliente = form.save()
#         cliente.save()
#         return super(CreateUser, self).form_valid(form)

class DetalleProducto(DetailView):
    model = Producto
    template_name = "detalle_producto.html"
    
    def get_context_data(self, **kwargs):
        context = super(DetalleProducto, self).get_context_data(**kwargs)
        context['titulo'] = 'Motor del mes'
        return context

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword",'')
        lista = Producto.objects.filter(
            idProducto__icontains=palabra_clave
        )
        return lista
    
    
    
class StaffRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):

    def test_func(self):
            return self.request.user.is_staff


class ListObj(StaffRequiredMixin, ListView):
           
    template_name = 'objetos_admin.html'
    login_url = reverse_lazy('users_app:user_login')
    paginate_by = 4
    ordering = 'idProducto'
    context_object_name = 'productos'
    
    def get_queryset(self):

        palabra_clave = self.request.GET.get("kword",'')
        
        lista = Producto.objects.filter(
            nombre_producto__icontains=palabra_clave
        )
        return lista

class CreateProduct(StaffRequiredMixin, CreateView):
    model = Producto
    template_name = "add_prd.html"
    form_class = ProductRegisterForm
   
    success_url = reverse_lazy('app_zavod:obj_adm')
    
    def form_valid(self, form):
        #logica del proceso
        producto = form.save()
        producto.save()
        return super(CreateProduct, self).form_valid(form)


class UpdateObj(StaffRequiredMixin, UpdateView):
    template_name= "update_obj.html"
    model = Producto
    fields = ('__all__')
    success_url = reverse_lazy('app_zavod:obj_adm')
    
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

class DeleteObj(StaffRequiredMixin, DeleteView):
    model = Producto
    template_name = "delete.html"
    success_url = reverse_lazy('app_zavod:obj_adm')