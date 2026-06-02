from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class UsuarioPersonalizado(AbstractUser):
    telefono = models.CharField(max_length=20, null=True, blank=True)
    dni = models.CharField(max_length=20, null=True, blank=True)
    # nombre_usuario = models.CharField(max_length=50, null=True, blank=True)
    direccion = models.CharField(max_length=100, null=True, blank=True)
    foto_perfil = models.ImageField(upload_to='users_fp/', null=True, blank=True)


    def __str__(self):
        return f"{self.username} - {self.dni}"