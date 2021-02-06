class NoneTypeError(Exception):
    def __init__(self, message: str = "Вводимое значения типа None") -> None:
        self.message = message
        super().__init__(self.message)

    def __str__(self) -> str:
        return f"{self.message}"
