from django.urls import path
from . import views
from order import views as o_views

urlpatterns = [
    path('', views.index, name="homepage"),
    path('openinghours/', views.opening_hours, name='openinghours'),
    path('aboutus/', views.about_us, name='aboutus'),
    path('remove_from_cart/<int:product_id>', o_views.remove_from_cart, name="p_remove_from_cart"),
    path('openinghours/remove_from_cart/<int:product_id>', o_views.remove_from_cart, name="op_remove_from_cart"),
    path('aboutus/remove_from_cart/<int:product_id>', o_views.remove_from_cart, name="ab_remove_from_cart"),
    #path('search_result/' , views.search_products, name='search_result')
]
