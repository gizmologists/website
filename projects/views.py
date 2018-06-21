from django.shortcuts import render, HttpResponse
from django.template import loader
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Project, Post
from .utility_functions import paginate_projects

def index(request):
    description = """
        All currently ongoing Gizmologists projects can be found on this page.  Check them out!
        """
    # Null end date means it's ongoing
    projects = Project.objects.filter(end_date__isnull=True)
    paginated_projects = paginate_projects(projects, request.GET.get('page'))
    return render(request, 'projects/index.html', {
        'title': 'Projects',
        'description': description,
        'projects': paginated_projects 
    })

def archive(request):
    description = """
        Gizmologists projects that have been completed can be found here.  Have a look at our past!
        """
    # Only get projects who have a non-null end date
    projects = Project.objects.filter(end_date__isnull=False)
    paginated_projects = paginate_projects(projects, request.GET.get('page'))
    return render(request, 'projects/index.html', {
        'title': 'Projects',
        'description': description,
        'projects': paginated_projects 
    })

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
