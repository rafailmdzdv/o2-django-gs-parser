from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Команда для запуска программы парсинга сайта rss.tatneft.ru"""

    help = 'Command for starting parsing program'

    def handle(self, *args, **kwargs):
        self.stdout.write('I started!')
