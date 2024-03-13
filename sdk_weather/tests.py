from django.conf import settings
from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from sdk_weather.models import Weather
from sdk_weather.services import get_weather


class TestSdkWeather(TestCase):

    def setUp(self):
        self.api_key = settings.WEATHER_API_KEY_1
        self.city = 'Bures-sur-Yvette'
        self.weather = Weather.objects.create(
            main="Clouds",
            description="overcast clouds",
            temp=52.29,
            feels_like=51.64,
            visibility=6000,
            speed=4.61,
            datetime="2024-03-13T00:00:04+01:00",
            sunrise="2024-03-13T06:08:18+01:00",
            sunset="2024-03-13T17:53:16+01:00",
            timezone=3600,
            name="Bures-sur-Yvette"
        )

    def test_get_weather(self):
        data = get_weather(self.city, api_key_1=self.api_key)

        self.assertEqual(data.get("name"), 'Bures-sur-Yvette')

    def test_WeatherListAPIView(self):
        response = self.client.get(
            reverse('sdk_weather:weather-list')
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_WeatherCreateAPIView(self):
        self.new_city = {
            "city": 'Barcelona'
        }

        response = self.client.post(
            reverse('sdk_weather:weather-create'),
            self.new_city
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )
