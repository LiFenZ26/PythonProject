from main import login, INVALID_LOGIN_ERROR


def test_login():
    error = login("randomuser", "randompassword")

    assert error == INVALID_LOGIN_ERROR
