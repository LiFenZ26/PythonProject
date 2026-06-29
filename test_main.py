from main import login, INVALID_LOGIN_ERROR


# Тест для проверки ошибки при неверном логине и пароле
def test_login():
    error = login("randomuser", "randompassword")

    assert error == INVALID_LOGIN_ERROR
