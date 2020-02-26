from django.db import models
from . import

# Create your models here.
class Cite(models.Model):
    barber = models.ForeignKey(Barber, on_delete=models.CASCADE)