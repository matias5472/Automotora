from django.shortcuts import render, redirect
from .models import Estado, Genero, Region, TipoVivienda, Raza, Mascota, Comuna,  Cliente
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def home(request):
    return render(request, 'core/home.html')


def galeria(request):
    return render(request, 'core/galeria.html')

def listado_mascotas(request):

    mascotas = Mascota.objects.all()

    variables = {
        'mascotas':mascotas
    }

    return render(request, 'core/listar_mascotas.html', variables)


def formulario(request):

    regiones = Region.objects.all()
    comunas = Comuna.objects.all()
    tipovivienda = TipoVivienda.objects.all()

    variable = {
        'regiones': regiones,
        'comunas': comunas,
        'tipovivienda': tipovivienda
    }

    if request.POST:

        cliente = Cliente()
        cliente.rut = request.POST.get('txtrut')
        cliente.nomCompleto = request.POST.get('txtnombres')
        cliente.email = request.POST.get('txtcorreo')
        cliente.fono = request.POST.get('txttelefono')
        cliente.fechaNaci = request.POST.get('fechanaci')

        region = Region()
        region.id = request.POST.get('cboregion')
        cliente.Region = region

        comuna = Comuna()
        comuna.id = request.POST.get('cbocomuna')
        cliente.Comuna = comuna

        tipovivienda = TipoVivienda()
        tipovivienda.id = request.POST.get('cbovivienda')
        cliente.TipoVivienda = tipovivienda

        cliente.save()
        try:

            variable['mensaje'] = 'Cliente Guardado correctamente'
        except:
            variable['mensaje'] = 'Cliente No se ha podido guardar'

    return render(request, 'core/registro.html', variable)



def agregar_mascota(request):
    #buscaremos todas las mascotas
    #y se las enviaremos al template

    genero = Genero.objects.all()
    estado = Estado.objects.all()
    raza = Raza.objects.all()

    variables = {
       'genero': genero,
        'estado': estado,
        'raza': raza,
    }

    if request.POST:

        Masc = Mascota()
        Masc.nombre = request.POST.get('nombremascota')
        Masc.fechaIngreso = request.POST.get('ingreso')
        Masc.fechaNacimiento = request.POST.get('nacimiento')
        Masc.Foto = request.FILES.get('Foto')

        genero = Genero()
        genero.id = request.POST.get('cbogenero')
        Masc.Genero = genero

        estado = Estado()
        estado.id = request.POST.get('cboestado')
        Masc.Estado = estado

        raza = Raza()
        raza.id = request.POST.get('razamascota')
        Masc.Raza = raza

        Masc.save()

        try:
            variables['mensaje'] = 'Mascota ingresada correctamente'
        except:
            variables['mensaje'] = 'La mascota no se pudo ingresar correctamente'
            
    return render(request, 'core/agregar_mascota.html', variables)

def eliminar_mascota(request, id):
    #primer paso encontrar el automovil
    mascota = Mascota.objects.get(id=id)

    #una vez encontrado el automovil se elimina
    try:
        mascota.delete()
        messages.success(request, 'Eliminado correctamente')
    except:
        messages.error(request, 'No se ha podido eliminar')
    
    #redirigiremos al usuario de vuelta al listado
    return redirect('listado_mascotas')

def modificar_mascota(request, id):
    #Buscamos la mascota para que el usuario lo pueda modificar
    mascota = Mascota.objects.get(id=id)
    raza = Raza.objects.all()
    genero = Genero.objects.all()
    estado = Estado.objects.all()
    variables = {
        'mascota':mascota,
        'raza':raza,
        'genero':genero,
        'estado':estado,
    }

    if request.POST:
        mascota = Mascota()
        mascota.nombre = request.POST.get('nombremascota')
        mascota.fechaIngreso = request.POST.get('ingreso')
        mascota.fechaNacimiento = request.POST.get('nacimiento')
        

        genero = Genero()
        genero.id = request.POST.get('cbogenero')
        mascota.Genero = genero

        estado = Estado()
        estado.id = request.POST.get('cboestado')
        mascota.Estado = estado

        raza = Raza()
        raza.id = request.POST.get('razamascota')
        mascota.Raza = raza

        mascota.imagen = request.FILES.get('Foto')

        try:
            mascota.save()
            messages.success(request, 'Mascota Modificada correctamente')
        except:
            messages.error(request, 'No se ha podido Modificar' )
        return redirect('listado_mascotas')

    return render(request,'core/modificar_mascota.html', variables)