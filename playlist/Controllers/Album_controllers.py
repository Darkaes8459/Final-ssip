from django.shortcuts import render
from django.core.paginator import Paginator
from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from playlist.models.Album import Album
from playlist.forms import AlbumForm


def index(request):
    if request.method == 'POST':
        req = request.POST.dict()
    
        name = req['name']
        Album = Album.objects.filter(name__contains=name).order_by('name')
    else:
        Album = Album.objects.all().order_by('name')  
    
    data = {
        'Album': Album,
    }
    # render to our html
    return render(request, 'index.html', context=data)

