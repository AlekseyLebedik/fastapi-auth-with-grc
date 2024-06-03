from datetime import datetime
from typing import Dict, List, Optional
from uuid import UUID


def convertFromComplexType(
    value: any,
    with_private_meta: bool = False,
    format: Optional[str] = None,
    without: List[str] = [],
):
    default_format = "%d:%m:%y %H:%M:%S"

    if isinstance(value, UUID):
        return str(value)
    if isinstance(value, datetime):
        return value.strftime(format if format is not None else default_format)
    if hasattr(value, "dump_to_dict"):
        return value.dump_to_dict(with_private_meta=with_private_meta, without=without)
    return value


def dumpToDict(
    without: List[str],
    with_private_meta: Optional[bool] = False,
    relationship_links: Dict[str, str] = {},
    format: Optional[str] = None,
    **args,
):
    dict = {}
    for key, value in args.items():
        if not without.__contains__(key):
            if value != None and not dict.get(key):
                convert = convertFromComplexType(
                    value=value,
                    format=format,
                    with_private_meta=with_private_meta,
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
