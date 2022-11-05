from enum import unique
from django.db import models
from .size import Size

class Flavor(models.Model):

    name = models.CharField(max_length=50, verbose_name='Sabor', unique=True)
    description = models.CharField(max_length=255, verbose_name='Descrição')
    is_active =  models.BooleanField(default=True, verbose_name='Disponível')

    def __str__(self):
        return f'{self.name} - {self.description}'
        