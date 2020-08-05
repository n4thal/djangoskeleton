from django.http import HttpResponse
from django.shortcuts import render
from core.models import Core

# Create your views here.


def index(request):
    core = Core.objects.all()
    context = {
        'core': core,
    }
    return render(request, 'landing.html', context)


def contact(request):
    contact = Core.objects.all()
    context = {
        'contact': contact,
    }
    return render(request, 'contact.html', context)


def impressum(request):
    impressum = Core.objects.all()
    context = {
        'imp': impressum,
    }
    return render(request, 'impressum.html', context)


def legal(request):
    legal = Core.objects.all()
    context = {
        'legal': legal
    }
    return render(request, 'legal.html', context)
