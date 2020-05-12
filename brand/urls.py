from django.urls import path
from . import views
from order import views as o_views


urlpatterns = [
    path('', views.index, name="brand-index"),
    path('remove_from_cart/<int:product_id>', o_views.remove_from_cart, name="b_remove_from_cart"),
]
