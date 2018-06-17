from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('archive/', views.archive, name='archive'),
    path('<slug:slug>/', views.show_project, name='show'),
    path('<slug:project_slug>/<slug:post_slug>', views.show_post, name='show_post'),
]
