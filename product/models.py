from django.db import models
from console.models import Console
from videogame.models import VideoGame
from accessory.models import Accessory


class Type(models.Model):
    name = models.CharField(max_length=255)


class Product(models.Model):
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    console = models.ForeignKey(Console, on_delete=models.CASCADE, null=True)
    videogame = models.ForeignKey(VideoGame, on_delete=models.CASCADE, null=True)
    accessory = models.ForeignKey(Accessory, on_delete=models.CASCADE, null=True)
