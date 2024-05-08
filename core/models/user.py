from datetime import datetime
from typing import List

from core.db.models import Base
from core.models.pydantic_models import PortalRole
from core.models.session import *
from core.models.user_meta import *
from core.utils import _print, dumpToDict
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import relationship


class UserModel(Base):
    """
    CLS: UserModel(roles: [ROLE_PORTAL_USER | ROLE_PORTAL_ADMIN | ROLE_PORTAL_SUPERADMIN],
                  hashed_password: str, phone_token:str, create_at: DateTime, updated_account: DateTime )

    PROPERTY: is_superadmin -> return bool;
    PROPERTY: is_admin -> return bool;
    PROPERTY: dump_to_dict -> dict with UserModel fields

    METHOD: enrich_admin_roles_by_admin_role() -> return [ROLE_PORTAL_USER | ROLE_PORTAL_SUPERADMIN , ROLE_PORTAL_ADMIN  ]
    METHOD: remove_admin_privileges_from_model() -> return [ROLE_PORTAL_USER | ROLE_PORTAL_SUPERADMIN ]
    """

    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True)
    roles = Column(
        ARRAY(String(60)),
        nullable=False,
        default=[PortalRole.ROLE_PORTAL_USER],
    )
    hashed_password = Column(String, nullable=False)
    phone_token = Column(String, nullable=True)
    create_at = Column(DateTime, default=datetime.utcnow())
    updated_account = Column(DateTime, default=datetime.utcnow())
    session = relationship(
        "Session",
        back_populates="user",
        cascade="all, delete-orphan",
        uselist=False,
        lazy="joined",
    )
    meta = relationship(
        "UserMeta",
        back_populates="user",
        cascade="all, delete-orphan",
        uselist=False,
        lazy="joined",
    )

    def __repr__(self):
        return f"UserModel(user_id={self.user_id})"

    @property
    def is_superadmin(self) -> bool:
        return PortalRole.ROLE_PORTAL_SUPERADMIN in self.roles

    @property
    def is_admin(self) -> bool:
        return PortalRole.ROLE_PORTAL_ADMIN in self.roles

    def enrich_admin_roles_by_admin_role(self):
        if not self.is_admin:
            return {*self.roles, PortalRole.ROLE_PORTAL_ADMIN}

    def remove_admin_privileges_from_model(self):
        if self.is_admin:
            return {role for role in self.roles if role != PortalRole.ROLE_PORTAL_ADMIN}

    def dump_to_dict(self, without: List[str] = []):
        relationship_links = {"meta": "user"}
        return dumpToDict(
            without=[*without, "_sa_instance_state"],
            relationship_links=relationship_links,
            **self.__dict__,
        )
