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
    access_token: str
    refresh_token: str
    detail: str
    status: int

    def __init__(
        self,
        access_token: str,
        refresh_token: str,
        detail: str,
        status: int,
    ) -> None: ...
