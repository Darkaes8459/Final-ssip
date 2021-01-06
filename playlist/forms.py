from django.forms import ModelForm
from django.core.exceptions import ValidationError
from playlist.models import Music, Composer , Genre , Radio , Album , Charts


class ComposerForm(ModelForm):
    class Meta:
        model = Composer
        fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']


class MusicForm(ModelForm):
    class Meta:
        model = Music 
        fields = ['title', 'composer', 'summary', 'ismn', 'genre']

class GenreForm(ModelForm):
    class Meta:
        model = Genre
        fields = ['music_name', 'Autour_name', 'date_of_make']

class RadioForm(ModelForm):
    class Meta:
        model = Radio
        fields = ['radio_id', 'radio_name', 'radio_description']

class AlbumForm(ModelForm):
    class Meta:
        model = Album
        fields = ['album_id', 'album_name', 'album_description', 'album_music', 'album_genre']

class ChartsForm(ModelForm):
    class Meta:
        model = Charts
        fields = ['charts_id', 'charts_name', 'charts_description']