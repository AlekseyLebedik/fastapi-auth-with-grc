import typing as t
from enum import Enum

from user_pb2 import User

class SessionRequest:
    phone_number: t.Optional[str] = None
    email: t.Optional[str] = None
    password: str

    def __init__(
        self,
        password: str,
        phone_number: t.Optional[str] = None,
        email: t.Optional[str] = None,
    ): ...

class SessionResponse:
    session_mark: str
    refresh_token: str
    details: str
    status: int

    def __init__(
        self,
        session_mark: str,
        refresh_token: str,
        details: str,
        status: int,
    ) -> None: ...

class StateSessionEnum(Enum):
    REFUSE = StateSessionEnum
    EXTENDING = StateSessionEnum
    ME = StateSessionEnum

class ConditionSessionRequest:
    state: StateSessionEnum
    session_mark: t.Optional[str]
    refresh_token: t.Optional[str]
    stream_condition: StreamConditionEnum

    def __init__(
        self,
        state: StateSessionEnum,
        session_mark: t.Optional[str],
        refresh_token: t.Optional[str],
        stream_condition: StreamConditionEnum,
    ) -> None: ...

class ConditionSessionResponse:
    session_mark: t.Optional[str]
    destroy_session: t.Optional[bool]
    isError: t.Optional[bool]
    user: t.Optional[User]
    stream_condition: StreamConditionEnum
    details: str
    status: int

    def __init__(
        self,
        session_mark: t.Optional[str],
        destroy_session: t.Optional[bool],
        user: t.Optional[User],
        isError: t.Optional[bool],
        stream_condition: StreamConditionEnum,
        details: str,
        status: int,
    ) -> None: ...

class StreamConditionEnum(Enum):
    CONTINUE = StreamConditionEnum
    CLOSE = StreamConditionEnum
