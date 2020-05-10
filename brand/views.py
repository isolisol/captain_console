from django.shortcuts import render
from videogame.models import Brand

# Create your views here.
def index(request):
    brands = {'brands': Brand.objects.all().order_by('name')}
    return render(request, 'brand/index.html', context=brands)
