from django.contrib import admin
from .models import *


class PartInline(admin.StackedInline):
    model = Part
    extra = 0


@admin.register(Process)
class ProcessAdmin(admin.ModelAdmin):
    list_display = ['id', 'number', 'subject', 'judge']
    search_fields = ['number', 'subject', 'judge']
    list_display_links = ['number', 'subject']
    ordering = ('number',)
    list_editable = ['judge']
    list_filter = ('judge',)
    inlines = [PartInline, ]


@admin.register(Part)
class PartAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']
    search_fields = ['name', 'category']
    list_display_links = ['name', 'category']
    ordering = ('name',)
    list_filter = ('category',)
