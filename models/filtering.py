import random


class FilteringData:
    def __init__(self, filtering):
        self.filtering = filtering

    @staticmethod
    def random(listing: list):
        return FilteringData(filtering=random.choices(listing, k=10))
