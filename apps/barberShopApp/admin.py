from django.contrib import admin
from apps.barberShopApp import models

# Register your models here.

admin.site.register(models.Barber)
admin.site.register(models.Client)
admin.site.register(models.Barberia)
admin.site.register(models.Cita)
