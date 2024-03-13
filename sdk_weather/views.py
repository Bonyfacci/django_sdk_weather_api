from rest_framework import generics
from rest_framework.permissions import AllowAny

from sdk_weather.models import Weather
from sdk_weather.serializers import WeatherSerializer, WeatherListSerializer


class WeatherListAPIView(generics.ListAPIView):
    queryset = Weather.objects.all()
    serializer_class = WeatherListSerializer
    permission_classes = [AllowAny]


class WeatherCreateAPIView(generics.CreateAPIView):
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer
    permission_classes = [AllowAny]
