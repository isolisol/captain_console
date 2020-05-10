from django.shortcuts import render

# Create your views here.
def cart_details(request):
    return render(request, 'order/cart_details.html')