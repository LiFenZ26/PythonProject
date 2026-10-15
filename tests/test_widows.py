from pages.windows_page import WindowsPage


def test_windows(page):
    url = "http://the-internet.herokuapp.com/windows"
    windows_page = WindowsPage(page)
    windows_page.open(url)
    new_page = windows_page.open_new_window()
    actual_text = windows_page.get_new_window_text(new_page)
    assert actual_text == "New Window"
    second_new_page = windows_page.open_new_window()
    actual_text = windows_page.get_new_window_text(second_new_page)
    assert actual_text == "New Window"
    windows_page.close_window(new_page)
    windows_page.close_window(second_new_page)
    count = windows_page.get_windows_count()
    assert count == 1
