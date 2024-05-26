from email.policy import default
from enum import auto
from secrets import choice
from tabnanny import verbose
from tkinter.tix import Tree
from django.db import models

from core.models.order_pizza import OrderPizza
from core.models.order_product import OrderProduct

class Order(models.Model):

    CANCELED = 0
    PENDING_CONFIRMATION = 1
    CONFIRMED = 2 
    IN_PRODUCTION = 3 
    READY = 4
    FINISHED = 5 

    DELIVERY = 1
    FACE_TO_FACE = 2

    situation_choices = (
        (CANCELED, 'Cancelado'),
        (PENDING_CONFIRMATION, 'Pendente de confirmação'),
        (CONFIRMED, 'Confirmado'),
        (IN_PRODUCTION, 'Em produção'),
        (READY, 'Pronto para retirada/entrega'),
        (FINISHED, 'Finalizado')
    )

    delivery_choices = (
        (DELIVERY, 'Entrega'),
        (FACE_TO_FACE, 'Presencial')
    )

    final_value = models.FloatField(null=True, verbose_name='Valor Final', blank=True)
    original_value = models.FloatField(null=True, verbose_name='Valor do Pedido', blank=True)
    customer = models.ForeignKey('User', verbose_name='Cliente', on_delete=models.DO_NOTHING)
    pizzas = models.ManyToManyField('Pizza', verbose_name='Pizza(s)', through='OrderPizza')
    products = models.ManyToManyField('Product', verbose_name='Produto(s)', through='OrderProduct')
    feedback = models.ForeignKey('Feedback', verbose_name='Feedback', on_delete=models.DO_NOTHING, null=True, blank=True)
    created_in = models.DateTimeField(auto_now=True)
    order_status = models.IntegerField(choices=situation_choices, verbose_name='Situação do Pedido', default=PENDING_CONFIRMATION)
    order_type = models.IntegerField(choices=delivery_choices,verbose_name='Tipo de Entrega', default=FACE_TO_FACE)
    observation = models.TextField(null=True, blank=True, verbose_name='Observação')
    discount = models.FloatField(verbose_name='Desconto', default=0)
    increase = models.FloatField(verbose_name='Acréscimo', default=0)
    address = models.ForeignKey('Address', on_delete=models.DO_NOTHING, verbose_name='Endereço', null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.id} - {self.customer} - {self.final_value}'
    
    def save(self, *args, **kwargs) -> None:
        if not self.id:
            return super().save(*args, **kwargs)
        pizzas_value = OrderPizza.objects.filter(order=self).aggregate(
            total_price=models.Sum('pizza_price'))['total_price'] or 0
        products_value = OrderProduct.objects.filter(order=self).aggregate(
            total_price=models.Sum('product_price'))['total_price'] or 0 
        self.original_value = pizzas_value + products_value
        self.final_value = self.original_value + self.increase - self.discount
        return super().save(*args, **kwargs)
