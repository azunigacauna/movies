from django.db import models

# Create your models here.
class Lista(models.Model):
  nombre = models.TextField()
  
  def __str__(self):
    return self.nombre

class Pelicula(models.Model):
  nombre = models.TextField()
  director = models.TextField()
  guionistas = models.TextField()
  estreno = models.IntegerField()
  protagonistas = models.TextField()
  duracion = models.IntegerField()
  clasificacion = models.CharField(max_length=1)
  descripcion = models.TextField()
  lista = models.ForeignKey(Lista,on_delete=models.CASCADE)
  
  def __str__(self):
    return self.nombre
