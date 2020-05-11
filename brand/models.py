from django.db import models

# Create your models here.


class Brand(models.Model):
    name = models.CharField(max_length=255)
    logo = models.CharField(max_length=999)
    website = models.CharField(max_length=999, blank=True, null=True)
