import time

from playwright.sync_api import sync_playwright
import schedule

from app.services.pw import get_gas_stations_xls_and_parse
from gs_parser.log import log


def start_montly_parse():
    with sync_playwright() as sp:
        browser = sp.chromium.launch()
        schedule.every(30).days.do(get_gas_stations_xls_and_parse, browser)
        log.debug(f'Next run at: {schedule.next_run()}')

    while True:
        schedule.run_pending()
        time.sleep(1)
