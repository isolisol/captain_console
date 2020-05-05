from django.db import models
from brand.models import Brand


class Type(models.Model):
    name = models.CharField(max_length=255)


class Genre(models.Model):
    name = models.CharField(max_length=255)


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    releaseDate = models.DateField()
    ageLimit = models.IntegerField(blank=True)
    description = models.CharField(max_length=999, blank=True)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, blank=True)
