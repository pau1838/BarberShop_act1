from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import Barberia

# Create your views here.

def detail(request, barberia_id):
    return HttpResponse("Estas buscant la següent barberia %s" % barberia_id)

def index(request):
    llista_barberies = Barberia.objects.order_by('ciutat')
    context = {
        'llista_barberies' : llista_barberies,

    }

    return render(request, 'home.html', context)