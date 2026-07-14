import pytest
from playwright.sync_api import sync_playwright

from config_reader import ConfigReader


@pytest.fixture()
def browser():
    config = ConfigReader()

    playwright = sync_playwright().start()

    browser = playwright.chromium.launch(
        channel=config.get("browser"),
        headless=config.get("headless"),
    )
    yield browser

    browser.close()
    playwright.stop()


@pytest.fixture()
def page(browser):
    page = browser.new_page()

    yield page

    page.close()
