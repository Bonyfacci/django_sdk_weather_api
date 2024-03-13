from django.urls import path

from sdk_weather.apps import SdkWeatherConfig
from sdk_weather.views import WeatherCreateAPIView, WeatherListAPIView

app_name = SdkWeatherConfig.name

urlpatterns = [
    path('api/weather/all/', WeatherListAPIView.as_view(), name='weather-list'),
    path('api/weather/', WeatherCreateAPIView.as_view(), name='weather-create'),
]
