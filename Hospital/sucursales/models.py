from django.db import models

# Create your models here.

class Sucursalesinfo(models.Model):
    nombre_sucursal = models.CharField(max_length=60,null=True)
    ubicacion = models.CharField(max_length=60,null=True)
    telefono =models.CharField(max_length=10,null=True)
    capacidad_pacientes = models.IntegerField(null=True)
    descripcion_servicios = models.CharField(max_length=60)

    def __str__(self):
        return self.nombre_sucursal, self.ubicacion, self.telefono, self.capacidad_pacientes, self.descripcion_servicios