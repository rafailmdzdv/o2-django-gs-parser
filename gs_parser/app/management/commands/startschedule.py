from django.core.management.base import BaseCommand

from app.services.schedule import start_montly_parse


class Command(BaseCommand):
    """Запускает ежемесячный парсинг"""

    help = 'starts monthly parsing'

    def handle(self, *args, **kwargs):
        self.stdout.write('Starting monthly parsing...')
        start_montly_parse()
