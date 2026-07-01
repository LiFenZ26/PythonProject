import pytest
from playwright.sync_api import sync_playwright
from faker import Faker

# URL тестируемого сайта
BASE_URL = "http://144.31.63.127:5000/"
# текст ошибки при неверном вводе данных
INVALID_LOGIN_ERROR = "Invalid login or password."


@pytest.fixture()
def page():
    with sync_playwright() as p:
        # Запуск браузера
        browser = p.chromium.launch()
        page = browser.new_page()

        yield page
        # Закрываем браузер
        browser.close()


def test_login(page):
    fake = Faker()
    # Генерация логина и пароля
    username = fake.user_name()
    password = fake.password()
    # Открываем страницу приложения
    page.goto(BASE_URL)
    # Нажимаем кнопку Login
    page.get_by_role("link", name="Login").click()
    # Заполняем поле Логин и Пароль
    page.fill("#username", username)
    page.fill("#password", password)
    # Подтверждаем вход
    page.get_by_role("button", name="Confirm").click()
    # Ждём появления и исчезновения
    page.wait_for_selector(".button-spinner", state="visible")
    page.wait_for_selector(".button-spinner", state="hidden")
    # Получаем текст ошибки
    error = page.get_by_text(INVALID_LOGIN_ERROR).text_content()
    assert error == INVALID_LOGIN_ERROR, (
        f"Expected error: '{INVALID_LOGIN_ERROR}', actual error: {error}"
    )
