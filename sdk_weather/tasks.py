import datetime
import logging

from celery import shared_task

from sdk_weather.models import Weather
from sdk_weather.services import get_weather

logger = logging.getLogger(__name__)


@shared_task
def create_or_update_weather():
    current_time = datetime.datetime.now().strftime('%d-%m-%Y_%H-%M-%S')
    print(f'Время сервера: {current_time}')

    logger.info(f"Обновление прогноза погоды")

    all_cities = Weather.objects.all()

    for weather in all_cities:
        get_weather(weather.name)
        logger.info(f"Погода {weather.name} обновлена")

    logger.info(f"Данные успешно обновлены")
