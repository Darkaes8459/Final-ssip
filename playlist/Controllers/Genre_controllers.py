from django.shortcuts import render
from django.core.paginator import Paginator
from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from playlist.models.Genre import Genre
from playlist.forms import GenreForm



def list_genres(request):
    genres = Genre.objects.all()
    context = {
        'genres': genres,
    }
    # process the template and pass the context
    return render(request, 'genres.html', context=context)