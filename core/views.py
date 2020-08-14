from django.shortcuts import render, get_object_or_404
from core.models import Author, MetaInfo
from blog.models import Post
from projects.models import Project


# Create your views here.
def landing(request):
    author = get_object_or_404(Author, pk=1)
    most_recent_post = Post.objects.all().order_by('-id')[:1]
    four_most_recent_projects = Project.objects.all().order_by('-id')[:4]
    context = {
        'author': author,
        'most_recent_post': most_recent_post,
        'recent_projects': four_most_recent_projects,
    }
    return render(request, 'landing.html', context)


def contact(request):
    author = get_object_or_404(Author, pk=1)
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


def metaInfo(request):
    meta = get_object_or_404(MetaInfo, pk=1)
    context = {
        'meta': meta,
    }
    return render(request, 'base.html', context)
