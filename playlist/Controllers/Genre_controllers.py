from django.shortcuts import render
from django.core.paginator import Paginator
from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from Music.models.genre import Genre

def index(request):
    # get all authors and add to context dictionary
    genre = Genre.objects.all()
    context = {
        'genre': genre,
    }
    # process the template and pass the context
    return render(request, 'genre/index.html', context=context)