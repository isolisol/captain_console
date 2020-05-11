from django.shortcuts import render, get_object_or_404
from accessory.models import Product


# Create your views here.
def index(request):
    accessories = {'accessories': Product.objects.filter(type_id=3).order_by('name')}
    return render(request, 'accessory/index.html', context=accessories)


def get_accessory_by_id(request,id):
    return render(request, 'accessory/accessory_detail.html', context={
        'accessory': get_object_or_404(Product, pk=id)
    })


def get_playstation_accessories(request):
    playstation1 = Product.objects.filter(type_id=3, console_id=6)
    playstation2 = Product.objects.filter(type_id=3, console_id=7)
    accessories = {'accessories': playstation1.union(playstation2)}
    return render(request, 'accessory/index.html', accessories)

def get_nintendo_accessories(request):
    nintendo_nes = Product.objects.filter(type_id=3, console_id=2)
    nintendo64 = Product.objects.filter(type_id=3, console_id=3)
    accessories = {'accessories': nintendo_nes.union(nintendo64)}
    return render(request, 'accessory/index.html', accessories)

def get_xbox_accessories(request):
    accessories = {'accessories': Product.objects.filter(type_id=3, console_id=8)}
    return render(request, 'accessory/index.html', accessories)

def get_gameboy_accessories(request):
    gameboycolor = Product.objects.filter(type_id=3, console_id=4)
    gameboyadvance = Product.objects.filter(type_id=3, console_id=5)
    accessories = {'accessories': gameboycolor.union(gameboyadvance)}
    return render(request, 'accessory/index.html', accessories)

def get_ps1_accessories(request):
    accessories = {'accessories': Product.objects.filter(type_id=3, console_id=6)}
    return render(request, 'accessory/index.html', accessories)

def get_ps2_accessories(request):
    accessories = {'accessories': Product.objects.filter(type_id=3, console_id=7)}
    return render(request, 'accessory/index.html', accessories)

def get_nintendo_nes_accessories(request):
    accessories = {'accessories': Product.objects.filter(type_id=3, console_id=2)}
    return render(request, 'accessory/index.html', accessories)

def get_nintendo_64_accessories(request):
    accessories = {'accessories': Product.objects.filter(type_id=3, console_id=3)}
    return render(request, 'accessory/index.html', accessories)

def get_gameboy_advance_accessories(request):
    accessories = {'accessories': Product.objects.filter(type_id=3, console_id=5)}
    return render(request, 'accessory/index.html', accessories)

def get_gameboy_color_accessories(request):
    accessories = {'accessories': Product.objects.filter(type_id=3, console_id=4)}
    return render(request, 'accessory/index.html', accessories)

def get_other_accessories(request):
    accessories = {'accessories': Product.objects.filter(type_id=3, console_id=None)}
    return render(request, 'accessory/index.html', accessories)