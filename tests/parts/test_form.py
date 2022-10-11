import pytest
from app.process.forms import PartsForm
from app.process.models import Part, Process


@pytest.mark.django_db
def test_part_post_form_valid():
    process = Process.objects.create(department='Execução de Título Extrajudicial', subject='Locação de Imóvel',
                                     judge='Mariana')
    form_data = {
        'name': 'Eduardo',
        'category': 'Advogado',
        'process': process,
    }
    form = PartsForm(data=form_data)
    assert form.is_valid() is True


@pytest.mark.django_db
def test_part_post_form_invalid():
    process = Process.objects.create(department='Execução de Título Extrajudicial', subject='Locação de Imóvel',
                                     judge='Mariana')
    form_data = {
        'name': None,
        'category': 132,
        'process': process,

    }
    form = PartsForm(data=form_data)
    assert form.is_valid() is False
