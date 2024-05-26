import typing as t

from sqlalchemy import DateTime

class UserMeta:
    from .user import UserModel

    id: int
    br_date: t.Optional[DateTime]
    document_id: t.Optional[str]
    document_photo_links: t.Optional[t.List[str]]
    nationality: t.Optional[str]
    mac_ids: t.Optional[t.List[str]]
    is_verify: bool
    verify_date: t.Optional[DateTime]
    user_id: int
    user: UserModel
    def __init__(
        self,
        id: int,
        br_date: t.Optional[DateTime],
        document_id: t.Optional[str],
        document_photo_links: t.Optional[t.List[str]],
        nationality: t.Optional[str],
        mac_ids: t.Optional[t.List[str]],
        is_verify: bool,
        verify_date: t.Optional[DateTime],
        user_id: int,
        user: UserModel,
    ) -> None: ...
    @property
    def get_private_meta(self) -> t.List[str]: ...
    def dump_to_dict(
        self,
        with_private_meta: t.Optional[bool],
        without: t.Optional[t.List[str]],
    ): ...
