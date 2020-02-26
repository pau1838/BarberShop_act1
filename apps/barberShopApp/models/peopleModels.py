from django.db import models


class Barber(models.Model):

    MORNING = 'MR'
    AFTERNOON = 'AT'
    WHOLE_DAY = 'WD'
    TURNS = [
        (MORNING, 'Matí'),
        (AFTERNOON, 'Tarda'),
        (WHOLE_DAY, 'Tot el dia')
    ]

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    turn = models.CharField(max_length=2, choices=TURNS)
    phone = models.CharField(max_length=9)

    def __str__(self):
        self.first_name + " " + self.last_name


class Client(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=9)

    def __str__(self):
        self.first_name + " " + self.last_name
