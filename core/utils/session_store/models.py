from datetime import datetime

from core.pydantic_models.user import User
from core.utils.expire_time import setExpireTime
from pydantic import BaseModel


class SessionNode(BaseModel):
    user: User
    session_mark: str
    expire_time: datetime = setExpireTime()
