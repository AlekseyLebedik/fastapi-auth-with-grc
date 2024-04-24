from typing import Optional

from core.db.models import Base
from core.utils.dump_to_dict import dumpToDict
from sqlalchemy import Boolean, Column, DateTime, Integer, String
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import relationship


class UserMeta(Base):
    """
    CLS: UserMeta(id:int, fname:str, lname:str, avatar:str | none, is_verify: bool,
                    verify_date: DateTime | none, email: str | none, phone: str | none,
                    document_id: str | none, document_photo_links: str | none, nationality: str | none)

    PROPERTY: get_private_meta -> return private metadata {document_id, document_photo_links,
                                                                        nationality, mac_ids }

    METHOD: dump_to_dict(with_private_meta:bool) -> return dict UserMeta() fields
    """

    __tablename__ = "users_meta"
    id = Column(Integer, primary_key=True)
    fname = Column(String)
    lname = Column(String)
    email = Column(String, unique=True, nullable=True)
    phone = Column(String, unique=True, nullable=True)
    document_id = Column(String, nullable=True, unique=True)
    document_photo_links = Column(ARRAY(String), nullable=True)
    avatar = Column(String, nullable=True)
    nationality = Column(String, nullable=True)
    mac_ids = Column(ARRAY(String), nullable=True)
    is_verify = Column(Boolean, default=False)
    verify_date = Column(DateTime, nullable=True)
    user = relationship(
        "UserModel", cascade="all, delete-orphan", back_populates="meta"
    )

    def __repr__(self):
        return f"UserMeta(id={self.id}, fname={self.fname}, lname={self.lname})"

    @property
    def get_private_meta(self):
        return {
            "document_id": self.document_id,
            "document_photo_links": self.document_photo_links,
            "mac_ids": self.mac_ids,
            "nationality": self.nationality,
        }

    def __iter__(self):
        return {
            "id": self.id,
            "is_verify": self.is_verify,
            "fname": self.fname,
            "lname": self.lname,
            "email": self.email,
            "phone": self.phone,
            "avatar": self.avatar,
            "verify_date": self.verify_date,
        }

    def dump_to_dict(self, with_private_meta: Optional[bool] = False):
        if with_private_meta:
            return dumpToDict(**self.__dict__, **self.get_private_meta)
        return dumpToDict(**self.__dict__)
