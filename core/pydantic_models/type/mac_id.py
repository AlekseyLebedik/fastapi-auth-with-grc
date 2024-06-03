import re
from typing import Annotated

from pydantic.functional_validators import AfterValidator

from core.exceptions import IncorectValueType


def macIdValidator(value: str):
    pattern = r"^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$"
    error = None
    if re.search(pattern, value) is None:
        error = "Invalid MAC address format. Please enter a valid MAC address in the format XX:XX:XX:XX:XX or XX-XX-XX-XX-XX-XX."
    if error:
        raise IncorectValueType(error)

    return value


MacIDType = Annotated[str, AfterValidator(macIdValidator)]
