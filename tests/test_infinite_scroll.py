from pages.infinite_scroll_page import InfiniteScrollPage


def test_infinite_scroll(page):
    url = "http://the-internet.herokuapp.com/infinite_scroll"

    infinite_scroll_page = InfiniteScrollPage(page)
    infinite_scroll_page.open(url)

    while infinite_scroll_page.get_paragraphs_count() < 10:
        previous_count = infinite_scroll_page.get_paragraphs_count()
        infinite_scroll_page.scroll_to_bottom()
        infinite_scroll_page.wait_for_new_paragraph(previous_count)

    assert infinite_scroll_page.get_paragraphs_count() >= 10
