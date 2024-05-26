from typing import Optional

import pendulum
from settings import settings

from .jwt import RequestDateType


def setExpireTime(expires_delta: Optional[RequestDateType] = None):
    current = pendulum.now(tz=pendulum.now().timezone)
    return current.add(
        minutes=expires_delta if expires_delta else settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )
