from django.db import models
from brand.models import Brand
from accessory.models import Accessory


# Create your models here.
class Console(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.CharField(max_length=999)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True)
    release_date = models.DateField()
    image = models.CharField(max_length=999)


class ConsoleHasAccessory(models.Model):
    console = models.ForeignKey(Console, on_delete=models.SET_NULL, null=True)
    accessory = models.ForeignKey(Accessory, on_delete=models.SET_NULL, null=True)