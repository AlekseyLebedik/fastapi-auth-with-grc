import uuid
from datetime import datetime
from enum import Enum

from core.db.models import Base
from core.models.session import EmailSession, PhoneSession
from core.utils.dump_to_dict import dumpToDict
from sqlalchemy import Boolean, Column, DateTime, Numeric, String
from sqlalchemy.dialects.postgresql import ARRAY, UUID
from sqlalchemy.orm import relationship


class PortalRole(str, Enum):
    ROLE_PORTAL_USER = "ROLE_PORTAL_USER"
    ROLE_PORTAL_ADMIN = "ROLE_PORTAL_ADMIN"
    ROLE_PORTAL_SUPERADMIN = "ROLE_PORTAL_SUPERADMIN"


class UserWithEmail(Base):
    __tablename__ = "users_with_email"
    email = Column(String, nullable=False, unique=True)
    user_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    roles = Column(ARRAY(String), nullable=False)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    create_at = Column(DateTime, default=datetime.utcnow())
    updated_account = Column(DateTime, default=datetime.utcnow())
    is_verify = Column(Boolean, default=True)
    email_session = relationship(
        "EmailSession", back_populates="user", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"UserModel(user_id={self.user_id}, name={self.name})"

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
            "name": self.name,
            "surname": self.surname,
            "email": self.email,
            "roles": self.roles,
            "updated_account": self.updated_account,
            "hashed_password": self.hashed_password,
            "create_at": self.create_at,
        }

    @property
    def dump_to_dict(self):
        dict = self.__dict__
        return dumpToDict(dict)


class UserWithPhone(Base):
    __tablename__ = "users_with_phone"
    phone = Column(Numeric, nullable=False, unique=True)
    user_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    roles = Column(ARRAY(String), nullable=False)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    create_at = Column(DateTime, default=datetime.utcnow())
    updated_account = Column(DateTime, default=datetime.utcnow())
    phone_session = relationship(
        "PhoneSession", back_populates="user", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"UserModel(user_id={self.user_id}, name={self.name})"

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
            "name": self.name,
            "phone": self.phone,
            "surname": self.surname,
            "roles": self.roles,
            "updated_account": self.updated_account,
            "hashed_password": self.hashed_password,
            "create_at": self.create_at,
        }

    @property
    def dump_to_dict(self):
        dict = self.__dict__
        return dumpToDict(dict)
