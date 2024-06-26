from enum import Enum
from typing import Optional

from pydantic import EmailStr
from sqlalchemy import Select, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from core.exceptions import DBCreate, DoNotValidCredential, HaventToken
from core.models.user import UserModel
from core.models.user_meta import UserMeta
from core.pydantic_models import User
from core.pydantic_models.type import PasswordType, PhoneType
from core.utils import (
    _logger,
    decodeJwtToken,
    getParams,
    hasher_instance,
    noneMethodUserDecorator,
    updateClassAttrByKey,
)
from core.utils.session_store.store import session_store

from .session import getSession


class MethodUserEnum(Enum):
    EMAIL = 0
    PHONE = 1


def grapMethodUser(method: MethodUserEnum, value: str) -> Select:
    if method == MethodUserEnum.EMAIL:
        return (
            select(UserModel)
            .where(UserModel.email == value)
            .options(joinedload(UserModel.meta))
        )

    return (
        select(UserModel)
        .where(UserModel.phone_token == value)
        .options(joinedload(UserModel.meta))
    )


async def currentUser(token: Optional[str] = None) -> User:
    if token is not None:
        try:
            async with getSession() as session:
                decoded_token = decodeJwtToken(token)
                return User(**decoded_token.get("user"))
        except Exception:
            raise

    raise HaventToken


@noneMethodUserDecorator
async def getUser(
    password: PasswordType,
    session: AsyncSession,
    email: Optional[EmailStr] = None,
    phone: Optional[PhoneType] = None,
) -> UserModel:
    method = MethodUserEnum.EMAIL if email else MethodUserEnum.PHONE
    stmt: Select = grapMethodUser(
        method, email if email else hasher_instance.get_password_hash(phone)
    )
    try:
        user_model: UserModel = await session.scalar(stmt)
        if user_model:
            if not hasher_instance.verify_password(
                password, user_model.hashed_password
            ):
                raise DoNotValidCredential()
            return user_model
        raise DoNotValidCredential("email or phone")
    except Exception:
        raise


@noneMethodUserDecorator
async def createUser(
    password: PasswordType,
    lname: str,
    fname: str,
    email: Optional[EmailStr],
    phone: Optional[PhoneType],
    mac_id: Optional[str] = None,
):
    try:
        phone_hash = (
            hasher_instance.get_password_hash(phone)
            if phone != None and len(phone) > 1
            else None
        )
        user_meta = UserMeta(mac_ids=[mac_id])
        user = UserModel(
            hashed_password=hasher_instance.get_password_hash(
                password=password,
            ),
            phone_token=phone_hash,
            meta=user_meta,
            email=email,
            lname=lname,
            fname=fname,
        )

        async with getSession() as session:
            session.add_all([user_meta, user])
            _logger.info(
                f"Successfull creating user and user_meta... {user.dump_to_dict()}"
            )
            return User(**user.dump_to_dict())
    except IntegrityError:
        raise DBCreate(". User exist inside the database")
    except Exception as ex:
        _logger.error(ex)
        raise


@noneMethodUserDecorator
async def ordinaryUpdateUser(
    email: Optional[EmailStr] = None,
    phone: Optional[PhoneType] = None,
    **updateKwargs,
) -> User:
    white_list = ["fname", "lname", "avatar", "br_date"]
    update_params = getParams(white_list=white_list, **updateKwargs)
    try:
        async with getSession() as session:
            user_meta = await getUser(
                email=email,
                phone=phone,
                password="Password1",
                session=session,
            )
            for key in update_params:
                updateClassAttrByKey(user_meta, key, updateKwargs.get(key))

            await session.commit()
            return User(**user_meta.dump_to_dict())
    except Exception:
        raise


@noneMethodUserDecorator
async def deleteUser(
    user_id: int,
    token: str,
    currentUser: Optional[UserMeta] = None,
) -> bool:
    pass
