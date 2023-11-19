from django.urls import path
from .views import home, poblar_bd,administrador, secretaria,cajero, medico, paciente, Usuario

urlpatterns = [
    path('', home, name="home"),
    path('poblar_bd', poblar_bd, name="poblar_bd"),
    path('Usuario/<action>/<id>', Usuario, name="Usuario"),
    path('administrador' ,administrador, name="administrador"),
    path('secretaria' ,secretaria, name= "secretaria"),
    path('paciente', paciente, name="paciente"),
    path('medico',medico, name="medico"),
    path('cajero', cajero, name="cajero")

]
