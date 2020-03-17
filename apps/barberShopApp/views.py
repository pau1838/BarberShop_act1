from .filters import CitaFilter
from django.shortcuts import render, redirect
from .models import *


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
    appointments = barber.appointments.all()
    cita_filter = CitaFilter(request.GET, queryset=appointments)

    context = {
        'barber': barber,
        'barber_shop': barber_shop,
        'appointments': appointments,
        'filter': cita_filter
    }

    return render(request, 'barber_calendar.html', context)


def appointment_reserve(request, pk_bs, pk_b, pk_p):
    barber_shop = Barberia.objects.get(pk=pk_bs)
    barber = barber_shop.barbers.get(pk=pk_b)
    appointment = Cita.objects.get(pk=pk_p)

    context = {
        'barber': barber,
        'barber_shop': barber_shop,
        'appointment': appointment,
    }

    return render(request, 'appointment_reserve.html', context)


def assign_appointment(request, pk_bs, pk_b, pk_p):
    barber_shop = Barberia.objects.get(pk=pk_bs)
    barber = barber_shop.barbers.get(pk=pk_b)
    appointment = Cita.objects.get(pk=pk_p)
    Cita.objects.filter(pk=pk_p).update(client=Client(1))

    context = {
        'barber': barber,
        'barber_shop': barber_shop,
        'appointment': appointment,
    }

    return render(request, 'thank_you.html', context)
