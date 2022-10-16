from django.db import models

class Size(models.Model):
    short_name = models.CharField(max_length=4, unique=True, verbose_name='Tamanho')
    description = models.CharField(max_length=255, verbose_name='Descrição')
    available = models.BooleanField(default=True, verbose_name='Disponível')

    def __str__(self) -> str:
        return self.short_name
