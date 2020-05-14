from django.contrib.auth.forms import UserCreationForm
from order.models import Order, Cart
from django.shortcuts import render, redirect
from user.models import Profile
from user.forms.profile_form import ProfileForm, UserForm, ProfileImageForm
from helper_services.helpers import build_context, calculateTotalPrice


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            profile = Profile.objects.create(user_id=user.id)
            return redirect('login')
        else:
            print('virkar ekki')
    return render(request, 'user/register.html', {
        'form': UserCreationForm()
    })


def past_orders(request):
    user = request.user
    context = build_context(user)
    completed_carts = tuple(Cart.objects.filter(user=user, complete=True).values_list('id'))
    context['orders'] = Order.objects.filter(cart_id__in=completed_carts)
    return render(request, 'user/past_orders.html', context)


def past_order(request, order_id):
    user = request.user
    context = build_context(user)
    order = Order.objects.get(id=order_id)
    context['order'] = order
    cart = order.cart
    context['cart_items'] = cart.productincart_set.all()
    return render(request, 'user/past_order.html', context)


def profile(request):
    user = request.user # User.objects.filter(id=profile.id).first()
    profile = Profile.objects.filter(user=user).first()
    context = build_context(user)
    context['profile'] = profile
    context['user'] = user
    user_profile = {
        'profile': profile,
        'user': user
    }
    return render(request, 'user/profile.html', context=context)


def edit_profile(request):
    user = request.user  # User.objects.filter(id=profile.id).first()
    profile = Profile.objects.filter(user=user).first()
    if request.method == 'POST':
        form1 = ProfileForm(instance=profile, data=request.POST)
        form2 = UserForm(instance=user, data=request.POST)
        if form1.is_valid() and form2.is_valid():
            profile = form1.save(commit=False)
            user = form2.save(commit=False)
            profile.user = request.user
            profile.save()
            user.save()
            return redirect('profile')
    else:
        return render(request, 'user/edit_profile.html', {
            'form1': ProfileForm(instance=profile),
            'form2': UserForm(instance=user)
        })


def edit_photo(request):
    profile = Profile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = ProfileImageForm(instance=profile, data=request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')
    else:
        return render(request, 'user/edit_image.html', {
            'form': ProfileImageForm(instance=profile)
        })


