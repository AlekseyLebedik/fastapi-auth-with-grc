from core.db.user_dals import createUser
from core.utils import _logger
from protobuff import session_models, session_services, user_models, user_services

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
                details=f"Succesfull create user!",
                status=201,
                user=user.protoUser(),
            )
        except Exception as ex:
            details = ex.detials if hasattr(ex, "details") else ex
            _logger.error(
                f"Exceptions: Error is called in {MethodsEnum.CREATE_USER.value} method.",
                details,
            )
