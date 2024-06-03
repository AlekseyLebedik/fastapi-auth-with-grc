from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, EmailStr

from core.utils import convertFromComplexType
from protobuff import user_models as proto_models

from . import models_enum as Enums


class User(BaseModel):
    email: Optional[EmailStr] = None
    lname: Optional[str] = None
    fname: Optional[str] = None
    phone: Optional[str] = None
    roles: List[Enums.PortalRole] = [Enums.PortalRole.ROLE_PORTAL_USER.value]
    hashed_password: str
    phone_token: Optional[str] = None
    br_date: Optional[str] = None
    document_id: Optional[str] = None
    document_photo_links: Optional[str] = None
    avatar: Optional[str] = None
    nationality: Optional[str] = None
    mac_ids: Optional[List[str]] = []
    is_verify: Optional[bool] = False
    verify_date: Optional[str] = None
    create_at: Optional[str] = convertFromComplexType(datetime.now())
    updated_account: Optional[str] = None

    def proto_user(
        self,
        withPrivateField: bool = False,
    ):
        private_meta = None
        if withPrivateField:
            private_meta = proto_models.UserPrivateMeta(
                document_id=self.document_id,
                document_photo_links=self.document_photo_links,
                nationality=self.nationality,
                mac_ids=self.mac_ids,
                verify_date=self.verify_date,
                br_date=self.br_date,
            )
        return proto_models.User(
            fname=self.fname,
            lname=self.lname,
            roles=self.roles,
            email=self.email,
            phone_token=self.phone_token,
            hashed_password=self.hashed_password,
            avatar=self.avatar,
            privateMeta=private_meta,
        )
