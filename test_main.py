import pytest
from config_reader import ConfigReader


@pytest.mark.parametrize(
    "name, n, filter_type",
    [
        ("city", 10, "Price: low to high"),
        ("city", 15, "Price: high to low"),
        ("habits", 10, "Price: low to high"),
        ("habits", 15, "Price: high to low"),
    ],
)
def test_articles_sorting(page, name, n, filter_type):
    config = ConfigReader()
    page.goto(config.get("base_url"))
    page.get_by_test_id("search-input").fill(name)
    page.get_by_test_id("search-button").click()
    page.get_by_test_id("filter-sort").select_option(label=filter_type)
    page.get_by_test_id("results-loader").wait_for(state="visible")
    page.get_by_test_id("results-loader").wait_for(state="hidden")
    prices_text = page.locator("[data-testid^='search-result-price-']").all_text_contents()
    first_price_text = prices_text[:n]
    prices = []
    for i in first_price_text:
        price = int(i.replace(" RUB", ""))
        prices.append(price)
    if filter_type == "Price: low to high":
        assert prices == sorted(prices), "Prices are not sorted from low to high"
    if filter_type == "Price: high to low":
        assert prices == sorted(prices, reverse=True), "Prices are not sorted from high to low"
