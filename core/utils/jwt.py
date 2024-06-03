from typing import Optional

import pendulum
from jose import JWTError, jwt
from pydantic import BaseModel

from core.exceptions import NoValidTokenRaw
from settings import settings


class RequestDateType(BaseModel):
    year: Optional[int] = None
    month: Optional[int] = None
    day: Optional[int] = None
    hour: Optional[int] = None
    minute: Optional[int] = None
    second: Optional[int] = None


def createAccessToken(email, expires_delta: Optional[RequestDateType] = None):
    current = pendulum.now(tz=pendulum.now().timezone)
    date = current.add(
        minutes=expires_delta if expires_delta else settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    encoded_jwt = jwt.encode(
        {"user": email, "exp": date.format("x")},
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM,
    )

    return encoded_jwt


def decodeJwtToken(token: str) -> dict:
    try:
        decoded_dict = jwt.decode(
            token=token,
            key=settings.SECRET_KEY,
            algorithms=settings.ALGORITHM,
        )
    except JWTError:
        raise NoValidTokenRaw

    return decoded_dict


def createRefreshToken(
    email: Optional[str] = None,
    phone: Optional[str] = None,
):
    verify = {"email": email} if email else {"phone_hash": phone}
    encoded_jwt = jwt.encode(verify, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt
