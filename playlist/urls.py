from django.urls import path
from playlist.Controllers import Album_controllers, Charts_controllers, Composer_contollers, Genre_controllers, Music_controllers, Radio_contollers,Index_controllers,Charts_controllers,registration_controller


urlpatterns = [
    path('', Index_controllers.index, name='index'),
    path('composers/', Composer_contollers.list_composers, name='composers'),
    path('composer/add/', Composer_contollers.add_composer, name='add_composer'),
    path('composer/edit/<int:composer_id>', Composer_contollers.edit_composer, name='edit_composer'),
    path('composer/delete/<int:composer_id>', Composer_contollers.delete_composer, name='delete_composer'),

    path('music/add/', Music_controllers.add_music, name='add_music'),
    path('music/edit/<int:music_id>', Music_controllers.edit_music, name='edit_music'),
    path('music/delete/<int:music_id>', Music_controllers.delete_music, name='delete_music'),

    path('radio/add/', Radio_contollers.add_radio, name='add_radio'),
    path('radio/edit/<int:radio_id>', Radio_contollers.edit_radio, name='edit_radio'),
    path('radio/delete/<int:radio_id>', Radio_contollers.delete_radio, name='delete_radio'),

    path('genres/', Genre_controllers.list_genres, name='genres'),
    path('music/', Music_controllers.list_musics, name='musics'),
    path('radio/', Radio_contollers.list_radio, name='radios'),
    path('albums/', Album_controllers.list_albums, name='albums'),

    path('charts/', Charts_controllers.list_Charts, name='charts'),
    path('charts/add/', Charts_controllers.add_Charts, name='add_charts'),
    path('charts/edit/<int:charts_id>', Charts_controllers.edit_Charts, name='edit_charts'),
    path('charts/delete/<int:charts_id>', Charts_controllers.delete_Charts, name='delete_charts'),

    path('album/add/', Album_controllers.add_album, name='add_album'),
    path('album/edit/<int:album_id>', Album_controllers.edit_album, name='edit_album'),
    path('album/delete/<int:album_id>', Album_controllers.delete_album, name='delete_album'),


    path('register', registration_controller.index, name='register'),

]
