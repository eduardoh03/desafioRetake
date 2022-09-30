from django.contrib import admin
from .models import *


@admin.register(Process)
class ProcessAdmin(admin.ModelAdmin):
    list_display = ['subject', 'judge']
    search_fields = ['subject', 'judge']
    list_display_links = ['subject', 'judge']
    ordering = ('number',)
    list_filter = ('judge',)
