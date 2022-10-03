import pprint

from django.forms import modelformset_factory, inlineformset_factory
from django.shortcuts import render
from .models import Process, Part
from .forms import ProcessForm, PartsForm
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404


def index(request):
    process = Process.objects.all()
    return render(request, 'home.html', locals())


def find_process(request):
    list_process = Process.objects.all()
    if 'buscar' in request.GET:
        attribute_process = request.GET['buscar']
        if attribute_process:
            list_process = list_process.filter(department__icontains=attribute_process) \
                           | list_process.filter(subject__icontains=attribute_process) \
                           | list_process.filter(judge__icontains=attribute_process)
    context = {
        'process': list_process
    }
    return render(request, 'partials/_search.html', context)


def get_process(request, process_id):
    parts_form = PartsForm()
    process = get_object_or_404(Process, pk=process_id)
    context = {
        'process': process,
        'parts_form': parts_form,
    }
    return render(request, 'view_process.html', context)


def create_process(request):
    process_form = ProcessForm()
    form_parts_factory = inlineformset_factory(Process, Part, form=PartsForm, extra=0, can_delete=False)
    form_parts = form_parts_factory()
    context = {
    }
    if request.method == 'POST':

        process_form = ProcessForm(request.POST)
        form_parts_factory = inlineformset_factory(Process, Part, form=PartsForm)
        form_parts = form_parts_factory(request.POST)
        if all([process_form.is_valid(), form_parts.is_valid()]):
            process = process_form.save()
            form_parts.instance = process
            form_parts.save()
            return redirect('index')
        else:
            context = {
                'p_form': process_form,
                'form_parts': form_parts
            }
            return render(request, 'process.html', context)
    else:
        context['p_form'] = process_form
        context['form_parts'] = form_parts
    return render(request, 'process.html', context)


def delete_process(request, process_id):
    process = get_object_or_404(Process, pk=process_id)
    process.delete()
    return redirect('index')


def update_process(request, process_id):
    process = get_object_or_404(Process, id=process_id)
    process_form = ProcessForm(instance=process)
    form_parts_factory = inlineformset_factory(Process, Part, form=PartsForm, extra=0, can_delete=False)
    form_parts = form_parts_factory(instance=process)
    context = {
        "id": process_id,
        "p_form": process_form,
        "form_parts": form_parts,
    }
    if request.method == 'POST':
        process_form = ProcessForm(data=request.POST, instance=process)
        form_parts_factory = inlineformset_factory(Process, Part, form=PartsForm)
        form_parts = form_parts_factory(request.POST, instance=process)

        if process_form.is_valid() and form_parts.is_valid():
            process = process_form.save()
            form_parts.instance = process
            form_parts.save()
            return redirect('index')
        else:
            context = {
                'p_form': process_form,
                'form_parts': form_parts
            }
            return render(request, 'edit_process.html', context)
    return render(request, 'edit_process.html', context)


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


def update_parts(request, part_id):
    part = get_object_or_404(Part, id=part_id)
    part_form = PartsForm(instance=part)
    pprint.pprint(part)
    context = {
        "part_form": part_form,
    }
    if request.method == 'POST':
        part_form = PartsForm(data=request.POST, instance=part)

        if part_form.is_valid():

            part_form.save()
            return redirect('index')
        else:
            context = {
                'part_form': part_form,
            }
            return render(request, 'view_process.html', context)
    return render(request, 'view_process.html', context)


def delete_parts(request, part_id):
    part = get_object_or_404(Part, id=part_id)
    process = Process.objects.get(parts__id=part.id)
    part.delete()
    return redirect('get_process', process.id)
