from typing import Annotated, List, Optional

import core.user_pb2 as model_user
import grpc
from core.db.user_dals import createUser, getUser
from core.models.pydantic_models import PasswordType, PhoneType
from core.user_pb2_grpc import *
from core.utils import _print
from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from pydantic import EmailStr
from settings import settings

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


def grpc_chanel():
    return grpc.insecure_channel(f"{settings.HOST_GRPC}:{settings.USER_PORT_GRPC}")


@app.post("/create_user")
async def get_user_test(
    request: Request,
    fname: str,
    lname: str,
    password: PasswordType,
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
            mac_id="20:39:30:50:10:22",
        )
    except Exception as reason:
        _print(reason)
        raise HTTPException(
            status_code=404,
            detail=(
                reason.get_message if hasattr(reason, "get_message") else str(reason)
            ),
        )


@app.get("/create_user")
def create_user(fname: str, lname: str, email: str):
    with grpc_chanel() as channel:
        stub = UserServiceStub(channel)
        response = stub.CreateUser(
            model_user.CreateUserRequest(
                user=model_user.User(
                    fname=fname,
                    lname=lname,
                    roles=[],
                    email=email,
                ),
            ),
            metadata=(
                ("initial-metadata-1", "The value should be str"),
                (
                    "binary-metadata-bin",
                    b"With -bin surffix, the value can be bytes",
                ),
                ("accesstoken", "gRPC Python is great"),
            ),
        )
    # Convert the gRPC response message to JSON and return it
    return JSONResponse(
        response.details,
    )


@app.get("/healthcheck")
def healthcheck():
    """
    Check the health of the application.
    """
    return JSONResponse(content={"status": "ok"})
