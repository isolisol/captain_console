from django.shortcuts import render, get_object_or_404
from accessory.models import Accessory


# Create your views here.
def index(request):
    accessories = {'accessories': Accessory.objects.all().order_by('name')}
    return render(request, 'accessory/index.html', context=accessories)


def get_accessory_by_id(request,id):
    return render(request, 'accessory/accessory_detail.html', context={
        'accessory': get_object_or_404(Accessory, pk=id)
    })