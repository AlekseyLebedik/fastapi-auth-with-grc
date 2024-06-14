
import grpc as g
import grpc.aio as gaio
from loguru import logger

from .methods import MethodsEnum


class AuthInterceptor(gaio.ServerInterceptor):
    def __init__(self) -> None:
        def abort(_, context:g.ServicerContext):
            logger.info("Reporting: AuthInterceptor call abort method ... ")
            authorization_abort_details = {"code": g.StatusCode.UNAUTHENTICATED, 
                                           "details": "The provided token is incorrect. Please ensure that the token is valid and properly formatted"}
            return context.abort(authorization_abort_details["code"], 
                                authorization_abort_details["details"])

        self._abort_hendler = g.unary_unary_rpc_method_handler(abort)

    async def intercept_service(
        self,
        continuation,
        handler_call_details,
    ):
        metadata = dict(handler_call_details.invocation_metadata)
        if metadata.get("authorization", "").__contains__("Bearer "):
            logger.info(f"Intercepter: with token {metadata.get("authorization")}")
            return await continuation(handler_call_details)
        else:
            if handler_call_details.method.endswith(MethodsEnum.CREATE_USER.value):
                logger.info(f"Intercepter: pass inside the {MethodsEnum.CREATE_USER.value} method")
                return await continuation(handler_call_details)
            elif handler_call_details.method.endswith(MethodsEnum.CREATE_SESSION.value):
                logger.info(f"Intercepter: pass inside the {MethodsEnum.CREATE_SESSION.value} method")
                return await continuation(handler_call_details)
            elif handler_call_details.method.endswith(MethodsEnum.CONDITION_SESSION.value):
                logger.info(f"Intercepter: pass inside the {MethodsEnum.CONDITION_SESSION.value} method")
                return await continuation(handler_call_details)
            return self._abort_hendler


