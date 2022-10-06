from django.contrib.auth.models import User

from app.process.models import Process, Part
import pytest
from django.urls import reverse
from django import urls


class TestClass:
    @pytest.mark.django_db
    def test_process_create(self, client):
        data = {
            'department': 'Execução de Título Extrajudicial',
            'subject': 'Locação de Imóvel',
            'judge': 'Mariana'
        }
        url = reverse('create_process')
        response = client.post(url, data=data)
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_invalid_process_create(self, client):
        data = {
            'department': 123,
            'subject': 'subject',
            'judge': 123
        }
        url = reverse('create_process')
        response = client.post(url, data=data)
        assert response.status_code == 400

    @pytest.mark.django_db
    def test_process_detail(self, client):
        process = Process.objects.create(department='Execução de Título Extrajudicial', subject='Locação de Imóvel',
                                         judge='Mariana')
        url = reverse('get_process', kwargs={'process_id': process.id})
        response = client.get(url)
        assert response.status_code == 200
