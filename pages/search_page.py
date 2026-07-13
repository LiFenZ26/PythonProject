from pages.base_page import BasePage


class SearchResultsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.sorting_filter = page.get_by_test_id("filter-sort")
        self.results_loader = page.get_by_test_id("results-loader")
        self.article_prices = page.locator(
            "[data-testid^='search-result-price-']"
        )
    def select_sorting_filter(self, filter_type):
        self.sorting_filter.select_option(label=filter_type.value)
        self.wait_results_loaded()

    def wait_results_loaded(self):
        self.results_loader.wait_for(state="visible")
        self.results_loader.wait_for(state="hidden")

    def get_first_article_prices(self, articles_count):
        prices = []

        for price_locator in  self.article_prices.all()[:articles_count]:
            price = int(price_locator.get_attribute("data-price"))
            price_rub = price // 100
            prices.append(price_rub)

        return prices