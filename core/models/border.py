from django.db import models


class Border(models.Model):
    flavor = models.CharField(max_length=255)
    size = models.ForeignKey('Size', on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return self.flavor