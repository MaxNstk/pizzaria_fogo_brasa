from django.db import models


class FeedBack(models.Model):

    GREAT = 5
    GOOD = 4
    OK = 3
    BAD = 2
    VERY_BAD = 1
    AWFUL = 0

    rating_choices = (
        ('Ótimo',GREAT),
        ('Muito Bom',GOOD),
        ('Bom',OK),
        ('Ruim',BAD),
        ('Muito Ruim',VERY_BAD),
        ('Horrível',AWFUL)
    )

    rating = models.IntegerField(choices=rating_choices, verbose_name='Classificação')
    description = models.CharField(max_length=255, null=True, blank=True, verbose_name='Descrição')