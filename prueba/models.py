from django.db import models

# Create your models here.

class Pilar(models.Model):
    nombre = models.CharField(max_length=60)
    respiracion = models.CharField(max_length=30)
    edad = models.IntegerField(default=14)

    def __str__(self):
        return  "pilar: " + self.nombre 