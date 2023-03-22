from playwright.sync_api import Browser, Page, sync_playwright
from progressbar import progressbar

from app.services.gas_stations import parse_gas_stations_xls
from gs_parser import settings
from gs_parser.log import log


def start_interacting():
    with sync_playwright() as sp:
        browser = sp.chromium.launch(headless=False)
        main_page = _open_rss_page(browser)
        log.debug('Opened rss.tatneft.ru page.')
        _start_clicking_buttons(main_page)
        get_gas_stations_xls_and_parse(browser)
        browser.close()


def _open_rss_page(browser: Browser, *paths: str) -> Page:
    page = browser.new_page()
    parsed_paths = '/'.join(paths)
    page.goto(f'https://rss.tatneft.ru/{parsed_paths}')
    return page


def _start_clicking_buttons(page: Page) -> None:
    """Начинает нажатие на кнопки из меню сайта rss.tatneft.ru"""
    buttons_alts = [button.get_attribute('alt') for button
                    in page.query_selector_all('.cufon-canvas')]
    for alt in progressbar(buttons_alts[2:]):
        button = page.get_by_alt_text(alt)  # type: ignore
        button.click(delay=settings.CLICKING_DELAY * 1000)
    log.debug('All buttons was clicked.')
    page.close()


def get_gas_stations_xls_and_parse(browser) -> None:
    _get_gas_stations_xls(browser)
    parse_gas_stations_xls()


def _get_gas_stations_xls(browser: Browser) -> None:
    """Переходит на страницу со списком АЗС и скачивает эксель-файл"""
    gas_stations_page = _open_rss_page(browser, 'locator', 'list')
    _download_gas_stations_xls(gas_stations_page)


def _download_gas_stations_xls(gs_page: Page) -> None:
    with gs_page.expect_download() as download_info:
        gs_page.locator('.btn').click()
    download = download_info.value
    download.save_as(settings.XLS_PATH)
