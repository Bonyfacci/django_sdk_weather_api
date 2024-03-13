import logging
import time

from django.core.management.base import BaseCommand
from django.db import IntegrityError

from sdk_weather.models import Weather
from sdk_weather.services import get_weather

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    """
    Команда для заполнения базы данных
    """

    def handle(self, *args, **options):

        cities = ["Барселона", "Bures-sur-Yvette", "Vancouver", "Paris", "Санкт-Петербург", "London"]

        for city in cities:
            data = get_weather(city)
            try:
                weather, created = Weather.objects.update_or_create(
                    name=data['name'],
                    defaults=data
                )
            except IntegrityError:
                weather = Weather.objects.create(**data)
            print(f'Прогноз погоды в городе {data.get("name")} записан в БД')
            time.sleep(1)

        logger.info(f"Информация по городам {' '.join(cities)} успешно сохранена в БД")
        print(f"Информация по городам {', '.join(cities)} успешно сохранена в БД")
