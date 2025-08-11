from django.shortcuts import render, redirect, get_object_or_404 # type: ignore
from django.http import HttpResponse, Http404
from AppCoder.models import Curso
from django.template import loader
from django.contrib.auth.models import User
from AppCoder.forms import CursoFormulario
from .forms import AlumnoRegistroForm, ProfesorRegistroForm, AvatarForm
from .models import Alumno, Profesor
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required

# Create your views here.


def inicio(request):
    return render(request, "AppCoder/inicio.html")



def cursos(request):
    cursos = Curso.objects.all()
    dicc = {"cursos":cursos}
    return render(request, "cursos.html", dicc)



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
    return render(request, 'AppCoder/contacto.html')




def curso_formulario(request):
    if request.method == "POST":
        mi_formulario = CursoFormulario(request.POST)  
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data          
            curso = Curso(nombre=datos['nombre'], camada=datos['camada'])
            curso.save()
            return redirect('AppCoder:cursos')  # redirige a la lista de cursos
    else:
        mi_formulario = CursoFormulario()  

    return render(request, "AppCoder/formulario.html", {"mi_formulario": mi_formulario})






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
    return render(request, "cursos.html", {"cursos": curso})




def editar_curso(request, id):
    curso = get_object_or_404(Curso, id=id)
    
    if request.method == 'POST':
       
        mi_formulario = CursoFormulario(request.POST, instance=curso)
        if mi_formulario.is_valid():
            mi_formulario.save()
            return redirect('cursos')  # Redirige a la lista de cursos
    else:
        
        mi_formulario = CursoFormulario(instance=curso)
    
    return render(request, 'editar_curso.html', {
        'mi_formulario': mi_formulario,
        'curso': curso
    })
       

def seleccion_registro(request):
    return render(request, 'AppCoder/seleccion_registro.html')

def registro_alumno(request):
    if request.method == 'POST':
        form = AlumnoRegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Crear perfil de alumno
            Alumno.objects.create(
                user=user,
                nombre=form.cleaned_data['nombre'],
                apellido=form.cleaned_data['apellido'],
                email=form.cleaned_data['email'],
                fecha_nacimiento=form.cleaned_data['fecha_nacimiento'],
                dni=form.cleaned_data['dni']
            )
            login(request, user)
            return redirect('AppCoder:inicio')  # Cambia esto según tu URL de inicio
    else:
        form = AlumnoRegistroForm()
    return render(request, 'AppCoder/registro_alumno.html', {'form': form})

def registro_profesor(request):
    if request.method == 'POST':
        form = ProfesorRegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Crear perfil de profesor
            Profesor.objects.create(
                user=user,
                nombre=form.cleaned_data['nombre'],
                apellido=form.cleaned_data['apellido'],
                email=form.cleaned_data['email'],
                dni=form.cleaned_data['dni'],
                profesion=form.cleaned_data.get('profesion', '')
            )
            login(request, user)
            return redirect('AppCoder:inicio')  # Cambia esto según tu URL de inicio
    else:
        form = ProfesorRegistroForm()
    return render(request, 'AppCoder/registro_profesor.html', {'form': form})


@login_required
def perfil_usuario(request):
    if request.method == 'POST':
        pass_form = PasswordChangeForm(request.user, request.POST)
        avatar_form = AvatarForm(request.POST, request.FILES, instance=request.user.profile)
        
        if 'password_change' in request.POST and pass_form.is_valid():
            user = pass_form.save()
            update_session_auth_hash(request, user)  # para que no cierre sesión
            return redirect('AppCoder:perfil_usuario')
        
        if 'avatar_change' in request.POST and avatar_form.is_valid():
            avatar_form.save()
            return redirect('AppCoder:perfil_usuario')
    else:
        pass_form = PasswordChangeForm(request.user)
        avatar_form = AvatarForm(instance=request.user.profile)
    
    return render(request, 'AppCoder/perfil_usuario.html', {
        'pass_form': pass_form,
        'avatar_form': avatar_form
    })

def trigger_404(request):
    raise Http404("Probando página 404 personalizada")