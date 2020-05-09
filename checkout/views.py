from django.shortcuts import render



def check_out(request):
    return render(request, 'homepage/checkout.html')