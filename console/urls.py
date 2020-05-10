from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="consoles-index"),
    path('<int:id>', views.get_console_by_id, name="console_detail"),
    path('playstation_consoles', views.get_playstation_consoles, name='playstation_consoles'),
    path('nintendo_consoles', views.get_nintendo_consoles, name='nintendo_consoles'),
    path('gameboy_consoles', views.get_gameboy_consoles, name='gameboy_consoles'),
    path('xbox_consoles', views.get_xbox_consoles, name='xbox_consoles')
]
