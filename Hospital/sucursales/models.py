
from django.db import models

# Create your models here.

class Sucursales(models.Model):
    nombre_sucursal = models.CharField(max_length=60),
    ubicacion = models.CharField(max_length=60),
    telefono =models.CharField(max_length=10),
    capacidad_pacientes = models.FloatField(),
    descripcion_servicios = models.CharField(max_length=60)

def __str__(self):
    return self.nombre_sucursal
