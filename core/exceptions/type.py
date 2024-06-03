import typing as t

import grpc as g


class IncorectValueType(Exception):
    status = g.StatusCode.INVALID_ARGUMENT
    details = "Incorect pass type."

    def __init__(self, reason: t.Optional[str] = None):
        self.details = f"{self.details} {reason if reason else ""}!"
