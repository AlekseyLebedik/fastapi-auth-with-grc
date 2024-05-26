import typing as t

from sqlalchemy import DateTime

class UserModel:
    from .session import Session
    from .user_meta import UserMeta

    user_id: int
    fname: str
    lname: str
    roles: t.List[str]
    email: str
    phone_token: str
    avatar: str
    hashed_password: str
    create_at: DateTime
    update_account: DateTime
    session: Session
    meta: UserMeta

    def __init__(
        self,
        user_id: int,
        fname: str,
        lname: str,
        roles: t.List[str],
        email: t.Optional[str],
        phone_token: t.Optional[str],
        avatar: t.Optional[str],
        hashed_password: str,
        create_at: DateTime,
        update_account: DateTime,
        session: Session,
        meta: UserMeta,
    ) -> None: ...
    @property
    def is_superadmin(self) -> bool: ...
    @property
    def is_admin(self) -> bool: ...
    def enrich_admin_roles_by_admin_role(self): ...
    def remove_admin_privileges_from_model(self): ...
    def dump_to_dict(
        self,
        without: t.Optional[t.List[str]],
    ): ...
