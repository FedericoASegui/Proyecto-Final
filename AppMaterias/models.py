from django.db import models

# Create your models here.

class Aprobada(models.Model):
    autor=models.CharField(max_length=40, default="")
    nombre=models.CharField(max_length=40)
    año=models.IntegerField()
    director=models.CharField(max_length=40)
    puntaje=models.FloatField()
    reseña=models.TextField(max_length=240)
    

class Materia(models.Model):

    Nombre=models.CharField(max_length=40)
    Calificación=models.IntegerField()
    imagen=models.ImageField(upload_to = 'materias', null=True)