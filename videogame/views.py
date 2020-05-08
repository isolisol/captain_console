from django.shortcuts import render
from videogame.models import VideoGame


# Create your views here.
def index(request):
    videogames = {'videogames': VideoGame.objects.all().order_by('name')}
    return render(request, 'videogame/index.html', context=videogames)
