from django.db import models
from .Music import Music
from .Genre import Genre

class Album(models.Model):
    album_id = models.AutoField(primary_key=True)
    album_name = models.CharField(max_length=50, blank=False, null=False)
    album_description = models.TextField(blank=True, null=True)
    album_music = models.ForeignKey(Music, on_delete=models.CASCADE)
    album_genre = models.ManyToManyField(Genre)
    

    class meta:
           app_label = 'playlist'

    def __str__(self):
        return f'{self.album_name} {self.album_id}'