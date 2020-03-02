from django.db import models
from .peopleModels import Barber, Client


# Create your models here.
class Cita(models.Model):
    barber = models.ForeignKey(Barber, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)


class Barberia(models.Model):
    name = models.CharField(max_length=30)
    ciutat = models.CharField(max_length=30)
    carrer = models.CharField(max_length=60)

    def __str__(self):
        return self.name
