from django.urls import path
from .views import home, galeria, formulario, agregar_mascota

urlpatterns = [
    path('', home, name='home'),
    path('galeria/', galeria, name='galeria'),
    path('registro/', formulario, name='formulario'),
    path('Registro-de-Mascota/', agregar_mascota, name="agregar_mascota"),
]
