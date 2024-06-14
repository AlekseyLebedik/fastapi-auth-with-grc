import asyncio
import typing as t

import grpc as g
from loguru import logger

from core.db.session_dals import createSession
from core.db.user_dals import createUser
from core.utils import _logger, exceptionHandlingWithContext, isErrorHandlingWithContext
from core.utils.session_store.store import session_store
from protobuff import session_models, session_services, user_models, user_services

from .extratype_decorator import extratypeDecorator
from .methods import MethodsEnum
from .status import StatusCode
from .stream_maker import ServerStreamMaker

stream = None


async def up_stream():
    global stream
    if stream is None:
        stream = ServerStreamMaker()

    return stream


class AuthServiceServicer(
    session_services.SessionServiceServicer,
    user_services.UserServiceServicer,
):
    def __init__(self) -> None:
        self._stream: t.Union[ServerStreamMaker, None] = None

    async def stream_watcher(self):
        self._stream = await up_stream() if self._stream is None else self._stream
        async for response in self._stream.stream():
            yield response

    @extratypeDecorator("user")
    async def CreateUser(self, request, context):
        logger.info(f"{MethodsEnum.CREATE_USER.value} methods starting ...")
        metadata = dict(context.invocation_metadata())
        try:
            user = request.user
            user = await createUser(
                password=user.password,
                lname=user.lname,
                fname=user.fname,
                email=user.email,
                phone=user.phone,
                mac_id=metadata.get("mac_id", ""),
            )
            logger.info(user.model_dump())
            return user_models.TotalResponse(
                details="Succesfull create user!",
                status=201,
                user=user.proto_user(),
            )
        except Exception as ex:
            exceptionHandlingWithContext(
                context=context,
                exception=ex,
                method=MethodsEnum.CREATE_USER.value,
            )

    @extratypeDecorator()
    async def CreateSession(self, request, context):
        try:
            return await createSession(
                password=request.password,
                email=request.email,
                phone=request.phone_number,
            )
        except Exception as ex:
            exceptionHandlingWithContext(
                context=context,
                exception=ex,
                method=MethodsEnum.CREATE_SESSION.value,
            )

    async def ConditionSessionStream(
        self,
        request_iterator,
        context: g.ServicerContext,
    ):
        try:
            self._stream = await up_stream() if self._stream is None else self._stream
            async for request in request_iterator:
                logger.error(request)
                self._stream.put_request(request)

            async for response in self.stream_watcher():
                handled_response = isErrorHandlingWithContext(context, response)

                if handled_response:
                    yield handled_response
                else:
                    return

        except Exception as ex:
            exceptionHandlingWithContext(
                context=context,
                exception=ex,
                method=MethodsEnum.CREATE_SESSION.value,
            )
