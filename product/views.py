from django.shortcuts import render

from accessory.models import Product
from helper_services.helpers import build_context


def index(request):
    user = request.user
    if user.is_authenticated:
        context = build_context(user)
        context['products'] = Product.objects.all().order_by('name')
    else:
        context = {'products': Product.objects.all().order_by('name')}
    context['product_type_id'] = 'all'
    context['show_sort'] = True
    return render(request, 'product/index.html', context=context)


# Get all products sorted by price
def get_all_products_sorted(request, orderby, text):
    user = request.user
    consoles = Product.objects.all().order_by(orderby)
    if user.is_authenticated:
        context = build_context(user)
        context['products'] = consoles
    else:
        context = {'products': consoles}
    context['product_type_id'] = 'all'
    context['sort_text'] = 'Sorted by ' + text
    return render(request, 'product/index.html', context=context)

def get_all_products_price_sorted_asc(request):
    orderby = str('price')
    text = 'price low to high'
    return get_all_products_sorted(request, orderby, text)


def get_all_products_price_sorted_desc(request):
    orderby = str('-price')
    text = 'price high to low'
    return get_all_products_sorted(request, orderby, text)


def get_all_products_sorted_by_name(request):
    orderby = str('name')
    text = 'name'
    return get_all_products_sorted(request, orderby, text)