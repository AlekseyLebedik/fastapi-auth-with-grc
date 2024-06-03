from typing import List, Optional

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import relationship

from core.db.models import Base
from core.models.user import *
from core.utils import dumpToDict


class UserMeta(Base):
    """
    CLS: UserMeta(id:int, is_verify: bool, verify_date: DateTime | none, email: str | none, phone: str | none,
                    document_id: str | none, document_photo_links: str | none, nationality: str | none)

    PROPERTY: get_private_meta -> return private metadata {document_id, document_photo_links, nationality, mac_ids}

    METHOD: dump_to_dict(with_private_meta:bool) -> return dict UserMeta() fields
    """

    __tablename__ = "users_meta"
    id = Column(Integer, primary_key=True)
    br_date = Column(DateTime, nullable=True)
    document_id = Column(String, nullable=True, unique=True)
    document_photo_links = Column(ARRAY(String), nullable=True)
    nationality = Column(String, nullable=True)
    mac_ids = Column(ARRAY(String(30)), nullable=True)
    is_verify = Column(Boolean, default=False)
    verify_date = Column(DateTime, nullable=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), unique=True)
    user = relationship(
        "UserModel",
        back_populates="meta",
        lazy="joined",
    )

    def __repr__(self):
        return f"UserMeta(id={self.id}, fname={self.fname}, lname={self.lname})"

    @property
    def get_private_meta(self):
        return [
            "document_photo_links",
            "mac_ids",
            "nationality",
            "br_date",
            "document_id",
        ]

    def dump_to_dict(
        self,
        with_private_meta: Optional[bool] = False,
        without: List[str] = [],
    ):
        relationship_links = {"user": "meta"}
        if with_private_meta:
            return dumpToDict(
                without=[
                    *self.get_private_meta,
                    *without,
                    "_sa_instance_state",
                ],
                relationship_links=relationship_links,
                **self.__dict__,
            )
        return dumpToDict(
            without=[*without, "_sa_instance_state"],
            relationship_links=relationship_links,
            **self.__dict__,
        )
