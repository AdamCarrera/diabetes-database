from django.db import models

# Create your models here.
class Insulin(models.Model):
    type = models.CharField(max_length=100)
    quantity = models.IntegerField()
    brand = models.CharField(max_length=100)

    def __str__(self) -> str:
       return self.brand 

class GlucoseMonitor(models.Model):
    type = models.CharField(max_length=100)
    quantity = models.IntegerField()

    def __str__(self) -> str:
        return self.type

class CareSupplies(models.Model):
    type = models.CharField(max_length=100)
    quantity = models.IntegerField()

    def __str__(self) -> str:
        return self.type