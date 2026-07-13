import pytest
from config_reader import ConfigReader
from enums import FilterType
from pages.home_page import HomePage


@pytest.mark.parametrize("name", ["city", "habits"])
@pytest.mark.parametrize(
    "articles_count, filter_type",
    [
        (10, FilterType.PRICE_LOW_TO_HIGH),
        (15, FilterType.PRICE_HIGH_TO_LOW,)
    ],
)
def test_articles_sorting(page, name, articles_count, filter_type):
    config = ConfigReader()

    page.goto(config.get("base_url"))

    home_page = HomePage(page)
    search_results_page = home_page.search_article(name)

    search_results_page.select_sorting_filter(filter_type)

    actual_prices = search_results_page.get_first_article_prices(
        articles_count
    )

    if filter_type == FilterType.PRICE_LOW_TO_HIGH:
        expected_prices = sorted(actual_prices)
    else:
        expected_prices = sorted(actual_prices, reverse=True)

    assert actual_prices == expected_prices, (
        f"Prices are not sorted by filter: {filter_type.value}. "
        f"Expected: {expected_prices}. "
        f"Actual: {actual_prices}."
    )
