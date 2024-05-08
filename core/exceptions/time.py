class IncorrectTimeStr(Exception):
    message = "Incorrectly transmitted time as a string!"

    def __str__(self) -> str:
        return self.message

    @property
    def get_message(self) -> str:
        return self.message
