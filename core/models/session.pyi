import typing as t

from sqlalchemy import DateTime

class Session:
    from .user import UserModel

    id: int
    user_id: int
    user: UserModel
    acess_token: t.Optional[str]
    refresh_token: t.Optional[str]
    verify_key: int
    expire_time: DateTime

    def __init__(
        self,
        id: int,
        user_id: int,
        user: UserModel,
        acess_token: t.Optional[str],
        refresh_token: t.Optional[str],
        verify_key: int,
        expire_time: DateTime,
    ) -> None: ...
    def dump_to_dict(
        self,
        without: t.Optional[t.List[str]],
    ): ...
