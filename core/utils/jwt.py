from typing import Optional

import pendulum
from core.exceptions import NoValidTokenRaw
from jose import JWTError, jwt
from pydantic import BaseModel
from settings import settings


class RequestDateType(BaseModel):
    year: Optional[int] = None
    month: Optional[int] = None
    day: Optional[int] = None
    hour: Optional[int] = None
    minute: Optional[int] = None
    second: Optional[int] = None


def createAccessToken(user, expires_delta: Optional[RequestDateType] = None):
    current = pendulum.now(tz=pendulum.now().timezone)
    date = current.add(
        minutes=expires_delta if expires_delta else settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    encoded_jwt = jwt.encode(
        {"user": user.dump_to_dict(), "exp": date.format("x")},
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM,
    )
    return encoded_jwt


def decodeJwtToken(token: str) -> dict:
    try:
        decoded_dict = jwt.decode(
            token=token, key=settings.SECRET_KEY, algorithms=settings.ALGORITHM
        )
    except JWTError:
        raise NoValidTokenRaw

    return decoded_dict


def createRefreshToken(user_id: str):
    encoded_jwt = jwt.encode(
        {"user_id": user_id}, settings.SECRET_KEY, algorithm=settings.ALGORITHM
    )
    return encoded_jwt
