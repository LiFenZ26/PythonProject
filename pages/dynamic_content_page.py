from playwright.sync_api import Page

from ui.page_actions import PageActions
from ui.web_element import WebElement


class DynamicContentPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.actions = PageActions(page)
        self.images = self.page.locator(".large-2 img")

    def open(self, url: str) -> None:
        self.actions.goto(url)

    def get_images_src(self) -> list[str]:
        image_list = []
        for index in range(self.images.count()):
            image = WebElement(
                self.images.nth(index),
                description="windows page -> get img"
            )
            src = image.get_attribute("src")
            image_list.append(src)
        return image_list

    def has_duplicate_images(self) -> bool:
        images = self.get_images_src()
        has_duplicates = (
                images[0] == images[1]
                or images[0] == images[2]
                or images[1] == images[2]
        )
        return has_duplicates

    def reload_page(self) -> None:
        self.page.reload()
