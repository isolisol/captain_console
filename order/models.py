from django.db import models
from django.contrib.auth.models import User
from accessory.models import Product
from datetime import date


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    complete = models.BooleanField(default=False)

    #@property
    #def total_price(self):
    #    product_prices = ProductInCart.objects.filter()
    #    total = 0
    #    for price, quantity in product_prices:
    #        total += (price * quantity)
    #   return total
    #   return self.user.first_name

    def __str__(self):
        return 'user name: {}, complete?: {}'.format(self.user.first_name, self.complete)


class ProductInCart(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()


class DeliveryMethod(models.Model):
    name = models.CharField(max_length=255)


class Order(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True)
    delivery_method = models.ForeignKey(DeliveryMethod, on_delete=models.CASCADE)
    date = models.DateField(default=date.today())
