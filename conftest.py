import pytest
from playwright.sync_api import sync_playwright

from config_reader import ConfigReader


@pytest.fixture()
def page():
    config = ConfigReader()

    playwright = sync_playwright().start()

    browser = playwright.chromium.launch(
        channel=config.get("browser"),
        headless=config.get("headless"),
    )

    page = browser.new_page()

    yield page

    browser.close()
    playwright.stop()