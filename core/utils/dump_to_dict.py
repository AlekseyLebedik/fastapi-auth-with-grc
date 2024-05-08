from datetime import datetime
from typing import Dict, List, Optional
from uuid import UUID


def convertFromComplexType(
    value: any,
    format: Optional[str] = None,
    without: List[str] = [],
):
    default_format = "%d:%m:%y %H:%M:%S %z"

    if isinstance(value, UUID):
        return str(value)
    if isinstance(value, datetime):
        return value.strftime(format if not format is None else default_format)
    if hasattr(value, "dump_to_dict"):
        return value.dump_to_dict(without=without)
    return value


def dumpToDict(
    without: List[str],
    relationship_links: Dict[str, str] = {},
    format: Optional[str] = None,
    **args,
):
    dict = {}
    for key, value in args.items():
        if not without.__contains__(key):
            if not value == None and not dict.get(key, None):
                convert = convertFromComplexType(
                    value,
                    format,
                    without=[
                        *dict.keys(),
                        relationship_links.get(key, ""),
                    ],
                )
                if isinstance(convert, Dict):
                    dict = {**dict, **convert}
                else:
                    dict.setdefault(key, convert)
    return dict
