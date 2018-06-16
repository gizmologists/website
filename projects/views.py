from django.shortcuts import render, HttpResponse
from django.template import loader

from .models import Project

def index(request):
    projects = Project.objects.filter(end_date__isnull=True)
    return render(request, 'projects/index.html', {'projects': projects })

def archive(request):
    # Only get projects who have a non-null end date
    projects = Project.objects.filter(end_date__isnull=False)
    return render(request, 'projects/archive.html', {'projects': projects})

def show(request, slug):
    return render(request, 'projects/show.html', {'project': Project.objects.get(slug=slug)})

