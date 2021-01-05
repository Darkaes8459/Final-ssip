from django.core.paginator import Paginator
from django.shortcuts import render
from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from pizza.models.topping import Topping


def add_composer(request):
    if request.method == 'POST':
        form = ComposerForm(request.POST)  # we accept post request from submit button
        if form.is_valid():  # django has its own validation
            form.save()  # directly save the form
            return HttpResponseRedirect(reverse('composers'))  # return to all authors page
    else:
        form = ComposerForm()  # pass empty form

    context = {
        'form': form
    }
    return render(request, 'composer_form.html', context=context)

def edit_composer(request, composer_id):
    if request.method == 'POST':
        composer = Composer.objects.get(pk=composer_id)
        form = ComposerForm(request.POST, instance=composer)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('composers'))
    else:
        composer = Radio.objects.get(pk=composer_id)
        fields = model_to_dict(composer)
        form = ComposerForm(initial=fields, instance=composer)
    context = {
        'form': form,
        'type': 'edit',
    }
    return render(request, 'composer_form.html', context=context)

def delete_composer(request, composer_id):
    composer = Composer.objects.get(pk=composer_id)
    if request.method == 'POST':
        composer.delete()
        return HttpResponseRedirect(reverse('composers'))
    context = {
        'composer': composer
    }
    return render(request, 'composer_delete_form.html', context=context)
