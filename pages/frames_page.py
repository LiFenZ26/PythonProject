from playwright.sync_api import Page

from ui.page_actions import PageActions
from ui.web_element import WebElement


class FramesPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.actions = PageActions(page)
        self.bottom = WebElement(
            self.page.frame_locator('[name="frame-bottom"]').locator("body"),
            description="Frames page -> bottom"
        )
        self.left = WebElement(
            self.page.frame_locator('[name="frame-top"]').frame_locator('[name="frame-left"]').locator("body"),
            description="Frames page -> left"
        )
        self.right = WebElement(
            self.page.frame_locator('[name="frame-top"]').frame_locator('[name="frame-right"]').locator("body"),
            description="Frames page -> right"
        )
        self.middle = WebElement(
            self.page.frame_locator('[name="frame-top"]').frame_locator('[name="frame-middle"]').locator("#content"),
            description="Frames page -> middle"
        )

    def open(self, url: str) -> None:
        self.actions.goto(url)

    def get_left_text(self) -> str:
        return self.left.get_inner_text()

    def get_middle_text(self) -> str:
        return self.middle.get_inner_text()

    def get_right_text(self) -> str:
        return self.right.get_inner_text()

    def get_bottom_text(self) -> str:
        return self.bottom.get_inner_text()
