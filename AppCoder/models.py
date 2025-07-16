from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()
    
    def __str__(self):
        return f"{self.nombre} ({self.camada})"



class Alumno(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField(unique=True)
    fecha_nacimiento = models.DateField()
    dni = models.IntegerField(unique=True)
    materia = models.ManyToManyField(Curso, blank=True)

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"

class Profesor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField(unique=True)
    dni = models.IntegerField(unique=True)
    materia = models.ManyToManyField(Curso, blank=True)
    profesion = models.CharField(max_length=40, null=True, blank=True)

    def __str__(self):
        return f"Prof. {self.apellido}"