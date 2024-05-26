import re
from typing import Annotated

from core.exceptions import IncorectValueType
from core.utils import _logger
from protobuff import user_models
from pydantic.functional_validators import AfterValidator


def passwordValidator(value: str):
    error = None
    if re.search(r"(?=.*[A-Z])(?=.*\d)", value) is None:
        error = "Password must contain 1 capital letter and 1 digit! Example Pasword123"
    elif len(value) < 4:
        error = "Password must not be less than 4 characters! Example Pass1"

    if error:
        raise IncorectValueType(error)

    return value


PasswordType = Annotated[str, AfterValidator(passwordValidator)]
