from django.db import models

# Create your models here.
class Item(models.Model):
    type = models.CharField(max_length=100)
    quantity = models.IntegerField()
    brand = models.CharField(max_length=100)