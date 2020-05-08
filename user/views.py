from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from user.models import Profile
from user.forms.profile_form import ProfileForm
from user.forms.profile_form import UserForm


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            print('virkar ekki')
    return render(request, 'user/register.html', {
        'form': UserCreationForm()
    })


def profile(request):
    profile = Profile.objects.filter(user=request.user).first()
    user = User.objects.filter(id=profile.id).first()
    user_profile = {
        'profile': profile,
        'user': user
    }
    return render(request, 'user/profile.html', context=user_profile)


def edit_profile(request):
    profile = Profile.objects.filter(user=request.user).first()
    user = User.objects.filter(id=profile.id).first()
    if request.method == 'POST':
        form1 = ProfileForm(instance=profile, data=request.POST)
        form2 = UserForm(instance=user, data=request.POST)
        if form1.is_valid() and form2.is_valid():
            profile = form1.save(commit=False)
            user = form2.save()
            profile.user = request.user
            profile.save()
            return redirect('profile')
    else:
        return render(request, 'user/edit_profile.html', {
            'form1': ProfileForm(instance=profile),
            'form2': UserForm(instance=user)
        })