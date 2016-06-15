from __future__ import unicode_literals

from django.db import models

# Create your models here.
class farmacia(models.Model):
    cod_farmacia=models.CharField(max_length=20)
    nombre=models.CharField(max_length=20)
    descuento=models.FloatField(max_length=20)
    def __unicode__(self):
        return self.nombre

class medicamento(models.Model):
    cod_medicamento=models.CharField(max_length=20)
    nombre=models.CharField(max_length=20)
    precio13=models.FloatField(max_length=20)
    precio14=models.FloatField(max_length=20)
    precio15=models.FloatField(max_length=20)

    def __unicode__(self):
        return self.nombre
