# Generated by Django 3.0.3 on 2020-02-28 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barberShopApp', '0002_auto_20200226_0929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barber',
            name='Torn',
            field=models.CharField(choices=[('MR', 'Morning'), ('AT', 'Afternoon'), ('WD', 'Whole day')], max_length=2),
        ),
    ]
