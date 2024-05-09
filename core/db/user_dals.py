from enum import Enum
from typing import List, Optional

from core.exceptions import DBCreate, DoNotValidCredential
from core.models import UserMeta, UserModel
from core.models.pydantic_models import PasswordType, PhoneType, User
from core.utils import _print, getParams, hasher_instance
from pydantic import EmailStr
from sqlalchemy import Select, select
from sqlalchemy.orm import joinedload

from .session import getSession


def none_method_user_decorator(func):
    def wrapper(*args, **kwargs):
        if kwargs.get("phone", None) is None and kwargs.get("email", None) is None:
            raise DBCreate(".Please pass along an email or phone number!")
        return func(*args, **kwargs)

    return wrapper


class MethodUserEnum(Enum):
    EMAIL = 0
    PHONE = 1


def grap_method_user(method: MethodUserEnum, value: str) -> Select:
    if method == MethodUserEnum.EMAIL:
        return (
            select(UserMeta)
            .where(UserMeta.email == value)
            .options(joinedload(UserMeta.user))
        )

    return (
        select(UserMeta)
        .where(UserMeta.phone == value)
        .options(joinedload(UserMeta.user))
    )


@none_method_user_decorator
async def getUser(
    password: PasswordType,
    email: Optional[EmailStr] = None,
    phone: Optional[PhoneType] = None,
) -> User:
    method = MethodUserEnum.EMAIL if email else MethodUserEnum.PHONE
    stmt: Select = grap_method_user(
        method,
        email if email else phone,
    )
    try:
        async with getSession() as session:
            for user_data in await session.scalars(stmt):
                user = User(**user_data.dump_to_dict(True))
                if not hasher_instance.verify_password(password, user.hashed_password):
                    raise DoNotValidCredential()
                return user
            raise DoNotValidCredential("email or phone")
    except Exception:
        raise


@none_method_user_decorator
async def createUser(
    password: PasswordType,
    lname: str,
    fname: str,
    email: Optional[EmailStr],
    phone: Optional[PhoneType],
    mac_id: str,
):
    phone_hash = hasher_instance.get_password_hash(phone) if not phone == None else None
    user_meta = UserMeta(
        phone=phone,
        email=email,
        lname=lname,
        fname=fname,
        mac_ids=[mac_id],
    )

    user = UserModel(
        hashed_password=hasher_instance.get_password_hash(
            password=password,
        ),
        phone_token=phone_hash,
        meta=user_meta,
    )

    try:
        async with getSession() as session:
            session.add_all([user_meta, user])
    except Exception:
        raise DBCreate(". User exist inside the database")


def updateUserMeta(**args) -> User:
    params = getParams(**args)
    try:
        pass
    except Exception:
        pass
