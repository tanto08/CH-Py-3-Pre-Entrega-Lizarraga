from django.contrib.auth.models import User
from django import forms
from .models import Alumno, Profesor
from django.contrib.auth.forms import UserCreationForm

class Curso_formulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    camada = forms.IntegerField()

class AlumnoRegistroForm(UserCreationForm):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    email = forms.EmailField()
    fecha_nacimiento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    dni = forms.IntegerField()
    
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'nombre', 'apellido', 'email', 'fecha_nacimiento', 'dni']

class ProfesorRegistroForm(UserCreationForm):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    email = forms.EmailField()
    dni = forms.IntegerField()
    profesion = forms.CharField(max_length=40, required=False)
    
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'nombre', 'apellido', 'email', 'dni', 'profesion']