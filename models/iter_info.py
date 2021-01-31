from typing import Any


class IterData:
    def __init__(self, data):
        self.data = data

    @staticmethod
    def check_data(listing: Any):
        for i in listing:
            if i.text is not None:
                print("true")
            else:
                return False
