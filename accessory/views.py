from django.shortcuts import render, get_object_or_404
from accessory.models import Product
from helper_services.helpers import build_context


# Create your views here.
def index(request):
    user = request.user
    if user.is_authenticated:
        context = build_context(user)
        context['accessories'] = Product.objects.filter(type_id=3).order_by('name')
    else:
        context = {'accessories': Product.objects.filter(type_id=3).order_by('name')}
    return render(request, 'accessory/index.html', context=context)


def get_accessory_by_id(request,id):
    user = request.user
    if user.is_authenticated:
        context = build_context(user)
        context['accessory'] = get_object_or_404(Product, pk=id)
    else:
        context = {'accessory': get_object_or_404(Product, pk=id)}
    return render(request, 'accessory/accessory_detail.html', context=context)


def get_playstation_accessories(request):
    user = request.user
    playstation1 = Product.objects.filter(type_id=3, console_id=6)
    playstation2 = Product.objects.filter(type_id=3, console_id=7)
    accessories = playstation1.union(playstation2)
    if user.is_authenticated:
        context = build_context(user)
        context['accessories'] = accessories
    else:
        context = {'accessories': accessories}
    return render(request, 'accessory/index.html', context=context)


def get_nintendo_accessories(request):
    user = request.user
    nintendo_nes = Product.objects.filter(type_id=3, console_id=2)
    nintendo64 = Product.objects.filter(type_id=3, console_id=3)
    accessories = nintendo_nes.union(nintendo64)
    if user.is_authenticated:
        context = build_context(user)
        context['accessories'] = accessories
    else:
        context = {'acessories': accessories}
    return render(request, 'accessory/index.html', context=context)


def get_xbox_accessories(request):
    user = request.user
    if user.is_authenticated:
        context = build_context(user)
        context['accessories'] = Product.objects.filter(type_id=3, console_id=8)
    else:
        context = {'accessories': Product.objects.filter(type_id=3, console_id=8)}
    return render(request, 'accessory/index.html', context=context)


def get_gameboy_accessories(request):
    user = request.user
    gameboycolor = Product.objects.filter(type_id=3, console_id=4)
    gameboyadvance = Product.objects.filter(type_id=3, console_id=5)
    accessories = gameboycolor.union(gameboyadvance)
    if user.is_authenticated:
        context = build_context(user)
        context['accessories'] = accessories
    else:
        context = accessories
    return render(request, 'accessory/index.html', context=context)


def get_ps1_accessories(request):
    user = request.user
    if user.is_authenticated:
        context = build_context(user)
        context['accessories'] = Product.objects.filter(type_id=3, console_id=6)
    else:
        context = {'accessories': Product.objects.filter(type_id=3, console_id=6)}
    return render(request, 'accessory/index.html', context=context)


def get_ps2_accessories(request):
    user = request.user
    if user.is_authenticated:
        context = build_context(user)
        context['accessories'] = Product.objects.filter(type_id=3, console_id=7)
    else:
        context = {'accessories': Product.objects.filter(type_id=3, console_id=7)}
    return render(request, 'accessory/index.html', context=context)


def get_nintendo_nes_accessories(request):
    user = request.user
    if user.is_authenticated:
        context = build_context(user)
        context['accessories'] = Product.objects.filter(type_id=3, console_id=2)
    else:
        context = {'accessories': Product.objects.filter(type_id=3, console_id=2)}
    return render(request, 'accessory/index.html', context=context)


def get_nintendo_64_accessories(request):
    user = request.user
    if user.is_authenticated:
        context = build_context(user)
        context['accessories'] = Product.objects.filter(type_id=3, console_id=3)
    else:
        context = {'accessories': Product.objects.filter(type_id=3, console_id=3)}
    return render(request, 'accessory/index.html', context=context)


def get_gameboy_advance_accessories(request):
    user = request.user
    if user.is_authenticated:
        context = build_context(user)
        context['accessories'] = Product.objects.filter(type_id=3, console_id=5)
    else:
        context = {'accessories': Product.objects.filter(type_id=3, console_id=5)}
    return render(request, 'accessory/index.html', context=context)


def get_gameboy_color_accessories(request):
    user = request.user
    if user.is_authenticated:
        context = build_context(user)
        context['accessories'] = Product.objects.filter(type_id=3, console_id=4)
    else:
        context = {'accessories': Product.objects.filter(type_id=3, console_id=4)}
    return render(request, 'accessory/index.html', context=context)


def get_other_accessories(request):
    user = request.user
    if user.is_authenticated:
        context = build_context(user)
        context['accessories'] = Product.objects.filter(type_id=3, console_id=None)
    else:
        context = {'accessories': Product.objects.filter(type_id=3, console_id=None)}
    return render(request, 'accessory/index.html', context=context)