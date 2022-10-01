import django.contrib.auth
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import create_process, index, create_parts

urlpatterns = [
    path('create', create_process, name='create_process'),
    path('create_parts', create_parts, name='create_parts'),
    path('', index, name='index'),

]
