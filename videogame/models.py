from django.db import models
from brand.models import Brand
from console.models import Console


class Genre(models.Model):
    name = models.CharField(max_length=255)


class VideoGame(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.CharField(max_length=999)
    release_date = models.DateField()
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True)
    age_limit = models.IntegerField()
    image = models.CharField(max_length=999)
    console = models.ForeignKey(Console, on_delete=models.SET_NULL, null=True)


class VideoGameHasGenre(models.Model):
    video_game = models.ForeignKey(VideoGame, on_delete=models.SET_NULL, null=True)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)
