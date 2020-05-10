from django.shortcuts import render, get_object_or_404
from accessory.models import Product


# Create your views here.
def index(request):
    videogames = {'videogames': Product.objects.filter(type_id=2).order_by('name')}
    return render(request, 'videogame/index.html', context=videogames)


def get_videogame_by_id(request, id):
    return render(request, 'videogame/videogame_detail.html', context={
        'videogame': get_object_or_404(Product, pk=id)
    })

def get_videogames_by_playstation(request):
    playstation1 = Product.objects.filter(type_id=2, console_id=6)
    playstation2 = Product.objects.filter(type_id=2, console_id=7)
    videogames = {'videogames': playstation1.union(playstation2)}
    return render(request, 'videogame/videogame_brand.html', videogames)
