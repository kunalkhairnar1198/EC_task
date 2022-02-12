from django.contrib.gis.db import models

# Create your models here.

class Geolocation(models.Model):
    name = models.CharField(max_length=100)
    location = models.PointField()