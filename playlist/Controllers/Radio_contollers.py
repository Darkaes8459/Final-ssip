from django.shortcuts import render
from django.core.paginator import Paginator
from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from playlist.models.Radio import Radio
from playlist.forms import RadioForm

def add_radio(request):
    if request.method == 'POST':
        form = RadioForm(request.POST)  # we accept post request from submit button
        if form.is_valid():  # django has its own validation
            form.save()  # directly save the form
            return HttpResponseRedirect(reverse('radios'))  # return to all authors page
    else:
        form = RadioForm()  # pass empty form

    context = {
        'form': form
    }
    return render(request, 'radio_form.html', context=context)

def edit_radio(request, Radio_id):
    if request.method == 'POST':
        radio = Radio.objects.get(pk=radio_id)
        form = RadioForm(request.POST, instance=radio)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('radios'))
    else:
        radio = Radio.objects.get(pk=radio_id)
        fields = model_to_dict(Radio)
        form = RadioForm(initial=fields, instance=radio)
    context = {
        'form': form,
        'type': 'edit',
    }
    return render(request, 'radio_form.html', context=context)

def delete_radio(request, radio_id):
    radio = Radio.objects.get(pk=radio_id)
    if request.method == 'POST':
        radio.delete()
        return HttpResponseRedirect(reverse('radios'))
    context = {
        'radio': radio
    }
    return render(request, 'radio_delete_form.html', context=context)
    
def list_radio(request):
    radio = radio.objects.all()
    context = {
        'radio': radio,
    }

    return render(request, 'Radio.html', context=context)
