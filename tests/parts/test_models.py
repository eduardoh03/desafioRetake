from app.process.models import Part, Process
import pytest
from django.urls import reverse
from django import urls


class TestClass:

    @pytest.mark.django_db
    def test_parts_create(self, client):
        process = Process.objects.create(department='Execução de Título Extrajudicial', subject='Locação de Imóvel',
                                         judge='Mariana')
        Part.objects.create(name='Eduardo', category='Advogado',
                            process=process)
        assert Part.objects.count() == 1

    @pytest.mark.django_db
    def test_invalid_parts_get(self, client):
        process = Process.objects.create(department='Execução de Título Extrajudicial', subject='Locação de Imóvel',
                                         judge='Mariana')
        Part.objects.create(name='Execução de Título Extrajudicial', category='Locação de Imóvel',
                            process=process)

        assert Part.objects.filter(id=33).exists() == False

    @pytest.mark.django_db
    def test_valid_parts_delete(self, client):
        process = Process.objects.create(department='Execução de Título Extrajudicial', subject='Locação de Imóvel',
                                         judge='Mariana')
        Part.objects.create(name='Execução de Título Extrajudicial', category='Locação de Imóvel',
                            process=process)
        part = Part.objects.get(id=1)
        part.delete()
        assert Part.objects.count() == 0


