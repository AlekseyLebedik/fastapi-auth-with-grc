import re
from typing import Annotated

from pydantic.functional_validators import AfterValidator

from core.exceptions import IncorectValueType

from .helpers import unwantedTypeDecorator

_raisen_msg = "Invalid email format. Please enter a valid email address"


@unwantedTypeDecorator(str, _raisen_msg)
def emailValidator(value: str):
    if re.search(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", value) is None:
        raise IncorectValueType(_raisen_msg)

    return value


EmailType = Annotated[str, AfterValidator(emailValidator)]
