import typing as t
from enum import Enum

class ADMIN_CONCLUSION(int, Enum):
    UNRELIABLE_DATA: ADMIN_CONCLUSION
    VERIFY: ADMIN_CONCLUSION
    POOR_QUALITY_PHOTO: ADMIN_CONCLUSION

class ROLES(int, Enum):
    ROLE_PORTAL_USER: ROLES
    ROLE_PORTAL_ADMIN: ROLES
    ROLE_PORTAL_SUPERADMIN: ROLES

class UserPrivateMeta:
    document_id: t.Optional[str] = None
    document_photo_links: t.Optional[str] = None
    nationality: t.Optional[str] = None
    mac_ids: t.Optional[str] = None
    verify_date: t.Optional[str] = None
    br_date: t.Optional[str] = None

    def __init__(
        self,
        document_id: t.Optional[str] = None,
        document_photo_links: t.Optional[str] = None,
        nationality: t.Optional[str] = None,
        mac_ids: t.Optional[str] = None,
        verify_date: t.Optional[str] = None,
        br_date: t.Optional[str] = None,
    ) -> None: ...

class User:
    fname: str
    lname: str
    roles: t.List[ROLES]
    email: t.Optional[str] = None
    phone: t.Optional[str] = None
    phone_token: t.Optional[str] = None
    password: t.Optional[str] = None
    hashed_password: t.Optional[str] = None
    avatar: t.Optional[bytes] = None
    privateMeta: t.Optional[UserPrivateMeta] = None

    def __init__(
        self,
        fname: str,
        lname: str,
        roles: t.List[ROLES],
        email: t.Optional[str] = None,
        phone_token: t.Optional[str] = None,
        password: t.Optional[str] = None,
        hashed_password: t.Optional[str] = None,
        avatar: t.Optional[bytes] = None,
        privateMeta: t.Optional[UserPrivateMeta] = None,
    ) -> None: ...

class AvailableFieldsToUpdate:
    fname: t.Optional[str] = None
    lname: t.Optional[str] = None
    avatar: t.Optional[bytes] = None
    br_date: t.Optional[str] = None

    def __init__(
        self,
        fname: t.Optional[str] = None,
        lname: t.Optional[str] = None,
        avatar: t.Optional[bytes] = None,
        br_date: t.Optional[str] = None,
    ) -> None: ...

class TotalResponse:
    details: str
    status: int
    user: t.Optional[User] = None
    condition: t.Optional[bool] = None

    def __init__(
        self,
        details: str,
        status: int,
        user: t.Optional[User] = None,
        condition: t.Optional[bool] = None,
    ) -> None: ...

class CreateUserRequest:
    user: User

    def __init__(
        self,
        user: User,
    ) -> None: ...

class OrdinaryUpdateUserRequest:
    user: AvailableFieldsToUpdate

    def __init__(
        self,
        user: AvailableFieldsToUpdate,
    ) -> None: ...

class ChangePhoneNumberRequest:
    phone_number: str
    verify_code: int
    verify_with_email: bool

    def __init__(
        self,
        phone_number: str,
        verify_code: int,
        verify_with_email: bool,
    ) -> None: ...

class DeleteUserRequest:
    user_id: int

    def __init__(
        self,
        user_id: int,
    ) -> None: ...

class VerifyUserWithDocsRequest:
    documents: t.List[bytes]

    def __init__(
        self,
        documents: t.List[bytes],
    ) -> None: ...

class ChangeUserRoleRequest:
    role: ROLES

    def __init__(
        self,
        role: ROLES,
    ) -> None: ...

class UserDataValidationByAdminRequest:
    user: t.Optional[User] = None

    def __init__(
        self,
        user: t.Optional[User] = None,
    ) -> None: ...

class LightVerifyUserRequest:
    verify_key: int

    def __init__(
        self,
        verify_key: int,
    ) -> None: ...
