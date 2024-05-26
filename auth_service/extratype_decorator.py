import asyncio

from core.exceptions import IncorectValueType
from core.pydantic_models.type import (
    emailValidator,
    macIdValidator,
    passwordValidator,
    phoneValidator,
)
from core.utils import _logger
from google.protobuf.json_format import MessageToDict


def extraValueCheck(key, value):
    if key in "phone":
        phoneValidator(value)
    elif key in "password":
        passwordValidator(value)
    elif key in "email":
        emailValidator(value)
    elif key in "mac":
        macIdValidator(value)


def extratypeDecorator(entry_key):
    def decorator(func):
        async def asyncWrapper(self, request, context):
            try:
                if asyncio.iscoroutine(request):
                    request = await request
                proto_dict = MessageToDict(request).get(entry_key)
                for key in proto_dict.keys():
                    extraValueCheck(key, proto_dict.get(key))
                return await func(self, request, context)
            except IncorectValueType as ivc:
                _logger.error(f"Exception: {str(ivc.details)}")
                context.set_code(ivc.status)
                context.set_details(ivc.details)

        def syncWrapper(self, request, context):
            proto_dict = MessageToDict(request).get(entry_key)
            try:
                for key in proto_dict.keys():
                    extraValueCheck(key, proto_dict.get(key))
                return func(self, request, context)
            except IncorectValueType as ivc:
                _logger.error(f"Exception: {str(ivc.details)}")
                context.set_code(ivc.status)
                context.set_details(ivc.details)

        if asyncio.iscoroutinefunction(func):
            return asyncWrapper
        else:
            return syncWrapper

    return decorator
