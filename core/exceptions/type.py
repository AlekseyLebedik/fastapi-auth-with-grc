import grpc as g


class IncorectValueType(Exception):
    status = g.StatusCode.INVALID_ARGUMENT
    details: str = "Incorect pass type."

    def __init__(self, reason: str):
        self.details = f"{self.details} {reason}!"
