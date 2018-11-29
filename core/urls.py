from django.urls import path
from .views import home, galeria, formulario, agregar_mascota, listado_mascotas, eliminar_mascota, modificar_mascota

urlpatterns = [
    path('', home, name='home'),
    path('galeria/', galeria, name='galeria'),
    path('registro/', formulario, name='formulario'),
    path('Registro-de-Mascota/', agregar_mascota, name="agregar_mascota"),
    path('listado-de-mascotas/', listado_mascotas, name="listado_mascotas"),
    path('eliminar-mascota/<id>/', eliminar_mascota, name="eliminar_mascota"),
    path('modificar-mascota/<id>/', modificar_mascota, name="modificar_mascota"),
]
