from django.db import models
from brand.models import Brand
# Create your models here.


class ProductType(models.Model):
    name = models.CharField(max_length=255)


class Product(models.Model):
    type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.CharField(max_length=999)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    image = models.CharField(max_length=999)
    release_date = models.DateField()
    age_limit = models.IntegerField(default=3)
    console = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
