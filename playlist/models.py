from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Music(models.Model):
    title = models.CharField(max_length=200)
    composer = models.ForeignKey('Composer', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000)
    ismn = models.CharField('ISMN', max_length=13)
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title


class Composer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'
