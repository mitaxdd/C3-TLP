from django.db import models

# Create your models here.
class Asignatura(models.Model):
    nombre = models.CharField(max_length=20)
    codigo = models.CharField(max_length=6,primary_key=True)
    profesor = models.CharField(max_length=50)

class Examen(models.Model):
    codigo = models.CharField(max_length=6,primary_key=True)
    descripcion = models.CharField(max_length=50)
    asignatura = models.ForeignKey("core.Asignatura", on_delete=models.CASCADE)
    fecha = models.DateTimeField()

    def fecha_examen(self):
        return self.fecha

class Actividad(models.Model):
    nombre = models.CharField(max_length=6,primary_key=True)
    inicio = models.DateTimeField()
    fin = models.DateTimeField()
    #añadir relacion a fechas de examenes

    #plazos solicitudes igual q periodo

    #gestion de beneficios??

    def duracion(self):
        return self.fin-self.inicio
    
    def __str__(self) -> str:
        return self.nombre
    
