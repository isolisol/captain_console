from django.forms import ModelForm, widgets
from order.models import Payment
from django.contrib.auth.models import User


class PaymentForm(ModelForm):
    class Meta:
        model = Payment
        exclude = ['id', 'user']
        widgets = {
            'cardholder_first_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'cardholder_last_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'country': widgets.Select(attrs={'class': 'form-control'}),
            'address': widgets.TextInput(attrs={'class': 'form-control'}),
            'house_number': widgets.TextInput(attrs={'class': 'form-control'}),
            'city': widgets.TextInput(attrs={'class': 'form-control'}),
            'postal_code': widgets.TextInput(attrs={'class': 'form-control'}),
            'card_number': widgets.TextInput(attrs={'class': 'form-control'}),
            'expiration_date': widgets.TextInput(attrs={'class': 'form-control'}),
            'cvv': widgets.TextInput(attrs={'class': 'form-control'})
        }
