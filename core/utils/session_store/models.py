from datetime import datetime

from pydantic import BaseModel

from core.pydantic_models.user import User
from core.utils.expire_time import setExpireTime


class SessionNode(BaseModel):
    user: User
    session_mark: str
    expire_time: datetime = setExpireTime()
