from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Geolocation

# Register your models here.

@admin.register(Geolocation)
class ShopAdmin(OSMGeoAdmin):
    list_display = ('name', 'location')