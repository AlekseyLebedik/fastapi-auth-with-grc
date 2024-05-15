from enum import Enum
from typing import List, Optional, Tuple

from core.exceptions import DBCreate, DoNotValidCredential
from core.models import UserMeta, UserModel
from core.models.pydantic_models import PasswordType, PhoneType, User
from core.utils import getParams, hasher_instance, updateClassAttrByKey
from pydantic import EmailStr
from sqlalchemy import Select, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from .session import getSession


def none_method_user_decorator(func):
    def wrapper(*args, **kwargs):
        if kwargs.get("phone", None) is None and kwargs.get("email", None) is None:
            raise DoNotValidCredential(". Please pass along an email or phone number!")
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
    session: AsyncSession,
    email: Optional[EmailStr] = None,
    phone: Optional[PhoneType] = None,
) -> UserMeta:
    method = MethodUserEnum.EMAIL if email else MethodUserEnum.PHONE
    stmt: Select = grap_method_user(
        method,
        email if email else phone,
    )
    try:
        user_meta = await session.scalar(stmt)
        if user_meta:
            if not hasher_instance.verify_password(
                password, user_meta.user.hashed_password
            ):
                raise DoNotValidCredential()
            return user_meta
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


@none_method_user_decorator
async def OrdinaryUpdateUser(**kwargs) -> User:
    white_list = ["fname", "lname", "avatar", "br_date"]
    update_params = getParams(white_list=white_list, **kwargs)
    try:
        async with getSession() as session:
            user_meta = await getUser(
                email=kwargs.get("email", None),
                phone=kwargs.get("phone", None),
                password="Password1",
                session=session,
            )
            for key in update_params:
                updateClassAttrByKey(user_meta, key, kwargs.get(key))
            await session.commit()

            return User(**user_meta.dump_to_dict())
    except Exception:
        raise
