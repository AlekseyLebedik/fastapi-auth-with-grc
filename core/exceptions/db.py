from typing import Optional


class DoNotValidCredential(Exception):
    message = "You have entered an incorrect"

    def __init__(self, reason: Optional[str] = "password"):
        self.message = f"{self.message} {reason}!"

    def __str__(self) -> str:
        return self.message

    @property
    def get_message(self) -> str:
        return self.message


class DBCreate(Exception):
    message = "Failed to create in the database"

    def __init__(self, reason: Optional[str] = ""):
        self.message = f"{self.message} {reason}!"

    def __str__(self) -> str:
        return self.message

    @property
    def get_message(self) -> str:
        return self.message
