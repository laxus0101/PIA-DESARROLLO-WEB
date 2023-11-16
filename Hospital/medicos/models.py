from django.db import models

# Create your models here.
<<<<<<< HEAD
class Medicos(models.Model):
    nombre_medico = models.CharField(max_length=60,null=True)
    direccion = models.CharField(max_length=60,null=True)
    telefono =models.CharField(max_length=10,null=True)
    edad = models.IntegerField(null=True)
=======
class medicos(models.Model):
    nombre_medico = models.CharField(max_length=60),
    direccion = models.CharField(max_length=60),
    telefono =models.CharField(max_length=10),
    edad = models.IntegerField(),
>>>>>>> 0427a346f88c86189d5c71ff6f82763ad738f8c4
    especialidad = models.CharField(max_length=60)

    def __str__(self):
        return self.nombre_medico