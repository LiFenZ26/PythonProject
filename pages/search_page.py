from pages.base_page import BasePage


class SearchResultsPage(BasePage):
    def select_sorting_filter(self, filter_type):
        self.page.get_by_test_id("filter-sort").select_option(label=filter_type.value)
        self.wait_results_loaded()

    def wait_results_loaded(self):
        self.page.get_by_test_id("results-loader").wait_for(state="visible")
        self.page.get_by_test_id("results-loader").wait_for(state="hidden")

    def get_first_article_prices(self, articles_count):
        prices_text = self.page.locator(
            "[data-testid^='search-result-price-']"
        ).all_text_contents()

        first_prices_text = prices_text[:articles_count]

        prices = []

        for price_text in first_prices_text:
            price = int(price_text.replace(" RUB", ""))
            prices.append(price)

        return prices