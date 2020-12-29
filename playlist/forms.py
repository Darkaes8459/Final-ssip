from django.forms import ModelForm
from django.core.exceptions import ValidationError
from playlist.models import Music, Composer


class ComposerForm(ModelForm):
    class Meta:
        model = Composer
        fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']


class MusicForm(ModelForm):
    class Meta:
        model = Music 
        fields = ['title', 'composer', 'summary', 'ismn', 'genre']