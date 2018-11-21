from django.urls import path
from .views import home, galeria, formulario, agregar_mascota, listado_mascotas

urlpatterns = [
    path('', home, name='home'),
    path('galeria/', galeria, name='galeria'),
    path('registro/', formulario, name='formulario'),
    path('Registro-de-Mascota/', agregar_mascota, name="agregar_mascota"),
    path('listado-de-mascotas', listado_mascotas, name="listado_mascotas"),
]