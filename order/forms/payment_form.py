from django.forms import ModelForm, widgets
from order.models import Payment


class PaymentForm(ModelForm):
    class Meta:

        MONTHS = [
            ('', 'month of expiration'),
            ('January', '01 January'),
            ('February', '02 Februrary'),
            ('March', '03 March'),
            ('April', '04 April'),
            ('May', '05 May'),
            ('June', '06 June'),
            ('July', '07 July'),
            ('August', '08 August'),
            ('September', '09 September'),
            ('October', '10 October'),
            ('November', '11 November'),
            ('December', '12 December')
        ]

        YEARS = [
            ('', 'year of expiration'),
            ('2020', '20'),
            ('2021', '21'),
            ('2022', '22'),
            ('2023', '23'),
            ('2024', '24'),
            ('2025', '25'),
            ('2026', '26'),
            ('2027', '27')
        ]

        #TODO: Taka út MONTHS og YEARS ef við ætlum ekki að nota það

        model = Payment
        fields = ['cardholder_name', 'card_number','exp_date', 'cvv', 'address', 'house_number', 'country', 'city', 'postal_code']
        widgets = {
            'cardholder_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'card_number': widgets.NumberInput(attrs={'class': 'form-control'}),
            'exp_date': widgets.TextInput(attrs={'class': 'form-control'}),
            'cvv': widgets.NumberInput(attrs={'class': 'form-control'}),
            'address': widgets.TextInput(attrs={'class': 'form-control'}),
            'house_number': widgets.TextInput(attrs={'class': 'form-control'}),
            'country': widgets.Select(attrs={'class': 'form-control'}),
            'city': widgets.TextInput(attrs={'class': 'form-control'}),
            'postal_code': widgets.TextInput(attrs={'class': 'form-control'}),
        }