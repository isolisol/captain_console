from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="accessories-index"),
    path('<int:id>', views.get_accessory_by_id, name="accessory_detail"),
    path('playstation_accessories', views.get_playstation_accessories, name="playstation_accessories"),
    path('nintendo_accessories', views.get_nintendo_accessories, name="nintendo_accessories"),
    path('xbox_accessories', views.get_xbox_accessories, name="xbox_accessories"),
    path('gameboy_accessories', views.get_gameboy_accessories, name="gameboy_accessories"),
    path('other_accessories', views.get_other_accessories, name="other_accessories")
]
