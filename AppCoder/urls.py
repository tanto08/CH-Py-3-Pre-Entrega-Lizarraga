from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import  LogoutView
from .forms import BootstrapAuthenticationForm, BootstrapPasswordResetForm, BootstrapSetPasswordForm
from django.conf import settings
from django.conf.urls.static import static

app_name = "AppCoder"

urlpatterns = [
    # URLs principales de la aplicación
    path('', views.inicio, name='inicio'), 
    path('profesores/', views.profesores, name='profesores'),
    path('alumnos/', views.alumnos, name='alumnos'),
    path('cursos/', views.cursos, name='cursos'),
    path('contacto/', views.contacto, name='contacto'),
    
    
    # URLs para gestión de cursos
    path('alta_curso/', views.curso_formulario, name='alta_curso'),
    path('buscar_curso/', views.buscar_curso, name='buscar_curso'),
    path('buscar/', views.buscar, name='buscar'),
    path('eliminar_curso/<int:id>/', views.eliminar_curso, name='eliminar_curso'),
    path('editar_curso/<int:id>/', views.editar_curso, name='editar_curso'),
    
    # URLs de registro de usuarios
    path('registro/alumno/', views.registro_alumno, name='registro_alumno'),
    path('registro/profesor/', views.registro_profesor, name='registro_profesor'),
    path('registro/', views.seleccion_registro, name='seleccion_registro'),
    
    # URLs de autenticación (con namespace AppCoder)
    path('accounts/login/', auth_views.LoginView.as_view(
        template_name='AppCoder/login.html',
        authentication_form=BootstrapAuthenticationForm,
        redirect_authenticated_user=True
    ), name='login'),
    
    path('accounts/logout/', LogoutView.as_view(next_page='AppCoder:inicio'), name="Logout"),

    #URLs para gestion de usuario
    path('perfil/', views.perfil_usuario, name='perfil_usuario'),
    
    # URLs para recuperación de contraseña
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(
        template_name='AppCoder/password_reset.html',
        form_class=BootstrapPasswordResetForm,
        email_template_name='AppCoder/password_reset_email.html',
        subject_template_name='AppCoder/password_reset_subject.txt',
        success_url='done/'
    ), name='password_reset'),
    
    path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='AppCoder/password_reset_done.html'
    ), name='password_reset_done'),
    
    path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='AppCoder/password_reset_confirm.html',
        form_class=BootstrapSetPasswordForm,
        success_url='/AppCoder/accounts/reset/done/'
    ), name='password_reset_confirm'),
    
    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='AppCoder/password_reset_complete.html'
    ), name='password_reset_complete'),

    path('trigger-404/', views.trigger_404, name='trigger_404'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)