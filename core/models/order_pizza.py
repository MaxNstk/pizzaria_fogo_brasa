
from django.db import models

class OrderPizza(models.Model):
    pizza = models.ForeignKey('Pizza', on_delete=models.DO_NOTHING)
    order = models.ForeignKey('Order', on_delete=models.DO_NOTHING)