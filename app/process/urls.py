import django.contrib.auth
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    # Process
    path('create', create_process, name='create_process'),
    path('<int:process_id>', get_process, name='get_process'),
    path('update/<int:process_id>', update_process, name='update_process'),
    path('delete/<int:process_id>', delete_process, name='delete_process'),
    path('busca', find_process, name='find_process'),
    path('', index, name='index'),
    # Parts
    path('create_parts', create_parts, name='create_parts'),
]
