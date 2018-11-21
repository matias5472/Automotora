from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ValidationError


class CustomCreationUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    full_name = forms.CharField(required=True, label="Nombre_completo")

    #validaremos que no se ingrese dos veces el mismo correo
    def clean_email(self):
        email = self.cleaned_data['email']


        usuario = User.objects.filter(email=email)

        if usuario:
            raise ValidationError("El email ingresado ya existe")

    class Meta:
        #le diremos al formulario que al momento de guardar los
        #datos utiliazra e modelo User
        model = User
        #ahora le diremos el orden en que se mostraran los campos
        #en el formulario(en el navegador)
        fields = ('username', 'full_name','email', 'password1', 'password2')