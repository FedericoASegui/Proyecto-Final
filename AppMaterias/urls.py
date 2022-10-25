from django.urls import path
from AppMaterias import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('about', views.about, name='Acerca de mí'),
    path('OfertaCalificada', views.addOfertaCalificada, name='Añadir Oferta Calificada'),
    path('buscar/', views.buscar),
    path('addMaterias', views.addMaterias, name='Añadir Materias'),
    path('Materias', views.materias, name='Materias'),
    path("editarMateria/<asignatura_materia>", views.editarMateria, name="Editar Materia"),
    path("borrarMateria/<asignatura_materia>", views.borrarMaterias, name="Borrar Materia"),
    path('agregarAvatar/', views.agregarAvatar, name="Avatar"),

    path('login', views.login_request, name = 'Login'),
    path('logout', LogoutView.as_view(template_name='AppMaterias/Autenticar/logout.html'), name='Logout'),
    path('register', views.register, name = 'Register'),
    path("editarUsuario", views.editarUsuario, name="Editar Usuario"),

]
