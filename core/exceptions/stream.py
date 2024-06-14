import grpc as g


class CloseStreamException(Exception):
    details = "The stream was shut down!"
    status = g.StatusCode.CANCELLED
