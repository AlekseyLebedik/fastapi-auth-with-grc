from core.db.models import Base
from core.utils.dump_to_dict import dumpToDict
from core.utils.expire_time import setExpireTime
from core.utils.verify_key import verifyKey
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class Session(Base):
    """
    CLS: Session(id:int, user_id:int, access_token:str | none, refresh_token:str | none,
                    verify_key:int, expire_time:Datetime)

    PROPERTY: dump_to_dict -> dict with Session fields
    """

    __tablename__ = "sessions"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    user = relationship(
        "UserModel",
        back_populates="session",
        cascade="all, delete-orphan",
    )
    access_token = Column(String, nullable=True)
    refresh_token = Column(String, nullable=True)
    verify_key = Column(Integer, default=verifyKey)
    expire_time = Column(DateTime, default=setExpireTime)

    def __repr__(self):
        return f"Session(id={self.id}, verify_key={self.verify_key}, expire_time={self.expire_time})"

    def __iter__(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "access_token": self.access_token,
            "refresh_token": self.refresh_token,
            "verify_key": self.verify_key,
            "expire_time": self.expire_time,
        }

    @property
    def dump_to_dict(self):
        dict = self.__dict__
        return dumpToDict(dict)
