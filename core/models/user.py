from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    phone_number = models.CharField(max_length=20, verbose_name='Número de Telefone')
    cpf_cnpj = models.CharField(max_length=30, verbose_name='CPF/CNPJ', unique=True)
    active = models.BooleanField(default=True, verbose_name='Ativo')

    def __str__(self) -> str:
        return self.get_full_name()