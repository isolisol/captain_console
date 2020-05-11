from django.shortcuts import render, get_object_or_404
from accessory.models import Product
from helper_services.helpers import build_context


def index(request):
    user = request.user
    consoles = Product.objects.filter(type_id=1).order_by('name')
    if user.is_authenticated:
        context = build_context(user)
        context['products'] = consoles
    else:
        context = {'products': consoles}
    return render(request, 'product/index.html', context=context)


def get_console_by_id(request,id):
    user = request.user
    console = get_object_or_404(Product, pk=id)
    if user.is_authenticated:
        context = build_context(user)
        context['product'] = console
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
    return render(request, 'product/index.html', context=context)


def get_xbox_consoles(request):
    user = request.user
    consoles = Product.objects.filter(id=8)
    if user.is_authenticated:
        context = build_context(user)
        context['products'] = consoles
    else:
        context = {'products': consoles}
    return render(request, 'product/index.html', context=context)


def get_ps1_consoles(request):
    user = request.user
    consoles = Product.objects.filter(id=6)
    if user.is_authenticated:
        context = build_context(user)
        context['products'] = consoles
    else:
        context = {'products': consoles}
    return render(request, 'product/index.html', context=context)


def get_ps2_consoles(request):
    user = request.user
    consoles = Product.objects.filter(id=7)
    if user.is_authenticated:
        context = build_context(user)
        context['products'] = consoles
    else:
        context = {'products': consoles}
    return render(request, 'product/index.html', context=context)


def get_nintendo_nes_consoles(request):
    user = request.user
    consoles = Product.objects.filter(id=2)
    if user.is_authenticated:
        context = build_context(user)
        context['products'] = consoles
    else:
        context = {'products': consoles}
    return render(request, 'product/index.html', context=context)


def get_nintendo_64_consoles(request):
    user = request.user
    consoles = Product.objects.filter(id=3)
    if user.is_authenticated:
        context = build_context(user)
        context['products'] = consoles
    else:
        context = {'products': consoles}
    return render(request, 'product/index.html', context=context)


def get_gameboy_color_consoles(request):
    user = request.user
    consoles = Product.objects.filter(id=4)
    if user.is_authenticated:
        context = build_context(user)
        context['products'] = consoles
    else:
        context = {'products': consoles}
    return render(request, 'product/index.html', context=context)


def get_gameboy_advance_consoles(request):
    user = request.user
    consoles = Product.objects.filter(id=5)
    if user.is_authenticated:
        context = build_context(user)
        context['products'] = consoles
    else:
        context = {'products': consoles}
    return render(request, 'product/index.html', context=context)