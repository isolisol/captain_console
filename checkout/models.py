from django.db import models
from django_countries.fields import CountryField
from user.models import City


class Payment(models.Model):
    cardholder_name = models.CharField(max_length=255)
    # Billing address
    country = CountryField()
    address = models.CharField(max_length=255)
    house_number = models.CharField(max_length=255)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

