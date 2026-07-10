from config_reader import ConfigReader
from pages.base_page import BasePage
from pages.search_page import SearchResultsPage


class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.config = ConfigReader()

    def open_home_page(self):
        self.open(self.config.get("base_url"))

    def search_article(self, name):
        self.page.get_by_test_id("search-input").fill(name)
        self.page.get_by_test_id("search-button").click()

        return SearchResultsPage(self.page)