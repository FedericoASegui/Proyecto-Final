from django.http import HttpResponse
from django.shortcuts import render
from AppMaterias.forms import AprobadaFormulario, MateriaFormulario, RegistroFormulario
from AppMaterias.models import Aprobada, Materia
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required


# Create your views here.

#Vista para registrarse
def register(request):

    if request.method == 'POST':    #cuando le haga click al botón

        form = RegistroFormulario(request.POST)   #leer los datos   llenados en el formulario

        if form.is_valid():

            user=form.cleaned_data['username']
            form.save()
            
            return render(request, "AppMaterias/inicio.html", {'mensaje':"Usuario Creado"})
    
    else:

        form = RegistroFormulario()   #formulario de django que nos permite crear usuarios.
    
    
    return render(request, "AppMaterias/Autenticar/registro.html", {'form':form})



#Vista para iniciar sesión
def login_request(request):

    if request.method == 'POST': #al presionar el botón "Iniciar Sesión"

        form = AuthenticationForm(request, data = request.POST) #leer la data del formulario de inicio de sesión

        if form.is_valid():
            
            usuario=form.cleaned_data.get('username')   #leer el usuario ingresado
            contra=form.cleaned_data.get('password')    #leer la contraseña ingresada

            user=authenticate(username=usuario, password=contra)    #buscar al usuario con los datos ingresados

            if user:    #si ha encontrado un usuario con eso datos

                login(request, user)   #hacemos login

                #mostramos la página de inicio con un mensaje de bienvenida.
                return render(request, "AppMaterias/inicio.html", {'mensaje':f"Bienvenido {user}"}) 

        else:   #si el formulario no es valido (no encuentra usuario)

            #mostramos la página de inicio junto a un mensaje de error.
    
            return render(request, "AppMaterias/inicio.html", {'mensaje':"Error. Datos incorrectos"})

    else:
            
        form = AuthenticationForm() #mostrar el formulario

    return render(request, "AppMaterias/Autenticar/login.html", {'form':form})    #vincular la vista con la plantilla de html



def about(request):
    return render(request, 'AppMaterias/about.html')

@login_required
def inicio(request):

    return render(request, 'AppMaterias/inicio.html')

@login_required
def addMateria(request):

    if request.method == 'POST':

        miFormulario=AprobadaFormulario(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            peli = Materia(autor=request.user,nombre=informacion['nombre'], año=informacion['año'],
             director=informacion['director'], puntaje=informacion['puntaje'], reseña=informacion['reseña'])

            peli.save()

            return render(request, 'AppMaterias/inicio.html')
    else:

        miFormulario=AprobadaFormulario()

    return render(request, 'AppMaterias/Aprobadas/añadirAprobadas.html', {'form':miFormulario})

@login_required
def buscar(request):

    if request.GET["reseña"]:

        nombre=request.GET['reseña']

        resultados=Aprobada.objects.filter(nombre__icontains=nombre)

        return render(request, "AppMaterias/Reseñas/resultadosBusqueda.html",{"resultados":resultados, "busqueda":nombre})

    else:

        respuesta="No enviaste datos."

    return HttpResponse(respuesta)

@login_required
def addMaterias(request):

    if request.method == 'POST':

        miFormulario=MateriaFormulario(request.POST, request.FILES)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data



            materia = Materia(nombre=informacion['nombre'], fecha=informacion['fecha'],
             imagen=informacion['imagen'])

            materia.save()

            return render(request, 'AppMaterias/inicio.html')
    else:

        miFormulario=MateriaFormulario()

    return render(request, 'AppMaterias/Materias/añadirMaterias.html', {'form':miFormulario})


@login_required
def materias(request):

    materias = Materia.objects.all()


    return render(request, "AppMaterias/Materias/listaMaterias.html",{'resultados':materias})


#Vista para Borrar Profes (Parte del CRUD)

@login_required
def borrarMaterias(request, materia_nombre):

    peli = Materia.objects.get(nombre=materia_nombre)
    
    peli.delete()
    
    materias = Materia.objects.all()

    return render(request, "AppMaterias/Materias/listaMaterias.html",{'resultados':materias})

@login_required
def editarMateria(request, materia_nombre):

    peli = Materia.objects.get(nombre=materia_nombre)

    if request.method == "POST":

        miFormulario = MateriaFormulario(request.POST, request.FILES)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            peli.nombre = informacion['nombre']
            peli.fecha = informacion['fecha']
            peli.imagen = informacion['imagen']

            peli.save()

            return render(request, "AppMaterias/inicio.html")

    else:

        miFormulario= MateriaFormulario(initial={'nombre':peli.nombre, 'fecha':peli.fecha,
        'imagen':peli.imagen})

    return render(request, "AppMaterias/Materias/editarMateria.html",{'miFormulario':miFormulario, 'resultado':materia_nombre})


#Vista para Editar Usuarios (Parte del CRUD)
@login_required
def editarUsuario(request):

    usuario = request.user #usuario activo (el que ha iniciado sesión)

    if request.method == "POST":    #al presionar el botón

        miFormulario = RegistroFormulario(request.POST) #el formulario es el del usuario

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data     #info en modo diccionario

            #actualizar la info del usuario activo
            usuario.username = informacion['username']
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password1']
            usuario.save()

            return render(request, "AppMaterias/Autenticar/inicio.html")

    else:

        miFormulario= RegistroFormulario(initial={'username':usuario.username, 'email':usuario.email})

    return render(request, "AppMaterias/Autenticar/editarUsuario.html",{'miFormulario':miFormulario, 'usuario':usuario.username})


