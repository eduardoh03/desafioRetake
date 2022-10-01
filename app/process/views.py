import pprint

from django.forms import modelformset_factory
from django.shortcuts import render
from .models import Process, Part
from .forms import ProcessForm, PartsForm
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404


def index(request):
    process = Process.objects.all()
    return render(request, 'home.html', locals())


def create_process(request):
    """Função que renderiza a pagina de criação de um processo"""
    context = {}
    process_form = ProcessForm(request.POST)
    PartsFormSet = modelformset_factory(Part, form=ProcessForm, extra=2, exclude=('process',))

    if request.method == 'POST':
        process_form = ProcessForm(data=request.POST)
        form_set = PartsFormSet(request.POST)
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
            return redirect('create_process')
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
    """Função que renderiza a pagina de criação de uma parte"""
    if request.method == 'POST':
        process_form = PartsForm(request.POST)
        if process_form.is_valid():
            return redirect('index')
        else:
            return redirect('create_process')
    else:
        p_form = ProcessForm()
    return render(request, 'parts.html', locals())
