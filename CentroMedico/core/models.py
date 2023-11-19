from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.contrib.auth.hashers import make_password

class Usuario(AbstractUser):
    rut = models.CharField(max_length=10, primary_key=True, unique=True, verbose_name="rut")
    nombre = models.CharField(max_length=80, blank=False, null=False, verbose_name="nombre")
    apellido = models.CharField(max_length=80, null=True, blank=True, verbose_name="apellido")

    TIPO_DE_USUARIO = (
        ('Secretaria', 'Secretaria'),
        ('Cajero', 'Cajero'),
        ('Medico', 'Medico'),
        ('Paciente', 'Paciente'),
    )
    
    tipo_de_usuario = models.CharField(
        max_length=40,
        blank=False, null=False,
        verbose_name="tipo de usuario",
        choices=TIPO_DE_USUARIO
    )
    username = models.CharField(max_length=30, unique=True, default="11.111.111-1")

    groups = models.ManyToManyField(Group, related_name='usuarios')
    user_permissions = models.ManyToManyField(Permission, related_name='usuarios_permissions')

    def save(self, *args, **kwargs):
        # Utiliza el campo rut como username
        self.username = self.rut

        # Hashea y guarda la contraseña de manera segura
        self.password = make_password(self.password)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.rut
