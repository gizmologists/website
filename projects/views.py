from django.shortcuts import render, HttpResponse
from django.template import loader
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Project, Post

def index(request):
    projects = Project.objects.filter(end_date__isnull=True)
    return render(request, 'projects/index.html', {'projects': projects })

def archive(request):
    # Only get projects who have a non-null end date
    projects = Project.objects.filter(end_date__isnull=False)
    return render(request, 'projects/archive.html', {'projects': projects})

def show_project(request, slug):
    project = Project.objects.get(slug=slug)

    post_list = project.posts.all()
    paginator = Paginator(post_list, 2)

    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request, 'projects/show_project.html', {
        'project': project,
        'posts':   posts
    })

def show_post(request, project_slug, post_slug):
    return render(request, 'projects/show_post.html', {
        'project': Project.objects.get(slug=project_slug),
        'post': Post.objects.get(slug=post_slug)
        })
