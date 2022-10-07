from app.process.models import Process, Part
import pytest
from django.urls import reverse
from django import urls


class TestClass:
    @pytest.mark.django_db
    def test_process_create(self, client):
        Process.objects.create(department='Execução de Título Extrajudicial', subject='Locação de Imóvel',
                               judge='Mariana')
        assert Process.objects.count() == 1

    @pytest.mark.django_db
    def test_process_delete(self, client):
        process = Process.objects.create(department='Execução de Título Extrajudicial', subject='Locação de Imóvel',
                                         judge='Mariana')
        process.delete()
        assert Process.objects.count() == 0
