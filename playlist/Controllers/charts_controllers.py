from django.shortcuts import render
from django.core.paginator import Paginator
from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from playlist.models.Charts import Charts
from playlist.forms import ChartsForm


def add_Charts(request):
    if request.method == 'POST':
        form = ChartsForm(request.POST)  # we accept post request from submit button
        if form.is_valid():  # django has its own validation
            form.save()  # directly save the form
            return HttpResponseRedirect(reverse('charts'))  # return to all authors page
    else:
        form = ChartsForm()  # pass empty form

    context = {
        'form': form
    }
    return render(request, 'charts_form.html', context=context)

def edit_Charts(request, charts_id):
    if request.method == 'POST':
        charts = Charts.objects.get(pk=charts_id)  # here we get the id  passed in author_id
        form = ChartsForm(request.POST, instance=charts)  # instance means we process form with current author
        if form.is_valid():
            form.save()  # save if valid
            return HttpResponseRedirect(reverse('charts'))
    else:
        charts = charts.objects.get(pk=charts_id)  # we get the author with the same id
        fields = model_to_dict(Charts)  # change model fields to dict
        form = chartsForm(initial=fields, instance=charts)  # use found author as initial values
    context = {
        'form': form,
        'type': 'edit',  # edit here is used in the html
    }
    return render(request, 'charts_form.html', context=context)

def delete_Charts(request, Charts_id):
    charts = Charts.objects.get(pk=Charts_id)
    if request.method == 'POST':
        Charts.delete()
        return HttpResponseRedirect(reverse('charts'))
    context = {
        'charts': charts
    }
    return render(request, 'charts_delete_form.html', context=context)


def list_Charts(request):
    Charts = Charts.objects.all()
    context = {
        'Charts': Charts,
    }

    return render(request, 'Charts.html', context=context)


