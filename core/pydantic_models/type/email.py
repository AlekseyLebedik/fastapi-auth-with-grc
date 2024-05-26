import re
from typing import Annotated

import grpc as g
from core.exceptions.type import IncorectValueType
from core.utils import _logger
from pydantic.functional_validators import AfterValidator


def emailValidator(value: str):
    error = None
    if re.search(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", value) is None:
        error = "Invalid email format. Please enter a valid email address."
    if error:
        raise IncorectValueType(error)

    return value


EmailType = Annotated[str, AfterValidator(emailValidator)]
