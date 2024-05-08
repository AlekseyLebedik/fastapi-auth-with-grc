import re
from typing import Annotated

from pydantic.functional_validators import AfterValidator


def password_validator(value: str):
    assert (
        re.search(r"(?=.*[A-Z])(?=.*\d)", value) is not None
    ), "Password must contain 1 capital letter and 1 digit! Example Pasword123"
    assert (
        not len(value) < 4
    ), "Password must not be less than 4 characters! Example Pass1"
    return value


PasswordType = Annotated[str, AfterValidator(password_validator)]
