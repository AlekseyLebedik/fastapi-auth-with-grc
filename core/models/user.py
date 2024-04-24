from datetime import datetime
from enum import Enum

from core.db.models import Base
from core.utils.dump_to_dict import dumpToDict
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import relationship


class PortalRole(str, Enum):
    ROLE_PORTAL_USER = "ROLE_PORTAL_USER"
    ROLE_PORTAL_ADMIN = "ROLE_PORTAL_ADMIN"
    ROLE_PORTAL_SUPERADMIN = "ROLE_PORTAL_SUPERADMIN"


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
    roles = Column(ARRAY(String), nullable=False)
    hashed_password = Column(String, nullable=False)
    phone_token = Column(String, nullable=True)
    create_at = Column(DateTime, default=datetime.utcnow())
    updated_account = Column(DateTime, default=datetime.utcnow())
    session = relationship(
        "Session", back_populates="user", cascade="all, delete-orphan", uselist=False
    )
    meta = relationship(
        "UserMeta", back_populates="user", cascade="all, delete-orphan", uselist=False
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

    def __iter__(self):
        return {
            "user_id": str(self.user_id),
            "roles": self.roles,
            "updated_account": self.updated_account,
            "hashed_password": self.hashed_password,
            "create_at": self.create_at,
        }

    @property
    def dump_to_dict(self):
        return dumpToDict(self.__dict__)
