from enum import StrEnum


class FilterType(StrEnum):
    PRICE_LOW_TO_HIGH = "Price: low to high"
    PRICE_HIGH_TO_LOW = "Price: high to low"