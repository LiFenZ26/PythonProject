from faker import Faker

# URL тестируемого сайта
BASE_URL = "http://144.31.63.127:5000/"
# текст ошибки при неверном вводе данных
INVALID_LOGIN_ERROR = "Invalid login or password."


def test_login(page):
    fake = Faker()
    # Генерация логина и пароля
    username = fake.user_name()
    password = fake.password()
    # Открываем страницу приложения
    page.goto(BASE_URL)
    # Нажимаем кнопку Login
    page.get_by_test_id("nav-login").click()
    # Заполняем поле Логин и Пароль
    page.fill("#username", username)
    page.fill("#password", password)
    # Подтверждаем вход
    page.get_by_test_id("login-submit").click()
    # Ждём появления и исчезновения
    spinner = page.get_by_test_id("login-submit-spinner")
    spinner.wait_for(state="visible")
    spinner.wait_for(state="hidden")
    # Получаем текст ошибки
    error = page.get_by_text(INVALID_LOGIN_ERROR).text_content()
    assert error == INVALID_LOGIN_ERROR, (
        f"Expected error: '{INVALID_LOGIN_ERROR}', actual error: {error}"
    )
