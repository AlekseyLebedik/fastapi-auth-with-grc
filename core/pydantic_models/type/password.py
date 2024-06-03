import re
from typing import Annotated

from pydantic.functional_validators import AfterValidator

from core.exceptions import IncorectValueType

from .helpers import unwantedTypeDecorator


@unwantedTypeDecorator(str, "You passed the incorrect password")
def passwordValidator(value: str):
    if re.search(r"(?=.*[A-Z])(?=.*\d)", value) is None:
        raise IncorectValueType(
            "Password must contain 1 capital letter and 1 digit! Example Pasword123"
        )
    elif len(value) < 4:
        raise IncorectValueType(
            "Password must not be less than 4 characters! Example Pass1"
        )

    return value


PasswordType = Annotated[str, AfterValidator(passwordValidator)]
