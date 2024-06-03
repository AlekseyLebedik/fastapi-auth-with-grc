from core.exceptions import IncorectValueType


def unwantedTypeDecorator(check_cls, exception_msg):
    def decorator(func):
        def wrapper(value, *args):
            if value and isinstance(value, check_cls):
                return func(value, *args)
            raise IncorectValueType(exception_msg)

        return wrapper

    return decorator
