from playwright.sync_api import Page

from ui.page_actions import PageActions


class InfiniteScrollPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.actions = PageActions(page)
        self.paragraphs = self.page.locator(".jscroll-added")

    def open(self, url: str) -> None:
        self.actions.goto(url)
        self.paragraphs.first.wait_for(state="visible")

    def get_paragraphs_count(self) -> int:
        return self.paragraphs.count()

    def scroll_to_bottom(self) -> None:
        self.page.evaluate("window.scrollTo(0, document.body.scrollHeight)")

    def wait_for_new_paragraph(self, previous_count: int) -> None:
        self.paragraphs.nth(previous_count).wait_for(state="attached")

        loading = self.page.locator(".jscroll-loading")
        loading.wait_for(state="hidden")
