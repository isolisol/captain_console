from django.forms import ModelForm, widgets
from user.models import Profile
from django.contrib.auth.models import User


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'last_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'email': widgets.TextInput(attrs={'class': 'form-control'})
        }


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['id', 'user', 'image']
        widgets = {
            'address': widgets.TextInput(attrs={'class': 'form-control'}),
            'house_number': widgets.TextInput(attrs={'class': 'form-control'}),
            'city': widgets.Select(attrs={'class': 'form-control'}),
            'phone_number': widgets.TextInput(attrs={'class': 'form-control'}),
            'country': widgets.Select(attrs={'class': 'form-control'})
        }


class ProfileImageForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
        widgets = {
            'image': widgets.TextInput(attrs={'class': 'form-control'})
        }
