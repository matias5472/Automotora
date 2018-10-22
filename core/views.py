from django.shortcuts import render

def home(request):
    return render(request, 'core/base.html')


def galeria(request):
    return render(request, 'core/galeria.html')


def formulario(request):
    return render(request, 'core/registro.html')


def agregar_mascota(request):
    return render(request, 'core/agregar_mascota.html')
