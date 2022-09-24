from django.db import models

class Size(models.Model):
    short_name = models.CharField(max_length=4)
    description = models.Charfield(max_lenght=255)

    def __str__(self) -> str:
        return self.short_name
