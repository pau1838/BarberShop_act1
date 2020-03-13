from django.db import models
from .peopleModels import Barber, Client


# Create your models here.
class Cita(models.Model):
    barber = models.ForeignKey(Barber, on_delete=models.CASCADE, related_name='appointments')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='appointments')
    date = models.DateTimeField()


class Barberia(models.Model):
    name = models.CharField(max_length=30)
    ciutat = models.CharField(max_length=30)
    carrer = models.CharField(max_length=60)
    image = models.ImageField()

    def __str__(self):
        return self.name
