import typing as t
from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import relationship

from core.db.models import Base
from core.models.session import *
from core.models.user_meta import *
from core.pydantic_models import models_enum as Emums
from core.utils import dumpToDict


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
    fname = Column(String)
    lname = Column(String)
    roles = Column(
        ARRAY(String(60)), nullable=False, default=[Emums.PortalRole.ROLE_PORTAL_USER]
    )
    email = Column(String, unique=True, nullable=True)
    phone_token = Column(String, unique=True, nullable=True)
    avatar = Column(String, nullable=True)
    hashed_password = Column(String, nullable=False)
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
        return Emums.PortalRole.ROLE_PORTAL_SUPERADMIN in self.roles

    @property
    def is_admin(self) -> bool:
        return Emums.PortalRole.ROLE_PORTAL_ADMIN in self.roles

    def enrich_admin_roles_by_admin_role(self):
        if not self.is_admin:
            return {*self.roles, Emums.PortalRole.ROLE_PORTAL_ADMIN}

    def remove_admin_privileges_from_model(self):
        if self.is_admin:
            return {
                role
                for role in self.roles
                if role != Emums.PortalRole.ROLE_PORTAL_ADMIN
            }

    def dump_to_dict(
        self, with_private_meta: t.Optional[bool] = False, without: t.List[str] = []
    ):
        relationship_links = {"meta": "user"}
        return dumpToDict(
            with_private_meta=with_private_meta,
            without=[*without, "_sa_instance_state"],
            relationship_links=relationship_links,
            **self.__dict__,
        )
