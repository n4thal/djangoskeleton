from django.shortcuts import render, get_object_or_404
from core.models import Author, MetaInfo


# Create your views here.
def landing(request):
    author = get_object_or_404(Author, pk=1)
    context = {
        'author': author,
    }
    return render(request, 'landing.html', context)


def contact(request):
    author = get_object_or_404(Author, pk=1)
    mail = author.mail
    context = {
        'author': author,
    }
    return render(request, 'contact.html', context)


def impressum(request):
    author = get_object_or_404(Author, pk=1)
    context = {
        'author': author,
    }
    return render(request, 'impressum.html', context)


def legal(request):
    author = get_object_or_404(Author, pk=1)
    context = {
        'author': author,
    }
    return render(request, 'legal.html', context)


def metaInfo(request):
    meta = get_object_or_404(MetaInfo, pk=1)
    context = {
        'meta': meta,
    }
    return render(request, 'base.html', context)
