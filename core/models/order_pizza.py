
from django.db import models

class OrderPizza(models.Model):
    pizza = models.ForeignKey('Pizza', verbose_name='Pizza', on_delete=models.DO_NOTHING)
    order = models.ForeignKey('Order', verbose_name='Pedido',  on_delete=models.DO_NOTHING)
    
    def save(self, *args, **kwargs) -> None:
        save = super().save(*args, **kwargs)
        self.order.save()
        return save