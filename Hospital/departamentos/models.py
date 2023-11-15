from django.db import models

# Create your models here.
class departamentos(models.Model):
    nombre_depa = models.CharField(max_length=60),
    clave = models.CharField(max_length=60)
    ubicacion = models.CharField(max_length=60),
    telefono =models.CharField(max_length=10),
    jefe_depa = models.CharField(max_length=40)

    def __str__(self):
        return self.nombre_depa