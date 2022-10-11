from app.process.models import Process, Part
import pytest
from django.urls import reverse
from app.process.views import index


class TestClass:
    @pytest.mark.django_db
    def test_valid_parts_delete(self, client):
        process = Process.objects.create(department='Execução de Título Extrajudicial', subject='Locação de Imóvel',
                                         judge='Mariana')
        part = Part.objects.create(name='Execução de Título Extrajudicial', category='Locação de Imóvel',
                                   process=process)
        url = reverse('delete_parts', kwargs={'part_id': part.id})
        response = client.delete(url)
        assert response.status_code == 302

    @pytest.mark.django_db
    def test_invalid_parts_delete(self, client):
        url = reverse('delete_parts', kwargs={'part_id': 55})
        response = client.delete(url)
        assert response.status_code == 404

    @pytest.mark.django_db
    def test_valid_parts_delete_all(self, client):
        process = Process.objects.create(department='Execução de Título Extrajudicial', subject='Locação de Imóvel',
                                         judge='Mariana')
        part = Part.objects.create(name='Execução de Título Extrajudicial', category='Locação de Imóvel',
                                   process=process)
        url = reverse('delete_all_parts', kwargs={'process_id': 1})
        response = client.delete(url)
        assert response.status_code == 302
