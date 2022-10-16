from django.db import models


class Address(models.Model):
    customer = models.ForeignKey('User', on_delete=models.DO_NOTHING)
    adress = models.CharField(max_length=255)
    number = models.CharField(max_length=255)
    district = models.CharField(max_length=255) 
    zip_code = models.CharField(max_length=255)