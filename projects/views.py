from django.shortcuts import render, get_object_or_404
from projects.models import Project
from core.models import Author, MetaInfo


# Create your views here.
def projects_index(request):
    projects = Project.objects.all()
    author = get_object_or_404(Author, pk=1)
    meta = get_object_or_404(MetaInfo, pk=1)
    context = {
        'projects': projects,
        'author': author,
        'meta': meta,
    }
    return render(request, 'projects_index.html', context)


def projects_detail(request, slug):
    project = Project.objects.get(slug=slug)
    author = get_object_or_404(Author, pk=1)
    meta = get_object_or_404(MetaInfo, pk=1)
    context = {
        'project': project,
        'author': author,
        'meta': meta,
    }
    return render(request, 'projects_detail.html', context)
