from django.shortcuts import render
from videogame.models import Brand
from helper_services.helpers import build_context

# Create your views here.
def index(request):
    user = request.user
    brands = Brand.objects.all().order_by('name')
    if user.is_authenticated:
        context = build_context(user)
        context['brands'] = brands
    else:
        context = None
    return render(request, 'brand/index.html', context=context)
