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
    path('', index, name='index'),

]
