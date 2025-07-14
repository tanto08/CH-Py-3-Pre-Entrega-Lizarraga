from django.shortcuts import render, redirect# type: ignore
from django.http import HttpResponse
from AppCoder.models import Curso
from django.template import loader
from django.contrib.auth.models import User
from AppCoder.forms import Curso_formulario
from .forms import AlumnoRegistroForm, ProfesorRegistroForm
from .models import Alumno, Profesor
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
# Create your views here.



def inicio(request):
    return render(request, "padre.html")


def cursos(request):
    cursos = Curso.objects.all()
    dicc = {"cursos":cursos}
    plantilla = loader.get_template("cursos.html")
    documento = plantilla.render(dicc)
    return HttpResponse( documento)



def alta_curso(request, nombre):
    curso = Curso(nombre=nombre , camada=99999)
    curso.save()
    msj = f"Se guardo el curso {curso.nombre} {curso.camada}"
    return HttpResponse(msj)



def profesores(request):
    return render(request, "profesores.html")


def alumnos(request):
    return render(request, "alumnos.html")



def contacto(request):
    return render(request, "contacto.html")




def curso_formulario(request):

    if request.method == "POST":
        mi_formulario = Curso_formulario( request.POST )

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data          
            
            curso = Curso( nombre=datos['nombre'] , camada=datos['camada'])
            curso.save()

            return render( request , "padre.html")                 
        
    
    return render( request , "formulario.html")






def buscar_curso(request):
    return render(request , "buscar_curso.html")

def buscar(request):
    
    if request.POST["nombre"]:
        cursos = Curso.objects.filter(nombre__icontains=request.POST["nombre"])
        return render(request, "resultado_busqueda.html", {"cursos":cursos})
    else:
        return HttpResponse("No se ha encontrado nada")
    


def eliminar_curso(request, id):
    
    curso = Curso.objects.get(id=id)
    curso.delete()

    curso = Curso.objects.all()

    return render(request, "cursos.html" , {"cursos":curso})




def editar( request , id ):

    curso = Curso.objects.get(id=id) 
    
    if request.method == "POST":
        mi_formulario = Curso_formulario(request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            curso.nombre = datos['nombre']
            curso.camada = datos['camada']
            curso.save()

            curso = Curso.objects.all()
            return render(request , "cursos.html" , {"cursos":curso})


    else:
        mi_formulario = Curso_formulario(initial={'nombre':curso.nombre, 'camada':curso.camada})

    return render(request , "editar_curso.html" , {"mi_formulario":mi_formulario, "curso":curso })
       

def seleccion_registro(request):
    return render(request, 'AppCoder/seleccion_registro.html')

def registro_alumno(request):
    if request.method == 'POST':
        form = AlumnoRegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('inicio')
    else:
        form = AlumnoRegistroForm()
    return render(request, 'AppCoder/registro_alumno.html', {'form': form})

def registro_profesor(request):
    if request.method == 'POST':
        form = ProfesorRegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('inicio')
    else:
        form = ProfesorRegistroForm()
    return render(request, 'AppCoder/registro_profesor.html', {'form': form})