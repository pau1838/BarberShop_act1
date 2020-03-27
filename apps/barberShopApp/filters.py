from django import forms

from apps.barberShopApp.models import Cita
import django_filters


class CitaFilter(django_filters.FilterSet):
    class Meta:
        model = Cita
        fields = ['date', 'hour']
