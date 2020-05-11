from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="consoles-index"),
    path('<int:id>', views.get_console_by_id, name="console_detail"),
    path('playstation_consoles', views.get_playstation_consoles, name='playstation_consoles'),
    path('nintendo_consoles', views.get_nintendo_consoles, name='nintendo_consoles'),
    path('ps1_consoles', views.get_ps1_consoles, name='ps1_consoles'),
    path('ps2_consoles', views.get_ps2_consoles, name='ps2_consoles'),
    path('nintendo_nes_consoles', views.get_nintendo_nes_consoles, name='nintendo_nes_consoles'),
    path('nintendo_64_consoles', views.get_nintendo_64_consoles, name='nintendo_64_consoles'),
    path('gameboy_color_consoles', views.get_gameboy_color_consoles, name='gameboy_color_consoles'),
    path('gameboy_advance_consoles', views.get_gameboy_advance_consoles, name='gameboy_advance_consoles'),
    path('xbox_consoles_consoles', views.get_xbox_consoles, name='xbox_consoles')


]
