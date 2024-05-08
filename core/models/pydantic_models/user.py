from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, EmailStr


class PortalRole(str, Enum):
    ROLE_PORTAL_USER = "ROLE_PORTAL_USER"
    ROLE_PORTAL_ADMIN = "ROLE_PORTAL_ADMIN"
    ROLE_PORTAL_SUPERADMIN = "ROLE_PORTAL_SUPERADMIN"


class User(BaseModel):
    email: Optional[EmailStr] = None
    lname: Optional[str] = None
    fname: Optional[str] = None
    phone: Optional[str] = None
    roles: List[PortalRole]
    hashed_password: str
    phone_token: str
    br_date: Optional[str] = None
    document_id: Optional[str] = None
    document_photo_links: Optional[str] = None
    avatar: Optional[str] = None
    nationality: Optional[str] = None
    mac_ids: Optional[List[str]] = None
    is_verify: bool
    verify_date: Optional[str] = None
    create_at: str
    updated_account: str = None
