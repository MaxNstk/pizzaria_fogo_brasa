from django.db import models

class Pizza(models.Model):

    flavor = models.ForeignKey('Flavor', on_delete=models.DO_NOTHING)
