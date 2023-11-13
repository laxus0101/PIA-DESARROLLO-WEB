from django.db import models

# Create your models here.
class Medicos(models.Model):
    nombre_medico = models.CharField(max_length=60),
    direccion = models.CharField(max_length=60),
    telefono =models.CharField(max_length=10),
    edad = models.IntegerField(),
    especialidad = models.CharField(max_length=60)

def __str__(self):
    return self.nombre_medico