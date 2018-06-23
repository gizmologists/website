from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

def paginate_projects(projects, page):
    paginator = Paginator(projects, 5)
    page_projects = paginator.get_page(page)
    return page_projects
