import datetime
from enum import Enum
from typing import ClassVar as _ClassVar
from typing import List as _List
from typing import Mapping as _Mapping
from typing import Optional as _Optional
from typing import Union as _Union

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class ROLES(Enum):
    ROLE_PORTAL_USER = "ROLE_PORTAL_USER"
    ROLE_PORTAL_ADMIN = "ROLE_PORTAL_ADMIN"
    ROLE_PORTAL_SUPERADMIN = "ROLE_PORTAL_SUPERADMIN"

class Timestamp(_message.Message):
    __slots__ = ["seconds", "nanos"]
    seconds: _Optional[int]
    nanos: _Optional[int]
    def __init__(
        self,
        seconds: _Optional[int],
        nanos: _Optional[int],
    ) -> None: ...

class User(_message.Message):
    __slots__ = [
        "fname",
        "lname",
        "roles",
        "email",
        "phone",
        "avatar",
        "document_id",
        "document_photo_links",
        "nationality",
        "mac_ids",
        "verify_date",
        "br_date",
    ]
    fname: str
    lname: str
    roles: _List[ROLES]
    email: _Optional[str]
    phone: _Optional[str]
    avatar: _Optional[str]
    document_id: _Optional[str]
    document_photo_links: _Optional[_List[str]]
    nationality: _Optional[str]
    mac_ids: _Optional[_List[str]]
    verify_date: _Optional[str]
    br_date: _Optional[str]

    def __init__(
        self,
        fname: str,
        lname: str,
        roles: _List[ROLES],
        email: _Optional[str] = ...,
        phone: _Optional[str] = ...,
        avatar: _Optional[str] = ...,
        document_id: _Optional[str] = ...,
        document_photo_links: _Optional[_List[str]] = ...,
        nationality: _Optional[str] = ...,
        mac_ids: _Optional[_List[str]] = ...,
        verify_date: _Optional[str] = ...,
        br_date: _Optional[str] = ...,
    ) -> None: ...

class CreateUserRequest(_message.Message):
    __slots__ = ["user"]
    user: User
    def __init__(
        self,
        user: User,
    ) -> None: ...

class TotalResponse(_message.Message):
    __slots__ = ["details", "status", "user", "condition"]
    details: int
    status: str
    user: _Optional[User]
    condition: _Optional[bool]
    def __init__(
        self,
        details: int,
        status: str,
        user: _Optional[User] = ...,
        condition: _Optional[bool] = ...,
    ) -> None: ...
