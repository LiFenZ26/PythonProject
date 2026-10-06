from playwright.sync_api import Page
from ui.page_actions import PageActions
from ui.web_element import WebElement
import random

class SliderPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.actions = PageActions(page)
        self.slider = WebElement(
            self.page.locator('input[type="range"]'),
            description="Slider page -> slider"
        )
        self.value = WebElement(
            self.page.locator("#range"),
            description="Slider page -> value"
        )

    def open(self, url: str) -> None:
        self.actions.goto(url)

    def set_random_value(self) -> float:
        press_count = random.randint(1, 9)
        value = press_count * 0.5
        for _ in range(press_count):
            self.slider.press("ArrowRight")
        return value
    def get_value(self) -> str:
        return self.value.get_inner_text()