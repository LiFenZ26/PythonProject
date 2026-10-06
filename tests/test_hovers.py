from pages.hovers_page import HoversPage


def test_hover(page):
    url = "http://the-internet.herokuapp.com/hovers"
    hovers_page = HoversPage(page)
    hovers_page.open(url)
    user_count = hovers_page.get_users_count()
    for index in range(user_count):
        actual_name = hovers_page.hover_user(index)
        assert actual_name == f"name: user{index + 1}"
