from django.shortcuts import render
from product.models import VideoGame


# Create your views here.
def index(request):
    context = {'video_games': VideoGame.objects.all().order_by('name')}
    return render(request, 'product/index.html', context)
