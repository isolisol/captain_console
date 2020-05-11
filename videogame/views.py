from django.shortcuts import render, get_object_or_404
from accessory.models import Product
from helper_services.helpers import build_context


def index(request):
    user = request.user
    if user.is_authenticated:
        context = build_context(user)
        context['products'] = Product.objects.filter(type_id=2).order_by('name')
    else:
        context = {'products': Product.objects.filter(type_id=2).order_by('name')}
    context['product_type_id'] = 2
    return render(request, 'product/index.html', context=context)


def get_videogame_by_id(request, id):
    user = request.user
    videogame = get_object_or_404(Product, pk=id)
    if user.is_authenticated:
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
    return render(request, 'product/index.html', context=context)


def get_videogames_by_xbox(request):
    user = request.user
    if user.is_authenticated:
        context = build_context(user)
        context['products'] = Product.objects.filter(type_id=2, console_id=8)
    else:
        context = {'products': Product.objects.filter(type_id=2, console_id=8)}
    context['product_type_id'] = 2
    return render(request, 'product/index.html', context=context)


def get_ps1_games(request):
    user = request.user
    videogames = Product.objects.filter(type_id=2, console_id=6)
    if user.is_authenticated:
        context = build_context(user)
        context['products'] = videogames
    else:
        context = {'products': videogames}
    context['product_type_id'] = 2
    return render(request, 'product/index.html', context=context)


def get_ps2_games(request):
    user = request.user
    videogames = Product.objects.filter(type_id=2, console_id=7)
    if user.is_authenticated:
        context = build_context(user)
        context['products'] = videogames
    else:
        context = {'products': videogames}
    context['product_type_id'] = 2
    return render(request, 'product/index.html', context=context)


def get_nintendo_nes_games(request):
    user = request.user
    videogames = Product.objects.filter(type_id=2, console_id=2)
    if user.is_authenticated:
        context = build_context(user)
        context['products'] = videogames
    else:
        context = {'products': videogames}
    context['product_type_id'] = 2
    return render(request, 'product/index.html', context=context)


def get_nintendo_64_games(request):
    user = request.user
    videogames = Product.objects.filter(type_id=2, console_id=3)
    if user.is_authenticated:
        context = build_context(user)
        context['products'] = videogames
    else:
        context = {'products': videogames}
    context['product_type_id'] = 2
    return render(request, 'product/index.html', context=context)


def get_gameboy_advance_games(request):
    user = request.user
    videogames = Product.objects.filter(type_id=2, console_id=5)
    if user.is_authenticated:
        context = build_context(user)
        context['products'] = videogames
    else:
        context = {'products': videogames}
    context['product_type_id'] = 2
    return render(request, 'product/index.html', context=context)


def get_gameboy_color_games(request):
    user = request.user
    videogames = Product.objects.filter(type_id=2, console_id=4)
    if user.is_authenticated:
        context = build_context(user)
        context['products'] =videogames
    else:
        context = {'products': videogames}
    context['product_type_id'] = 2
    return render(request, 'product/index.html', context=context)