import re
from typing import Annotated

from pydantic.functional_validators import AfterValidator

from core.exceptions import IncorectValueType
from core.pydantic_models.type.helpers import unwantedTypeDecorator


@unwantedTypeDecorator(str, "You passed the incorrect phone number")
def phoneValidator(value: str):
    if re.search(r"^\d+$", value[1::]) is None:
        error = "There should not be any letters in the phone number."
    elif not value.startswith("+"):
        error = "Your phone number does not start with a country code prefix '+'. Example +38XXXXXXXXXX"
    elif len(value) < 10 and len(value) < 18:
        error = "You have entered an incorrect phone number, it should be in the range of 10 - 18 chars including country code and prefix ('+'). Example +38XXXXXXXXXX"

    if error:
        raise IncorectValueType(error)

    return value


PhoneType = Annotated[str, AfterValidator(phoneValidator)]
