from django.urls import path
from . import views
from order import views as o_views

urlpatterns = [
    path('', views.index, name='all-products-index'),
    path('sort_all_products_price_asc', views.get_all_products_price_sorted_asc, name='all_sort_price_asc'),
    path('sort_all_products_price_desc', views.get_all_products_price_sorted_desc, name='all_sort_price_desc'),
    path('sort_all_products_by_name', views.get_all_products_sorted_by_name, name='all_sort_by_name')
]
