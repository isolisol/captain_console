from django.shortcuts import render
#from .models import VideoGame

videoGames = [
    {'name': 'GTA', 'price': 20},
    {'name': 'Gran Turismo', 'price': 30}
]

# Create your views here.
def index(request):
    return render(request, 'product/index.html', context={
        'videoGames': videoGames
    })