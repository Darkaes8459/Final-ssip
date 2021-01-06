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
def add_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)  # we accept post request from submit button
        if form.is_valid():  # django has its own validation
            form.save()  # directly save the form
            return HttpResponseRedirect(reverse('albums'))  # return to all authors page
    else:
        form = AlbumForm()  # pass empty form

    context = {
        'form': form
    }
    return render(request, 'album_form.html', context=context)

def edit_album(request, album_id):
    if request.method == 'POST':
        album = Album.objects.get(pk=album_id)  # here we get the id  passed in author_id
        form = AlbumForm(request.POST, instance=album)  # instance means we process form with current author
        if form.is_valid():
            form.save()  # save if valid
            return HttpResponseRedirect(reverse('albums'))
    else:
        album = Album.objects.get(pk=album_id)  # we get the author with the same id
        fields = model_to_dict(album)  # change model fields to dict
        form = AlbumForm(initial=fields, instance=album)  # use found author as initial values
    context = {
        'form': form,
        'type': 'edit',  # edit here is used in the html
    }
    return render(request, 'album_form.html', context=context)

def delete_album(request, album_id):
    album = Album.objects.get(pk=album_id)
    if request.method == 'POST':
        album.delete()
        return HttpResponseRedirect(reverse('albums'))
    context = {
        'album': album
    }
    return render(request, 'album_delete_form.html', context=context)

def list_albums(request):
    albums = Album.objects.all()
    context = {
        'albums': albums,
    }
    # process the template and pass the context
    return render(request, 'album.html', context=context)