from django import forms

from AppMaterias.models import Materia

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class AprobadaFormulario(forms.Form):

    nombre=forms.CharField(max_length=40)
    año=forms.IntegerField()
    director=forms.CharField(max_length=40)
    puntaje=forms.FloatField()
    reseña=forms.CharField(widget=forms.Textarea)


#Otra manera de hacer formularios es usar el ModelForm
class MateriaFormulario(forms.ModelForm):

    class Meta:

        model = Materia
        fields = ['Nombre', 'Calificación']

class RegistroFormulario(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = ['username', 'email', 'password1', 'password2'] 
