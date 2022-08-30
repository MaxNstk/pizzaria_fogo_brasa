from django.db import models

class Size(models.Model):

    description = models.Charfield(max_lenght=255)