from django.shortcuts import render
#from videogame.models import VideoGame


# Create your views here.
def index(request):
    videogames = [
        {'name': 'GTA', 'price': '5.99$'},
        {'name': 'Pokemon', 'price': '4.99$'}
    ]
    # {'videogames': VideoGame.objects.all().order_by('name')}
    return render(request, 'videogame/index.html', context={'videogames': videogames})
