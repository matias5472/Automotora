from django.urls import path
from .views import agregar_mascota, listado_mascotas, eliminar_mascota, modificar_mascota,agregar_token

urlpatterns = [
    path('registro-de-mascota/', agregar_mascota, name="api_agregar_mascota"),
    path('listado-de-mascotas/', listado_mascotas, name="api_listado_mascotas"),
    path('eliminar-mascota/<id>/', eliminar_mascota, name="api_eliminar_mascota"),
    path('modificar-mascota/', modificar_mascota, name="api_modificar_mascota"),
    path('agregar-token/', agregar_token, name="api_agregar_token"),
]   