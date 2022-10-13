from django.db import models


class Order(models.Model):

    total_value = models.FloatField(null=True, blank=True)
    customer = models.ForeignKey('User', on_delete=models.DO_NOTHING)
    pizzas = models.ManyToManyField('Pizza', through='OrderPizza')
    feedback = models.ForeignKey('Feedback', on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.id} - {self.customer} - {self.total_value}'
    
    def save(self, *args, **kwargs):
        total_value = 0
        for pizza in self.pizzas:
            total_value += pizza.price
        self.total_value = total_value
        return super().save(self, *args, **kwargs)