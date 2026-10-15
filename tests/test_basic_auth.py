from pages.basic_auth_page import BasicAuthPage


def test_basic_auth(page):
    url = "http://the-internet.herokuapp.com/basic_auth"
    username = "admin"
    password = "admin"

    basic_auth_page = BasicAuthPage(page)
    basic_auth_page.open(url, username, password)

    message = basic_auth_page.get_message()

    assert message == "Congratulations! You must have the proper credentials."
