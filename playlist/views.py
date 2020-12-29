from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from playlist.models import Composer, Music, Genre
from playlist.forms import ComposerForm, MusicForm

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
        composer = Composer.objects.get(pk=composer_id)
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

def index(request): 
    num_musics = Music.objects.all().count()
    num_composers = Composer.objects.all().count()
    num_genres = Genre.objects.all().count()
    context = {
        'num_musics': num_musics,
        'num_composers': num_composers,
        'num_genres': num_genres,
    }
    return render(request, 'index.html', context=context)

def list_composers(request):
    composers = Composer.objects.all()
    context = {
        'composers': composers,
    }

    return render(request, 'composers.html', context=context)

def list_musics(request):
    musics = Music.objects.all()
    context = {
        'musics': musics,
    }
    # process the template and pass the context
    return render(request, 'musics.html', context=context)

def list_genres(request):
    genres = Genre.objects.all()
    context = {
        'genres': genres,
    }
    # process the template and pass the context
    return render(request, 'genres.html', context=context)