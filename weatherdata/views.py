from django.shortcuts import render

import weatherdata
from .models import Geolocation
import requests
import math
import json

def index(request):
    geolocations = Geolocation.objects.all()
    data_to_display = []
    weather_to_display=[]
    for geolocation in geolocations:
        lat = geolocation.location.y
        lon = geolocation.location.x
        data = [lat,lon]
        data_to_display.append(data)
        url = 'https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid=2dd3b37103c89a12b8c4f3e8de6a2ae7'.format(round(lat,2),round(lon,2))
        data = requests.get(url).json()

        weatherdata = {
            'name':data['name'],
            'temperature':data['main']['temp'],
            'humidity':data['main']['humidity']
        }
        # json_data = data.text
        # loaded_json = json.loads(json_data)
        weather_to_display.append(weatherdata)

    print(type(data_to_display))
    print(weather_to_display)

    context = {'data_to_display':data_to_display,'weather_to_display':weather_to_display}
    return render(request,'weatherdata/index.html',context)