from django.urls import path
from . import views
from order import views as o_views

urlpatterns = [
    path('', views.index, name="accessories-index"),
    path('<int:id>', views.get_accessory_by_id, name="accessory_detail"),

    path('playstation_accessories', views.get_playstation_accessories, name="playstation_accessories"),
    path('nintendo_accessories', views.get_nintendo_accessories, name="nintendo_accessories"),
    path('xbox_accessories', views.get_xbox_accessories, name="xbox_accessories"),
    path('other_accessories', views.get_other_accessories, name="other_accessories"),
    path('ps1_accessories', views.get_ps1_accessories, name="ps1_accessories"),
    path('ps2_accessories', views.get_ps2_accessories, name="ps2_accessories"),
    path('nintendo_nes_accessories', views.get_nintendo_nes_accessories, name="nintendo_nes_accessories"),
    path('nintendo_64_accessories', views.get_nintendo_64_accessories, name="nintendo_64_accessories"),
    path('gameboy_color_accessories', views.get_gameboy_color_accessories, name="gameboy_color_accessories"),
    path('gameboy_advance_accessories', views.get_gameboy_advance_accessories, name="gameboy_advance_accessories"),

    path('add_to_cart/<int:product_id>', views.a_add_to_cart, name="a_add_to_cart"),
    path('remove_from_cart/<int:product_id>', o_views.remove_from_cart, name="a_remove_from_cart"),

    path('sort_accessories_price_asc', views.get_accessories_price_sorted_asc, name='a_sort_price_asc'),
    path('sort_accessories_price_desc', views.get_accessories_price_sorted_desc, name='a_sort_price_desc'),
    path('sort_accessories_by_name', views.get_accessories_sorted_by_name, name='a_sort_by_name')
]
