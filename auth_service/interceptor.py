
import grpc as g
import grpc.aio as gaio

from core.utils import _logger

from .methods import MethodsEnum


class AuthInterceptor(gaio.ServerInterceptor):
    def __init__(self) -> None:
        def abort(request, context):
            _logger.info("Reporting: AuthInterceptor call abort method ... ")
            return context.abort(g.StatusCode.UNAUTHENTICATED, "The provided token is incorrect. Please ensure that the token is valid and properly formatted")

        self._abort_hendler = g.unary_unary_rpc_method_handler(abort)

    async def intercept_service(
        self,
        continuation,
        handler_call_details,
    ):
        metadata = dict(handler_call_details.invocation_metadata)
        if metadata.get("authorization", "").__contains__("Bearer "):
            _logger.info(f"Intercepter: with token {metadata.get("authorization")}")
            return await continuation(handler_call_details)
        else:
            if handler_call_details.method.endswith(MethodsEnum.CREATE_USER.value):
                _logger.info(f"Intercepter: pass inside the {MethodsEnum.CREATE_USER.value} method")
                return await continuation(handler_call_details)
            elif handler_call_details.method.endswith(MethodsEnum.CREATE_SESSION.value):
                _logger.info(f"Intercepter: pass inside the {MethodsEnum.CREATE_SESSION.value} method")
                return await continuation(handler_call_details)
            return self._abort_hendler


