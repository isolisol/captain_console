from django.shortcuts import render, get_object_or_404
from accessory.models import Product
from helperServices.helpers import build_context


# Create your views here.
def index(request):
    user = request.user
    if user.is_authenticated:
        context = build_context(user)
        context['videogames'] = Product.objects.filter(type_id=2).order_by('name')
    else:
        context = {'videogames': Product.objects.filter(type_id=2).order_by('name')}
    return render(request, 'videogame/index.html', context=context)


def get_videogame_by_id(request, id):
    user = request.user
    if user.is_authenticated:
        context = build_context(user)
        context['videogame']: get_object_or_404(Product, pk=id)
    else:
        context = {'videogame': get_object_or_404(Product, pk=id)}
    return render(request, 'videogame/videogame_detail.html', context=context)


def get_videogames_by_playstation(request):
    playstation1 = Product.objects.filter(type_id=2, console_id=6)
    playstation2 = Product.objects.filter(type_id=2, console_id=7)
    videogames = {'videogames': playstation1.union(playstation2)}
    return render(request, 'videogame/index.html', videogames)


def get_videogames_by_nintendo(request):
    nintendo_nes = Product.objects.filter(type_id=2, console_id=2)
    nintendo64 = Product.objects.filter(type_id=2, console_id=3)
    videogames = {'videogames': nintendo_nes.union(nintendo64)}
    return render(request, 'videogame/index.html', videogames)


def get_videogames_by_xbox(request):
    videogames = {'videogames': Product.objects.filter(type_id=2, console_id=8)}
    return render(request, 'videogame/index.html', videogames)


def get_videogames_by_gameboy(request):
    gameboycolor = Product.objects.filter(type_id=2, console_id=5)
    gameboyadvance = Product.objects.filter(type_id=2, console_id=4)
    videogames = {'videogames': gameboycolor.union(gameboyadvance)}
    return render(request, 'videogame/index.html', videogames)

def get_ps1_games(request):
    videogames = {'videogames': Product.objects.filter(type_id=2, console_id=6)}
    return render(request, 'videogame/index.html', videogames)

def get_ps2_games(request):
    videogames = {'videogames': Product.objects.filter(type_id=2, console_id=7)}
    return render(request, 'videogame/index.html', videogames)

def get_nintendo_nes_games(request):
    videogames = {'videogames': Product.objects.filter(type_id=2, console_id=2)}
    return render(request, 'videogame/index.html', videogames)

def get_nintendo_64_games(request):
    videogames = {'videogames': Product.objects.filter(type_id=2, console_id=3)}
    return render(request, 'videogame/index.html', videogames)

def get_gameboy_advance_games(request):
    videogames = {'videogames': Product.objects.filter(type_id=2, console_id=5)}
    return render(request, 'videogame/index.html', videogames)

def get_gameboy_color_games(request):
    videogames = {'videogames': Product.objects.filter(type_id=2, console_id=4)}
    return render(request, 'videogame/index.html', videogames)