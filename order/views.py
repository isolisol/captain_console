from django.shortcuts import render, redirect, reverse
from accessory.models import Product
from .models import Order, Cart, ContactInformation, Payment
from helper_services.helpers import build_context, get_next_order_no
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


def checkout(request):
    user = request.user
    context = build_context(user)
    context['form'] = ContactInfoForm()
    if request.method == 'POST':
        form = ContactInfoForm(data=request.POST)
        if form.is_valid():
            contact_information = form.save()
            request.session['contact_info'] = contact_information.id
            cart = Cart.objects.get(user_id=user.id, complete=False)
            request.session['cart'] = cart.id
            order = Order.objects.create(cart_id=cart.id, date=date.today(), contact_info_id=contact_information.id)
            request.session['order'] = order.id
            return redirect('payment')
    else:
        return render(request, 'checkout/index.html', context)


def payment(request):
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
            order_id = request.session['order']
            order = Order.objects.get(id=order_id) #=request.session['order_id'])
            order.payment = new_payment
            order.save()
            return redirect(reverse('review', args=[]))
    else:
        return render(request, 'checkout/payment.html', context)


def review(request):
    user = request.user
    context = build_context(user)
    order_id = request.session['order']
    order = Order.objects.get(id=order_id)
    contact_info = ContactInformation.objects.get(id=order.contact_info.id)
    payment_info = Payment.objects.get(id=order.payment.id)
    context['contact_info'] = contact_info
    context['payment_info'] = payment_info
    return render(request, 'checkout/review_info.html', context)


def cancel_order(request):
    # Eyðum öllum línum
    order_id = request.session['order']
    payment_id = request.session['payment']
    contact_info_id = request.session['contact_info']
    Order.objects.get(id=order_id).delete()
    Payment.objects.get(id=payment_id).delete()
    ContactInformation.objects.get(id=contact_info_id).delete()
    for key in list(request.session.keys()):
        if not key.startswith('_'):
            del request.session[key]
    return redirect('cart_details')


def place_order(request):
    # Staðfesta pöntun
    cart_id = request.session['cart']
    cart = Cart.objects.get(id=cart_id)
    cart.complete = True
    cart.save()
    order = Order.objects.get(id=request.session['order'])
    order.order_number = get_next_order_no()
    order.save()
    new_cart = Cart.objects.create(user=request.user, complete=False)
    for key in list(request.session.keys()):
        if not key.startswith('_') and key != 'order':
            del request.session[key]
    return redirect('confirmation')


def confirmation(request):
    user = request.user
    context = build_context(user)
    context['order'] = Order.objects.get(id=request.session['order'])
    return render(request, 'checkout/confirmation.html', context)