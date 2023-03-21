from django.core.management.base import BaseCommand

from app.services.pw import start_interacting


class Command(BaseCommand):
    """Команда для запуска программы парсинга сайта rss.tatneft.ru"""

    help = 'command for starting parsing program'

    def handle(self, *args, **kwargs):
        self.stdout.write('I started!')
        start_interacting()
