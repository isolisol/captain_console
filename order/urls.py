from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_details, name="cart_details"),
    path('checkout', views.checkout, name="checkout"),
    path('review', views.review, name="review"),
    path('remove_from_cart/<int:product_id>', views.remove_from_cart, name="remove_from_cart"),
    path('place_order', views.place_order, name="place_order"),
    path('cancel_order', views.cancel_order, name="cancel_order"),
    path('confirmation', views.confirmation, name="confirmation")
]
