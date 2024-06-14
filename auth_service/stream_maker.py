import asyncio
import random
import typing as t
from enum import Enum

from loguru import logger
from python_event_bus import EventBus

from core.exceptions import CloseStreamException
from core.utils.logger import _logger
from core.utils.session_store.store import session_store
from protobuff import session_models

from .status import StatusHttpGrpc


class StreamEventEnum(str, Enum):
    READY_REQUEST = "ready_request"


def _marker_asyncio(prefix: t.Optional[str] = "request"):
    def wrapper(func):
        def wrapped(self, *args, **kwargs):
            marker = self.get_marker(prefix)
            return asyncio.create_task(
                func(self, *args, **kwargs, name_request=marker),
                name=marker,
            )

        return wrapped

    return wrapper


class ServerStreamMaker:
    def __init__(self) -> None:
        self.response = []
        self.response_event = asyncio.Event()
        self.store = session_store
        self._tasks: t.Dict[str, t.Tuple[asyncio.Task, t.Callable]] = {}
        self._close_stream_event = asyncio.Event()
        self._closing_event = asyncio.Event()
        self._marker = 0
        self._stream_condition = session_models.StreamConditionEnum.CONTINUE
        EventBus.subscribe(StreamEventEnum.READY_REQUEST, self.response_watcher)

    @_marker_asyncio()
    async def put_request(
        self,
        request: session_models.ConditionSessionRequest,
        **kwargs,
    ):
        await self.__check_condition_stream()
        name_request = kwargs.get("name_request")

        if session_models.StateSessionEnum.EXTENDING == request.state:
            self.__callback_with_event(
                self.__extending_request(request, name_request),
                StreamEventEnum.READY_REQUEST,
                name_task=request.session_mark,
            )
        elif session_models.StateSessionEnum.ME == request.state:
            self.__callback_with_event(
                self.__me_request(request, name_request),
                StreamEventEnum.READY_REQUEST,
                name_task=request.session_mark,
            )
        elif session_models.StateSessionEnum.REFUSE == request.state:
            self.__callback_with_event(
                self.__refuse_request(request, name_request),
                StreamEventEnum.READY_REQUEST,
                name_task=request.session_mark,
            )

    def response_watcher(self, data):
        self.response.append(data)
        self.response_event.set()

    async def stream(self):
        while not self._close_stream_event.is_set():
            await self.response_event.wait()
            if len(self.response) > 0:
                response = self.response.pop()
                yield response
            else:
                await self.__check_condition_stream()
                self.response_event.clear()

    """
        REQUEST METHOD: Create for handling another variant which user passed.
    """

    async def __me_request(
        self,
        request: session_models.ConditionSessionRequest,
        name_request: str,
    ):
        try:
            session = self.store.get_session(request.session_mark)
            if session:
                user = session.user.proto_user()
                return session_models.ConditionSessionResponse(
                    stream_condition=self._stream_condition,
                    user=user,
                    details="You are logged into a session with this user.",
                    status=StatusHttpGrpc.HTTP_200_OK.http,
                )

            else:
                return session_models.ConditionSessionResponse(
                    stream_condition=self._stream_condition,
                    isError=True,
                    details=f"Your session with this session-mark: ({request.session_mark}) was not found!",
                    status=StatusHttpGrpc.HTTP_401_UNAUTHORIZED.http,
                )

        except asyncio.CancelledError:
            logger.error(f"Request {name_request} was cancelled!")
            return session_models.ConditionSessionResponse(
                stream_condition=self._stream_condition,
                isError=True,
                details=f"Request with this session-mark: ({request.session_mark}) was cancelled!",
                status=StatusHttpGrpc.HTTP_409_CONFLICT.http,
            )

        finally:
            if self._tasks.get(name_request):
                self._tasks.pop(name_request)

    async def __refuse_request(
        self,
        request: session_models.ConditionSessionRequest,
        name_request: str,
    ):
        pass

    async def __extending_request(
        self,
        request: session_models.ConditionSessionRequest,
        name_request: str,
    ):
        pass

    """
        HANDLERS METHOD:
    """

    def __callback_with_event(
        self,
        coro: t.Coroutine,
        event: StreamEventEnum,
        /,
        name_task: t.Optional[str] = None,
    ):
        self.__callback_handler(
            coro,
            lambda done_task: EventBus.call(event, done_task.result()),
            name_task=name_task,
        )

    def __callback_handler(
        self,
        coro: t.Coroutine,
        callback: t.Callable,
        /,
        name_task: t.Optional[str] = None,
    ):
        task = asyncio.create_task(coro, name=name_task)
        task.add_done_callback(callback)
        if name_task:
            self._tasks[name_task] = [task, callback]

    async def __check_condition_stream(self):
        if self._close_stream_event.is_set():
            raise CloseStreamException

    """
        HELPER METHOD: 
    """

    async def closing_stream(self):
        await asyncio.gather(*[task for task, _ in self._tasks.values()])
        self._tasks = {}
        self._stream_condition = session_models.StreamConditionEnum.CLOSE
        self._close_stream_event.set()

    def get_marker(self, prefix):
        marker = f"{prefix}_{self._marker}"
        self._marker += 1
        return marker
