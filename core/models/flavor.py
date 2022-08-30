from django.db import models
from .size import Size

class Flavor(models.Model):

    name = models.CharField(max_length=50)
    ingredients = models.CharField(max_length=255)
    sizes = models.ManyToManyField(Size, through='Pizza')

    def __str__(self):
        return f'{self.name} - {self.ingredients}'