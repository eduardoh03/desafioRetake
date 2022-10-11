from app.process.forms import ProcessForm
import pytest


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
