from playwright.sync_api import Page
from ui.page_actions import PageActions
from utils.url_utils import embed_credentials_in_url
from ui.web_element import WebElement

class BasicAuthPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.actions = PageActions(page)
        self.message = WebElement(
            self.page.locator("#content p"),
            description="Basic auth -> Message")
    def open(self, url: str, username: str, password: str) -> None:
        url = embed_credentials_in_url(url, username, password)
        self.actions.goto(url)

    def get_message(self) -> str:
        return self.message.get_inner_text()