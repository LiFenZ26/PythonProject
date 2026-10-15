from pages.dynamic_content_page import DynamicContentPage


def test_dynamic_content(page):
    url = "http://the-internet.herokuapp.com/dynamic_content"
    dynamic_content_page = DynamicContentPage(page)
    dynamic_content_page.open(url)
    while not dynamic_content_page.has_duplicate_images():
        dynamic_content_page.reload_page()
    assert dynamic_content_page.has_duplicate_images()
