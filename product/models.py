from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=255)
    logo = models.CharField(max_length=999, blank=True)

    def get_image(self):
        return self.logo


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.CharField(max_length=999)
    release_date = models.DateField()
    image = models.CharField(max_length=999, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Console(Product):
    pass


class Genre(models.Model):
    name = models.CharField(max_length=255)


class AgeLimitImage(models.Model):
    image = models.CharField(max_length=999)


class VideoGame(Product):
    age_limit = models.IntegerField()
    console = models.ForeignKey(Console, on_delete=models.SET_NULL, null=True)


class Accessory(Product):
    pass


class ConsoleHasAccessory(models.Model):
    console = models.ForeignKey(Console, on_delete=models.CASCADE) #TODO: Skoða ondelete betur
    accessory = models.ForeignKey(Accessory, on_delete=models.CASCADE) #TODO: Skoða ondelete betur


#class ProductImage(models.Model):
    #image = models.CharField(max_length=999)
    #product = models.ForeignKey(Product, on_delete=models.CASCADE)
    #console = models.ForeignKey(Console, on_delete=models.CASCADE, null=True)
    #video_game = models.ForeignKey(VideoGame, on_delete=models.CASCADE, null=True)
    #accessory = models.ForeignKey(Accessory, on_delete=models.CASCADE, null=True)
