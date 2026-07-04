import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture()
def page():
    playwright = sync_playwright().start()
    # Запуск браузера
    browser = playwright.chromium.launch()
    page = browser.new_page()

    yield page
    # Закрываем браузер
    browser.close()

    playwright.stop()
