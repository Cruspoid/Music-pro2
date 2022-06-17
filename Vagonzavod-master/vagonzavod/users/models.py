from django.db import models
from .managers import UserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

class User(AbstractBaseUser, PermissionsMixin):
    
    GENDER_CHOICES = (
        ('M', 'MASCULINO'),
        ('F', 'FEMENINO'),
        ('O', 'OTRO'),
    )
    
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField()
    nombres = models.CharField(max_length=50, blank=True)
    apellidos = models.CharField(max_length=50, blank=True)
    genero = models.CharField(max_length=1, choices = GENDER_CHOICES, blank=True)
    #
    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'
    
    REQUIRED_FIELDS = ['email',]

    objects = UserManager()

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return self.nombres + ' ' + self.apellidos