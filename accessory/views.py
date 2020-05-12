from django.shortcuts import render, get_object_or_404, redirect
from accessory.models import Product
from order.models import Cart, ProductInCart
from helper_services.helpers import build_context


def a_add_to_cart(request, product_id):
    user = request.user
    product = get_object_or_404(Product, pk=product_id)
    cart, created = Cart.objects.get_or_create(user_id=user.id, complete=False)
    cart_add, created = ProductInCart.objects.get_or_create(product_id=product.id, cart_id=cart.id)
    if not created:
        cart_add.quantity += 1
        cart_add.save()
    return redirect('cart_details')


def index(request):
    user = request.user
    if user.is_authenticated:
        context = build_context(user)
        context['products'] = Product.objects.filter(type_id=3).order_by('name')
    else:
        context = {'products': Product.objects.filter(type_id=3).order_by('name')}
    context['product_type_id'] = 3
    return render(request, 'product/index.html', context=context)


def get_accessory_by_id(request,id):
    user = request.user
    if user.is_authenticated:
        context = build_context(user)
        context['product'] = get_object_or_404(Product, pk=id)
    else:
        context = {'product': get_object_or_404(Product, pk=id)}
    return render(request, 'product/product_details.html', context=context)


def get_playstation_accessories(request):
    user = request.user
    playstation1 = Product.objects.filter(type_id=3, console_id=6)
    playstation2 = Product.objects.filter(type_id=3, console_id=7)
    accessories = playstation1.union(playstation2)
    if user.is_authenticated:
        context = build_context(user)
        context['products'] = accessories
    else:
        context = {'products': accessories}
    context['product_type_id'] = 3
    return render(request, 'product/index.html', context=context)


def get_nintendo_accessories(request):
    user = request.user
    nintendo_nes = Product.objects.filter(type_id=3, console_id=2)
    nintendo64 = Product.objects.filter(type_id=3, console_id=3)
    gameboy_color = Product.objects.filter(type_id=3, console_id=4)
    gameboy_advance = Product.objects.filter(type_id=3, console_id=5)
    accessories = nintendo_nes.union(nintendo64, gameboy_color, gameboy_advance)
    if user.is_authenticated:
        context = build_context(user)
        context['products'] = accessories
    else:
        context = {'products': accessories}
    context['product_type_id'] = 3
    return render(request, 'product/index.html', context=context)


def get_xbox_accessories(request):
    user = request.user
    if user.is_authenticated:
        context = build_context(user)
        context['products'] = Product.objects.filter(type_id=3, console_id=8)
    else:
        context = {'products': Product.objects.filter(type_id=3, console_id=8)}
    context['product_type_id'] = 3
    return render(request, 'product/index.html', context=context)


def get_ps1_accessories(request):
    user = request.user
    if user.is_authenticated:
        context = build_context(user)
        context['products'] = Product.objects.filter(type_id=3, console_id=6)
    else:
        context = {'products': Product.objects.filter(type_id=3, console_id=6)}
    context['product_type_id'] = 3
    return render(request, 'product/index.html', context=context)


def get_ps2_accessories(request):
    user = request.user
    if user.is_authenticated:
        context = build_context(user)
        context['products'] = Product.objects.filter(type_id=3, console_id=7)
    else:
        context = {'products': Product.objects.filter(type_id=3, console_id=7)}
    context['product_type_id'] = 3
    return render(request, 'product/index.html', context=context)


def get_nintendo_nes_accessories(request):
    user = request.user
    if user.is_authenticated:
        context = build_context(user)
        context['products'] = Product.objects.filter(type_id=3, console_id=2)
    else:
        context = {'products': Product.objects.filter(type_id=3, console_id=2)}
    context['product_type_id'] = 3
    return render(request, 'product/index.html', context=context)


def get_nintendo_64_accessories(request):
    user = request.user
    if user.is_authenticated:
        context = build_context(user)
        context['products'] = Product.objects.filter(type_id=3, console_id=3)
    else:
        context = {'products': Product.objects.filter(type_id=3, console_id=3)}
    context['product_type_id'] = 3
    return render(request, 'product/index.html', context=context)


def get_gameboy_advance_accessories(request):
    user = request.user
    if user.is_authenticated:
        context = build_context(user)
        context['products'] = Product.objects.filter(type_id=3, console_id=5)
    else:
        context = {'products': Product.objects.filter(type_id=3, console_id=5)}
    context['product_type_id'] = 3
    return render(request, 'product/index.html', context=context)


def get_gameboy_color_accessories(request):
    user = request.user
    if user.is_authenticated:
        context = build_context(user)
        context['products'] = Product.objects.filter(type_id=3, console_id=4)
    else:
        context = {'products': Product.objects.filter(type_id=3, console_id=4)}
    context['product_type_id'] = 3
    return render(request, 'product/index.html', context=context)


def get_other_accessories(request):
    user = request.user
    if user.is_authenticated:
        context = build_context(user)
        context['products'] = Product.objects.filter(type_id=3, console_id=None)
    else:
        context = {'products': Product.objects.filter(type_id=3, console_id=None)}
    context['product_type_id'] = 3
    return render(request, 'product/index.html', context=context)


# Get videgames sorted by price
def get_accessories_price_sorted_asc(request):
    user = request.user
    videogames = Product.objects.filter(type_id=3).order_by('price')
    if user.is_authenticated:
        context = build_context(user)
        context['products'] = videogames
    else:
        context = {'products': videogames}
    context['product_type_id'] = 3
    return render(request, 'product/index.html', context=context)


def get_accessories_price_sorted_desc(request):
    user = request.user
    videogames = Product.objects.filter(type_id=3).order_by('-price')
    if user.is_authenticated:
        context = build_context(user)
        context['products'] = videogames
    else:
        context = {'products': videogames}
    context['product_type_id'] = 3
    return render(request, 'product/index.html', context=context)


def get_accessories_sorted_by_name(request):
    user = request.user
    videogames = Product.objects.filter(type_id=3).order_by('name')
    if user.is_authenticated:
        context = build_context(user)
        context['products'] = videogames
    else:
        context = {'products': videogames}
    context['product_type_id'] = 3
    return render(request, 'product/index.html', context=context)
