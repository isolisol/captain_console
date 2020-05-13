from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from accessory.models import Product
from user.models import RecentlyViewed, Profile
from order.models import Cart, ProductInCart
from helper_services.helpers import build_context
from datetime import date


@login_required()
def v_add_to_cart(request, product_id):
    user = request.user
    product = get_object_or_404(Product, pk=product_id)
    cart, created = Cart.objects.get_or_create(user_id=user.id, complete=False)
    cart_add, created = ProductInCart.objects.get_or_create(product_id=product.id, cart_id=cart.id)
    if not created:
        cart_add.quantity += 1
        cart_add.save()
    return redirect('cart_details')


def index(request):
    user = request.user
    if user.is_authenticated:
        context = build_context(user)
        context['products'] = Product.objects.filter(type_id=2).order_by('name')
    else:
        context = {'products': Product.objects.filter(type_id=2).order_by('name')}
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        context['products'] = [{
            'id': x.id,
            'name': x.name,
            'description': x.description,
            'price': x.price,
            'image': x.image
        } for x in Product.objects.filter(type_id=2, name__icontains=search_filter)]
        return JsonResponse({'data': context['products']})
    context['product_type_id'] = 2
    context['show_sort'] = True
    context['header_text'] = 'All '
    return render(request, 'product/index.html', context=context)


# Get specific product
def get_videogame_by_id(request, id):
    user = request.user
    videogame = get_object_or_404(Product, pk=id)
    if user.is_authenticated:
        user_profile = Profile.objects.get(user=user)
        viewed_product = Product.objects.get(id=id)
        RecentlyViewed.objects.create(profile=user_profile, product=viewed_product, date=date.today())
        context = build_context(user)
        context['product'] = videogame
    else:
        context = {'product': videogame}
    return render(request, 'product/product_details.html', context=context)


# Get video games for specific consoles
def get_videogames_by_playstation(request):
    user = request.user
    playstation1 = Product.objects.filter(type_id=2, console_id=6)
    playstation2 = Product.objects.filter(type_id=2, console_id=7)
    videogames = playstation1.union(playstation2)
    if user.is_authenticated:
        context = build_context(user)
        context['products'] = videogames
    else:
        context = {'products': videogames}
    context['product_type_id'] = 2
    context['header_text'] = str('Playstation ')
    return render(request, 'product/index.html', context=context)


def get_videogames_by_nintendo(request):
    user = request.user
    nintendo_nes = Product.objects.filter(type_id=2, console_id=2)
    nintendo64 = Product.objects.filter(type_id=2, console_id=3)
    gameboy_color = Product.objects.filter(type_id=2, console_id=4)
    gameboy_advanced = Product.objects.filter(type_id=2, console_id=5)
    videogames = nintendo_nes.union(nintendo64, gameboy_color, gameboy_advanced)
    if user.is_authenticated:
        context = build_context(user)
        context['products'] = videogames
    else:
        context = {'products': videogames}
    context['product_type_id'] = 2
    context['header_text'] = str('Nintendo ')
    return render(request, 'product/index.html', context=context)


def get_videogames_by_xbox(request):
    user = request.user
    if user.is_authenticated:
        context = build_context(user)
        context['products'] = Product.objects.filter(type_id=2, console_id=8)
    else:
        context = {'products': Product.objects.filter(type_id=2, console_id=8)}
    context['product_type_id'] = 2
    context['header_text'] = str('Xbox ')
    return render(request, 'product/index.html', context=context)


# Get videogames for specific console

# Main function
def get_videogames_for_console(request, consoleid, header_text):
    user = request.user
    videogames = Product.objects.filter(type_id=2, console_id=consoleid)
    if user.is_authenticated:
        context = build_context(user)
        context['products'] = videogames
    else:
        context = {'products': videogames}
    context['product_type_id'] = 2
    context['header_text'] = header_text
    return render(request, 'product/index.html', context=context)


def get_ps1_games(request):
    header_text = str('Playstation 1 ')
    return get_videogames_for_console(request, 6, header_text)


def get_ps2_games(request):
    header_text = str('Playstation 2 ')
    return get_videogames_for_console(request, 7, header_text)


def get_nintendo_nes_games(request):
    header_text = str('Nintendo NES ')
    return get_videogames_for_console(request, 2, header_text)


def get_nintendo_64_games(request):
    header_text = str('Nintendo 64 ')
    return get_videogames_for_console(request, 3, header_text)


def get_gameboy_advance_games(request):
    header_text = str('GameBoy Advance ')
    return get_videogames_for_console(request, 5, header_text)


def get_gameboy_color_games(request):
    header_text = str('GameBoy Color ')
    return get_videogames_for_console(request, 4, header_text)


# Get videogames filtered by genre

# Main function that gets genreid and returns
# videogames by genre
def get_videogames_by_genreid(request, genreid, header_text):
    user = request.user
    videogames = Product.objects.filter(videogamehasgenre__genre_id=genreid)
    if user.is_authenticated:
        context = build_context(user)
        context['products'] = videogames
    else:
        context = {'products': videogames}
    context['product_type_id'] = 2
    context['header_text'] = header_text
    context['show_sort'] = True
    return render(request, 'product/index.html', context=context)


def get_action_videogames(request):
    header_text = str('Action ')
    return get_videogames_by_genreid(request, 1, header_text)


def get_adventure_videogames(request):
    header_text = str('Adventure ')
    return get_videogames_by_genreid(request, 2, header_text)


def get_puzzle_videogames(request):
    header_text = str('Puzzle ')
    return get_videogames_by_genreid(request, 4, header_text)


def get_sport_videogames(request):
    header_text = str('Sport ')
    return get_videogames_by_genreid(request, 5, header_text)


def get_tacticalshooter_videogames(request):
    header_text = str('Tactical Shooter ')
    return get_videogames_by_genreid(request, 6, header_text)


def get_roleplaying_videogames(request):
    header_text = str('Roleplaying ')
    return get_videogames_by_genreid(request, 7, header_text)


def get_racing_videogames(request):
    header_text = str('Racing ')
    return get_videogames_by_genreid(request, 3, header_text)


def get_platforming_videogames(request):
    header_text = str('Platforming ')
    return get_videogames_by_genreid(request, 8, header_text)


def get_fighting_videogames(request):
    header_text = str('Fighting ')
    return get_videogames_by_genreid(request, 9, header_text)
    #return render(request, 'product/index.html', context=context)


# Get all videgames sorted by price and name
def get_videogames_sorted(request, orderby, text):
    user = request.user
    videogames = Product.objects.filter(type_id=2).order_by(orderby)
    if user.is_authenticated:
        context = build_context(user)
        context['products'] = videogames
    else:
        context = {'products': videogames}
    context['product_type_id'] = 2
    context['show_sort'] = True
    context['sort_text'] = 'Sorted by ' + text
    return render(request, 'product/index.html', context=context)


def get_videogames_price_sorted_asc(request):
    orderby = str('price')
    text = 'price low to high'
    return get_videogames_sorted(request, orderby, text)


def get_videogames_price_sorted_desc(request):
    orderby = str('-price')
    text = 'price high to low'
    return get_videogames_sorted(request, orderby, text)


def get_videogames_sorted_by_name(request):
    orderby = str('name')
    text = 'name'
    return get_videogames_sorted(request, orderby, text)


# Get videogame category sorted by price and name

#def get_vg_by_playstation_sorted_by_price_acs(request):
#    user = request.user
#    playstation1 = Product.objects.filter(type_id=2, console_id=6)
#    playstation2 = Product.objects.filter(type_id=2, console_id=7)
#    videogames = playstation1.union(playstation2).order_by('price')
#    if user.is_authenticated:
#        context = build_context(user)
#        context['products'] = videogames
#    else:
#        context = {'products': videogames}
#    context['product_type_id'] = 2
#    context['header_text'] = str('Playstation ')
#    context['orderby'] = str('playstation')
#    return render(request, 'product/index.html', context=context)