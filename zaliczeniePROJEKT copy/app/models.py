from django.db import models

class Vehicle(models.Model):
    name = models.CharField(max_length=50)
    fuel_consumption = models.FloatField()  # w litrach na 100 km
    fuel_tank_capacity = models.FloatField()  # w litrach

class Route(models.Model):
    length = models.FloatField()  # długość trasy w km
# Create your models here.