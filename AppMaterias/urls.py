from django.urls import path
from AppMaterias import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('about', views.about, name='Acerca de mí'),
    path('Aprobadas', views.addMateria, name='Añadir Materia'),
    path('buscar/', views.buscar),
    path('addMaterias',views.addMaterias, name='Añadir Materias'),
    path('Materias', views.materias, name='Materias'),
    path("editarMateria/<materia_nombre>", views.editarMateria, name="Editar Materia"),

    path('login', views.login_request, name = 'Login'),
    path('logout', LogoutView.as_view(template_name='AppMaterias/Autenticar/logout.html'), name='Logout'),
    path('register', views.register, name = 'Register'),
    path("editarUsuario", views.editarUsuario, name="Editar Usuario"),

]
