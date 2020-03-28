from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.contrib.auth import login, authenticate, logout
from apps.barberShopApp.forms import RegistrationForm
from .models import *
from .filters import CitaFilter
from django.contrib import messages


def index(request):
    llista_barberies = Barberia.objects.order_by('ciutat')
    if request.user.is_authenticated:
        user = request.user
    else:
        user = None
    context = {
        'llista_barberies': llista_barberies,
        'user': user
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


def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")

            account = authenticate(username=username, password=raw_password)
            login(request, account)
            return redirect('index')
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'register.html', context)


def user_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect('index')
            else:
                return HttpResponse("Compte inactiu!")
        else:
            return HttpResponse("Detalls de login invalids")
    else:
        return render(request, 'login.html', {})


def user_logout(request):
    logout(request)
    return redirect('index')


def appointment_reserve(request, pk_bs, pk_b, pk_p):
    if request.user.is_authenticated:
        barber_shop = Barberia.objects.get(pk=pk_bs)
        barber = barber_shop.barbers.get(pk=pk_b)
        appointment = Cita.objects.get(pk=pk_p)

        context = {
            'barber': barber,
            'barber_shop': barber_shop,
            'appointment': appointment,
        }

        return render(request, 'appointment_reserve.html', context)
    else:
        return redirect('login')


def assign_appointment(request, pk_bs, pk_b, pk_p):
    barber_shop = Barberia.objects.get(pk=pk_bs)
    barber = barber_shop.barbers.get(pk=pk_b)
    appointment = Cita.objects.get(pk=pk_p)
    Cita.objects.filter(pk=pk_p).update(client=request.user)

    context = {
        'barber': barber,
        'barber_shop': barber_shop,
        'appointment': appointment,
    }

    return render(request, 'thank_you.html', context)


def show_reservations(request, pk):
    user = Client.object.get(pk=pk)
    appointments = Cita.objects.filter(client=user)

    context = {
        'appointments': appointments,
        'user': user
    }

    return render(request, 'show_reservations.html', context)

