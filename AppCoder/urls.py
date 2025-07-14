from django.urls import path 
from . import views
from django.contrib.auth import views as auth_views

urlpatterns=[
    path("", views.inicio), 
    path("profesores", views.profesores , name="profesores"),
    path("alumnos", views.alumnos, name="alumnos"),
    path('cursos' , views.cursos, name="cursos"),
    path("contacto", views.contacto, name="contacto"),
     #path("alta_curso/<str:nombre>" , views.alta_curso),
    path("alta_curso", views.curso_formulario, name="alta_curso"),
    path("buscar_curso", views.buscar_curso),
    path("buscar", views.buscar),
    path("eliminar_curso/<int:id>", views.eliminar_curso, name="eliminar_curso"),    
    path("editar_curso/<int:id>", views.editar, name="editar_curso"),
    path('registro/alumno/', views.registro_alumno, name='registro_alumno'),
    path('registro/profesor/', views.registro_profesor, name='registro_profesor'),
    path('registro/', views.seleccion_registro, name='seleccion_registro'),
     
      
] 