import typing as t
from uuid import uuid4

from core.pydantic_models.type import EmailType, PasswordType, PhoneType
from core.pydantic_models.user import User
from core.utils import _logger, createAccessToken, createRefreshToken
from core.utils.session_store.store import session_store
from protobuff import session_models

from .session import getSession
from .user_dals import getUser


async def createSession(
    password: PasswordType,
    email: t.Optional[EmailType] = None,
    phone: t.Optional[PhoneType] = None,
):
    async with getSession() as session:
        session_mark = str(uuid4())

        user = await getUser(password, session, email, phone)

        session_store.set_session(
            key=session_mark,
            user=User(**user.dump_to_dict(with_private_meta=True)),
            session_mark=session_mark,
        )
        refresh_token = createRefreshToken(user.email, user.phone_token)

        return session_models.SessionResponse(
            session_mark=session_mark,
            refresh_token=refresh_token,
            details="You have successfully created a session.",
            status=200,
        )


async def updateSession(prev_session_mark: str):
    next_session_mark = str(uuid4())

    session = session_store.get_session(prev_session_mark)

    if session:
        pass
