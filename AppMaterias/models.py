from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class OfertaCalificada(models.Model):
    usuario=models.CharField(max_length=40, default="")
    materia=models.CharField(max_length=40)
    catedra=models.CharField(max_length=40)
    profesor=models.CharField(max_length=40)
    año=models.IntegerField()
    puntaje=models.FloatField()
    reseña=models.TextField(max_length=240)
    

class Materia(models.Model):

    materia=models.CharField(max_length=40)
    catedra=models.CharField(max_length=40)
    profesor=models.CharField(max_length=40)
    año=models.IntegerField()
    nota=models.IntegerField()
    bibliografia=models.ImageField(upload_to = 'materias', null=True)
    

class Avatar(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)