from datetime import datetime

import requests
from django.conf import settings
from django.utils import timezone
from rest_framework import serializers


def get_weather(city, api_key_1=settings.WEATHER_API_KEY_1, api_key_2=settings.WEATHER_API_KEY_2):
    if api_key_1 == api_key_2:
        raise ValueError('Ваши api keys одинаковые')

    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": {city},
        "units": "imperial",
        "appid": {api_key_1}
    }
    data = requests.get(url, params=params).json()

    if data.get('cod') == '404':
        raise serializers.ValidationError("City not found", code=404)

    info = {
        "main": data['weather'][0]['main'],
        "description": data['weather'][0]['description'],
        "temp": data['main']['temp'],
        "feels_like": data['main']['feels_like'],
        "visibility": data['visibility'],
        "speed": data['wind']['speed'],
        "datetime": timezone.make_aware(datetime.utcfromtimestamp(data['dt']).replace(microsecond=0)),
        "sunrise": timezone.make_aware(datetime.utcfromtimestamp(data['sys']['sunrise']).replace(microsecond=0)),
        "sunset": timezone.make_aware(datetime.utcfromtimestamp(data['sys']['sunset']).replace(microsecond=0)),
        "timezone": data['timezone'],
        "name": data['name'],
    }

    return info
