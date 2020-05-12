from django.contrib.auth.models import User
from django.db import models
from django_countries.fields import CountryField


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
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    image = models.CharField(max_length=999, null=True)
    phone_number = models.IntegerField(null=True)


