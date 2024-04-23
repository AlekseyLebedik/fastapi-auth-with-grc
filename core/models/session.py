from core.db.models import Base
from core.utils.dump_to_dict import dumpToDict
from core.utils.expire_time import setExpireTime
from sqlalchemy import Column, DateTime, ForeignKey, Numeric, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class EmailSession(Base):
    __tablename__ = "emails_session"
    id = Column(
        Numeric,
        primary_key=True,
    )
    user_id = Column(
        UUID,
        ForeignKey("users_with_email.user_id", ondelete="CASCADE", name="fk_user_id"),
    )
    user = relationship(
        "UserWithEmail", back_populates="email_verify", cascade="all, delete-orphan"
    )
    access_token = Column(String, nullable=True)
    refresh_token = Column(String, nullable=True)
    verify_key = Column(Numeric, nullable=True)
    expire_time = Column(DateTime, default=setExpireTime)

    def __iter__(self):
        return {
            "id": self.id,
            "user_id": str(self.user_id),
            "user": self.user,
            "access_token": self.access_token,
            "refresh_token": self.refresh_token,
            "verify_key": self.verify_key,
            "expire_time": self.expire_time,
        }

    @property
    def dump_to_dict(self):
        dict = self.__dict__
        return dumpToDict(dict)


class PhoneSession(Base):
    __tablename__ = "phones_session"
    id = Column(
        Numeric,
        primary_key=True,
    )
    user_id = Column(
        UUID,
        ForeignKey("users_with_phone.user_id", ondelete="CASCADE", name="fk_user_id"),
    )
    user = relationship(
        "UserWithPhone", back_populates="phone_session", cascade="all, delete-orphan"
    )
    access_token = Column(String, nullable=True)
    refresh_token = Column(String, nullable=True)
    verify_key = Column(Numeric, nullable=True)
    expire_time = Column(DateTime, default=setExpireTime)

    def __iter__(self):
        return {
            "id": self.id,
            "user_id": str(self.user_id),
            "user": self.user,
            "access_token": self.access_token,
            "refresh_token": self.refresh_token,
            "verify_key": self.verify_key,
            "expire_time": self.expire_time,
        }

    @property
    def dump_to_dict(self):
        dict = self.__dict__
        return dumpToDict(dict)
