from django.shortcuts import render
from django.core.paginator import Paginator
from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from playlist.models.Music import Music
from playlist.models.Genre import Genre
from playlist.models.Composer import Composer
from playlist.models.Charts import Charts
from playlist.models.Radio import Radio
from playlist.models.Album import Album


def index(request): 
    num_musics = Music.objects.all().count()
    num_composers = Composer.objects.all().count()
    num_genres = Genre.objects.all().count()
    num_albums = Album.objects.all().count()
    num_charts = Charts.objects.all().count()
    num_Radio  = Radio.objects.all().count()

    context = {
        'num_musics': num_musics,
        'num_composers': num_composers,
        'num_genres': num_genres,
        'num_albums': num_albums,
        'num_charts': num_charts,
        'num_radios': num_Radio,
    }
    return render(request, 'index.html', context=context)
