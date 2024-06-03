import grpc as g


class NoValidTokenRaw(Exception):
    details = "Your token is not valid. You are denied access!"
    status = g.StatusCode.UNAUTHENTICATED

    def __str__(self) -> str:
        return self.details


class HaventToken(Exception):
    details = "You haven't transferred the token!"
    status = g.StatusCode.INVALID_ARGUMENT

    def __str__(self) -> str:
        return self.details
