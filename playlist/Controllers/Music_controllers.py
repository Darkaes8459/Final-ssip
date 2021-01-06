from django.shortcuts import render
from django.core.paginator import Paginator
from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from playlist.models.Genre import Genre
from playlist.models.Music import Music
from playlist.forms import MusicForm



def add_music(request):
    if request.method == 'POST':
        form = MusicForm(request.POST)  # we accept post request from submit button
        if form.is_valid():  # django has its own validation
            form.save()  # directly save the form
            return HttpResponseRedirect(reverse('musics'))  # return to all authors page
    else:
        form = MusicForm()  # pass empty form

    context = {
        'form': form
    }
    return render(request, 'music_form.html', context=context)

def edit_music(request, music_id):
    if request.method == 'POST':
        music = Music.objects.get(pk=music_id)  # here we get the id  passed in author_id
        form = MusicForm(request.POST, instance=music)  # instance means we process form with current author
        if form.is_valid():
            form.save()  # save if valid
            return HttpResponseRedirect(reverse('musics'))
    else:
        music = Music.objects.get(pk=music_id)  # we get the author with the same id
        fields = model_to_dict(music)  # change model fields to dict
        form = MusicForm(initial=fields, instance=music)  # use found author as initial values
    context = {
        'form': form,
        'type': 'edit',  # edit here is used in the html
    }
    return render(request, 'music_form.html', context=context)

def delete_music(request, music_id):
    music = Music.objects.get(pk=music_id)
    if request.method == 'POST':
        music.delete()
        return HttpResponseRedirect(reverse('musics'))
    context = {
        'music': music
    }
    return render(request, 'music_delete_form.html', context=context)

def list_musics(request):
    musics = Music.objects.all()
    context = {
        'musics': musics,
    }
    # process the template and pass the context
    return render(request, 'musics.html', context=context)