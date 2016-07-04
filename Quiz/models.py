from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from django.core.urlresolvers import reverse

# Create your models here.

class Quiz(models.Model):
    pin = models.CharField(max_length=15)

    def __str__(self):
        return str(self.pin)

class Pregunta(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=200)
    titulo = models.CharField(max_length=500)
    tiempo = models.IntegerField(blank=True, null=True)
    opCorrecta = models.CharField(max_length=150)
    op1 = models.CharField(max_length=150)
    op2 = models.CharField(max_length=150)
    op3 = models.CharField(max_length=150)

    def __str__(self):
        return str(self.titulo)

class Jugadores(models.Model):
    quiz_jugador = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    puntuacion = models.CharField(max_length=200)