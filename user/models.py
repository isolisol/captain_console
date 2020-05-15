from django.contrib.auth.models import User
from django.db import models
from django_countries.fields import CountryField
from accessory.models import Product
from helper_services.validators import validate_number_input


# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=255)
    postal_code = models.IntegerField()

    class Meta:
        ordering = ['postal_code']

    def __str__(self):
        return '{}  {}'.format(self.postal_code, self.name)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = CountryField()
    address = models.CharField(max_length=255, null=True)
    house_number = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255, null=True)
    postal_code = models.CharField(max_length=10, null=True)
    image = models.CharField(max_length=999, null=True)
    phone_number = models.IntegerField(null=True, validators=[validate_number_input])
    product = models.ManyToManyField(Product, through='RecentlyViewed')


class RecentlyViewed(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    date = models.DateTimeField(null=True)


class Search(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    search_text = models.CharField(max_length=255)
    date = models.DateTimeField()
