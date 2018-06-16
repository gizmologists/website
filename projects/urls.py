from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('archive/', views.archive, name='archive'),
    path('<slug:slug>/', views.show, name='show'),
]
