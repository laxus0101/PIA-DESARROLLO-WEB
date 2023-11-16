from django.db import models

# Create your models here.
class Medicos(models.Model):
    nombre_medico = models.CharField(max_length=60,null=True)
    direccion = models.CharField(max_length=60,null=True)
    telefono =models.CharField(max_length=10,null=True)
    edad = models.IntegerField(null=True)
    especialidad = models.CharField(max_length=60)

    def __str__(self):
        return self.nombre_medico