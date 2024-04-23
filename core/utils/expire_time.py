from typing import Optional

import pendulum
from pydantic import BaseModel
from settings import settings


class RequestDateType(BaseModel):
    year: Optional[int] = None
    month: Optional[int] = None
    day: Optional[int] = None
    hour: Optional[int] = None
    minute: Optional[int] = None
    second: Optional[int] = None


def setExpireTime(expires_delta: Optional[RequestDateType] = None):
    current = pendulum.now(tz=pendulum.now().timezone)
    return current.add(
        minutes=expires_delta if expires_delta else settings.EXPIRE_MINUTES
    )
