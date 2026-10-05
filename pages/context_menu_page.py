from playwright.sync_api import Page
from ui.page_actions import PageActions
from ui.web_element import WebElement


class ContextMenuPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.actions = PageActions(page)
        self.hot_spot = WebElement(
            self.page.locator("#hot-spot"),
            description="Context menu -> Hot spot")

    def open(self, url: str) -> None:
        self.actions.goto(url)

    def open_context_menu(self) -> str:
        return self.actions.run_and_accept_alert(self.hot_spot.right_click)
