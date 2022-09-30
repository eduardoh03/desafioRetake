from django.db import models


class Process(models.Model):
    number = models.IntegerField(verbose_name="Number of Process", unique=True)
    department = models.CharField(verbose_name="Class", max_length=50)
    subject = models.CharField(verbose_name="Subject", max_length=50)
    judge = models.CharField(verbose_name="Judge", max_length=50)

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = "Process"
        verbose_name_plural = "Processes"
