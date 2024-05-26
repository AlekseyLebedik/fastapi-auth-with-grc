import asyncio
import os
import sys
import time
from concurrent import futures
from contextlib import contextmanager

import grpc as g
from auth_service import AuthInterceptor, AuthServiceServicer
from core.db.user_dals import createUser
from core.utils import _logger
from grpc.experimental import aio
from protobuff import session_services, user_services

token = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImZuYW1lIjoiaGVsbG8zIiwiZW1haWwiOiJ0ZXN0QGdtYWlsLmNvbSIsImlzX3ZlcmlmeSI6ZmFsc2UsInVzZXJfaWQiOjI0LCJpZCI6MjQsImxuYW1lIjoic29tZSIsInBob25lIjoiKzM4MDkzMDk3MDA5MCIsIm1hY19pZHMiOlsiMjM6MzM6MzQ6NDQ6NjYiXSwiY3JlYXRlX2F0IjoiMDk6MDU6MjQgMTI6MTY6MjgiLCJoYXNoZWRfcGFzc3dvcmQiOiIkMmIkMTIkWm81dVhvejhxQnpoNGhFOXIubk8zZVhsTDBBckJNS2xiNUxIZ2JxRHFYaEdkUUhxTFpuZXkiLCJyb2xlcyI6WyJST0xFX1BPUlRBTF9VU0VSIl0sInVwZGF0ZWRfYWNjb3VudCI6IjA5OjA1OjI0IDEyOjE2OjI4In0sImV4cCI6IjE3MTU4OTc5ODA2NzIifQ.vY1AOAmqOY5pIE5GUWX0DwQCKbsYiHzZ5Le5m3fkj9I"
from settings import settings


async def serve():
    server = aio.server(
        futures.ThreadPoolExecutor(max_workers=10),
        interceptors=(AuthInterceptor(),),
    )
    user_services.add_UserServiceServicer_to_server(AuthServiceServicer(), server)
    session_services.add_SessionServiceServicer_to_server(AuthServiceServicer(), server)
    server.add_insecure_port(f"{settings.HOST_GRPC}:{settings.PORT_GRPC}")
    await server.start()
    _logger.info(
        f"GRPC server starting in {settings.HOST_GRPC}:{settings.PORT_GRPC}",
    )
    await server.wait_for_termination()


if __name__ == "__main__":
    try:
        asyncio.run(serve())
    except Exception as ex:
        _logger.error(f"GRPC server stopped. Reason: {ex}")
