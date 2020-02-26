from django.db import models


class Barber(models.Model):
    MORNING = 'MR'
    AFTERNOON = 'AT'
    WHOLE_DAY = 'WD'
    TURNS = [
        (MORNING, 'morning'),
        (AFTERNOON, 'afternoon'),
        (WHOLE_DAY, 'whole day')
    ]

    first_name = models.CharField(name='Nom', max_length=30)
    last_name = models.CharField(name='Cognoms', max_length=30)
    turn = models.CharField(name='Torn', max_length=2, choices=TURNS)
    phone = models.CharField(name='Telèfon', max_length=9)


class Client(models.Model):
    first_name = models.CharField(name='Nom', max_length=30)
    last_name = models.CharField(name='Cognoms', max_length=30)
    email = models.EmailField(name='Email', max_length=50)
    phone = models.TextField(name='Telèfon')
