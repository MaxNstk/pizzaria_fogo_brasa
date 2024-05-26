from django.db import models


class Address(models.Model):
    customer = models.ForeignKey('User', on_delete=models.DO_NOTHING)
    address = models.CharField(max_length=255, verbose_name='Endereço')
    number = models.CharField(max_length=255, verbose_name='Número')
    district = models.CharField(max_length=255, verbose_name='Bairro') 
    zip_code = models.CharField(max_length=255, verbose_name='CEP')
    note = models.CharField(max_length=255, verbose_name='Observações', null=True, blank=True)