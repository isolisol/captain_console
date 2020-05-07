from django.db import models
from brand.models import Brand
from console.models import Console
# Create your models here.


class Accessory(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.CharField(max_length=999)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    image = models.CharField(max_length=999)
    console = models.ForeignKey(Console, on_delete=models.SET_NULL, null=True)