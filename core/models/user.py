from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    phone_number = models.CharField(max_length=20)
    cpf_cnpj = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.get_full_name()