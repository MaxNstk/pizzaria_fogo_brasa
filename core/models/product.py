from django.db import models

class Product(models.Model):
    description = models.CharField(max_length=255, verbose_name='Descrição')
    price = models.FloatField(verbose_name='Preço')
    is_active =  models.BooleanField(default=True, verbose_name='Disponível')

    def __str__(self) -> str:
        return f'{self.description}, R$: {self.price}'