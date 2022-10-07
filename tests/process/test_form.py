from app.process.forms import ProcessForm, PartsForm
import pytest

from app.process.models import Part, Process


@pytest.mark.django_db
def test_process_post_form_valid():
    form_data = {
        'department': 'Execução de Título Extrajudicial',
        'subject': 'Locação de Imóvel',
        'judge': 'Mariana',

    }
    form = ProcessForm(data=form_data)
    assert form.is_valid() is True


@pytest.mark.django_db
def test_process_post_form_invalid():
    form_data = {
        'department': None,
        'subject': 'Locação de Imóvel',
        'judge': 1354,

    }
    form = ProcessForm(data=form_data)
    assert form.is_valid() is False


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
