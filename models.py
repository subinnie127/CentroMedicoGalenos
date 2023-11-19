from django.db import models

class Usuario(models.Model):
    rut = models.CharField(max_length=10, primary_key=True, verbose_name="rut")
    nombre = models.CharField(max_length=80, blank=False, null=False, verbose_name="nombre")
    apellido = models.CharField(max_length=80, null=True, blank=True, verbose_name="apellido")
    TIPO_DE_USUARIO = (
        ('Secretaria', 'Secretaria'),
        ('Cajero', 'Cajero'),
        ('Medico', 'Medico'),
        ('Paciente', 'Paciente'),
    )
    tipo_de_usuario = models.CharField(max_length=40, 
                                       blank=False, null=False, 
                                       verbose_name="tipo de usuario", 
                                       choices=TIPO_DE_USUARIO)

    def __str__(self):
        return self.rut
