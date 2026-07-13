from pages.base_page import BasePage
from pages.search_page import SearchResultsPage


class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.search_input = page.get_by_test_id("search-input")
        self.search_button = page.get_by_test_id("search-button")
    def search_article(self, name):
        self.search_input.fill(name)
        self.search_button.click()

        return SearchResultsPage(self.page)
