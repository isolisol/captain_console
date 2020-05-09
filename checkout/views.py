from django.shortcuts import render
#from videogame.models import Brand

# Create your views here.
def index(request):
    return render(request, 'checkout/index.html')
