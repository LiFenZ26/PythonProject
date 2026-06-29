from playwright.sync_api import sync_playwright

# URL тестируемого сайта
BASE_URL = "http://144.31.63.127:5000/"
# текст ошибки при неверном вводе данных
INVALID_LOGIN_ERROR = "Invalid login or password."


def login(username, password):
    with sync_playwright() as p:
        # Запуск браузера
        browser = p.chromium.launch()
        page = browser.new_page()
        # Открываем страницу приложение
        page.goto(BASE_URL)
        # Нажимаем кнопу Login
        button = page.locator("text = Login")
        button.click()
        # Заполняем поле Логин и Пароль
        page.fill("#username", username)
        page.fill("#password", password)
        # Подтверждаем вход
        button = page.locator("text = Confirm")
        button.click()
        # Ждём появления и исчезновения
        page.wait_for_selector(".button-spinner", state="visible")
        page.wait_for_selector(".button-spinner", state="hidden")
        # Получаем текст ошибки
        error = page.get_by_text(INVALID_LOGIN_ERROR).text_content()
        # Закрываем браузер
        browser.close()
        # Возвращаем текст ошибки в тест
        return error
