from core.db.session_dals import createSession
from core.db.user_dals import createUser
from core.utils import _logger, exceptionHandlingWithContext
from protobuff import session_services, user_models, user_services

from .extratype_decorator import extratypeDecorator
from .methods import MethodsEnum


class AuthServiceServicer(
    session_services.SessionServiceServicer,
    user_services.UserServiceServicer,
):
    @extratypeDecorator("user")
    async def CreateUser(self, request, context):
        _logger.info(f"{MethodsEnum.CREATE_USER.value} methods starting ...")
        metadata = dict(context.invocation_metadata())
        try:
            user = request.user
            user = await createUser(
                password=user.password,
                lname=user.lname,
                fname=user.fname,
                email=user.email,
                phone=user.phone,
                mac_id=metadata.get("mac_id", ""),
            )
            _logger.info(user.model_dump())
            return user_models.TotalResponse(
                details="Succesfull create user!",
                status=201,
                user=user.proto_user(),
            )
        except Exception as ex:
            exceptionHandlingWithContext(
                context=context,
                exception=ex,
                method=MethodsEnum.CREATE_USER.value,
            )

    @extratypeDecorator()
    async def CreateSession(self, request, context):
        try:
            return await createSession(
                password=request.password,
                email=request.email,
                phone=request.phone_number,
            )
        except Exception as ex:
            exceptionHandlingWithContext(
                context=context,
                exception=ex,
                method=MethodsEnum.CREATE_SESSION.value,
            )
