from import_export import resources

from .models import Process, Part


class ProcessResource(resources.ModelResource):
    class Meta:
        model = Process


class PartResource(resources.ModelResource):
    class Meta:
        model = Part
