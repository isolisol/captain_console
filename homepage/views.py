from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'homepage/index.html')


def opening_hours(request):
    return render(request, 'homepage/opening_hours.html')