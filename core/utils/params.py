from enum import Enum


class WithoutValueEnum(Enum):
    NONE = 0
    NEGATIVE = 1


def negativeCondition(value):
    negative = [None, False]
    if value < 0 or negative.__contains__(value):
        return True


def getParamsWithoutNoneValue(**args):
    return {key: value for key, value in args if not value == None}


def getParamsWithoutNegativeValue(**args):
    return {key: value for key, value in args if not negativeCondition(value)}


def getParams(without: WithoutValueEnum = WithoutValueEnum.NONE, **args):
    if without == WithoutValueEnum.NEGATIVE:
        return getParamsWithoutNegativeValue(**args)
    return getParamsWithoutNoneValue(**args)
