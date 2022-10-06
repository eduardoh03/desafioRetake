from django.contrib.auth.models import User

from app.process.models import Process, Part
import pytest
from django.urls import reverse


class TestClass:
    @pytest.mark.django_db
    def test_process_create(self, client):
        url = reverse('create_process')
        data = {
            'department': 'Execução de Título Extrajudicial',
            'subject': 'Locação de Imóvel',
            'judge': 'Mariana'
        }
        response = client.post(url, data=data)
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_invalid_process_create(self, client):
        data = {
            'department': 123,
            'subject': 'subject',
        }
        url = reverse('create_process')
        response = client.post(url, data=data)
        assert response.status_code == 400

    @pytest.mark.django_db
    def test_valid_process_detail(self, client):
        process = Process.objects.create(department='Execução de Título Extrajudicial', subject='Locação de Imóvel',
                                         judge='Mariana')
        url = reverse('get_process', kwargs={'process_id': process.id})
        response = client.get(url)
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_invalid_process_detail(self, client):
        url = reverse('get_process', kwargs={'process_id': 5})
        response = client.get(url)
        assert response.status_code == 404

    @pytest.mark.django_db
    def test_valid_process_delete(self, client):
        process = Process.objects.create(department='Execução de Título Extrajudicial', subject='Locação de Imóvel',
                                         judge='Mariana')
        url = reverse('delete_process', kwargs={'process_id': process.id})
        response = client.delete(url)
        assert response.status_code == 302

    @pytest.mark.django_db
    def test_invalid_process_delete(self, client):
        url = reverse('delete_process', kwargs={'process_id': 55})
        response = client.delete(url)
        assert response.status_code == 404
