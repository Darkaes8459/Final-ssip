from django.db import models
from .Genre import Genre

class Music(models.Model):
    title = models.CharField(max_length=200)
    composer = models.ForeignKey('Composer', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000)
    ismn = models.CharField('ISMN', max_length=13)
    genre = models.ManyToManyField(Genre)

    class meta:
            app_label = 'playlist'

    def __str__(self):
        return self.title