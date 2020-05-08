from django.shortcuts import render, get_object_or_404
from videogame.models import VideoGame


# Create your views here.
def index(request):
    videogames = {'videogames': VideoGame.objects.all().order_by('name')}
    return render(request, 'videogame/index.html', context=videogames)


def get_videogame_by_id(request, id):
    return render(request, 'videogame/videogame_detail.html', context={
        'videogame': get_object_or_404(VideoGame, pk=id)
    })
