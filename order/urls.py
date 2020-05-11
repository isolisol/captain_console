from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_details, name="cart_details"),
    path('myorders', views.past_orders, name="past_orders"),
]
