from playwright.sync_api import Browser, Page, sync_playwright

from gs_parser import settings


def start_interacting():
    with sync_playwright() as sp:
        browser = sp.chromium.launch(headless=False)
        main_page = _open_rss_page(browser)
        _start_clicking_buttons(main_page)
        _get_gas_stations_xls(browser)
        browser.close()


def _open_rss_page(browser: Browser, *paths: str) -> Page:
    page = browser.new_page()
    parsed_paths = '/'.join(paths)
    page.goto(f'https://rss.tatneft.ru/{parsed_paths}')
    return page


def _start_clicking_buttons(page: Page) -> None:
    buttons_alts = [button.get_attribute('alt') for button
                    in page.query_selector_all('.cufon-canvas')]
    for alt in buttons_alts[2:]:
        button = page.get_by_alt_text(alt)  # type: ignore
        button.click(delay=settings.CLICKING_DELAY * 1000)
    page.close()


def _get_gas_stations_xls(browser: Browser) -> None:
    gas_stations_page = _open_rss_page(browser, 'locator', 'list')
    _download_gas_stations_xls(gas_stations_page)


def _download_gas_stations_xls(gs_page: Page) -> None:
    with gs_page.expect_download() as download_info:
        gs_page.locator('.btn').click()
    download = download_info.value
    download.save_as(settings.XLS_PATH)
