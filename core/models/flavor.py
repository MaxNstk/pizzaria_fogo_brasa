from enum import unique
from django.db import models
from .size import Size

class Flavor(models.Model):

    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name} - {self.description}'
        