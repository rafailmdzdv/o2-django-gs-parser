from django.core.management.base import BaseCommand

from app.services.pw import start_interacting
from app.services.gas_stations import parse_gas_stations_xls
from gs_parser.log import log


class Command(BaseCommand):
    """Команда для запуска программы парсинга сайта rss.tatneft.ru"""

    help = 'command for starting parsing program'

    def handle(self, *args, **kwargs):
        self.stdout.write('Starting interact with rss.tatneft.ru')
        while True:
            try:
                start_interacting()
                break
            except Exception as _ex:
                log.error(_ex)
