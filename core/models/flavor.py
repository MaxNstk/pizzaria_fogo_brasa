from django.db import models
from .size import Size

class Flavor(models.Model):

    name = models.Charfield(max_length=50)
    ingredients = models.Charfield(max_length=255)

    def __str__(self):
        return f'{self.name} - {self.ingredients}'