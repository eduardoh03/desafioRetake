from django.forms import modelformset_factory, inlineformset_factory
from django.shortcuts import render
from .models import Process, Part
from .forms import ProcessForm, PartsForm
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404


def index(request):
    process = Process.objects.all()
    context = {
        "process": process
    }
    return render(request, 'home.html', context)


def find_process(request):
    list_process = Process.objects.all()
    context = {
    }
    if 'buscar' in request.GET:
        attribute_process = request.GET['buscar']
        context['search'] = attribute_process
        if attribute_process:
            list_process = list_process.filter(department__icontains=attribute_process) \
                           | list_process.filter(subject__icontains=attribute_process) \
                           | list_process.filter(judge__icontains=attribute_process)
    context['process'] = list_process
    return render(request, 'partials/_search.html', context)


def get_process(request, process_id):
    process = get_object_or_404(Process, pk=process_id)
    context = {
        'process': process,
    }
    return render(request, 'view_process.html', context)


def create_process(request):
    process_form = ProcessForm()
    form_parts_factory = inlineformset_factory(Process, Part, form=PartsForm, extra=1, can_delete=True)
    form_parts = form_parts_factory()
    context = {
    }
    if request.method == 'POST':
        process_form = ProcessForm(request.POST)
        form_parts_factory = inlineformset_factory(Process, Part, form=PartsForm)
        form_parts = form_parts_factory(request.POST)
        if process_form.is_valid() and form_parts.is_valid() == False:
            process_form.save()
            process = Process.objects.all()
            context = {
                'process': process
            }
            return render(request, 'home.html', context, status=201)
        elif process_form.is_valid() and form_parts.is_valid():
            process = process_form.save()
            form_parts.instance = process
            form_parts.save()
            process = Process.objects.all()
            context = {
                'process': process
            }
            return render(request, 'home.html', context, status=201)
        else:
            context = {
                'p_form': process_form,
                'form_parts': form_parts
            }
            return render(request, 'create_process.html', context, status=400)

    else:
        context['p_form'] = process_form
        context['form_parts'] = form_parts
    return render(request, 'create_process.html', context)


def delete_process(request, process_id):
    process = get_object_or_404(Process, pk=process_id)
    process.delete()
    return redirect('index')


def update_process(request, process_id):
    process = get_object_or_404(Process, id=process_id)
    process_form = ProcessForm(instance=process)
    par = Part.objects.filter(process=process)
    if par.count() == 0:
        form_parts_factory = inlineformset_factory(Process, Part, form=PartsForm, extra=1, can_delete=True)
    else:
        form_parts_factory = inlineformset_factory(Process, Part, form=PartsForm, extra=0, can_delete=True)
    form_parts = form_parts_factory(instance=process)
    context = {
        "process": process,
        "p_form": process_form,
        "form_parts": form_parts,
    }
    if request.method == 'POST':
        process_form = ProcessForm(data=request.POST, instance=process)
        form_parts_factory = inlineformset_factory(Process, Part, form=PartsForm)
        form_parts = form_parts_factory(request.POST, instance=process)
        if all([process_form.is_valid(), form_parts.is_valid()]):
            process = process_form.save()
            for form in form_parts:
                try:
                    parts = form.save(commit=False)
                    parts.process = process
                    parts.save()
                    form_parts.instance = process
                    form_parts.save()
                except:
                    return redirect('index')
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


def delete_all_parts(request, process_id):
    process = get_object_or_404(Process, id=process_id)
    for part in process.parts.all():
        part.delete()
    return redirect('get_process', process_id)


def view_404(request, exception):
    return render(request, 'not_found.html', status=404)


def view_500(request):
    return render(request, 'server_error.html', status=500)
