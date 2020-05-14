from django.db import models
from django.contrib.auth.models import User
from accessory.models import Product
from django_countries.fields import CountryField


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    complete = models.BooleanField(default=False)
    product = models.ManyToManyField(Product, through='ProductInCart')

    def __str__(self):
        return 'user name: {}, complete: {}'.format(self.user.first_name, self.complete)


class ProductInCart(models.Model):
    quantity = models.IntegerField(default=1)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    cardholder_name = models.CharField(max_length=255)
    card_number = models.CharField(max_length=16)
    exp_date = models.CharField(max_length=5)
    cvv = models.CharField(max_length=4)
    # Billing address:
    country = CountryField()
    address = models.CharField(max_length=255)
    house_number = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=10)


class ContactInformation(models.Model):
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    country = CountryField(null=True)
    address = models.CharField(max_length=255, null=True)
    house_number = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255, null=True)
    postal_code = models.CharField(max_length=10, null=True)


class Order(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True)
    date = models.DateField()
    contact_info = models.ForeignKey(ContactInformation, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, null=True)
    order_number = models.IntegerField(null=True)
    total_price = models.FloatField(null=True)


class BestSellers(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    sold_how_often = models.IntegerField(null=True)
