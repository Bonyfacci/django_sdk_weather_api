from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class SdkWeatherConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sdk_weather'
    verbose_name = _('Current weather data')
