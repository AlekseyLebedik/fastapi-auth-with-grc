import typing as t

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
