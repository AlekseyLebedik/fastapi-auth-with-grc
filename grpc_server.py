import os
import sys
import time
from concurrent import futures

import core.user_pb2 as user_model_grpc
import core.user_pb2_grpc as user_service_grpc
import grpc
from core.utils import terminal_grpc_server

sys.path.append(os.getcwd())
from settings import settings

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class UserServiceServicer(user_service_grpc.UserServiceServicer):
    def CreateUser(self, request, context):
        try:

            return user_model_grpc.TotalResponse(
                details="Hello world", status=200, condition=False
            )
        except Exception as ex:
            pass


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_service_grpc.add_UserServiceServicer_to_server(UserServiceServicer(), server)
    server.add_insecure_port(f"[::]:{settings.USER_PORT_GRPC}")
    server.start()
    server.wait_for_termination()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == "__main__":
    terminal_grpc_server(
        url=settings.USER_PORT_GRPC,
        name_server="User Service",
        time_interapt=_ONE_DAY_IN_SECONDS,
    )
    serve()
