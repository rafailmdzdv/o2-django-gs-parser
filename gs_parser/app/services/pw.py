from playwright.sync_api import Browser, Page, sync_playwright

from gs_parser.settings import CLICKING_DELAY


def start_interacting():
    with sync_playwright() as sp:
        browser = sp.chromium.launch(headless=False)
        page = _open_rss_page(browser)
        _start_clicking_buttons(page)
        browser.close()


def _open_rss_page(browser: Browser) -> Page:
    page = browser.new_page()
    page.goto('https://rss.tatneft.ru')
    return page


def _start_clicking_buttons(page: Page) -> None:
    buttons_alts = [button.get_attribute('alt') for button
                    in page.query_selector_all('.cufon-canvas')]
    for alt in buttons_alts[2:]:
        button = page.get_by_alt_text(alt)  # type: ignore
        button.click(delay=CLICKING_DELAY * 1000)
