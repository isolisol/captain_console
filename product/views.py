from django.http import JsonResponse
from django.shortcuts import render
from accessory.models import Product
from order.models import BestSellers
from user.models import RecentlyViewed, Search
from helper_services.helpers import build_context
import datetime


def index(request):
    user = request.user
    if user.is_authenticated:
        context = build_context(user)
        context['products'] = Product.objects.all().order_by('name')
    else:
        context = {'products': Product.objects.all().order_by('name')}
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        if user.is_authenticated and len(search_filter) > 0:
            user_searches = Search.objects.create(profile=user.profile, search_text=search_filter, date=datetime.datetime.now())
        context['products'] = [{
            'id': x.id,
            'name': x.name,
            'description': x.description,
            'price': x.price,
            'image': x.image
        } for x in Product.objects.filter(name__icontains=search_filter)]
        return JsonResponse({'data': context['products']})
    context['product_type_id'] = 'all'
    context['show_sort'] = True
    return render(request, 'product/index.html', context=context)


def get_best_sellers(request):
    user = request.user
    context = build_context(user)
    best_sellers = BestSellers.objects.all().order_by('-sold_how_often')
    context['products'] = best_sellers
    context['show_best_sell'] = True
    return render(request, 'product/index.html', context)


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
    context['show_sort'] = True
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


def get_recently_viewed_items(request):
    pass
