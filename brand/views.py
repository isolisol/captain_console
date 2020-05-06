from django.shortcuts import render
from product.models import Brand

# Create your views here.
def index(request):
    context = {'brands': Brand.objects.all().order_by('name')}
    return render(request, 'brand/index.html', context)
