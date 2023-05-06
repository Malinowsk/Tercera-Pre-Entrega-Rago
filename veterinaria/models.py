from django.db import models
from django.contrib.auth.models import User


class Animal(models.Model):
    nombre = models.CharField(max_length=256)
    raza = models.CharField(max_length=256)
    altura = models.DecimalField(max_digits=7, decimal_places=2)
    peso = models.DecimalField(max_digits=7, decimal_places=2)
    vacunado = models.BooleanField(default=False)
    dueño = models.CharField(max_length=256)

    def __str__(self):
        return f"{self.nombre} | {self.raza}"
    

class Doctor(models.Model):
    apellido = models.CharField(max_length=256)
    nombre = models.CharField(max_length=256)
    dni = models.CharField(max_length=32)
    email = models.EmailField(blank=True)
    puesto = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"



class Consultorio(models.Model):
    nombre = models.CharField(max_length=256)
    num_piso = models.CharField(max_length=32)
    metros_cuadrados = models.DecimalField(max_digits=7, decimal_places=2)
    con_tetoscopio = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nombre}, {self.num_piso}"
