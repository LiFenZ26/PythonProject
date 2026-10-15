from playwright.sync_api import Page

from ui.page_actions import PageActions
from ui.web_element import WebElement


class WindowsPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.actions = PageActions(page)
        self.click_here = WebElement(
            self.page.locator('a[href="/windows/new"]'),
            description="Windows page -> click"
        )

    def open(self, url: str) -> None:
        self.actions.goto(url)

    def open_new_window(self) -> Page:
        with self.page.expect_popup() as popup_info:
            self.click_here.click()
        return popup_info.value

    def get_new_window_text(self, new_page: Page) -> str:
        n_page = WebElement(
            new_page.locator('h3'),
            description="Windows page -> new page"
        )
        return n_page.get_inner_text()

    def close_window(self, window: Page) -> None:
        window.close()

    def get_windows_count(self) -> int:
        return len(self.page.context.pages)
