from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import Barberia


def index(request):
    llista_barberies = Barberia.objects.order_by('ciutat')
    context = {
        'llista_barberies': llista_barberies,
    }

    return render(request, 'home.html', context)


def barbers_list(request, pk):
    barber_shop = Barberia.objects.get(pk=pk)
    barbers = barber_shop.barbers.all()

    context = {'barbers': barbers,
               'barber_shop': barber_shop}

    return render(request, 'barbershop_detail.html', context)


def barber_detail(request, pk_bs, pk_b):
    barber_shop = Barberia.objects.get(pk=pk_bs)
    barber = barber_shop.barbers.get(pk=pk_b)

    context = {
        'barber': barber,
        'barber_shop': barber_shop
    }

    return render(request, 'barber_calendar.html', context)
