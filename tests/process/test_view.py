from app.process.models import Process, Part
import pytest
from django.urls import reverse
from app.process.views import index


class TestClass:
    @pytest.mark.django_db
    def test_index_view(self, client):
        Process.objects.create(department='Execução de Título Extrajudicial', subject='Alienação Fiduciária',
                               judge='Mariana')
        Process.objects.create(department='Execução de Título Extrajudicial', subject='Locação de Imóvel',
                               judge='Eduardo')
        url = reverse("index")
        request = client.get(url)
        response = index(request)
        content = response.content.decode(response.charset)
        assert response.status_code == 200
        assert "Execução de Título Extrajudicial" in content
        assert "Locação de Imóvel" in content

    @pytest.mark.django_db
    @pytest.mark.parametrize(
        'department, subject, judge, status_code', [
            (None, None, None, 400),
            (None, 'strong_pass', None, 400),
            ('user@example.com', None, None, 400),
            ('user@example.com', 'invalid_pass', None, 400),
            ('Busca e Apreensão em Alienação Fiduciária', 'Alienação Fiduciária', 'Domingos Parra Neto', 201),
        ]
    )
    def test_process_create(self, client, department, subject, judge, status_code):
        url = reverse('create_process')
        data = {
            'department': 'Execução de Título Extrajudicial',
            'subject': 'Locação de Imóvel',
            'judge': 'Mariana'
        }
        response = client.post(url, data=data)
        assert response.status_code == 201

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
