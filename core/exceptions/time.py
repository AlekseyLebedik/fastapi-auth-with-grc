from fastapi import status


class IncorrectTimeStr(Exception):
    message = "Incorrectly transmitted time as a string!"
    status_code = status.HTTP_400_BAD_REQUEST

    def __str__(self) -> str:
        return self.message

    @property
    def get_message(self) -> str:
        return self.message
