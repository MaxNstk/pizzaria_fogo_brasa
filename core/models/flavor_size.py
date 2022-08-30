from django.db import models

class FlavorSize(models.Model):

    size = models.ForeignKey('Size',on_delete=models.DO_NOTHING)
    flavor = models.ForeignKey('Flavor',on_delete=models.DO_NOTHING)
    price = models.FlotField()