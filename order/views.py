from django.shortcuts import render, redirect
from accessory.models import Product
from .models import Order, Cart
from helper_services.helpers import build_context
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages


#@login_required
#def add_to_cart(request, product_id):
#    messages.success(request, "Cart updated")
#    return redirect('cart_details')


def cart_dropdown(request):
    user = request.user
    cart_info = build_context(user)
    return render(request, 'base.html', context=cart_info)


def cart_details(request):
    user = request.user
    cart_info = build_context(user)
    return render(request, 'order/cart_details.html', context=cart_info)


def past_orders(request):
    user = request.user
    cart_ids = []
    for cart in Cart.objects.filter(user_id=user.id).values('id'):
        cart_ids.append(cart.get('id'))
        print(cart)
        print(cart_ids)
    orders_temp = Order.objects.filter(cart_id=cart_ids[0])
    for id in cart_ids[1:]:
        order = Order.objects.filter(cart_id=id)
        orders_temp.union(order)
    orders = {'orders': orders_temp}
    return render(request, 'order/past_orders.html', orders)