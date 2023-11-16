from django.db import models

# Create your models here.

class Sucursalesinfo(models.Model):
    nombre_sucursal = models.CharField(max_length=60,null=True)
    ubicacion = models.CharField(max_length=60,null=True)
    telefono =models.CharField(max_length=10,null=True)
    capacidad_pacientes = models.FloatField(null=True)
    descripcion_servicios = models.CharField(max_length=60)

    def __str__(self):
<<<<<<< HEAD
        return self.nombre_sucursal, self.ubicacion, self.telefono, self.capacidad_pacientes, self.descripcion_servicios
=======
        return self.nombre_sucursal
>>>>>>> 0427a346f88c86189d5c71ff6f82763ad738f8c4
