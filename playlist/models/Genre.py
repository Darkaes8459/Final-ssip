from django.db import models

class Genre(models.Model):
    music_name = models.CharField(max_length=200)
    Autour_name=models.CharField(max_length=200)
    date_of_make=models.CharField(max_length=200)
    class meta:
        app_label = 'playlist'

    def __str__(self):
        return self.name

