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

    path('add_to_cart/<int:product_id>', views.v_add_to_cart, name="v_add_to_cart"),

    path('action', views.get_action_videogames, name='action_videogames'),
    path('adventure', views.get_adventure_videogames, name='adventure_videogames'),
    path('roleplaying', views.get_roleplaying_videogames, name='roleplaying_videogames'),
    path('racing', views.get_racing_videogames, name='racing_videogames'),
    path('puzzle', views.get_puzzle_videogames, name='puzzle_videogames'),
    path('platforming', views.get_platforming_videogames, name='platforming_videogames'),
    path('fighting', views.get_fighting_videogames, name='fighting_videogames'),
    path('sports', views.get_sport_videogaems, name='sports_videogames'),
    path('tactical_shooter', views.get_tacticalshooter_videogames, name='tacticalshooter_videogames'),

    path('sort_videogames_price_asc', views.get_videogames_price_sorted_asc, name='v_sort_price_asc'),
    path('sort_videogames_price_desc', views.get_videogames_price_sorted_desc, name='v_sort_price_desc'),
    path('sort_videogames_by_name', views.get_videogames_sorted_by_name, name='v_sort_by_name')
]
