import re
from typing import Annotated

from core.utils import _print
from pydantic.functional_validators import AfterValidator


def phone_validator(value: str):
    assert (
        re.search(r"^\d+$", value[1::]) is not None
    ), "There should not be any letters in the phone number."
    assert value.startswith(
        "+"
    ), "Your phone number does not start with a country code prefix '+'. Example +38XXXXXXXXXX"
    assert (
        len(value) > 10 and len(value) < 18
    ), "You have entered an incorrect phone number, it should be in the range of 10 - 18 chars including country code and prefix ('+'). Example +38XXXXXXXXXX"
    return value


PhoneType = Annotated[str, AfterValidator(phone_validator)]
