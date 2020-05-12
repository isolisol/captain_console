from django.shortcuts import render
#from videogame.models import Brand


def index(request):
    return render(request, 'checkout/index.html')

def contact_info(request):
    pass