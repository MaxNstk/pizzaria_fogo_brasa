from django.db import models

class OrderProduct(models.Model):
    product = models.ForeignKey('Product', verbose_name='Produto', on_delete=models.DO_NOTHING)
    order = models.ForeignKey('Order', verbose_name='Pedido',  on_delete=models.DO_NOTHING)
    product_price = models.FloatField()

    def save(self, *args, **kwargs) -> None:
        self.product_price = self.product.price
        super().save(*args, **kwargs)
        self.order.save()
