from playwright.sync_api import Page
from ui.page_actions import PageActions
from ui.web_element import WebElement


class HoversPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.actions = PageActions(page)
        self.users = self.page.locator(".figure")

    def open(self, url: str) -> None:
        self.actions.goto(url)

    def get_users_count(self) -> int:
        users_count = self.users.count()
        return users_count

    def hover_user(self, index: int):
        user_locator = self.users.nth(index)

        user = WebElement(
            user_locator,
            description="Hovers page -> user",
        )
        user.hover()

        name_locator = user_locator.locator(".figcaption h5")
        name = WebElement(
            name_locator,
            description="Hovers page -> user name",
        )

        return name.get_inner_text()
