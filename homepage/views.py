from django.contrib.auth.models import User
from django.shortcuts import render
from helper_services.helpers import build_context

# Create your views here.



def index(request):
    user = request.user
    if user.is_authenticated:
        context = build_context(user)
    else:
        context = None
    return render(request, 'homepage/index.html', context=context)

def opening_hours(request):
    user = request.user
    if user.is_authenticated:
        context = build_context(user)
    else:
        context = None
    return render(request, 'homepage/opening_hours.html', context=context)


def about_us(request):
    user = request.user
    if user.is_authenticated:
        context = build_context(user)
    else:
        context = None
    return render(request, 'homepage/about_us.html', context=context)


def handler404(request, exception):
    user = request.user
    if user.is_authenticated:
        context = build_context(user)
    else:
        context = None
    return render(request, '404.html', context)


def handler500(request):
    user = request.user
    if user.is_authenticated:
        context = build_context(user)
    else:
        context = None
    return render(request, '500.html', context)