from pages.frames_page import FramesPage


def test_frames(page):
    url = "http://the-internet.herokuapp.com/nested_frames"
    frames_page = FramesPage(page)
    frames_page.open(url)

    left = frames_page.get_left_text()
    assert left == "LEFT"
    right = frames_page.get_right_text()
    assert right == "RIGHT"
    bottom = frames_page.get_bottom_text()
    assert bottom == "BOTTOM"
    middle = frames_page.get_middle_text()
    assert middle == "MIDDLE"
