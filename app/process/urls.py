import django.contrib.auth
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import create_process, index, create_parts,update_process, get_process

urlpatterns = [
    path('create', create_process, name='create_process'),
    path('<int:process_id>', get_process, name='get_process'),
    path('create_parts', create_parts, name='create_parts'),
    path('update/<process_id>', update_process, name='update_process'),
    path('', index, name='index'),

]
