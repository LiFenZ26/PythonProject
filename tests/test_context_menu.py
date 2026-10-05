from pages.context_menu_page import ContextMenuPage


def test_context_menu(page):
    url = "http://the-internet.herokuapp.com/context_menu"
    context_auth_page = ContextMenuPage(page)
    context_auth_page.open(url)
    context_auth = context_auth_page.open_context_menu()
    assert context_auth == "You selected a context menu"
