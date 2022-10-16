from email.policy import default
from enum import auto
from secrets import choice
from django.db import models

class Order(models.Model):

    CANCELED = 0
    PENDING_CONFIRMATION = 1
    CONFIRMED = 2 
    IN_PRODUCTION = 3 
    READY = 4
    FINISHED = 5 

    situation_choices = (
        ('Cancelado',CANCELED),
        ('Pendente de confirmação',PENDING_CONFIRMATION),
        ('Confirmado',CONFIRMED),
        ('Em produção',IN_PRODUCTION),
        ('Pronto para retirada/entrega',READY),
        ('Finalizado',FINISHED)
    )

    total_value = models.FloatField(null=True, verbose_name='Valor Total', blank=True)
    customer = models.ForeignKey('User', verbose_name='Cliente', on_delete=models.DO_NOTHING)
    pizzas = models.ManyToManyField('Pizza', verbose_name='Pizza(s)', through='OrderPizza')
    products = models.ManyToManyField('Product')
    feedback = models.ForeignKey('Feedback', verbose_name='Feedback', on_delete=models.DO_NOTHING, null=True, blank=True)
    created_in = models.DateTimeField(auto_now=True)
    situation = models.IntegerField(choices=situation_choices, default=PENDING_CONFIRMATION)
    observation = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.id} - {self.customer} - {self.total_value}'
    
    def save(self, *args, **kwargs):
        if not self.id:
            return super().save(self, *args, **kwargs)
        self.total_value = self.pizzas.all().aggregate(
            total_price=models.Sum('price'))['total_price']
        self.total_value += self.products.all().aggregate(
            total_price=models.Sum('price'))['total_price']
        return super().save(self, *args, **kwargs)