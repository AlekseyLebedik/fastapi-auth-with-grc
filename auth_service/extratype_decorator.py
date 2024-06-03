import asyncio

from google.protobuf.json_format import MessageToDict

from core.exceptions import IncorectValueType
from core.pydantic_models.type import (
    emailValidator,
    macIdValidator,
    passwordValidator,
    phoneValidator,
)
from core.utils import exceptionHandlingWithContext


def extraValueCheck(key, value):
    if key in "phone":
        phoneValidator(value)
    elif key in "password":
        passwordValidator(value)
    elif key in "email":
        emailValidator(value)
    elif key in "mac":
        macIdValidator(value)


def extratypeDecorator(entry_key=None):
    def decorator(func):
        async def asyncWrapper(self, request, context):
            try:
                if asyncio.iscoroutine(request):
                    request = await request
                proto_dict = (
                    MessageToDict(request).get(entry_key)
                    if entry_key
                    else MessageToDict(request)
                )
                for key in proto_dict:
                    extraValueCheck(key, proto_dict.get(key))
                return await func(self, request, context)
            except IncorectValueType as ivc:
                exceptionHandlingWithContext(context, ivc)

        def syncWrapper(self, request, context):
            proto_dict = (
                MessageToDict(request).get(entry_key)
                if entry_key is not None
                else MessageToDict(request)
            )
            try:
                for key in proto_dict:
                    extraValueCheck(key, proto_dict.get(key))
                return func(self, request, context)
            except IncorectValueType as ivc:
                exceptionHandlingWithContext(context, ivc)

        if asyncio.iscoroutinefunction(func):
            return asyncWrapper
        else:
            return syncWrapper

    return decorator
