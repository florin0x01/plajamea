import logging
import time
import urllib.request
import json
from urllib.error import URLError


class WeatherController:
    cache = {}

    def __init__(self, api_key):
        self.api_key = api_key
        self.EXPIRY = 30

    def get_temp_for_city(self, city):
        if city in WeatherController.cache:
            print ("Cached for ", city)
            if time.time() - WeatherController.cache[city]['expiry'] <= 0 :
                return WeatherController.cache[city]
            else:
                print ("DELETING")
                del WeatherController.cache[city]
        url = f'http://api.weatherapi.com/v1/current.json?key={self.api_key}&q={city}&aqi=yes'
        resp = urllib.request.urlopen(url)
        weather_data_str = resp.read()
        weather_data = json.loads(weather_data_str)
        print ("NonCached for ", city)

        WeatherController.cache[city] = {
            'temp': weather_data['current']['temp_c'],
            'co': weather_data['current']['air_quality']['co'],
            'expiry': time.time() + self.EXPIRY
        }
        return WeatherController.cache[city]

