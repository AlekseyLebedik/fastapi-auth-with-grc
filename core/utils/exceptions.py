import typing as t

import grpc as g


def exceptionHandlingWithContext(
    context: g.ServicerContext,
    exception: t.Union[Exception,],
    method: str = "",
    default_status=g.StatusCode.UNKNOWN,
) -> None:
    from loguru import logger

    status = default_status
    details = exception
    logger.error(exception)
    if hasattr(context, "set_code") and isinstance(exception, Exception):
        if hasattr(exception, "details") and hasattr(exception, "status"):
            logger.error(
                f"Exceptions: Error is called in {method}. Details: {exception.details}"
            )
            details = exception.details
            status = exception.status

        return _contextErrorHandler(context, details, status)

    logger.error(f"Exceptions: Error is called in {method}. Details: {exception}")


ResponseT = t.TypeVar("ResponseT")


def isErrorHandlingWithContext(
    context: g.ServicerContext,
    response: ResponseT,
) -> t.Union[ResponseT, None]:
    from auth_service.status import StatusCode

    if response.HasField("isError") and response.status and response.details:
        return _contextErrorHandler(
            context,
            response.details,
            StatusCode.get_grpc_code(response.status),
        )

    return response


def _contextErrorHandler(
    context: g.ServicerContext,
    details: str,
    status: t.Optional[g.StatusCode] = g.StatusCode.UNKNOWN,
    /,
) -> None:
    context.set_code(status)
    context.set_details(details)

    return
