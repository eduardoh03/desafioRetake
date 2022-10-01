import pprint

from django.forms import modelformset_factory
from django.shortcuts import render
from .models import Process, Part
from .forms import ProcessForm, PartsForm
from django.contrib import messages
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404


def index(request):
    """Função que renderiza a tela inicial"""
    process = Process.objects.all()
    parts = Part.objects.all()
    return render(request, 'home.html', locals())


def get_process(request, process_id):
    """Função que renderiza um processo específico"""
    process = get_object_or_404(Process, pk=process_id)
    context = {
        'process': process
    }
    return render(request, 'view_process.html', context)


def update_process(request, process_id):
    """Função que renderiza a pagina com dados de alteração dos dados do Processo"""
    process = Process.objects.get(id=process_id)
    if request.method == 'POST':
        process_form = ProcessForm(data=request.POST, instance=process)
        if process_form.is_valid():
            process_form.save()
            messages.success(request, 'Processo atualizado!')
            return redirect('get_process', process_id)
        else:
            messages.error(request, message=process_form.errors)
            return redirect('account_detail_contact')
    else:
        process_form = ProcessForm(instance=process)
    return render(request, 'update_process.html', locals())


def delete_process(request, process_id):
    """Função que renderiza um processo específico"""
    process = get_object_or_404(Process, pk=process_id)
    process.delete()
    messages.success(request, "Processo Apagado")
    return redirect('index')


def create_process(request):
    """Função que renderiza a pagina de criação de um processo"""
    context = {}
    process_form = ProcessForm()
    PartsFormSet = modelformset_factory(Part, form=ProcessForm, extra=1, exclude=('process',))

    if request.method == 'POST':
        process_form = ProcessForm(data=request.POST)
        form_set = PartsFormSet(request.POST)

        if not form_set.is_valid():
            if form_set.non_form_errors():  # not caused by error of an individual form
                error_info = form_set.non_form_errors()[0]
                messages.error(request, error_info)
        if all([process_form.is_valid(), form_set.is_valid()]):
            department = process_form.cleaned_data['department']
            subject = process_form.cleaned_data['subject']
            judge = process_form.cleaned_data['judge']
            process = Process.objects.create(department=department, subject=subject, judge=judge)
            process.save()
            for form in form_set:
                instances = form.save(commit=False)
                instances.process = process
                instances.save()
            messages.success(request, "Processo Criado")
            return redirect('index')
        else:
            if form_set.total_form_count() > 0:
                context['form_set'] = form_set
            return redirect('create_process')
    else:
        context['p_form'] = process_form
        form_set = PartsFormSet(queryset=Part.objects.none())
        context['form_set'] = form_set
    return render(request, 'process.html', context)


def create_parts(request):
    PartFormSet = modelformset_factory(Part, exclude=('process',))
    if request.method == 'POST':
        process_form = PartsForm(request.POST)
        if process_form.is_valid():
            return redirect('index')
        else:
            return redirect('create_process')
    else:
        p_form = ProcessForm()
    return render(request, 'parts.html', locals())
