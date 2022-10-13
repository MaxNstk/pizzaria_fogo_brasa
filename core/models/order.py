from django.db import models


class Order(models.Model):

    total_value = models.FloatField()
    customer = models.ForeignKey('User', on_delete=models.DO_NOTHING)
    pizzas = models.ManyToManyField('Pizza')
    feedback = models.ForeignKey('Feedback', on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return f'{self.id} - {self.customer} - {self.total_value}'