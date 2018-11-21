from django.shortcuts import render
#importaremos el formulario de registro desde django
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomCreationUserForm

# Create your views here.

def register(request):

    variables = {
        'form':CustomCreationUserForm
    }
    
    if request.POST:
        #llenamos el objeto formulario con los datos
        #que vienen por POST
        form = CustomCreationUserForm(request.POST)
        if form.is_valid():
            #si no hay errores de validaciones
            #guardaremos el usuario
            form.save()
            variables['mensaje'] = "Usuario registrado"
        else:
            variables['mensaje'] = "No se pudo registrar el usuairo"
            #volvemos a enviar el formulario para que se muestren los errores de valdiacion
            variables['form'] = form

    return render(request, 'accounts/register.html', variables)
