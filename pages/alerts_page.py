from playwright.sync_api import Page

from ui.page_actions import PageActions
from ui.web_element import WebElement


class AlertsPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.actions = PageActions(page)
        self.alert_button = WebElement(
            self.page.get_by_role("button", name="Click for JS Alert"),
            description="Alerts -> JS Alert button",
        )
        self.confirm_button = WebElement(
            self.page.get_by_role("button", name="Click for JS Confirm"),
            description="Alerts -> JS Confirm button",
        )
        self.prompt_button = WebElement(
            self.page.get_by_role("button", name="Click for JS Prompt"),
            description="Alerts -> JS Prompt button",
        )
        self.result = WebElement(
            self.page.locator("#result"),
            description="Alerts -> Result",
        )

    def open(self, url: str) -> None:
        self.actions.goto(url)

    def accept_alert(self) -> str:
        return self.actions.run_and_accept_alert(self.alert_button.click)

    def accept_confirm(self) -> str:
        return self.actions.run_and_accept_alert(self.confirm_button.click)

    def accept_prompt(self, text: str) -> str:
        return self.actions.run_and_accept_prompt(self.prompt_button.click, text)

    def get_result(self) -> str:
        return self.result.get_inner_text()
