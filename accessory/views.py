from django.shortcuts import render
from accessory.models import Accessory


# Create your views here.
def index(request):
    accessories = {'accessories': Accessory.objects.all().order_by('name')}
    return render(request, 'accessory/index.html', context=accessories)
