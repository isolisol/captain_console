from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_details, name="cart_details"),
    path('myorders', views.past_orders, name="past_orders"),
    path('checkout', views.checkout, name="checkout"),
    path('<int:order_id>/payment', views.payment, name="payment"),
    path('<int:order_id>/review', views.review, name="review"),
    path('remove_from_cart/<int:product_id>', views.remove_from_cart, name="remove_from_cart")
]
