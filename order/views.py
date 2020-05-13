from django.shortcuts import render, redirect, reverse
from accessory.models import Product
from .models import Order, Cart, ContactInformation, Payment
from helper_services.helpers import build_context
from django.contrib.auth.decorators import login_required
from order.forms.contact_info_form import ContactInfoForm
from order.forms.payment_form import PaymentForm
from datetime import date


def remove_from_cart(request, product_id):
    cart = Cart.objects.get(user=request.user, complete=False)
    cart.product.remove(Product.objects.get(id=product_id))
    return redirect('cart_details')


@login_required
def cart_dropdown(request):
    user = request.user
    cart_info = build_context(user)
    return render(request, 'base.html', context=cart_info)


@login_required
def cart_details(request):
    user = request.user
    cart_info = build_context(user)
    return render(request, 'order/cart_details.html', context=cart_info)


@login_required()
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


def checkout(request):
    user = request.user
    context = build_context(user)
    context['form'] = ContactInfoForm()
    if request.method == 'POST':
        form = ContactInfoForm(data=request.POST)
        if form.is_valid():
            contact_information = form.save()
            request.session['contact_info'] = contact_information.id
            cart = Cart.objects.get(user_id=user.id)
            request.session['cart'] = cart.id
            order = Order.objects.create(cart_id=cart.id, date=date.today(), contact_info_id=contact_information.id)
            request.session['order'] = order.id
            return redirect(reverse('payment', args=[order.id]))
    else:
        return render(request, 'checkout/index.html', context)


def payment(request, order_id):
    user = request.user
    context = build_context(user)
    context['form'] = PaymentForm()
    if request.method == 'POST':
        form = PaymentForm(data=request.POST)
        if form.is_valid():
            new_payment = form.save(commit=False)
            new_payment.user = user
            new_payment.save()
            request.session['payment'] = new_payment.id
            order = Order.objects.get(id=order_id) #=request.session['order_id'])
            order.payment = new_payment
            order.save()
            return redirect(reverse('review', args=[order_id]))
    else:
        return render(request, 'checkout/payment.html', context)


def review(request, order_id):
    user = request.user
    context = build_context(user)
    order = Order.objects.get(id=order_id)
    contact_info = ContactInformation.objects.get(id=order.contact_info.id)
    payment_info = Payment.objects.get(id=order.payment.id)
    context['contact_info'] = contact_info
    context['payment_info'] = payment_info
    return render(request, 'checkout/review_info.html', context)


def cancel_order(request):
    # Eyðum öllum línum
    pass


def place_order(request):
    # Staðfesta pöntun
    pass