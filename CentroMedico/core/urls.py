from django.urls import path
from .views import home, poblar_bd, vehiculo, vehiculo_tienda, vehiculo_ficha,admin, secretaria,cajero, medico, paciente

urlpatterns = [
    path('', home, name="home"),
    path('poblar_bd', poblar_bd, name="poblar_bd"),
    path('vehiculo/<action>/<id>', vehiculo, name="vehiculo"),
    path('vehiculo_tienda', vehiculo_tienda, name="vehiculo_tienda"),
    path('vehiculo_ficha/<id>', vehiculo_ficha, name="vehiculo_ficha"),
    path('admin' ,admin, name="admin"),
    path('secretaria' ,secretaria, name= "secretaria"),
    path('paciente', paciente, name="paciente"),
    path('medico',medico, name="medico"),
    path('cajero', cajero, name="cajero")

]
