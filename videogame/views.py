from django.shortcuts import render, get_object_or_404
from accessory.models import Product


# Create your views here.
def index(request):
    videogames = {'videogames': Product.objects.all().order_by('name')}
    return render(request, 'videogame/index.html', context=videogames)


def get_videogame_by_id(request, id):
    return render(request, 'videogame/videogame_detail.html', context={
        'videogame': get_object_or_404(Product, pk=id)
    })
