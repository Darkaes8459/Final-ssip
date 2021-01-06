from django.urls import path
from Controllers import Album_controllers, Charts_controllers, Composer_contollers, Genre_controllers, Music_controllers, Radio_contollers


urlpatterns = [
    path('', views.index, name='index'),
    path('composers/', views.list_composers, name='composers'),
    path('composer/add/', views.add_composer, name='add_composer'),
    path('composer/edit/<int:composer_id>', views.edit_composer, name='edit_composer'),
    path('composer/delete/<int:composer_id>', views.delete_composer, name='delete_composer'),

    path('music/add/', views.add_music, name='add_music'),
    path('music/edit/<int:music_id>', views.edit_music, name='edit_music'),
    path('music/delete/<int:music_id>', views.delete_music, name='delete_music'),

    path('radio/add/', views.add_radio, name='add_radio'),
    path('radio/edit/<int:radio_id>', views.edit_radio, name='edit_radio'),
    path('radio/delete/<int:radio_id>', views.delete_radio, name='delete_radio'),

    path('genres/', views.list_genres, name='genres'),
    path('musics/', views.list_musics, name='musics'),
    path('radios/', views.list_musics, name='radios'),
]
jgkhjbkjj