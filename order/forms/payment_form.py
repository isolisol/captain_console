from django.forms import ModelForm, widgets
from order.models import Payment


class PaymentForm(ModelForm):
    class Meta:
        model = Payment
        fields = ['cardholder_name', 'address', 'house_number', 'country', 'city', 'postal_code']
        widgets = {
            'cardholder_name': widgets.TextInput(attrs={'class': 'form-control'}, ),
            'address': widgets.TextInput(attrs={'class': 'form-control'}),
            'house_number': widgets.TextInput(attrs={'class': 'form-control'}),
            'country': widgets.Select(attrs={'class': 'form-control'}),
            'city': widgets.TextInput(attrs={'class': 'form-control'}),
            'postal_code': widgets.TextInput(attrs={'class': 'form-control'}),
        }