from django.db import models

class Pizza(models.Model):

    size = models.ForeignKey('Size',on_delete=models.DO_NOTHING)
    flavor = models.ForeignKey('Flavor',on_delete=models.DO_NOTHING)
    price = models.FloatField()

    def __str__(self):
        return f'{self.flavor.name} - {self.size.description} - {self.price}'