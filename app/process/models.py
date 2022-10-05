from django.db import models
import uuid


class Process(models.Model):
    number = models.UUIDField(verbose_name="Number of Process", default=uuid.uuid4, editable=False, unique=True)
    department = models.CharField(verbose_name="Class", max_length=50)
    subject = models.CharField(verbose_name="Subject", max_length=50)
    judge = models.CharField(verbose_name="Judge", max_length=50)

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = "Process"
        verbose_name_plural = "Process"


class Part(models.Model):
    name = models.CharField(verbose_name="Name", max_length=100)
    category = models.CharField(verbose_name="Category", max_length=50)
    process = models.ForeignKey(Process, related_name="parts", verbose_name="Process", on_delete=models.SET_NULL,
                                null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Part"
        verbose_name_plural = "Parts"
