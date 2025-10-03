from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

# He puesto que los valores de tipo "numero" de las habitaciones sean Integer(valores que salían buscando en los parámetros de la clase models).
# En mi caso, voy a utilizar PositiveIntegerField, que sólo permitirá valores positivos (no hay habitaciones negativas) con un máximo de 5 carácteres (Hasta 99999 asignaciones).

class Habitaciones(models.Model):
    # Campo numero utilizado como clave primaria, ya que no debe haber dos habitaciones con el mismo numero.
    planta = models.IntegerField()
    numero = models.PositiveIntegerField(primary_key=True)
    descripcion = models.TextField()
    
    def __str__(self):
        return "Numero:"+str(self.numero)


class Pacientes(models.Model):
    #Campo habitacion como clave foránea de la clase habitaciones
    nombre = models.CharField(max_length=200)
    habitacion = models.ForeignKey(Habitaciones, to_field='numero', on_delete=models.CASCADE)
    fecha_ingreso = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return "Nombre:"+self.nombre


class Doctores(models.Model):
    nombre = models.CharField(max_length=200)
    especialidad = models.CharField(max_length=100)
    fecha_contratacion = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return "Nombre:"+self.nombre