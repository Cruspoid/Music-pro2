from django import forms

from .models import Cliente, Producto

class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('__all__')
        
class ProductRegisterForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('__all__')
        