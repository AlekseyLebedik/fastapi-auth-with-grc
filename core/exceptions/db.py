from typing import Optional

import grpc as g


class DoNotValidCredential(Exception):
    details = "You have entered an incorrect"
    status = g.StatusCode.INVALID_ARGUMENT

    def __init__(self, reason: Optional[str] = "password"):
        from core.utils import _logger

        self.details = f"{self.details} {reason}!"

        _logger.warning(reason, self.details)

    def __str__(self) -> str:
        return self.details


class DBCreate(Exception):
    details = "Failed in the database"
    status = g.StatusCode.INVALID_ARGUMENT

    def __init__(self, reason: Optional[str] = ""):
        self.details = f"{self.details} {reason}!"

    def __str__(self) -> str:
        return self.details
