from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.contrib.auth import login, authenticate, logout
from apps.barberShopApp.forms import RegistrationForm
from .models import Barberia, Client


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
    morning_turn = ["9:00", "9:30", "10:00", "10:30", "11:00", "11:30", "12:00", "12:30", "13:00"]
    afternoon_turn = ["16:00", "16:30", "17:00", "17:30", "18:00", "18:30", "19:00", "19:30", "20:00"]
    complete_turn = []
    complete_turn.extend(morning_turn)
    complete_turn.extend(afternoon_turn)

    context = {
        'barber': barber,
        'barber_shop': barber_shop,
        'morning_turn': morning_turn,
        'afternoon_turn': afternoon_turn,
        'complete_turn': complete_turn
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