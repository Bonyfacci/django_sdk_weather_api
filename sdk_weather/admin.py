from django.contrib import admin

from sdk_weather.models import Weather


@admin.register(Weather)
class WeatherAdmin(admin.ModelAdmin):
    ...
