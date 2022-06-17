from django.shortcuts import render
from .forms import UserRegisterForm, LoginForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
# Create your views here.
from django.views.generic import(
    View,
    CreateView
)
from django.views.generic.edit import(
    FormView
)

from .models import User

class UserRegisterView(FormView):
    template_name = 'registro.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('users_app:user_login')
    
    def form_valid(self, form):
        #
        User.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['email'],
            form.cleaned_data['password1'],
            nombres = form.cleaned_data['nombres'],
            apellidos = form.cleaned_data['apellidos'],
            genero = form.cleaned_data['genero'],
        )
        #
        return super(UserRegisterView, self).form_valid(form)
    
class LoginUser(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('app_zavod:home')
    
    def form_valid(self, form):
        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password'],
            
        )
        login(self.request, user)
        return super(LoginUser, self).form_valid(form)

class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(
            reverse('app_zavod:home')
        )
    
