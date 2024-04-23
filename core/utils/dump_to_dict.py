from datetime import datetime
from typing import Optional
from uuid import UUID


def convertFromAnScalarType(value: any, format: Optional[str] = None):
    default_format = "%d:%m:%y %H:%M:%S %z"
    if isinstance(value, UUID):
        return str(value)
    if isinstance(value, datetime):
        return value.strftime(format if not format is None else default_format)
    return value


def dumpToDict(format: Optional[str] = None, **args):
    dict = {}
    for key, value in args.items():
        dict.setdefault(key, convertFromAnScalarType(value, format))
    return dict
