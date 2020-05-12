from django.forms import ModelForm, widgets
from order.models import ContactInformation


class ContactInfoForm(ModelForm):
    class Meta:
        model = ContactInformation
        fields = ['first_name', 'last_name', 'address', 'house_number', 'country', 'city', 'postal_code']
        widgets = {
            'first_name': widgets.TextInput(attrs={'class': 'form-control'}, ),
            'last_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'address': widgets.TextInput(attrs={'class': 'form-control'}),
            'house_number': widgets.TextInput(attrs={'class': 'form-control'}),
            'country': widgets.Select(attrs={'class': 'form-control'}),
            'city': widgets.TextInput(attrs={'class': 'form-control'}),
            'postal_code': widgets.TextInput(attrs={'class': 'form-control'}),
        }
