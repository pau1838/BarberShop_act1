from django.db import models


class Barber(models.Model):
    MORNING = 'MR'
    AFTERNOON = 'AT'
    WHOLE_DAY = 'WD'
    TURNS = [
        (MORNING, 'Morning'),
        (AFTERNOON, 'Afternoon'),
        (WHOLE_DAY, 'Whole day')
    ]

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    turn = models.CharField(max_length=2, choices=TURNS, default='MR')
    phone = models.CharField(max_length=9)
    barberShop = models.ForeignKey('Barberia', on_delete=models.SET_NULL, null=True, related_name='barbers')

    def __str__(self):
        return self.first_name + " " + self.last_name


class Client(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    phone = models.TextField()

    def __str__(self):
        return self.first_name + " " + self.last_name

