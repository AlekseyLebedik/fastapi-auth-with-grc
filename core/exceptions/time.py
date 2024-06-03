import grpc as g


class IncorrectTimeStr(Exception):
    details = "Incorrectly transmitted time as a string!"
    status_code = g.StatusCode.INVALID_ARGUMENT

    def __str__(self) -> str:
        return self.details
