from django.shortcuts import render, redirect, reverse
from accessory.models import Product
from .models import Order, Cart, ContactInformation, Payment
from helper_services.helpers import build_context, get_next_order_no, calculateTotalPrice
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from order.forms.contact_info_form import ContactInfoForm
from order.forms.payment_form import PaymentForm
from datetime import date
from order.models import BestSellers


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


#@transaction.non_atomic_requests
def checkout(request):
    user = request.user
    context = build_context(user)
    if request.method == 'POST':
        contact_info_form = ContactInfoForm(data=request.POST)
        payment_form = PaymentForm(data=request.POST)
        if contact_info_form.is_valid() and payment_form.is_valid():
            cart = Cart.objects.get(user=user, complete=False)
            request.session['cart_id'] = cart.id
            contact_info = contact_info_form.save()
            payment = payment_form.save(commit=False)
            payment.user = user
            payment.save()
            request.session['contact_info_id'] = contact_info.id
            request.session['payment_id'] = payment.id
            return redirect(reverse('review', args=[]))
        else:
            context['errors'] = payment_form.errors
            context['contact_info_form'] = ContactInfoForm()
            context['payment_form'] = PaymentForm()
            return render(request, 'checkout/index.html', context)
    else:
        context['contact_info_form'] = ContactInfoForm()
        context['payment_form'] = PaymentForm()
        return render(request, 'checkout/index.html', context)


def review(request):
    user = request.user
    context = build_context(user)
    context['contact_info'] = ContactInformation.objects.get(id=request.session['contact_info_id'])
    context['payment'] = Payment.objects.get(id=request.session['payment_id'])
    return render(request, 'checkout/review_info.html', context)


def place_order(request):
    user = request.user
    context = build_context(user)
    date_now = date.today()
    order_num = get_next_order_no()
    cart = Cart.objects.get(id=request.session['cart_id'])
    total_price = calculateTotalPrice(cart.productincart_set.all())
    order = Order.objects.create(
        date=date_now,
        cart_id=request.session['cart_id'],
        contact_info_id=request.session['contact_info_id'],
        payment_id=request.session['payment_id'],
        order_number=order_num,
        total_price=total_price
    )
    order.save()
    request.session['order_id'] = order.id
    cart = Cart.objects.get(id=request.session['cart_id'])
    cart.complete = True
    cart.save()
    for product in cart.productincart_set.all():
        seller, created = BestSellers.objects.get_or_create(product=product.product)
        if not created:
            seller.sold_how_often += product.quantity
        else:
            seller.sold_how_often = product.quantity
        seller.save()
    return redirect('confirmation')


def cancel_order(request):
    ContactInformation.objects.get(id=request.session['contact_info_id']).delete()
    Payment.objects.get(id=request.session['payment_id']).delete()
    for key in list(request.session.keys()):
        if not key.startswith('_'):
            del request.session[key]
    return redirect('cart_details')


def review_back(request):
    ContactInformation.objects.get(id=request.session['contact_info_id']).delete()
    Payment.objects.get(id=request.session['payment_id']).delete()
    for key in list(request.session.keys()):
        if not key.startswith('_'):
            del request.session[key]
    return redirect('checkout')


def confirmation(request):
    user = request.user
    context = build_context(user)
    context['order'] = Order.objects.get(id=request.session['order_id'])
    for key in list(request.session.keys()):
        if not key.startswith('_'):
            del request.session[key]
    return render(request, 'checkout/confirmation.html', context)
