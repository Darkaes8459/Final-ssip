

from playlist.models import Composer, Music, Genre
from playlist.forms import ComposerForm, MusicForm




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