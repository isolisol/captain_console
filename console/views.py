from django.shortcuts import render, get_object_or_404
from accessory.models import Product


# Create your views here.
def index(request):
    consoles = {'consoles': Product.objects.filter(type_id=1).order_by('name')}
    return render(request, 'console/index.html', context=consoles)

def get_console_by_id(request,id):
    return render(request, 'console/console_detail.html', context={
        'console': get_object_or_404(Product, pk=id)
    })


def get_playstation_consoles(request):
    playstation1 = Product.objects.filter(id=6)
    playstation2 = Product.objects.filter(id=7)
    consoles = {'consoles': playstation1.union(playstation2)}
    return render(request, 'console/index.html', consoles)

def get_nintendo_consoles(request):
    nintendo_nes = Product.objects.filter(id=2)
    nintendo64 = Product.objects.filter(id=3)
    consoles = {'consoles': nintendo_nes.union(nintendo64)}
    return render(request, 'console/index.html', consoles)

def get_xbox_consoles(request):
    consoles = {'consoles': Product.objects.filter(id=8)}
    return render(request, 'console/index.html', consoles)

def get_gameboy_consoles(request):
    gameboycolor = Product.objects.filter(id=4)
    gameboyadvance = Product.objects.filter(id=5)
    consoles = {'consoles': gameboycolor.union(gameboyadvance)}
    return render(request, 'console/index.html', consoles)

def get_ps1_consoles(request):
    consoles = {'consoles': Product.objects.filter(id=6)}
    return render(request, 'console/index.html', consoles)

def get_ps2_consoles(request):
    consoles = {'consoles': Product.objects.filter(id=7)}
    return render(request, 'console/index.html', consoles)

def get_nintendo_nes_consoles(request):
    consoles = {'consoles': Product.objects.filter(id=2)}
    return render(request, 'console/index.html', consoles)

def get_nintendo_64_consoles(request):
    consoles = {'consoles': Product.objects.filter(id=3)}
    return render(request, 'console/index.html', consoles)

def get_gameboy_color_consoles(request):
    consoles = {'consoles': Product.objects.filter(id=4)}
    return render(request, 'console/index.html', consoles)

def get_gameboy_advance_consoles(request):
    consoles = {'consoles': Product.objects.filter(id=5)}
    return render(request, 'console/index.html', consoles)