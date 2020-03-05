# Generated by Django 3.0.3 on 2020-03-05 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Barber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('turn', models.CharField(choices=[('MR', 'Morning'), ('AT', 'Afternoon'), ('WD', 'Whole day')], max_length=2)),
                ('phone', models.CharField(max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='Barberia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('ciutat', models.CharField(max_length=30)),
                ('carrer', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('barber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='barberShopApp.Barber')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='barberShopApp.Client')),
            ],
        ),
        migrations.AddField(
            model_name='barber',
            name='barberShop',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='barbers', to='barberShopApp.Barberia'),
        ),
    ]
