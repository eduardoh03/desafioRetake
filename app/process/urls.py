import django.contrib.auth
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path('create', create_process, name='create_process'),
    path('<int:process_id>', get_process, name='get_process'),
    path('update/<int:process_id>', update_process, name='update_process'),
    path('delete/<int:process_id>', delete_process, name='delete_process'),

    path('create_parts', create_parts, name='create_parts'),
    path('update_parts/<int:part_id>', update_parts, name='update_parts'),
    path('delete_parts/<int:part_id>', delete_parts, name='delete_parts'),
    path('delete_all_parts/<int:process_id>', delete_all_parts, name='delete_all_parts'),

    path('busca', find_process, name='find_process'),
    path('', index, name='index'),
    path('export_process_v1', export_process_v1, name='export_process_v1'),
    path('export_process_v2', export_process_v2, name='export_process_v2'),
    path('export_parts_v1', export_parts_v1, name='export_parts_v1'),
    path('export_parts_v2', export_parts_v2, name='export_parts_v2'),

]
