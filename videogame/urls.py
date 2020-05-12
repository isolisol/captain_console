from django.urls import path
from . import views
from order import views as o_views

urlpatterns = [
    path('', views.index, name="videogame-index"),
    path('<int:id>', views.get_videogame_by_id, name="videogame_detail"),
    path('playstation_games', views.get_videogames_by_playstation, name="playstation_games"),
    path('nintendo_games', views.get_videogames_by_nintendo, name="nintendo_games"),
    path('ps1_games', views.get_ps1_games, name="ps1_games"),
    path('ps2_games', views.get_ps2_games, name="ps2_games"),
    path('nintendo_nes_games', views.get_nintendo_nes_games, name="nintendo_nes_games"),
    path('nintendo_64_games', views.get_nintendo_64_games, name="nintendo_64_games"),
    path('gameboy_color_games', views.get_gameboy_color_games, name="gameboy_color_games"),
    path('gameboy_advance_games', views.get_gameboy_advance_games, name="gameboy_advance_games"),
    path('xbox_games', views.get_videogames_by_xbox, name="xbox_games"),
    path('add_to_cart/<int:product_id>', views.v_add_to_cart, name="v_add_to_cart")
]
