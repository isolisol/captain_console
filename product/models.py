from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=255)
    logo = models.CharField(max_length=999, blank=True)


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.CharField(max_length=999)
    release_date = models.DateField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Console(Product):
    pass


class Genre(models.Model):
    name = models.CharField(max_length=255)


class VideoGame(Product):
    ageLimit = models.IntegerField()
    console = models.ForeignKey(Console, on_delete=models.SET_NULL, null=True)


class Accessory(Product):
    pass


class ConsoleHasAccessory(models.Model):
    console = models.ForeignKey(Console, on_delete=models.SET_NULL, null=True) #TODO: Skoða ondelete betur
    accessory = models.ForeignKey(Accessory, on_delete=models.SET_NULL, null=True) #TODO: Skoða ondelete betur

    
# class Products(models.Model):
#    name = models.CharField(max_length=255)
#    price = models.FloatField()
#    releaseDate = models.DateField()
#    ageLimit = models.IntegerField(blank=True)
#    description = models.CharField(max_length=999, blank=True)
#    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
#    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, blank=True)
