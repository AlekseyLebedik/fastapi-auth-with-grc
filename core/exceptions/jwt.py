from fastapi import status


class NoValidTokenRaw(Exception):
    message = "Your token is not valid. You are denied access!"
    status_code = status.HTTP_401_UNAUTHORIZED

    def __str__(self) -> str:
        return self.message

    @property
    def get_message(self) -> str:
        return self.message


class HaventToken(Exception):
    message = "You haven't transferred the token!"
    status_code = status.HTTP_400_BAD_REQUEST

    def __str__(self) -> str:
        return self.message

    @property
    def get_message(self) -> str:
        return self.message
