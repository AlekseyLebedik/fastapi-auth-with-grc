import grpc as g


def exceptionHandlingWithContext(
    context,
    exception,
    method: str = "",
    default_status=g.StatusCode.UNKNOWN,
):
    from core.utils import _logger

    status = default_status
    details = exception
    _logger.error(exception)
    if hasattr(context, "set_code") and isinstance(exception, Exception):
        if hasattr(exception, "details") and hasattr(exception, "status"):
            _logger.error(
                f"Exceptions: Error is called in {method}. Details: {exception.details}"
            )
            details = exception.details
            status = exception.status

        context.set_code(status)
        context.set_details(details)
        return

    _logger.error(f"Exceptions: Error is called in {method}. Details: {exception}")
