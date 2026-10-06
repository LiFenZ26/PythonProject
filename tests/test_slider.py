from pages.page_slider import SliderPage

def test_page_slider(page):
    url = "http://the-internet.herokuapp.com/horizontal_slider"
    slider_page = SliderPage(page)
    slider_page.open(url)
    expected_value = slider_page.set_random_value()
    actual_value = float(slider_page.get_value())
    assert expected_value == actual_value