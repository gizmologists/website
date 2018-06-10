from django.shortcuts import render, HttpResponse
from django.template import loader

from .models import Project

def index(request):
    return render(request, 'projects/index.html', {'projects': Project.objects.all()})
