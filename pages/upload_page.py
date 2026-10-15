from playwright.sync_api import Page
from ui.page_actions import PageActions


class UploadPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.actions = PageActions(page)
        self.file_input = self.page.locator("#file-upload")
        self.upload_button = self.page.locator("#file-submit")
        self.success_message = self.page.locator("h3")
        self.uploaded_file_name = self.page.locator("#uploaded-files")

    def open(self, url: str) -> None:
        self.actions.goto(url)

    def upload_file(self, file_path: str) -> None:
        self.file_input.set_input_files(file_path)
        self.upload_button.click()

    def get_success_message(self) -> str:
        return self.success_message.inner_text()

    def get_uploaded_file_name(self) -> str:
        return self.uploaded_file_name.inner_text()
