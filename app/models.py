from django.db import models

class Pharmacy(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

class Medicine(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    in_stock = models.IntegerField()
    pharmacy = models.ForeignKey(Pharmacy, on_delete=models.CASCADE)
