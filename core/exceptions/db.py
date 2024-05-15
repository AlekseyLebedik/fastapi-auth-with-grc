from typing import Optional

from fastapi import status


class DoNotValidCredential(Exception):
    message = "You have entered an incorrect"
    status_code = status.HTTP_400_BAD_REQUEST

    def __init__(self, reason: Optional[str] = "password"):
        self.message = f"{self.message} {reason}!"

    def __str__(self) -> str:
        return self.message

    @property
    def get_message(self) -> str:
        return self.message


class DBCreate(Exception):
    message = "Failed in the database"
    status_code = status.HTTP_409_CONFLICT

    def __init__(self, reason: Optional[str] = ""):
        self.message = f"{self.message} {reason}!"

    def __str__(self) -> str:
        return self.message

    @property
    def get_message(self) -> str:
        return self.message
