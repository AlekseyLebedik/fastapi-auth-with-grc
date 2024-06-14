from grpc import StatusCode as status_g
from loguru import logger


class StatusVariant:
    def __init__(self, http: int, grpc) -> None:
        self.http = http
        self.grpc = grpc

    def __repr__(self) -> str:
        return f"StatusVariant(http={self.http}, grpc={self.grpc})"

    def __eq__(self, value: int) -> bool:
        if self.http == value:
            return False
        return True


class StatusHttpGrpc:
    HTTP_400_BAD_REQUEST = StatusVariant(http=400, grpc=status_g.INVALID_ARGUMENT)
    HTTP_200_OK = StatusVariant(http=200, grpc=status_g.OK)
    HTTP_201_CREATED = StatusVariant(http=201, grpc=status_g.OK)
    HTTP_401_UNAUTHORIZED = StatusVariant(http=401, grpc=status_g.UNAUTHENTICATED)
    HTTP_403_FORBIDDEN = StatusVariant(http=403, grpc=status_g.PERMISSION_DENIED)
    HTTP_409_CONFLICT = StatusVariant(http=409, grpc=status_g.CANCELLED)

    @classmethod
    def get_grpc_code(self, status: int) -> status_g:
        for key, value in self.__dict__.items():
            if key.__contains__("HTTP") and status == value:
                return value.grpc

        status_separator_group = str(status)[0]
        if status_separator_group == "2":
            return status_g.OK
        elif status_separator_group == "3":
            return status_g.NOT_FOUND
        elif status_separator_group == "4":
            return status_g.NOT_FOUND
        elif status_separator_group == "5":
            return status_g.UNIMPLEMENTED
