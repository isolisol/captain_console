from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=255)
    postal_code = models.IntegerField()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255, null=True)
    house_number = models.CharField(max_length=255, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    image = models.CharField(max_length=999)
    phone_number = models.IntegerField()
