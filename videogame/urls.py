from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="videogame-index"),
    path('<int:id>', views.get_videogame_by_id, name="videogame_detail"),
    path('playstation_games', views.get_videogames_by_playstation, name="playstation_games"),
    path('nintendo_games', views.get_videogames_by_nintendo, name="nintendo_games"),
    path('xbox_games', views.get_videogames_by_xbox, name="xbox_games"),
    path('gameboy_games', views.get_videogames_by_gameboy, name="gameboy_games")
]
