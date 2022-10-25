from django import forms

from AppMaterias.models import Avatar, Materia

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from AppMaterias.models import Avatar

class OfertaCalificadaFormulario(forms.Form):

    materia=forms.CharField(max_length=40)
    catedra=forms.CharField(max_length=40)
    profesor=forms.CharField(max_length=40)
    año=forms.IntegerField()
    puntaje=forms.FloatField()
    reseña=forms.CharField(widget=forms.Textarea)


#Otra manera de hacer formularios es usar el ModelForm
class MateriaFormulario(forms.ModelForm):

    class Meta:

        model = Materia
        fields = ['materia', 'catedra', 'profesor', 'año', 'nota', 'bibliografia']

class RegistroFormulario(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = ['username', 'email', 'password1', 'password2'] 

class AvatarFormulario(forms.ModelForm):

    class Meta:

        model = Avatar
        fields = ["imagen"]