from playwright.sync_api import Page

from ui.page_actions import PageActions


class DownloadPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.actions = PageActions(page)
        self.files = self.page.locator(".example a")

    def open(self, url: str) -> None:
        self.actions.goto(url)

    def get_third_file_name(self) -> str:
        return self.files.nth(2).inner_text()

    def download_third_file(self) -> str:
        with self.page.expect_download() as download_info:
            self.files.nth(2).click()
        download = download_info.value
        return download.suggested_filename