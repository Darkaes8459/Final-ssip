from django.contrib import admin
from .models import Composer, Music, Genre, Album, Radio, Charts


admin.site.register(Composer)
admin.site.register(Music)
admin.site.register(Genre)
admin.site.register(Album)
admin.site.register(Radio)
admin.site.register(Charts)
