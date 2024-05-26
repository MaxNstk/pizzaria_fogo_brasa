from django.db import models

class Pizza(models.Model):

    flavor = models.ForeignKey('Flavor', verbose_name='Sabor', on_delete=models.DO_NOTHING)
    size = models.ForeignKey('Size', verbose_name='Tamanho', on_delete=models.DO_NOTHING)
    price = models.FloatField(verbose_name='Preço')
    is_active =  models.BooleanField(default=True, verbose_name='Disponível')

    def __str__(self) -> str:
        return f'{self.flavor} - {self.size} - R$:{self.price}'

    class Meta:
        unique_together = ('flavor', 'size')