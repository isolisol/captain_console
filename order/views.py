from django.shortcuts import render
from order.models import Order, Cart
from helper_services.helpers import build_context


# Create your views here.
def cart_dropdown(request):
    user = request.user
    cart_info = build_context(user)
    #return render(request, 'order/cart_dropdown.html', context=cart_info)
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