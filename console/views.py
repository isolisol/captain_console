from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from accessory.models import Product
from user.models import RecentlyViewed, Profile, Search
from helper_services.helpers import build_context, get_recently_viewed
from order.models import Cart, ProductInCart
from django.contrib.auth.decorators import login_required
import datetime


@login_required
def c_add_to_cart(request, product_id):
    user = request.user
    product = get_object_or_404(Product, pk=product_id)
    cart, created = Cart.objects.get_or_create(user_id=user.id, complete=False)
    cart_add, created = ProductInCart.objects.get_or_create(product_id=product.id, cart_id=cart.id)
    if not created:
        cart_add.quantity += 1
        cart_add.save()
    return redirect('cart_details')

@login_required
def remove_product_from_cart(request, product_id):
    pass


def index(request):
    user = request.user
    consoles = Product.objects.filter(type_id=1).order_by('name')
    if user.is_authenticated:
        context = build_context(user)
        context['products'] = consoles
    else:
        context = {'products': consoles}
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
        } for x in Product.objects.filter(type_id=1 ,name__icontains=search_filter)]
        return JsonResponse({'data': context['products']})
    context['product_type_id'] = 1
    context['show_sort'] = True
    context['header_text'] = 'All '
    return render(request, 'product/index.html', context=context)


def get_console_by_id(request, id):
    user = request.user
    console = get_object_or_404(Product, pk=id)
    if user.is_authenticated:
        user_profile = Profile.objects.get(user=user)
        viewed_product = Product.objects.get(id=id)
        recently_viewed, created = RecentlyViewed.objects.get_or_create(profile=user_profile, product=viewed_product,
                                                                        date=datetime.datetime.today())
        if not created:
            recently_viewed.date = datetime.datetime.now()
            recently_viewed.save()
        context = build_context(user)
        context['product'] = console
        context['recently_viewed'] = get_recently_viewed(user)
    else:
        context = {'product': console}
    return render(request, 'product/product_details.html', context=context)


def get_playstation_consoles(request):
    user = request.user
    playstation1 = Product.objects.filter(id=6)
    playstation2 = Product.objects.filter(id=7)
    consoles = playstation1.union(playstation2)
    if user.is_authenticated:
        context = build_context(user)
        context['products'] = consoles
    else:
        context = {'products': consoles}
    context['product_type_id'] = 1
    context['header_text'] = str('Playstation ')
    return render(request, 'product/index.html', context=context)


def get_nintendo_consoles(request):
    user = request.user
    nintendo_nes = Product.objects.filter(id=2)
    nintendo64 = Product.objects.filter(id=3)
    gameboy_color = Product.objects.filter(id=4)
    gameboy_advance = Product.objects.filter(id=5)
    consoles = nintendo_nes.union(nintendo64, gameboy_color, gameboy_advance)
    if user.is_authenticated:
        context = build_context(user)
        context['products'] = consoles
    else:
        context = {'products': consoles}
    context['product_type_id'] = 1
    context['header_text'] = str('Nintendo ')
    return render(request, 'product/index.html', context=context)


def get_xbox_consoles(request):
    user = request.user
    consoles = Product.objects.filter(id=8)
    if user.is_authenticated:
        context = build_context(user)
        context['products'] = consoles
    else:
        context = {'products': consoles}
    context['product_type_id'] = 1
    context['header_text'] = str('Xbox ')
    return render(request, 'product/index.html', context=context)


def get_ps1_consoles(request):
    user = request.user
    consoles = Product.objects.filter(id=6)
    if user.is_authenticated:
        context = build_context(user)
        context['products'] = consoles
    else:
        context = {'products': consoles}
    context['product_type_id'] = 1
    context['header_text'] = str('Playstation 1 ')
    return render(request, 'product/index.html', context=context)


def get_ps2_consoles(request):
    user = request.user
    consoles = Product.objects.filter(id=7)
    if user.is_authenticated:
        context = build_context(user)
        context['products'] = consoles
    else:
        context = {'products': consoles}
    context['product_type_id'] = 1
    context['header_text'] = str('Playstation 2 ')
    return render(request, 'product/index.html', context=context)


def get_nintendo_nes_consoles(request):
    user = request.user
    consoles = Product.objects.filter(id=2)
    if user.is_authenticated:
        context = build_context(user)
        context['products'] = consoles
    else:
        context = {'products': consoles}
    context['product_type_id'] = 1
    context['header_text'] = str('Nintendo NES ')
    return render(request, 'product/index.html', context=context)


def get_nintendo_64_consoles(request):
    user = request.user
    consoles = Product.objects.filter(id=3)
    if user.is_authenticated:
        context = build_context(user)
        context['products'] = consoles
    else:
        context = {'products': consoles}
    context['product_type_id'] = 1
    context['header_text'] = str('Nintendo 64 ')
    return render(request, 'product/index.html', context=context)


def get_gameboy_color_consoles(request):
    user = request.user
    consoles = Product.objects.filter(id=4)
    if user.is_authenticated:
        context = build_context(user)
        context['products'] = consoles
    else:
        context = {'products': consoles}
    context['product_type_id'] = 1
    context['header_text'] = str('GameBoy Color ')
    return render(request, 'product/index.html', context=context)


def get_gameboy_advance_consoles(request):
    user = request.user
    consoles = Product.objects.filter(id=5)
    if user.is_authenticated:
        context = build_context(user)
        context['products'] = consoles
    else:
        context = {'products': consoles}
    context['product_type_id'] = 1
    context['header_text'] = str('GameBoy Advance ')
    return render(request, 'product/index.html', context=context)


# Get videgames sorted by price
def get_consoles_sorted(request, orderby, text):
    user = request.user
    consoles = Product.objects.filter(type_id=1).order_by(orderby)
    if user.is_authenticated:
        context = build_context(user)
        context['products'] = consoles
    else:
        context = {'products': consoles}
    context['product_type_id'] = 1
    context['show_sort'] = True
    context['sort_text'] = 'Sorted by ' + text
    context['header_text'] = 'All '
    return render(request, 'product/index.html', context=context)


def get_consoles_price_sorted_asc(request):
    orderby = str('price')
    text = 'price low to high'
    return get_consoles_sorted(request, orderby, text)


def get_consoles_price_sorted_desc(request):
    orderby = str('-price')
    text = 'price high to low'
    return get_consoles_sorted(request, orderby, text)


def get_consoles_sorted_by_name(request):
    orderby = str('name')
    text = 'name'
    return get_consoles_sorted(request, orderby, text)