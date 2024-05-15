from enum import Enum
from typing import List, Optional

from core.utils.terminal import _print


def updateClassAttrByKey(cls, key: str, newValue):
    if hasattr(cls, key):
        setattr(cls, key, newValue)
    return cls


class WithoutValueEnum(Enum):
    NONE = 0
    NEGATIVE = 1


def negativeCondition(value):
    negative = [None, False]
    if value < 0 or negative.__contains__(value):
        return True


def noneCondition(value):
    return value != None


def getParamsWithWhiteList(without: WithoutValueEnum, whiteList: List[str], **kwargs):
    withoutCondition = (
        noneCondition if without == WithoutValueEnum.NONE else negativeCondition
    )
    return {
        key: value
        for key, value in kwargs.items()
        if whiteList.__contains__(key) and withoutCondition(value)
    }


def getParamsWithoutNoneValue(**kwargs):
    return {key: value for key, value in kwargs.items() if noneCondition(value)}


def getParamsWithoutNegativeValue(**kwargs):
    return {key: value for key, value in kwargs.items() if not negativeCondition(value)}


def getParams(
    without: WithoutValueEnum = WithoutValueEnum.NONE,
    white_list: Optional[List[str]] = None,
    **kwargs
):
    if white_list != None:
        return getParamsWithWhiteList(without, white_list, **kwargs)
    if without == WithoutValueEnum.NEGATIVE:
        return getParamsWithoutNegativeValue(**kwargs)
    return getParamsWithoutNoneValue(**kwargs)
