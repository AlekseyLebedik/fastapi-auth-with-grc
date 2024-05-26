import os
from typing import Annotated, List, Optional

import grpc as g
from core.db.user_dals import createUser, currentUser, ordinaryUpdateUser
from core.pydantic_models.type import PasswordType, PhoneType
from core.utils import _logger
from core.utils.channels import createClientChannel
from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from protobuff import session_models, session_services, user_models, user_services
from pydantic import EmailStr
from settings import settings

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImZuYW1lIjoiaGVsbG8zIiwiZW1haWwiOiJ0ZXN0QGdtYWlsLmNvbSIsImlzX3ZlcmlmeSI6ZmFsc2UsInVzZXJfaWQiOjI0LCJpZCI6MjQsImxuYW1lIjoic29tZSIsInBob25lIjoiKzM4MDkzMDk3MDA5MCIsIm1hY19pZHMiOlsiMjM6MzM6MzQ6NDQ6NjYiXSwiY3JlYXRlX2F0IjoiMDk6MDU6MjQgMTI6MTY6MjgiLCJoYXNoZWRfcGFzc3dvcmQiOiIkMmIkMTIkWm81dVhvejhxQnpoNGhFOXIubk8zZVhsTDBBckJNS2xiNUxIZ2JxRHFYaEdkUUhxTFpuZXkiLCJyb2xlcyI6WyJST0xFX1BPUlRBTF9VU0VSIl0sInVwZGF0ZWRfYWNjb3VudCI6IjA5OjA1OjI0IDEyOjE2OjI4In0sImV4cCI6IjE3MTU4OTc5ODA2NzIifQ.vY1AOAmqOY5pIE5GUWX0DwQCKbsYiHzZ5Le5m3fkj9I"

app = FastAPI(
    title="User test",
    version="0.0.1",
    terms_of_service="http://example.com/terms/",
    license_info={"name": "MIT"},
    docs_url="/swagger",
)


"""
    fname: Optional[str] = None,
    lname: Optional[str] = None,
    br_date: Optional[str] = None,
    document_id: Optional[str] = None,
    document_photo_links: Optional[List[str]] = None,
    avatar: Optional[str] = None,
    nationality: Optional[str] = None,
    mac_ids: Optional[List[str]] = None,
    is_verify: Optional[bool] = None,
    verify_date: Optional[str] = None,
"""


@app.delete("/delete_user")
async def deleteUser(
    request: Request,
    user_id: int,
    email: Optional[EmailStr] = None,
    phone: Optional[PhoneType] = None,
):
    pass


@app.post("/ordinary_update_user")
async def ordinary_update_user(
    request: Request,
    password: PasswordType,
    fname: Optional[str] = None,
    lname: Optional[str] = None,
    br_date: Optional[str] = None,
    avatar: Optional[str] = None,
    email: Optional[EmailStr] = None,
    phone: Optional[PhoneType] = None,
):
    try:
        user = await createUser(
            password=password,
            lname=lname,
            fname=fname,
            email=email,
            phone=phone,
            mac_id=["20:23:30:39:59"],
        )
    except Exception as reason:
        raise HTTPException(
            status_code=404,
            detail=(
                reason.get_message if hasattr(reason, "get_message") else str(reason)
            ),
        )


@app.post("/grpc_create_user")
async def grpc_create(
    fname: str,
    lname: str,
    password: str,
    email: Optional[str] = None,
    phone: Optional[str] = None,
):
    try:
        user = user_models.User(
            fname=fname,
            lname=lname,
            roles=("ROLE_PORTAL_USER",),
            email=email,
            phone=phone,
            password=password,
        )
        async with createClientChannel() as channel:
            stub = user_services.UserServiceStub(channel)
            request = user_models.CreateUserRequest(user=user)
            response = await stub.CreateUser(request)
            _logger.info(response)
    except Exception as ex:
        _logger.error(ex)


@app.get("/healthcheck")
def healthcheck():
    """
    Check the health of the application.
    """
    return JSONResponse(content={"status": "ok"})
