from django.db import models

class Movie(models.Model):
    titulo = models.CharField(max_length = 50)
    director = models.CharField(max_length = 50)
    duracion = models.CharField(max_length = 50)
    sinopsis = models.TextField()
    disponible = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo
    

# Create your models here.
