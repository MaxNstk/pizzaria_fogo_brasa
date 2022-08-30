from django.db import models

class Flavor(models.Model):

    name = models.Charfield(max_length=50)
    ingredients = models.Charfield(max_length=255)
    sizes = models.ManyToManyField(Size, through='FlavorSize')

    def __str__(self):
        return self.name