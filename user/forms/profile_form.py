from django.forms import ModelForm, widgets
from user.models import Profile
from django.contrib.auth.models import User


class ProfileForm(ModelForm):
    class Meta:
        model = User
        exclude = ['id', 'is_superuser', 'is_staff', 'is_active']
        widgets = {
            'username': widgets.TextInput(attrs={'class': 'form-control'})
        }

    class Meta:
        model = Profile
        exclude = ['id', 'user']
        widgets = {
            'address': widgets.TextInput(attrs={'class': 'form-control'}),
            'house_number': widgets.TextInput(attrs={'class': 'form-control'}),
            'city': widgets.Select(attrs={'class': 'form-control'}),
            'phone_number': widgets.TextInput(attrs={'class': 'form-control'}),
            'image': widgets.TextInput(attrs={'class': 'form-control'})
        }
