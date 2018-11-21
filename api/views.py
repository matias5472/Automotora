from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import json
from django.core import serializers
from django.http import HttpResponse, HttpResponseBadRequest
from core.models import Raza, Genero, Estado, Foto, Mascota

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods


# Create your views here.

from fcm_django.models import FCMDevice

@csrf_exempt
@require_http_methods(['POST'])
def agregar_token(request):
    body = request.body.decode('utf-8')
    bodyDict = jsin.loads(body)
    token = bodyDict['token']

    #preguntamos si ya existe el token en la BBDD
    existe = FCMDevice.objects.filter(registration_id=token, active=True)

    if existe:
        return HttpResponseBadRequest(json.dumps({'mensaje':'El Token ya Existe'}), content_type="application/json")


    dispositivo = FCMDevice()
    dispositivo.registration_id = token
    dispositivo.active = True
    #solo en caso de que el usuario este autenticado lo guardaremos

    if request.user.is_authenticated:
        dispositivo.user = request.user
    
    #procedemos a guardar el dispositivo con el token en la abse de datos
    try:
        dispositivo.save()
        return HttpResponse(json.dumps({'mensaje':'Token Guardado'}), content_type="application/json")
    except:
        return HttpResponseBadRequest(json.dumps({'mensaje':'No se pudo Guardar Token'}), content_type="application/json")


#Crearemos un listado de automoviles en formato json
def listado_mascotas(request):
    mascotas = Mascota.objects.all()
    #transformamos el listado de autos en json
    mascotasSerializadas = serializers.serialize('json', mascotas)

    #mostramos al usuario los datos
    return HttpResponse(mascotasSerializadas, content_type = "application/json")

@csrf_exempt
@require_http_methods(['POST'])
def agregar_mascota(request):
    body = request.body.decode('utf-8')
    #transformamos el body que estaba en un string a un json
    bodyJson = json.loads(body)

    mascota = Mascota()
    mascota.nombre = bodyJson['nombremascota']
    mascota.fechaIngreso = bodyJson['ingreso']
    mascota.fechaNacimiento = bodyJson['nacimiento']
    mascota.Raza = (id=bodyJson['Raza_id'])
    mascota.Genero = (id=bodyJson['Genero_id'])
    mascota.Estado = (id=bodyJson['Estado_id'])
    #mascota.Foto = ()

    try:
        auto.save()
        return HttpResponse(json.dumps({'mensaje':'agregado correctamente'}), content_type="application/json")
    except:
        return HttpResponseBadRequest(json.dumps({'mensaje':'no se ha podido correctamente'}), content_type="application/json")

@csrf_exempt
@require_http_methods(['PUT'])
def modificar_auto(request):
    body = request.body.decode('utf-8')
    #transformamos el body que estaba en un string a un json
    bodyJson = json.loads(body)

    auto = Automovil()
    auto.id = bodyJson['id']
    #auto.patente = bodyJson['patente']
    auto.modelo = bodyJson['modelo']
    auto.anio = bodyJson['anio']
    auto.marca = Marca(id=bodyJson['marca_id'])

    try:
        auto.save()
        return HttpResponse(json.dumps({'mensaje':'modificado correctamente'}), content_type="application/json")
    except:
        return HttpResponseBadRequest(json.dumps({'mensaje':'no se ha modificar correctamente'}), content_type="application/json")

@csrf_exempt
@require_http_methods(['DELETE'])
def eliminar_auto(request, id):
    try:
        auto = Automovil.objects.get( id=id )
        auto.delete()
        return HttpResponse(json.dumps({'mensaje':'Eliminado correctamente'}), content_type="application/json")
    except:
        return HttpResponseBadRequest(json.dumps({'mensaje':'no se ha eliminar correctamente'}), content_type="application/json")