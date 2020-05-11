from django.db import models
from brand.models import Brand
from accessory.models import Product


class Genre(models.Model):
    name = models.CharField(max_length=255)


class VideoGameHasGenre(models.Model):
    video_game = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)
