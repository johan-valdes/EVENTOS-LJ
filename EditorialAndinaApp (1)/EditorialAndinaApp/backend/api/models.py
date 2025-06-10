from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=100)
    edad = models.IntegerField()

    def _str_(self):
        return self.nombre

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)
    paginas = models.IntegerField()
    anio = models.IntegerField()

    def _str_(self):
        return self.titulo
