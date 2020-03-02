from django.shortcuts import render
from apps.barberShopApp.models import *


def barbers_list(request, pk):
    barber_shop = Barberia.objects.get(pk=pk)
    barbers = barber_shop.barbers.all()

    context = {'barbers': barbers,
               'barber_shop': barber_shop}

    return render(request, 'barbershop_detail.html', context)
